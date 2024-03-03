KUBECTL := kubectl
SLEEP_DURATION := 10

.PHONY: deploy clean

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
	$(KUBECTL) create configmap redis-config-map --from-file=redis.conf

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
	$(KUBECTL) delete configmap redis-config-map