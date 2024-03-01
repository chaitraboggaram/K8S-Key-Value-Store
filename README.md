# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

## Create a network and add conatiners to the network

```bash
docker network create my-network
```
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

#### GET value for specific key
```bash
docker exec -it <ProducerContainerID> http GET http://localhost:8000/get/Key
```

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