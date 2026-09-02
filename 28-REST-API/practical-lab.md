# REST API – Practical Lab

## 1. Lab Objective

In this lab, we will practice REST API concepts using Linux and `curl`.

We will learn how to:

* Send GET requests
* Send POST requests
* Send PUT requests
* Send PATCH requests
* Send DELETE requests
* Work with JSON
* Use HTTP headers
* Check HTTP status codes
* Test API response time
* Troubleshoot DNS, TCP, TLS, and HTTP
* Create an API health-check script
* Test a REST API locally
* Test APIs in Docker
* Test APIs in Kubernetes

---

# 2. Prerequisites

Make sure these commands work:

```bash
curl --version
```

```bash
jq --version
```

```bash
docker --version
```

```bash
kubectl version --client
```

Optional:

```bash
dig -v
```

```bash
openssl version
```

---

# 3. Lab 1 – Test a Public HTTPS Endpoint

Run:

```bash
curl https://example.com
```

You should receive an HTML response.

Now show headers:

```bash
curl -i https://example.com
```

Verbose mode:

```bash
curl -v https://example.com
```

### Observe

Look for:

```text
HTTP status code
Response headers
TLS connection
Server information
Response body
```

---

# 4. Lab 2 – Check HTTP Status Code

Run:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Expected:

```text
200
```

This is useful for automation and CI/CD health checks.

---

# 5. Lab 3 – Check Response Time

Run:

```bash
curl -o /dev/null -s \
-w "HTTP Status: %{http_code}\nResponse Time: %{time_total}s\n" \
https://example.com
```

Example:

```text
HTTP Status: 200
Response Time: 0.25s
```

---

# 6. Lab 4 – Test DNS

Run:

```bash
dig +short example.com
```

If `dig` is not installed:

```bash
sudo apt update
sudo apt install dnsutils -y
```

Then:

```bash
dig +short example.com
```

Alternative:

```bash
nslookup example.com
```

### Understand the flow

```text
example.com
     |
     ↓
    DNS
     |
     ↓
   IP Address
```

---

# 7. Lab 5 – Test TCP Connectivity

HTTPS normally uses TCP port `443`.

Run:

```bash
nc -vz example.com 443
```

If `nc` is not installed:

```bash
sudo apt install netcat-openbsd -y
```

Then:

```bash
nc -vz example.com 443
```

You should see a successful connection if the host and port are reachable.

---

# 8. Lab 6 – Test TLS

Run:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

Look for:

```text
Certificate
Protocol
Cipher
Verify return code
```

Exit:

```text
Ctrl + C
```

---

# 9. Lab 7 – Test HTTP Headers

Run:

```bash
curl -I https://example.com
```

You may see headers such as:

```text
HTTP/1.1 200 OK
Content-Type
Content-Length
Server
Date
```

---

# 10. Lab 8 – Test GET Request

Use a public test API:

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

The response should contain JSON.

Example structure:

```json
{
  "userId": 1,
  "id": 1,
  "title": "...",
  "body": "..."
}
```

---

# 11. Lab 9 – Pretty Print JSON

Run:

```bash
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq
```

This makes JSON easier to read.

---

# 12. Lab 10 – Extract JSON Data

Get the title:

```bash
curl -s \
https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
```

Get the ID:

```bash
curl -s \
https://jsonplaceholder.typicode.com/posts/1 | jq '.id'
```

Get multiple fields:

```bash
curl -s \
https://jsonplaceholder.typicode.com/posts/1 | jq '.id, .title'
```

---

# 13. Lab 11 – GET Multiple Resources

Run:

```bash
curl -s \
https://jsonplaceholder.typicode.com/posts | jq '.[0:5]'
```

This displays the first five objects.

Count objects:

```bash
curl -s \
https://jsonplaceholder.typicode.com/posts | jq 'length'
```

---

# 14. Lab 12 – POST Request

