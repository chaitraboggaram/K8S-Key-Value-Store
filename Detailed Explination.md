# K8S-Key-Value-Store

- [Pre-requisites](#pre-requisites)
- [Working with Kubernetes Pods and Services](#working-with-kubernetes-pods-and-services)
  - [Start Minikube](#start-minikube)
  - [Apply Kubernetes Configuration](#apply-kubernetes-configuration)
  - [Install Network Plugin](#install-network-plugin)
  - [Post Key-Value Pair to Redis](#post-key-value-pair-to-redis)
  - [Get Keys for Specific Key](#get-keys-for-specific-key)
  - [Path to Huey Consumer File](#path-to-huey-consumer-file)
  - [Check Deployments, Pods, and Services](#check-deployments-pods-and-services)
  - [Connecting to Any Pod](#connecting-to-any-pod)
  - [Connect to Redis CLI from Any Pod](#connect-to-redis-cli-from-any-pod)
- [Other Useful Commands](#other-useful-commands)
  - [Deleting Pods](#deleting-pods)
  - [Deleting Services](#deleting-services)
  - [Completely Clean the Kubernetes Cluster](#completely-clean-the-kubernetes-cluster)
  - [Open Minikube Dashboard](#open-minikube-dashboard)
  - [Get Minikube IP](#get-minikube-ip)
  - [Port Forwarding](#port-forwarding)
  - [Create a Service using kubectl or Exposing Producer Ports](#create-a-service-using-kubectl-or-exposing-producer-ports)
  - [Check for Logs in the Pods](#check-for-logs-in-the-pods)
- [Deploying Key-Value-Store on Docker Container](#deploying-key-value-store-on-docker-container)
  - [Create a Network and Add Containers to the Network](#create-a-network-and-add-containers-to-the-network)
- [Building Docker Image](#building-docker-image)
- [Running Docker Compose](#running-docker-compose)
- [Pushing the Docker Images to Docker Registry](#pushing-the-docker-images-to-docker-registry)
- [Redis CLI Commands to Test](#redis-cli-commands-to-test)
- [Managing Data](#managing-data)
  - [POST Key-Value Pair](#post-key-value-pair)
  - [GET Value for a Specific Key](#get-value-for-a-specific-key)
- [Other Commands](#other-commands)
  - [Obtain Required Images](#obtain-required-images)
  - [View All Containers in My Network](#view-all-containers-in-my-network)
  - [Get IP of the Container](#get-ip-of-the-container)
  - [Stop All Running Docker Containers](#stop-all-running-docker-containers)
  - [Remove All Docker Images from Your Machine](#remove-all-docker-images-from-your-machine)
  - [Force Delete Images](#force-delete-images)
  - [View All Networks](#view-all-networks)

---

## Pre-requisites

1. Install Homebrew

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install Docker

    - Download Docker from [Docker Documentation](https://docs.docker.com/) based on your Operating System. Sign up with your email address.
    - Check Docker version:

        ```bash
        docker --version
        ```

3. Install MiniKube

    ```bash
    brew install minikube
    ```
    
## Working with Kubernetes Pods and Services

### Start Minikube

```bash
minikube start
```

### Apply Kubernetes Configuration

```bash
kubectl apply -f <FileName>.yaml
```

### Install Network Plugin

```bash
kubectl apply -f https://docs.projectcalico.org/v3.15/manifests/calico.yaml
```

### Check Deployments, Pods, and Services

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Use -o wide to get more details about pods and services for example `kubectl get pods -o wide`

### Post Key-Value Pair to Redis

```bash
kubectl exec -it <ProducerPodName> -- sh -c 'http POST http://producer-service:8000/set/Key5/Value5'
```

### Get Keys for Specific Key

```bash
kubectl exec -it <ProducerPodName> -- sh -c 'http GET http://producer-service:8000/get/Key5'
```

### Path to Huey Consumer File

```bash
python /usr/local/lib/python3.11/site-packages/huey/bin/huey_consumer.py main.huey
```


### Connecting to Any Pod

```bash
kubectl exec -it <PodName> -- /bin/bash
```

### Connect to Redis CLI from Any Pod

```bash
redis-cli -h redis-primary-service -p 6379
```

## Other Useful Commands

### Deleting Pods

Note deleting pod is similar to refresh of pod, just in case the pod does not get updated with configuration changes in deployment or services file

```bash
kubectl delete pod <PodName>

# Delete all pods
kubectl delete pods --all
```

### Deleting Services

```bash
kubectl get services
kubectl delete service redis-service consumer-service producer-service
```

### Completely Clean the Kubernetes Cluster

```bash
# Note that this is not recommended
kubectl delete all --all
```

### Open Minikube Dashboard

```bash
minikube dashboard
```

### Get Minikube IP

```bash
minikube ip
```

### Port Forwarding

```bash
kubectl port-forward service/my-loadbalancer-service 8000:80
```

### Create a Service using kubectl or Exposing Producer Ports

```bash
kubectl expose deployment consumer --port=80 --target-port=8080 \
        --name=loadbalancer-consumer --type=LoadBalancer
```

OR

```bash
kubectl expose deployment producer --port=80 --target-port=8000
```

### Check for Logs in the Pods

```bash
kubectl logs <PodName>
```

## Deploying Key-Value-Store on Docker Container

You can clone the content from [GitHub Repository](https://github.com/chaitraboggaram/K8S-Key-Value-Store/commit/a2f3054617aa62f75ff3fe72bdbe26bf986b5291)

### Create a Network and Add Containers to the Network

```bash
docker login -u <UserName> -p <Password> docker.io

docker network create my-network
```

Make sure the Docker application is open and running.

## Building Docker Image

Build the Docker file with the prerequisites locally using

```bash
docker compose up --build
```

Run producer, consumer, and Redis separately in 3 different terminals and have them running as below:
![Docker Compose](images/docker-compose.png)

## Running Docker Compose

After a successful build, for subsequent runs, use:

```bash
docker-compose up
```

### Pushing the Docker Images to Docker Registry

```bash
docker push <DockerUserName>/<RepositoryName>:latest
```

This will start the necessary containers and

 services.

### Redis CLI Commands to Test

1. To Login to Container

```bash
docker exec -it <RedisContainerID> /bin/bash
```

Run the following command to get the container ID:

```bash
docker ps
```

2. Once logged inside the Redis Container, login to the CLI

```bash
redis-cli
```

3. Commands to test

- To get all keys
```bash
keys *
```

- Set key-value pair
```bash
SET key "value"
```

- Get key-value pair
```bash
GET key
```


## Managing Data

### POST key-value pair

```bash
docker exec -it <ProducerContainerID> http POST http://localhost:8000/set/Key/Value
```

### GET value for a specific key

```bash
docker exec -it <ProducerContainerID> http GET http://localhost:8000/get/Key
```

## Other Commands

### Obtain Required Images

```bash
docker images
```

### View all the containers in my network

```bash
docker network inspect my-network
```

### Get IP of the container

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <ContainerID>
```

### Stop all running Docker containers

```bash
docker stop $(docker ps -aq)
```

### Remove all Docker images from your machine

```bash
docker rmi $(docker images -q)
```

### To force delete images use

```bash
docker rmi -f $(docker images -q)
```

### To view all networks

```bash
docker network ls
```