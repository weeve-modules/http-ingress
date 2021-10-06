SHELL := /bin/bash

create_image:
	docker build -t weevenetwork/http-ingress . -f image/Dockerfile
.phony: create_image

push_latest:
	docker image push weevenetwork/http-ingress
.phony: push_latest

run_image:
	docker run -p 5000:80 --rm --env-file=./config.env weevenetwork/http-ingress:latest
.phony: run_image

lint:
	pylint main.py app/
.phony: lint

install_local:
	pip3 install -r requirements.txt
.phony: install_local

run_local:
	 python main.py
.phony: run_local
