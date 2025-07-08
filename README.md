# python_projects
100 Days of Code: The Complete Python Pro Bootcamp
Hello , this is created in remote

alertmanagerconfig.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: alertmanager-config
data:
  alertmanager.yml: |
    route:
      receiver: webhook
    receivers:
    - name: webhook
      webhook_configs:
      - url: 'http://webhook-service.default.svc.cluster.local:5001/alert'

alertmanagerdeoyment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: alertmanager
spec:
  replicas: 1
  selector:
    matchLabels:
      app: alertmanager
  template:
    metadata:
      labels:
        app: alertmanager
    spec:
      containers:
      - name: alertmanager
        image: prom/alertmanager
        ports:
        - containerPort: 9093
        volumeMounts:
        - name: config-volume
          mountPath: /etc/alertmanager
      volumes:
      - name: config-volume
        configMap:
          name: alertmanager-config

alertmanagerservice.yaml
apiVersion: v1
kind: Service
metadata:
  name: alertmanager-service
spec:
  selector:
    app: alertmanager
  ports:
    - protocol: TCP
      port: 9093
      targetPort: 9093
Update prometheus.yml to include:
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - alertmanager-service:9093

 webhook.py
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def handle_alert():
    data = request.json
    print("Received alert:", data)

    for alert in data.get("alerts", []):
        name = alert["labels"].get("alertname")
        if name == "HighLatency":
            # Example: Restart webapp deployment
            subprocess.run(["kubectl", "rollout", "restart", "deployment/webapp"])
        elif name == "HighCPU":
            # Example: Scale up replicas to 3
            subprocess.run(["kubectl", "scale", "deployment/webapp", "--replicas=3"])
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

webhook-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webhook-handler
spec:
  replicas: 1
  selector:
    matchLabels:
      app: webhook-handler
  template:
    metadata:
      labels:
        app: webhook-handler
    spec:
      containers:
      - name: webhook-handler
        image: <your-dockerhub-username>/webhook-handler
        ports:
        - containerPort: 5001
webhookservice.yaml
apiVersion: v1
kind: Service
metadata:
  name: webhook-service
spec:
  selector:
    app: webhook-handler
  ports:
    - port: 5001
      targetPort: 5001

✅ Example Flow
	1.	You hit /api/get and cause latency
	2.	Prometheus evaluates HighLatency rule
	3.	Alert fires and is sent to Alertmanager
	4.	Alertmanager sends alert to your webhook
	5.	Webhook restarts pods or scales up

⸻

✅ Bonus: Autoscaling via HPA

You already have HPA set up — it will handle scaling based on CPU.

This automation fills in other gaps like restarts or manual scale triggers when metrics like latency go high.

 📊 End-to-End Architecture Overview

You’ve built a self-healing and scalable system for a Flask web application deployed on Kubernetes, monitored by Prometheus. It can automatically restart pods, scale replicas, or take other actions when alerts are triggered.

Component
Role
Flask App
Web API providing /api/get and /metrics endpoints
Kubernetes
Orchestrates app deployment, service, scaling, and pod management
Prometheus
Monitors app metrics and evaluates alerting rules
Alertmanager
Receives alerts and routes them to a webhook
Webhook Handler
Listens for alerts and executes automated actions (e.g. restart pods)

system flow visual summry 
User Hit: /api/get
        ↓
Flask App Handles Request
        ↓
/metrics exposes latency, CPU, etc.
        ↓
Prometheus scrapes /metrics every 15s
        ↓
Alert rule checks: latency > 0.5s, CPU > 80%
        ↓
[If Alert Condition True]
Prometheus → Alertmanager → Webhook Handler
        ↓
Webhook takes action:
  - Restart pod
  - Scale replicas
  - Update resource limits

