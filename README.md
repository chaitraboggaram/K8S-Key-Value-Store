# K8S-Key-Value-Store

Developing a key-value store using Kubernetes (K8s), FastAPI, and Huey as a REDIS queue on Apple M2 MacBook.


### Building Docker Image Locally

Build the Docker file with the prerequisites locally using:

```bash
docker compose up --build
```

Ensure that the base image is Python.


### Running Docker Compose

After a successful build, for subsequent runs, use:

```bash
docker-compose up
```

This will start the necessary containers and services.

### Docker Images

To obtain the required images, use the following commands:

```bash
docker images
```

Terminals
1. redis-server
2. Docker in one or uvicorn
3. huey_consumer.py main.huey --workers 1

And then for inserting key value pair
http POST http://localhost:8000/set/key1/value1
OR
curl -X POST "http://localhost:8000/set/my_key3/my_value3"

http GET http://localhost:8000/get/key1
OR
curl "http://localhost:8000/get/my_key2"



redis-cli
Opens Redis CLI

keys *
To get all keys

SET key "value"
Set key value pair

GET key
Get the key value pair

