# 🧪 Chapter 25 — HTTP & HTTPS Practical Lab

## 🎯 Objective

In this lab, I will practice:

* HTTP requests
* HTTP response codes
* HTTP headers
* `curl`
* HTTP methods
* DNS + HTTP troubleshooting
* Docker HTTP networking
* Kubernetes Service HTTP testing
* HTTPS
* TLS certificates
* Basic HTTP troubleshooting

---

# Lab 1 — Test HTTP Connectivity

## Step 1: Send an HTTP request

```bash
curl http://example.com
```

### Observation

The server returns an HTTP response containing HTML content.

---

## Step 2: Check HTTP headers

```bash
curl -I http://example.com
```

### Observation

Record:

```text
HTTP status:
Content-Type:
Server:
Location:
```

---

# Lab 2 — Test HTTPS

Run:

```bash
curl -I https://example.com
```

### Observation

Record:

```text
HTTP status:
Content-Type:
Server:
```

HTTPS uses TLS to protect communication between the client and server.

---

# Lab 3 — Verbose HTTP Troubleshooting

Run:

```bash
curl -v https://example.com
```

Observe:

```text
DNS resolution
TCP connection
TLS handshake
HTTP request
HTTP response
```

### Observation

Write what you observed:

```text
DNS:
TCP:
TLS:
HTTP:
Status:
```

---

# Lab 4 — Check HTTP Status Code

Run:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Expected type of output:

```text
200
```

### Observation

The HTTP status code indicates whether the request succeeded or failed.

---

# Lab 5 — Test Redirect

Run:

```bash
curl -I http://example.com
```

If the server redirects, look for:

```text
301
302
Location:
```

Now follow redirects:

```bash
curl -IL http://example.com
```

### Observation

Record:

```text
Initial status:
Redirect destination:
Final status:
```

---

# Lab 6 — Inspect TLS Certificate

Run:

```bash
openssl s_client -connect example.com:443
```

Look for certificate information.

You can stop the command using:

```text
Ctrl + C
```

### Observe

Find:

```text
Certificate
Issuer
Subject
TLS version
Cipher
```

---

# Lab 7 — Check Certificate Validity

Run:

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

Example:

```text
notBefore=...
notAfter=...
```

### Observation

Check the certificate's validity period.

---

# Lab 8 — Check Certificate Issuer

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -issuer
```

### Observation

Record the certificate issuer.

---

# Lab 9 — Check DNS

Run:

```bash
getent hosts example.com
```

Then:

```bash
dig example.com
```

### Observation

Record the resolved IP address.

```text
Domain:
IP:
```

---

# Lab 10 — Test HTTPS Port

Run:

```bash
nc -vz example.com 443
```

### Observation

A successful connection confirms that TCP connectivity to port 443 is available.

Remember:

```text
TCP connectivity ≠ complete HTTPS health
```

The TLS handshake and HTTP request still need to work.

---

# Lab 11 — Test HTTP Port

```bash
nc -vz example.com 80
```

### Observation

Check whether TCP port 80 is reachable.

---

# Lab 12 — Check Local Listening Ports

Run:

```bash
sudo ss -ltnp
```

Look for:

```text
:80
:443
```

### Observation

Record any web server processes listening on those ports.

---

# Lab 13 — Docker HTTP Server

Run an Nginx container:

```bash
docker run -d --name http-lab -p 8080:80 nginx
```

Check:

```bash
docker ps
```

Test:

```bash
curl -I http://localhost:8080
```

Expected result:

```text
HTTP/1.1 200 OK
```

---

## Step 2 — Verbose test

```bash
curl -v http://localhost:8080
```

### Observation

Record:

```text
Host port:
Container port:
HTTP status:
Server:
```

---

## Step 3 — Check container port

```bash
docker port http-lab
```

Expected type of output:

```text
80/tcp -> 0.0.0.0:8080
```

---

## Step 4 — Clean up

```bash
docker rm -f http-lab
```

Verify:

```bash
docker ps
```

---

# Lab 14 — Kubernetes HTTP Service

First check the existing services:

```bash
kubectl get svc
```

If your `web-app-nodeport` service still exists:

```bash
kubectl get svc web-app-nodeport
```

Expected format:

```text
NAME               TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)
web-app-nodeport   NodePort   10.x.x.x        <none>        80:30080/TCP
```

---

# Lab 15 — Check Kubernetes Pods

Run:

```bash
kubectl get pods -l app=web-app -o wide
```

Record:

```text
Pod:
Status:
Pod IP:
Node:
```

All selected pods should ideally be:

```text
Running
```

and:

```text
READY 1/1
```

---

# Lab 16 — Check Kubernetes Endpoints

Run:

```bash
kubectl get endpointslice \
  -l kubernetes.io/service-name=web-app-nodeport
