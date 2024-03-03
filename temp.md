minikube tunnel
minikube service loadbalancer-service --url
http://127.0.0.1:57000

curl -X POST http://127.0.0.1:8000/set/Key1/Value1
curl http://127.0.0.1:8000/get/Key1

