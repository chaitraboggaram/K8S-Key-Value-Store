# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

## Create a network and add conatiners to the network

```bash
docker network create my-network
```
Make sure docker application is open and running

</br>

## Building Docker Image

Build the Docker file with the prerequisites locally using

```bash
docker compose up --build
```
Run producer, consumer and redis seperately in 3 different terminals and have them running as below
![Alt text](images/docker-compose.png)

</br>

## Running Docker Compose

After a successful build, for subsequent runs, use:

```bash
docker-compose up
```

This will start the necessary containers and services.

</br>

## Redis CLI Commands to Test
1. Login Redis Container

```bash
docker exec -it <RedisContainerID> /bin/bash
```

Run the following command to get the container ID:
```bash
docker ps
```

2. Once logged inside Redis Container, login to CLI
```bash
redis-cli
```

3. Commands to test
```bash
keys *
```
To get all keys

```bash
SET key "value"
```
Set key value pair

```bash
GET key
```
Get the key value pair

</br>


## Managing Data
#### POST key value pair
```bash
docker exec -it <ProducerContainerID> http POST http://localhost:8000/set/Key/Value
```
docker exec -it 6c876c6250bb http POST http://localhost:8000/set/Key/Value


#### GET value for specific key
```bash
docker exec -it <ProducerContainerID> http GET http://localhost:8000/get/Key
```
docker exec -it 6c876c6250bb http GET http://localhost:8000/get/Key

#### Update value for a particular key
```bash
docker exec -it <ProducerContainerID> http PUT http://localhost:8000/update/Key/NewValue
```
#### Delete a key value pair
```bash
docker exec -it <ProducerContainerID> http DELETE http://localhost:8000/delete/Key
```
</br>

## Other commands
To obtain the required images, use the following commands:

```bash
docker images
```

Views all the containers in my network
```bash
docker network inspect my-network
```

Get IP of container
```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <ContainerID>
```
</br>

Stop all running docker containers
```bash
docker stop $(docker ps -aq)
```

Remove all docker images from your machine
```bash
docker rmi $(docker images -q)
```

To force delete images use
```bash
docker rmi -f $(docker images -q)
```

To view all networks
```bash
docker network ls
```

docker login -u "chaitraboggaram" -p "Padhu@1996" docker.io

docker tag consumer:latest k8s-key-value-store:consumer
docker tag producer:latest k8s-key-value-store:producer
docker tag redis:latest k8s-key-value-store:redis

cd to redis
docker build -t chaitraboggaram/k8s-key-value-store:redis .
docker push chaitraboggaram/k8s-key-value-store:redis

cd to producer
docker build -t chaitraboggaram/k8s-key-value-store:producer .
docker push chaitraboggaram/k8s-key-value-store:producer

cd to consumer
docker build -t chaitraboggaram/k8s-key-value-store:consumer .
docker push chaitraboggaram/k8s-key-value-store:consumer

Creating pods and network for pods
cd k8s
kubectl apply -f producer-pod.yaml
kubectl apply -f consumer-pod.yaml
kubectl apply -f producer-service.yaml
kubectl apply -f consumer-service.yaml
kubectl apply -f loadbalancer-service.yaml
kubectl apply -f redis-primary-service.yaml
kubectl apply -f redis-secondary-service.yaml
kubectl apply -f redis-primary.yaml
kubectl apply -f redis-secondary.yaml
kubectl apply -f loadbalancer-service.yaml
kubectl apply -f network-policy.yaml

Get all pods
kubectl get pods

Deleting pods
kubectl delete pod redis-pod producer-pod consumer-pod
kubectl delete pods --all

minikube dashboard

Deleting services
kubectl get services
kubectl delete service redis-service consumer-service producer-service

Delete everything
kubectl delete all --all

kubectl exec -it <producer-pod-name> --container <container-name> http POST http://<producer-service-name>:8000/set/Key/Value
kubectl exec -it producer-79544f6d68-4blzh --container producer http POST http://producer-service:8000/set/Key1/Value1

