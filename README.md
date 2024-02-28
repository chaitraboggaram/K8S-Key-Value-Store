# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

## Requirements

### Install MiniKube

```bash
brew install minikube
```

### Install Docker

Download Docker from [https://docs.docker.com/](https://docs.docker.com/) based on your Operating System. Sign up with your email address.

Check Docker version:

```bash
docker --version
```

Create a Docker repository on [Docker Hub](https://hub.docker.com/):

Docker repository: `chaitraboggaram/k8s-key-value-store/`

Login to Docker:

```bash
docker login
```

Enter your Docker username and password.

Build Docker image:

```bash
docker build -t chaitraboggaram/k8s-key-value-store:latest
```

Start MiniKube with Docker driver:

```bash
minikube start --driver=docker
```
