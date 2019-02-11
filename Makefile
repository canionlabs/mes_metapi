py-tests:
	docker-compose run \
		-e DJANGO_SETTINGS_MODULE=mes_metapi.settings.tests \
		--no-deps --rm web sh -c "./manage.py migrate && py.test -vx"