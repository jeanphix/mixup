docs:
	sass styles.scss static/css/styles.css
	_bin/documentor.py
	rm _gh-pages/* -rf
	jekyll
	cp _site/* _gh-pages/ -r



.PHONY: docs 
