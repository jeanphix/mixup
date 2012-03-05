docs:
	touch static/css/mixup/forms.css
	rm static/css/mixup/*
	sass ../builder/form.scss static/css/mixup/form.css
	sass ../builder/layout.scss static/css/mixup/layout.css
	sass styles.scss static/css/styles.css
	_bin/documentor.py

.PHONY: docs 
