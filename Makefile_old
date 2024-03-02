# Variables
DOCKER_IMAGE = chaitraboggaram/k8s-key-value-store:latest
REQUIREMENTS_FILE = requirements.txt
PYTHON_ENV = venv

# Targets
.PHONY: all build minikube-start install-dependencies install-minikube install-huey-dependencies generate-requirements run-app

all: build minikube-start install-dependencies run-app

build:
	docker build -t $(DOCKER_IMAGE) .

minikube-start:
	minikube start --driver=docker

install-dependencies: install-huey-dependencies install-minikube
	python3 -m venv $(PYTHON_ENV)
	source $(PYTHON_ENV)/bin/activate && pip install -r $(REQUIREMENTS_FILE)

install-minikube:
	command -v minikube >/dev/null 2>&1 || { brew install minikube; }

install-huey-dependencies:
	pip install -r $(REQUIREMENTS_FILE)

generate-requirements:
	pip freeze > $(REQUIREMENTS_FILE)

run:
	@echo
	@echo "Run the following command in a new terminal:"
	@echo "kubectl port-forward service/k8s-key-value-store-service 8000:80"
	@echo
	@echo "Then, in another terminal, run:"
	@echo "uvicorn main:app --reload"
	@echo
	@echo "Make sure both kubernetes port forwarding and uvicorn are running and visit http://127.0.0.1:8000/"
	@echo
