test:
	autopep8 -ria apps/
	flake8 apps/
	pytest
	DJANGO_SETTINGS_MODULE=demo_project.settings.test python manage.py behave


