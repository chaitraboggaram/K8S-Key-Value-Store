# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

## Requirements

**Note:** Before starting, a `requirements.txt` file and `makefile` have been created. You can install the Python dependencies by running:

```bash
make
```
When you run make, it will execute the following targets in order:
- build: Builds the Docker image.
- minikube-start: Starts MiniKube with the Docker driver.
- install-dependencies: Installs Python dependencies and MiniKube if needed.
- run: Outputs instructions for running the application.

If you get any errors on any installations, then check the appropriate dependency from the below and install using the given commands.

### 1. Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install MiniKube

```bash
brew install minikube
```

### 3. Install Docker

- Download Docker from [Docker Documentation](https://docs.docker.com/) based on your Operating System. Sign up with your email address.
- Check Docker version:

    ```bash
    docker --version
    ```

- Create a Docker repository on [Docker Hub](https://hub.docker.com/):

    Docker repository: `chaitraboggaram/k8s-key-value-store/`

- Build and push Docker image:

    ```bash
    docker build -t chaitraboggaram/k8s-key-value-store:latest
    docker push chaitraboggaram/k8s-key-value-store:latest
    ```

### 4. Install Python Dependencies

```bash
pip install fastapi==0.68.0 huey==2.4.2
```

### 5. Install Huey Optional Dependencies

Refer to [Huey Installation Guide](https://huey.readthedocs.io/en/latest/installation.html#using-git) for installation details.

### 6. Start MiniKube with Docker driver

```bash
minikube start --driver=docker
```

```bash
minikube status
```
Verify MiniKube Installation

### 7. Apply Kubernetes Configuration

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 8. Check Deployments, Pods, and Services

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### 9. Get MiniKube IP

```bash
minikube ip
```

### 10. Port Forwarding

```bash
kubectl port-forward service/k8s-key-value-store-service 8000:80
```

### 11. Run FastAPI Application

Once port forwarding is successful, run:

```bash
uvicorn main:app --reload
```

This loads the content from `main.py` file in [http://localhost:8000/](http://localhost:8000/)

### 12. Check Kubernetes Events

```bash
kubectl get events
```

This provides information about all events occurring on the pod.