```

### Observation

Verify that the Service has backend endpoints.

Example:

```text
10.244.0.4
10.244.0.5
10.244.0.6
```

This confirms that the Service selector is finding the application Pods.

---

# Lab 17 — Test Kubernetes ClusterIP

Get the ClusterIP:

```bash
kubectl get svc web-app-nodeport
```

Example:

```text
10.96.202.92
```

Start a temporary curl Pod:

```bash
kubectl run network-test \
  --rm -it \
  --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://10.96.202.92:80
```

### Expected

```text
HTTP/1.1 200 OK
```

### Observation

The request path is:

```text
Temporary Pod
      ↓
ClusterIP Service
      ↓
Kubernetes Service routing
      ↓
Web App Pod
      ↓
Nginx
```

---

# Lab 18 — Test Kubernetes NodePort

Find the node IP:

```bash
kubectl get nodes -o wide
```

Example:

```text
INTERNAL-IP
172.23.0.2
```

Test:

```bash
curl -v http://172.23.0.2:30080
```

### Expected

```text
HTTP/1.1 200 OK
Server: nginx/...
```

### Observation

The request path is:

```text
Host
 ↓
Node IP:30080
 ↓
NodePort
 ↓
Kubernetes Service
 ↓
Pod
 ↓
Nginx
```

---

# Lab 19 — Test localhost NodePort

Try:

```bash
curl -v http://127.0.0.1:30080
```

If it fails while the node IP works, do not immediately assume the Kubernetes Service is broken.

In containerized local Kubernetes environments such as Kind, the NodePort may be reachable through the container/node network address while not being published on the host's loopback interface.

Compare:

```bash
curl -v http://127.0.0.1:30080
```

with:

```bash
curl -v http://<NODE-IP>:30080
```

---

# Lab 20 — Check Kubernetes Service Configuration

Run:

```bash
kubectl describe svc web-app-nodeport
```

Check:

```text
Type:
IP:
Port:
TargetPort:
NodePort:
Selector:
Endpoints:
```

### Important relationship

```text
Service Port
     ↓
TargetPort
     ↓
Pod Port
```

For example:

```text
80
 ↓
80
 ↓
Nginx :80
```

---

# Lab 21 — Test Service Using DNS

Run:

```bash
kubectl run dns-http-test \
  --rm -it \
  --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://web-app-nodeport.default.svc.cluster.local
```

### Observation

This tests:

```text
Kubernetes DNS
       ↓
Service
       ↓
Pod
       ↓
HTTP
```

---

# Lab 22 — HTTP Headers

Run:

```bash
curl -I http://localhost:8080
```

If the Docker lab is running, inspect:

```text
Server:
Date:
Content-Type:
Content-Length:
Connection:
```

---

# Lab 23 — Test Different HTTP Methods

Use a test API or your own application endpoint.

GET:

```bash
curl -X GET https://example.com
```

POST:

```bash
curl -X POST https://example.com/api
```

PUT:

```bash
curl -X PUT https://example.com/api/1
```

PATCH:

```bash
curl -X PATCH https://example.com/api/1
```

DELETE:

```bash
curl -X DELETE https://example.com/api/1
```

### Observation

Record which methods the application accepts.

---

# Lab 24 — Test HTTP Errors

Test a nonexistent path:

```bash
curl -i https://example.com/this-page-does-not-exist
```

Look for:

```text
404 Not Found
```

### Observation

A 404 generally means the server/application could not find the requested resource.

---

# Lab 25 — HTTP Health Check

Run:

```bash
curl -f https://example.com
```

Check the shell exit code:

```bash
echo $?
```

A successful request generally returns:

```text
0
```

---

# Lab 26 — Measure Response Time

Run:

```bash
curl -o /dev/null -s \
  -w "Status: %{http_code}\nTime: %{time_total}s\n" \
  https://example.com
