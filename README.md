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

Make sure you have this running in one terminal
redis-server

Docker in one

And then for inserting key value pair
http POST http://localhost:8000/set/my_key/my_value

http http://localhost:8000/get/my_key
