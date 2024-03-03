KUBECTL := kubectl
SLEEP_DURATION := 2

create:
	cd k8s && \
	$(KUBECTL) apply -f https://docs.projectcalico.org/v3.15/manifests/calico.yaml && \
	$(KUBECTL) apply -f producer-deployment.yaml && \
	$(KUBECTL) apply -f consumer-deployment.yaml && \
	$(KUBECTL) apply -f producer-service.yaml && \
	$(KUBECTL) apply -f consumer-service.yaml && \
	$(KUBECTL) apply -f loadbalancer-service.yaml && \
	$(KUBECTL) apply -f redis-primary-service.yaml && \
	$(KUBECTL) apply -f redis-primary.yaml && \
	$(KUBECTL) apply -f redis-secondary-service.yaml && \
	$(KUBECTL) apply -f redis-secondary.yaml && \
	$(KUBECTL) apply -f network-policy.yaml && \
	$(KUBECTL) apply -f configmap.yaml && \
	$(KUBECTL) apply -f producer-autoscale.yaml && \
	$(KUBECTL) apply -f consumer-autoscale.yaml && \
	$(KUBECTL) create configmap redis-config-map --from-file=redis.conf && \
	minikube addons enable metrics-server && \
	sleep $(SLEEP_DURATION) && \
	minikube tunnel

test:
	curl -X POST http://localhost:8000/set/Key1/Value1 && \
	sleep $(SLEEP_DURATION) && \
	curl http://127.0.0.1:8000/get/Key1

load-test:
	kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://loadbalancer-service:8000/get/Key1; done"

deploy:
	cd k8s && \
	$(KUBECTL) apply -f https://docs.projectcalico.org/v3.15/manifests/calico.yaml && \
	$(KUBECTL) apply -f producer-deployment.yaml && \
	$(KUBECTL) apply -f consumer-deployment.yaml && \
	$(KUBECTL) apply -f producer-service.yaml && \
	$(KUBECTL) apply -f consumer-service.yaml && \
	$(KUBECTL) apply -f loadbalancer-service.yaml && \
	$(KUBECTL) apply -f redis-primary-service.yaml && \
	$(KUBECTL) apply -f redis-primary.yaml && \
	$(KUBECTL) apply -f redis-secondary-service.yaml && \
	$(KUBECTL) apply -f redis-secondary.yaml && \
	$(KUBECTL) apply -f network-policy.yaml && \
	$(KUBECTL) apply -f configmap.yaml && \
	$(KUBECTL) apply -f producer-autoscale.yaml && \
	$(KUBECTL) apply -f consumer-autoscale.yaml
	
clean:
	cd k8s && \
	$(KUBECTL) delete -f https://docs.projectcalico.org/v3.15/manifests/calico.yaml && \
	$(KUBECTL) delete -f producer-deployment.yaml && \
	$(KUBECTL) delete -f consumer-deployment.yaml && \
	$(KUBECTL) delete -f producer-service.yaml && \
	$(KUBECTL) delete -f consumer-service.yaml && \
	$(KUBECTL) delete -f loadbalancer-service.yaml && \
	$(KUBECTL) delete -f redis-primary-service.yaml && \
	$(KUBECTL) delete -f redis-primary.yaml && \
	$(KUBECTL) delete -f redis-secondary-service.yaml && \
	$(KUBECTL) delete -f redis-secondary.yaml && \
	$(KUBECTL) delete -f network-policy.yaml && \
	$(KUBECTL) delete -f configmap.yaml && \
	$(KUBECTL) delete -f producer-autoscale.yaml && \
	$(KUBECTL) delete -f consumer-autoscale.yaml && \
	$(KUBECTL) delete configmap redis-config-map