Send a POST request:

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
  "title": "REST API Lab",
  "body": "Learning REST APIs",
  "userId": 1
}' \
https://jsonplaceholder.typicode.com/posts
```

The API should return a created resource.

Check the HTTP status:

```bash
curl -o /dev/null -s \
-w "%{http_code}\n" \
-X POST \
-H "Content-Type: application/json" \
-d '{"title":"REST API Lab","body":"Learning REST APIs","userId":1}' \
https://jsonplaceholder.typicode.com/posts
```

---

# 15. Lab 13 – PUT Request

Run:

```bash
curl -X PUT \
-H "Content-Type: application/json" \
-d '{
  "id": 1,
  "title": "Updated REST API",
  "body": "Updated content",
  "userId": 1
}' \
https://jsonplaceholder.typicode.com/posts/1
```

---

# 16. Lab 14 – PATCH Request

Run:

```bash
curl -X PATCH \
-H "Content-Type: application/json" \
-d '{
  "title": "Partially Updated Title"
}' \
https://jsonplaceholder.typicode.com/posts/1
```

Difference:

```text
PUT
→ Replace/update the resource representation

PATCH
→ Partially update the resource
```

---

# 17. Lab 15 – DELETE Request

Run:

```bash
curl -X DELETE \
https://jsonplaceholder.typicode.com/posts/1
```

Check status:

```bash
curl -o /dev/null -s \
-w "%{http_code}\n" \
-X DELETE \
https://jsonplaceholder.typicode.com/posts/1
```

---

# 18. Lab 16 – Use Custom Headers

Run:

```bash
curl \
-H "Accept: application/json" \
-H "User-Agent: DevOps-Lab" \
https://jsonplaceholder.typicode.com/posts/1
```

Inspect the request:

```bash
curl -v \
-H "Accept: application/json" \
https://jsonplaceholder.typicode.com/posts/1
```

---

# 19. Lab 17 – Query Parameters

Run:

```bash
curl \
"https://jsonplaceholder.typicode.com/posts?userId=1"
```

Pretty print:

```bash
curl -s \
"https://jsonplaceholder.typicode.com/posts?userId=1" | jq
```

This demonstrates query parameters.

---

# 20. Lab 18 – Path Parameters

Run:

```bash
curl \
https://jsonplaceholder.typicode.com/posts/1
```

Here:

```text
/posts/1
        ↑
   Resource ID
```

The `1` is a path parameter.

---

# 21. Lab 19 – Save API Response

Run:

```bash
curl -s \
https://jsonplaceholder.typicode.com/posts/1 \
-o post.json
```

Check:

```bash
cat post.json
```

Pretty print:

```bash
jq . post.json
```

Check file:

```bash
ls -lh post.json
```

---

# 22. Lab 20 – Build a Local REST API

Now create a small REST API locally.

Create a directory:

```bash
mkdir -p ~/rest-api-lab
cd ~/rest-api-lab
```

Create a Python application:

```bash
nano app.py
```

Add:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class APIHandler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        response = json.dumps(data).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {
                "status": "healthy"
            })

        elif self.path == "/api/users":
            self.send_json(200, {
                "users": [
                    {
                        "id": 1,
                        "name": "Shraddha",
                        "role": "DevOps Engineer"
                    }
                ]
            })

        else:
            self.send_json(404, {
                "error": "Resource not found"
            })

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), APIHandler)

    print("REST API running on port 8080")

    server.serve_forever()
```

Save:

```text
Ctrl + O
Enter
Ctrl + X
```

---

# 23. Lab 21 – Start the Local API

Run:

```bash
python3 app.py
```

You should see:

```text
REST API running on port 8080
```

Keep this terminal running.

---

# 24. Lab 22 – Test Local Health Endpoint

Open another terminal.

Run:

```bash
curl http://localhost:8080/health
```

Expected:

```json
{
  "status": "healthy"
}
```

Pretty print:

```bash
curl -s http://localhost:8080/health | jq
```

---

# 25. Lab 23 – Test Local Users Endpoint

Run:

```bash
curl http://localhost:8080/api/users
```

Pretty print:

```bash
curl -s http://localhost:8080/api/users | jq
```

---

# 26. Lab 24 – Test 404 Error

Run:

```bash
curl -i http://localhost:8080/unknown
```

Expected status:

```text
404
```

This demonstrates API error handling.

---

# 27. Lab 25 – Check Listening Port

Run:

```bash
ss -ltnp | grep :8080
```

You should see the Python process listening on port `8080`.

You can also run:

```bash
ss -ltnp
```

---

# 28. Lab 26 – Test API Response Time

Run:

```bash
curl -o /dev/null -s \
-w "Status: %{http_code}\nTime: %{time_total}s\n" \
http://localhost:8080/health
```

---

# 29. Lab 27 – Create an API Health Check

