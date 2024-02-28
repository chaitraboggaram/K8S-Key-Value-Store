# Makefile for K8S-Key-Value-Store

# Variables
DOCKER_IMAGE = chaitraboggaram/k8s-key-value-store:latest
REQUIREMENTS_FILE = requirements.txt
PYTHON_ENV = venv

# Targets
.PHONY: all build minikube-start install-dependencies install-minikube install-huey-dependencies generate-requirements

all: build minikube-start install-dependencies

build:
	docker build -t $(DOCKER_IMAGE) .

minikube-start:
	minikube start --driver=docker

install-dependencies: install-minikube install-huey-dependencies
	python3 -m venv $(PYTHON_ENV)
	source $(PYTHON_ENV)/bin/activate && pip install -r $(REQUIREMENTS_FILE)