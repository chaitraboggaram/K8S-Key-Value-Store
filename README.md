Certainly! Here's a beautified version with proper subheadings and content:

---

# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

## Requirements

**Note:** Before starting, a `requirements.txt` file and `makefile` have been created. You can install the Python dependencies by running:

```bash
pip install -r requirements.txt
make
```

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

- Login to Docker:

    ```bash
    docker login
    ```

    Enter your Docker username and password.

- Build Docker image:

    ```bash
    docker build -t chaitraboggaram/k8s-key-value-store:latest
    ```

### 4. Install Python and Pip (if not already installed)

```bash
brew install python
easy_install pip
```

### 5. Install Python Dependencies

```bash
pip install fastapi==0.68.0
pip install huey==2.4.2
```

### 6. Install Huey Optional Dependencies

Refer to [Huey Installation Guide](https://huey.readthedocs.io/en/latest/installation.html#using-git) for installation details.

### 7. Run Dockerfile

- After installing Docker, build the Docker image:

    ```bash
    docker build -t chaitraboggaram/k8s-key-value-store:latest
    ```

- Push Docker image:

    ```bash
    docker push chaitraboggaram/k8s-key-value-store:latest
    ```

### 8. Run Makefile

If you have a Makefile for your project, you can run it to perform various tasks. For example:

```bash
make install-dependencies
```

### 9. Start MiniKube with Docker driver

```bash
minikube start --driver=docker
```


### 10. Verify MiniKube Installation

To check if MiniKube is installed successfully:

```bash
minikube status
```

### 11. Apply Kubernetes Configuration

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 12. Check Deployments

```bash
kubectl get deployments
```

Now you should see the deployments.

### 13. Check Pods and Services

```bash
kubectl get pods
kubectl get services
```

### 14. Get MiniKube IP

```bash
minikube ip
```

This provides a local IP for MiniKube.

### 15. Port Forwarding

```bash
kubectl port-forward service/k8s-key-value-store-service 8000:80
```

Make sure this is running in one terminal

### 16. Run FastAPI Application

Once port forwarding is successful, run in another terminal:

```bash
uvicorn main:app --reload
```

This loads the content from `main.py` file in [http://localhost:8000/](http://localhost:8000/)

### 17. Check Kubernetes Events

```bash
kubectl get events
```

This command provides information about all events occurring on the pod.

