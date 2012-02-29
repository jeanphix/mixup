#!/usr/bin/env python
import os
import sys
import re
from yaml import load, dump


def extract_doc(source, topnamespace):
    """Extract docs from scss file.
    """
    f = open(source, 'r')
    file_content = f.read()

    r = re.compile(r"/\*(.[^\*]*)//\*\n@mixin ([a-z\-]{1,})", re.DOTALL)

    docs = []

    current_namespace = {'label': None}

    for doc, mixin in r.findall(file_content):
        doc_tree = load(doc.replace('//', ''))
        namespace = doc_tree['namespace']
        if current_namespace['label'] != namespace:
            if current_namespace['label'] is not None:
                docs.append(current_namespace)
            current_namespace = {'label': namespace, 'mixins': []}
        doc_tree['label'] = mixin
        current_namespace['mixins'].append(doc_tree)

    docs.append(current_namespace)

    return "- %s" % dump({topnamespace: {'label': topnamespace, 'namespaces': docs}})


def put_docs_in_file(scss_file, source, flag, namespace, destination=None):
    f = open(source, 'r')
    file_content = f.read()
    file_content = file_content.replace(flag,
            extract_doc(scss_file, namespace))
    f = open(destination, 'w')
    f.write(file_content)


put_docs_in_file("mixin/style.scss", "docs/_sources/mixins.html",
    "#{style}", "style", "docs/mixins.html")
put_docs_in_file("mixin/layout.scss", "docs/mixins.html",
    "#{layout}", "layout", "docs/mixins.html")
put_docs_in_file("mixin/component.scss", "docs/mixins.html",
    "#{component}", "components", "docs/mixins.html")
