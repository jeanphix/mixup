#!/usr/bin/env python
import os
import sys
import re
from yaml import load, dump


def extract_doc(source):
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

    return dump(docs)


def put_docs_in_file(scss_file, source, flag, destination):
    f = open(source, 'r')
    file_content = f.read()
    file_content = file_content.replace(flag,
            extract_doc(scss_file))
    f = open(destination, 'w')
    f.write(file_content)


put_docs_in_file("../mixin/style.scss", "_sources/style.html",
    "#{docs}", "style.html")
put_docs_in_file("../mixin/layout.scss", "_sources/layout.html",
    "#{docs}", "layout.html")
put_docs_in_file("../mixin/component.scss", "_sources/component.html",
    "#{docs}", "component.html")

