# K8S-Key-Value-Store

### Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

</br>

## Table of Contents

- [**Pre-requisites**](#pre-requisites)
  - [1. Install Homebrew](#1-install-homebrew)
  - [2. Install Docker](#2-install-docker)
  - [3. Install MiniKube](#3-install-minikube)
- [**How to Start the K8S-Key-Value Service**](#how-to-start-the-k8s-key-value-service)
  - [1. Start Minikube](#1-start-minikube)
  - [2. Run the Makefile](#2-run-the-makefile)
  - [3. Check if Pods are Working](#3-check-if-pods-are-working)
  - [4. Post Key-Value Pair to Redis](#4-post-key-value-pair-to-redis)
  - [5. Get Keys for Specific Key](#5-get-keys-for-specific-key)
  - [6. Clean Installation](#6-clean-installation)
  - [7. Stop Minikube](#7-stop-minikube)
- [**In Case of Issues or Additional Commands**](#in-case-of-issues-or-additional-commands)
  - [Refer to Detailed Explanation.md](#refer-to-detailed-explanationmd)

</br>

---

### Pre-requisites

1. **Install Homebrew:**

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Install Docker:**

    - Download Docker from [Docker Documentation](https://docs.docker.com/) based on your Operating System. Sign up with your email address.
    - Check Docker version:

        ```bash
        docker --version
        ```

3. **Install MiniKube:**

    ```bash
    brew install minikube
    ```

</br>

---

### How to Start the K8S-Key-Value Service

1. **Start Minikube:**

    ```bash
    minikube start
    ```
If this does not start up or throw error especially for Apple Silicon Chip Macbooks, run `minikube start --driver=docker`

2. **Run the Makefile:**

    ```bash
    make
    ```

3. **Check if Pods are Working:**

    ```bash
    kubectl get pods
    ```

    Use `-o wide` to get more details about pods and services. For example, `kubectl get pods -o wide`.

4. **Post Key-Value Pair to Redis:**

    ```bash
    kubectl exec -it <ProducerPodName> -- sh -c 'http POST http://producer-service:8000/set/Key/Value'
    ```

5. **Get Keys for Specific Key:**

    ```bash
    kubectl exec -it <ProducerPodName> -- sh -c 'http GET http://producer-service:8000/get/Key'
    ```

6. **Clean Installation:**

    ```bash
    make clean 
    ```

7. **Stop Minikube:**

    ```bash
    minikube stop
    ```

### In case of any issues or for additional commands, refer to [Detailed Explanation.md](Detailed%20Explanation.md).