Create:

```bash
nano health-check.sh
```

Add:

```bash
#!/bin/bash

URL="http://localhost:8080/health"

STATUS=$(curl -o /dev/null -s \
-w "%{http_code}" \
"$URL")

if [ "$STATUS" -eq 200 ]; then
    echo "API is healthy: HTTP $STATUS"
else
    echo "API is unhealthy: HTTP $STATUS"
    exit 1
fi
```

Make executable:

```bash
chmod +x health-check.sh
```

Run:

```bash
./health-check.sh
```

Expected:

```text
API is healthy: HTTP 200
```

---

# 30. Lab 28 – Test API Failure

Stop the Python API:

```text
Ctrl + C
```

Run:

```bash
./health-check.sh
```

Now the health check should fail.

Start the API again:

```bash
python3 app.py
```

Run:

```bash
./health-check.sh
```

The check should pass again.

This demonstrates how a CI/CD pipeline can detect an unhealthy service.

---

# 31. Lab 29 – Dockerize the REST API

Inside:

```bash
cd ~/rest-api-lab
```

Create:

```bash
nano Dockerfile
```

Add:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

EXPOSE 8080

CMD ["python3", "app.py"]
```

Build:

```bash
docker build -t rest-api-lab .
```

Check image:

```bash
docker images | grep rest-api-lab
```

---

# 32. Lab 30 – Run REST API Container

Run:

```bash
docker run -d \
--name rest-api \
-p 8080:8080 \
rest-api-lab
```

Check:

```bash
docker ps
```

Test:

```bash
curl http://localhost:8080/health
```

Pretty print:

```bash
curl -s http://localhost:8080/health | jq
```

---

# 33. Lab 31 – Docker API Logs

Run:

```bash
docker logs rest-api
```

Follow logs:

```bash
docker logs -f rest-api
```

Stop following:

```text
Ctrl + C
```

---

# 34. Lab 32 – Docker API Troubleshooting

Check container:

```bash
docker ps
```

Check all containers:

```bash
docker ps -a
```

Inspect container:

```bash
docker inspect rest-api
```

Check port mapping:

```bash
docker port rest-api
```

Check logs:

```bash
docker logs rest-api
```

Test endpoint:

```bash
curl -v http://localhost:8080/health
```

---

# 35. Lab 33 – Kubernetes REST API Deployment

Create:

```bash
nano deployment.yaml
```

Add:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rest-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: rest-api
  template:
    metadata:
      labels:
        app: rest-api
    spec:
      containers:
        - name: rest-api
          image: rest-api-lab:latest
          imagePullPolicy: Never
          ports:
            - containerPort: 8080
```

Apply:

```bash
kubectl apply -f deployment.yaml
```

Check:

```bash
kubectl get pods
```

---

# 36. Lab 34 – Kubernetes Service

Create:

```bash
nano service.yaml
```

Add:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: rest-api
spec:
  selector:
    app: rest-api
  ports:
    - port: 80
      targetPort: 8080
```

Apply:

```bash
kubectl apply -f service.yaml
```

Check:

```bash
kubectl get svc
```

---

# 37. Lab 35 – Kubernetes Port Forward

Run:

```bash
kubectl port-forward svc/rest-api 8080:80
```

Open another terminal.

Test:

```bash
curl http://localhost:8080/health
```

Pretty print:

```bash
curl -s http://localhost:8080/health | jq
```

---

# 38. Lab 36 – Kubernetes Logs

Check Pods:

```bash
kubectl get pods
```

Get logs:

```bash
kubectl logs <pod-name>
```

Follow logs:

```bash
kubectl logs -f <pod-name>
```

---

# 39. Lab 37 – Kubernetes Service Troubleshooting

Check:

```bash
kubectl get svc
```

Then:

```bash
kubectl describe svc rest-api
```

Check endpoints:

```bash
kubectl get endpoints rest-api
```

Modern Kubernetes:

```bash
kubectl get endpointslices
```

If there are no endpoints, check Pod labels:

```bash
kubectl get pods --show-labels
```

The Service selector must match the Pod labels.

---

# 40. Lab 38 – Complete API Troubleshooting

Suppose:

```bash
curl https://api.example.com
```

fails.

Follow this sequence.

### Step 1 – DNS

```bash
dig +short api.example.com
```

### Step 2 – TCP

```bash
nc -vz api.example.com 443
```

### Step 3 – TLS

```bash
openssl s_client \
-connect api.example.com:443 \
-servername api.example.com
```

### Step 4 – HTTP

```bash
curl -v https://api.example.com
```

### Step 5 – Status Code

```bash
curl -o /dev/null -s \
-w "%{http_code}\n" \
https://api.example.com
```

### Step 6 – Application Logs

Docker:

```bash
docker logs <container>
```

Kubernetes:

```bash
kubectl logs <pod>
```

---

# 41. Lab 39 – Test Different HTTP Errors

You should understand these responses:

```text
200 → Success
201 → Resource Created
204 → No Content

