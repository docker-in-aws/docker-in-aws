.PHONY: test release clean login logout publish

DOCKER_HOST ?= localhost

login:
	$$(aws ecr get-login --no-include-email)

logout:
	docker logout 385605022855.dkr.ecr.us-east-1.amazonaws.com

test:
	docker-compose build --pull test
	docker-compose run test

release: test
	docker-compose build release
	docker-compose up --exit-code-from migrate migrate
	docker-compose run app python3 manage.py collectstatic --no-input
	docker-compose up -d app
	@ echo App running at http://$$(docker-compose port app 8000 | sed s/0.0.0.0/$(DOCKER_HOST)/g)

publish: login
	docker-compose push release

clean:
	docker-compose down -v
	docker images -q -f dangling=true -f label=application=todobackend | xargs -I ARGS docker rmi -f ARGS