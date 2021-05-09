.ONESHELL:
django-base-template: hugo
	cp public/django-base-template/index.html django_site/mwdata/templates/base.html
	sed -i 's/¤{/{/g' django_site/mwdata/templates/base.html
	sed -i 's/¤}/}/g' django_site/mwdata/templates/base.html
	cp -r public/static/* django_site/mwdata/static/


.ONESHELL:
hugo:
	hugo
