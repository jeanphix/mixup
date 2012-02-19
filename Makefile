docs:
	touch docs/static/css/mixup/forms.css
	rm docs/static/css/mixup/*
	sass builder/form.scss docs/static/css/mixup/form.css
	sass builder/layout.scss docs/static/css/mixup/layout.css
	sass docs/styles.scss docs/static/css/styles.css


.PHONY: docs 
