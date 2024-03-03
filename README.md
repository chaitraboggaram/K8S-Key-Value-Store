# K8S-Key-Value-Store

### Developing a key-value store using Kubernetes (K8s) with Minikube for clustering, Docker Containers as containers in minikube pods, FastAPI web framework for building APIs, and Huey as a REDIS queue and storage with replication and autoscaling.


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
  - [4. Start Minikube Tunnel](#4-start-minikube-tunnel)
  - [5. Post Key-Value Pair to Redis](#5-post-key-value-pair-to-redis)
  - [6. Get Keys for Specific Key](#6-get-keys-for-specific-key)
  - [7. Clean Installation](#7-clean-installation)
  - [8. Stop Minikube](#8-stop-minikube)
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

4. **Enable minikube metrics**
    ```bash
    minikube addons enable metrics-server
    ```
    This is optional to check for autoscaling metrics. Wait for 2 mins and then type `kubectl get hpa` to check the metrics

5. **Start Minikube Tunnel**

    ```bash
    minikube tunnel
    ```
    Minikube tunnel creates a secure tunnel to the minikube node, allowing external traffic to reach the node port and the service. In our example this gives external IP address for the loadbalancer i.e `127.0.0.1` or `localhost`. To test if the webserver is running access http://127.0.0.1:8000 on your browser.

6. **Post Key-Value Pair to Redis:**

    ```bash
    curl -X POST http://127.0.0.1:8000/set/Key1/Value1
    ```

7. **Get Keys for Specific Key:**

    ```bash
    curl http://127.0.0.1:8000/get/Key1
    ```

8. **Clean Installation:**

    ```bash
    make clean 
    ```

9. **Stop Minikube:**

    ```bash
    minikube stop
    ```

---

</br>

### Load Testing

1. **If you want to test load without any key pair**
```bash
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://loadbalancer-service:8000/; done"
```

2. **If you want to load test on an existing key**
```bash
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://loadbalancer-service:8000/get/Key1; done"
```
Wait for 2 mins to view the changes, you can run `kubectl get hpa` to check the metrics updates or run `kubectl get pods` number of pods that are running currently
### In case of any issues or for additional commands, refer to [Detailed Explanation.md](Detailed%20Explanation.md).