```

Record:

```text
Status:
Response time:
```

---

# Lab 27 — Inspect HTTP Traffic

For plain HTTP:

```bash
sudo tcpdump -i any port 80
```

In another terminal, run:

```bash
curl http://example.com
```

Stop tcpdump:

```text
Ctrl + C
```

### Observation

You can observe network packets associated with HTTP traffic.

---

# Lab 28 — Inspect HTTPS Traffic

Run:

```bash
sudo tcpdump -i any port 443
```

In another terminal:

```bash
curl https://example.com
```

### Observation

You can observe packets, but HTTPS application data is encrypted by TLS.

---

# Lab 29 — Troubleshooting Exercise

Imagine:

```text
curl https://myapp.example.com
```

returns:

```text
502 Bad Gateway
```

Follow this workflow:

### Step 1 — DNS

```bash
dig myapp.example.com
```

### Step 2 — TCP

```bash
nc -vz myapp.example.com 443
```

### Step 3 — TLS

```bash
openssl s_client -connect myapp.example.com:443
```

### Step 4 — HTTP

```bash
curl -v https://myapp.example.com
```

### Step 5 — Check reverse proxy

```bash
sudo ss -ltnp
```

### Step 6 — Check application

Test the backend directly if accessible:

```bash
curl -v http://<BACKEND-IP>:<PORT>
```

### Step 7 — Kubernetes

If the application runs in Kubernetes:

```bash
kubectl get pods
kubectl get svc
kubectl get endpointslice
```

---

# 🧠 Lab Observations Summary

Complete this table after performing the labs:

| Test                 | Command                | Result |
| -------------------- | ---------------------- | ------ |
| HTTP                 | `curl http://...`      |        |
| HTTPS                | `curl https://...`     |        |
| Headers              | `curl -I ...`          |        |
| Verbose              | `curl -v ...`          |        |
| DNS                  | `dig ...`              |        |
| TCP 80               | `nc -vz ... 80`        |        |
| TCP 443              | `nc -vz ... 443`       |        |
| TLS                  | `openssl s_client ...` |        |
| Docker HTTP          | `curl localhost:8080`  |        |
| Kubernetes ClusterIP | `curl <ClusterIP>:80`  |        |
| Kubernetes NodePort  | `curl <NodeIP>:30080`  |        |

---

# 🎯 Final Challenge

Without looking at the notes, troubleshoot this architecture:

```text
User
 ↓
DNS
 ↓
HTTPS :443
 ↓
Load Balancer
 ↓
Nginx Reverse Proxy
 ↓
Kubernetes Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```

The user reports:

```text
Website is not opening.
```

Use this troubleshooting sequence:

```text
1. DNS
2. IP connectivity
3. TCP 443
4. TLS
5. HTTP status
6. Load Balancer
7. Nginx
8. Ingress
9. Service
10. Endpoints
11. Pod
12. Application
```

Useful commands:

```bash
dig example.com
```

```bash
nc -vz example.com 443
```

```bash
curl -v https://example.com
```

```bash
openssl s_client -connect example.com:443
```

```bash
kubectl get ingress
```

```bash
kubectl get svc
```

```bash
kubectl get endpointslice
```

```bash
kubectl get pods -o wide
```

---

# ✅ Completion Checklist

* [ ] Tested HTTP
* [ ] Tested HTTPS
* [ ] Inspected HTTP headers
* [ ] Used `curl -v`
* [ ] Checked status codes
* [ ] Tested redirects
* [ ] Checked DNS
* [ ] Tested ports 80 and 443
* [ ] Inspected TLS certificate
* [ ] Tested Docker HTTP
* [ ] Tested Kubernetes ClusterIP
* [ ] Tested Kubernetes NodePort
* [ ] Checked EndpointSlices
* [ ] Practiced HTTP troubleshooting
* [ ] Completed final troubleshooting challenge

---

# 🏆 What I Learned

After completing this lab, I can use practical tools to troubleshoot HTTP/HTTPS connectivity from:

```text
Client
 ↓
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Reverse Proxy
 ↓
Kubernetes
 ↓
Application
```

This is an important real-world troubleshooting skill for a DevOps engineer.
