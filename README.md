# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.

## Building Docker Image

Build the Docker file with the prerequisites locally using:

```bash
docker compose up --build
```
Run producer, consumer and redis seperately in 3 different terminals and have them running as below
![Alt text](images/docker-compose.png)


## Running Docker Compose

After a successful build, for subsequent runs, use:

```bash
docker-compose up
```

This will start the necessary containers and services.


## Redis CLI Commands to Test
1. Login Redis Container

```bash
docker exec -it <RedisContainerID> /bin/bash
Run `docker ps` to get container ID
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

## Create a network and add conatiners to the network

```bash
docker network create my-network
docker run --name redis --network my-network -d redis
docker run --name producer-container --network my-network -d producer-web
docker run --name consumer-container --network my-network -d consumer-web
```
</br>

### Other commands
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

#### POST key value pair
```bash
curl -X POST -d "value=Value2" http://<ContainerIP>:8000/set/Key2
```

#### GET value for specific key
```bash
docker exec -it ba653fa08bd8 http GET http://localhost:8000/get/Key3
```