KUBECTL := kubectl
SLEEP_DURATION := 10

.PHONY: deploy

deploy:
	cd /Users/ipadhu/Documents/GitHub/K8S-Key-Value-Store/k8s && \
	$(KUBECTL) delete all --all && \
	$(KUBECTL) apply -f https://docs.projectcalico.org/v3.15/manifests/calico.yaml && \
	$(KUBECTL) apply -f producer-deployment.yaml && \
	$(KUBECTL) apply -f consumer-deployment.yaml && \
	$(KUBECTL) apply -f producer-service.yaml && \
	$(KUBECTL) apply -f consumer-service.yaml && \
	$(KUBECTL) apply -f loadbalancer-service.yaml && \
	$(KUBECTL) apply -f redis-primary-service.yaml && \
	$(KUBECTL) apply -f redis-primary.yaml && \
	$(KUBECTL) apply -f network-policy.yaml && \
	$(KUBECTL) apply -f configmap.yaml && \
	$(KUBECTL) create configmap redis-config-map --from-file=redis.conf && \
	sleep $(SLEEP_DURATION) && \
	$(KUBECTL) get pods -o wide