400 → Bad Request
401 → Authentication Required
403 → Forbidden
404 → Not Found
429 → Too Many Requests

500 → Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout
```

Try to identify the cause from the status code before checking logs.

---

# 42. Lab 40 – DevOps API Health Check

Create:

```bash
nano api-monitor.sh
```

Add:

```bash
#!/bin/bash

URL="http://localhost:8080/health"

echo "Checking REST API..."
echo "URL: $URL"

RESULT=$(curl -o /dev/null -s \
-w "%{http_code} %{time_total}" \
"$URL")

STATUS=$(echo "$RESULT" | awk '{print $1}')
TIME=$(echo "$RESULT" | awk '{print $2}')

echo "HTTP Status: $STATUS"
echo "Response Time: ${TIME}s"

if [ "$STATUS" -eq 200 ]; then
    echo "API Status: HEALTHY"
    exit 0
else
    echo "API Status: UNHEALTHY"
    exit 1
fi
```

Make executable:

```bash
chmod +x api-monitor.sh
```

Run:

```bash
./api-monitor.sh
```

---

# 43. Lab 41 – CI/CD Simulation

Run:

```bash
./api-monitor.sh
```

If the API is healthy:

```text
API Status: HEALTHY
```

Exit code:

```bash
echo $?
```

Expected:

```text
0
```

If the API fails:

```text
API Status: UNHEALTHY
```

Exit code:

```text
1
```

This is how an API health check can be used in CI/CD.

---

# 44. Lab 42 – Final Architecture

After completing the labs, understand this architecture:

```text
                    Client
                       |
                       ↓
                     DNS
                       |
                       ↓
                 Load Balancer
                       |
                       ↓
                 Reverse Proxy
                       |
                       ↓
                    REST API
                       |
              ┌────────┴────────┐
              ↓                 ↓
          Application        Logging
              |
              ↓
           Database
```

In Kubernetes:

```text
Client
  |
  ↓
Ingress
  |
  ↓
Service
  |
  ↓
Deployment
  |
  ↓
Pods
```

---

# 45. Lab Verification Checklist

Check each item after completing the lab:

```text
[ ] curl installed
[ ] GET request tested
[ ] POST request tested
[ ] PUT request tested
[ ] PATCH request tested
[ ] DELETE request tested
[ ] JSON tested
[ ] jq used
[ ] HTTP headers inspected
[ ] HTTP status code checked
[ ] Response time checked
[ ] DNS tested
[ ] TCP connectivity tested
[ ] TLS tested
[ ] Local Python REST API created
[ ] Health endpoint tested
[ ] Health-check script created
[ ] Docker image built
[ ] Docker container tested
[ ] Docker logs checked
[ ] Kubernetes Deployment created
[ ] Kubernetes Service created
[ ] Port forwarding tested
[ ] Kubernetes logs checked
[ ] Kubernetes endpoints checked
[ ] API troubleshooting flow practiced
[ ] CI/CD-style health check tested
```

---

# 46. Key Learning

The most important troubleshooting pattern from this lab is:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Authentication
 ↓
Application
 ↓
Database
```

For a DevOps engineer, this sequence helps isolate REST API failures systematically.

---

# 47. Cleanup

Stop the local Python server:

```text
Ctrl + C
```

Remove Docker container:

```bash
docker rm -f rest-api
```

Remove Docker image if required:

```bash
docker rmi rest-api-lab
```

Delete Kubernetes resources:

```bash
kubectl delete -f deployment.yaml
```

```bash
kubectl delete -f service.yaml
```

Remove lab directory if you no longer need it:

```bash
rm -rf ~/rest-api-lab
```

**Only run the final cleanup command if you have finished the lab and no longer need the files.**