Get loadbalancer port
kubectl get services my-loadbalancer-service --output='jsonpath="{.spec.ports[0].nodePort}"'

Get minikube IP
minikube ip

Combination of these 2 gives for example: http://192.168.49.2:31181

To get external IP for loadbalancer, have this running in 1 terminal window
minikube tunnel

Check if external IP is assigned
kubectl get services my-loadbalancer-service

kubernetes cluster info
kubectl cluster-info | grep 'Kubernetes master'
kubectl config view --minify | grep server

http POST http://192.168.49.2:32122/set/Key1/Value1

http POST http://127.0.0.1:8000/set/Key1/Value1

Port forwarding 
kubectl port-forward service/my-loadbalancer-service 8000:80

http POST http://127.0.0.1:8000/set/Key1/Value1

Create a Service using kubectl 
kubectl expose deployment consumer --port=80 --target-port=8080 \
        --name=loadbalancer-consumer --type=LoadBalancer

kubectl expose deployment producer --port=80 --target-port=8000


minikube service k8s-key-value-store-service --url

Login to pod with 1 container
kubectl exec -it consumer-579f8c79db-pzshd -- /bin/bash


Login to a container inside kubernetes pod
kubectl exec -it producer-79544f6d68-4blzh --container producer -- sh

kubectl exec -it producer-85dc9f9dbd-trckw --container producer -- sh -c 'http POST http://producer-service:8000/set/Key1/Value1'



In Kubernetes directory
kubectl apply -f deployment.yaml
Creates 3 containers inside 1 pod

Login to particular container inside pod
kubectl exec -it <PodName> -c <ContainerName> -- /bin/bash
kubectl exec -it app-7667fb7d8-hz6g9 -c producer -- /bin/bash
http localhost:8000
http POST http://localhost:8000/set/Key/Value --> Did not work


Start again
kubectl delete all --all

Do all changes in the docker containers
docker push chaitraboggaram/k8s-key-value-store-consumer:latest
docker push chaitraboggaram/k8s-key-value-store-producer:latest
docker push chaitraboggaram/k8s-key-value-store-redis:latest


Install network pulgin
kubectl apply -f https://docs.projectcalico.org/v3.15/manifests/calico.yaml
kubectl get nodes

# Run a container based on the image
docker run -it chaitraboggaram/k8s-key-value-store:producer /bin/bash

kubectl apply -f producer-deployment.yaml
kubectl apply -f consumer-deployment.yaml
kubectl apply -f producer-service.yaml
kubectl apply -f consumer-service.yaml
kubectl apply -f loadbalancer-service.yaml
kubectl apply -f redis-primary-service.yaml
kubectl apply -f redis-primary.yaml
kubectl apply -f network-policy.yaml

Communicate between pods
kubectl get pods -o wide
Copy IP address of pod you want to test

kubectl exec <ConsumerPodName> -- curl http://<ProducerPodIP>:<ProducerPodPort>
kubectl exec consumer-579f8c79db-pzshd -- curl http://10.244.0.28:6379
kubectl exec -it consumer-579f8c79db-pzshd -- redis-cli -h 10.244.0.28 -p 6379

kubectl logs <PodName>
kubectl logs consumer-579f8c79db-pzshd


kubectl exec -it consumer-57b8877f55-nxkb2 -- /bin/bash

Connect to redis cli from consumer pod
apt-get update
apt-get install redis-tools
pip install redis-cli
redis-cli -h redis-primary-service


Post keys
kubectl exec -it producer-9db84d6cd-76r9s --container producer -- sh -c 'http POST http://producer-service:8000/set/Key1/Value1'


REDIS_HOST = os.environ.get("REDIS_HOST", "redis-primary-service", "127.0.0.1", "localhost")

Make sure to get this command running on consumer
python /usr/local/lib/python3.11/site-packages/huey/bin/huey_consumer.py main.huey

