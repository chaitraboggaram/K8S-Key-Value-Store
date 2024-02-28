# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

## Requirements

**Note:** Before starting, a requirements.txt file and make file has been created. You can install the Python dependencies by running:

```bash
pip install -r requirements.txt
make
```

### Below are the step-by-step instructions for installing and configuring the application:

1. **Install Homebrew:**
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Install MiniKube:**
    ```bash
    brew install minikube
    ```

3. **Install Docker:**
    - Download Docker from [https://docs.docker.com/](https://docs.docker.com/) based on your Operating System. Sign up with your email address.
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
        docker build -t chaitraboggaram/k8s-key-value-store:latest .
        ```

4. **Install Python and Pip (if not already installed):**
    ```bash
    brew install python
    easy_install pip
    ```

5. **Install Python Dependencies:**
    ```bash
    pip install fastapi==0.68.0
    pip install huey==2.4.2
    ```

6. **Install Huey Optional Dependencies:**
    - Refer to [Huey Installation Guide](https://huey.readthedocs.io/en/latest/installation.html#using-git) for installation details.

7. **Run Dockerfile:**
    - After installing Docker, build the Docker image:
        ```bash
        docker build -t chaitraboggaram/k8s-key-value-store:latest .
        ```

8. **Run Makefile:**
    - If you have a Makefile for your project, you can run it to perform various tasks. For example:
        ```bash
        make install-dependencies
        ```

9. **requirements.txt:**
    - You can use a requirements.txt file to manage Python dependencies. Create or update the file with the required dependencies:
        ```plaintext
        # requirements.txt
        fastapi==0.68.0
        huey==2.4.2
        uvicorn[standard]
        ```

    - Install Python dependencies from requirements.txt:
        ```bash
        pip install -r requirements.txt
        ```

10. **Start MiniKube with Docker driver:**
    ```bash
    minikube start --driver=docker
    ```

To check if the minikube is successfully installed.
minikube status

