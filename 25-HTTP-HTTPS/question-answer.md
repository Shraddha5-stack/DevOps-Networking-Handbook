# 🎯 Chapter 25 — HTTP & HTTPS Interview Questions

## Beginner Level

### 1. What is HTTP?

**Answer:**

HTTP stands for **Hypertext Transfer Protocol**. It is an application-layer protocol used for communication between clients and web servers.

For example:

```text
Browser → HTTP Request → Web Server
Browser ← HTTP Response ← Web Server
```

---

### 2. What is HTTPS?

**Answer:**

HTTPS stands for **Hypertext Transfer Protocol Secure**.

It is HTTP communication protected using **TLS (Transport Layer Security)**.

```text
HTTP  → Unencrypted application data
HTTPS → HTTP + TLS encryption
```

HTTPS provides:

* Confidentiality
* Integrity
* Server authentication

---

### 3. What is the difference between HTTP and HTTPS?

| HTTP                            | HTTPS             |
| ------------------------------- | ----------------- |
| Usually port 80                 | Usually port 443  |
| No TLS encryption               | Uses TLS          |
| Data can be read if intercepted | Data is encrypted |
| No TLS certificate              | Uses certificates |
| Less secure                     | More secure       |

---

### 4. What is HTTP port 80?

**Answer:**

Port **80** is the standard TCP port commonly used for HTTP traffic.

Example:

```text
http://example.com:80
```

Usually `:80` can be omitted.

---

### 5. What is HTTPS port 443?

**Answer:**

Port **443** is the standard TCP port commonly used for HTTPS traffic.

Example:

```text
https://example.com:443
```

Usually `:443` can be omitted.

---

### 6. What is an HTTP request?

**Answer:**

An HTTP request is a message sent by a client to a server to request a resource or perform an operation.

Example:

```text
GET /index.html HTTP/1.1
Host: example.com
```

---

### 7. What is an HTTP response?

**Answer:**

An HTTP response is the message returned by the server after processing an HTTP request.

Example:

```text
HTTP/1.1 200 OK
Content-Type: text/html
```

---

### 8. What is an HTTP method?

**Answer:**

An HTTP method specifies the operation the client wants to perform.

Common methods:

```text
GET
POST
PUT
PATCH
DELETE
HEAD
OPTIONS
```

---

### 9. What is GET?

**Answer:**

`GET` is commonly used to retrieve data from a server.

Example:

```bash
curl https://example.com
```

---

### 10. What is POST?

**Answer:**

`POST` is commonly used to send data to a server, such as creating a resource.

Example:

```bash
curl -X POST https://example.com/api/users
```

---

### 11. What is PUT?

**Answer:**

`PUT` is commonly used to replace or update a resource.

Example:

```bash
curl -X PUT https://example.com/api/users/1
```

---

### 12. What is PATCH?

**Answer:**

`PATCH` is commonly used for a partial update of a resource.

Example:

```bash
curl -X PATCH https://example.com/api/users/1
```

---

### 13. What is DELETE?

**Answer:**

`DELETE` is used to request deletion of a resource.

Example:

```bash
curl -X DELETE https://example.com/api/users/1
```

---

# HTTP Status Codes

### 14. What does HTTP 200 mean?

**Answer:**

`200 OK` means the request was successfully processed.

---

### 15. What does HTTP 201 mean?

**Answer:**

`201 Created` generally means a new resource was successfully created.

---

### 16. What does HTTP 301 mean?

**Answer:**

`301 Moved Permanently` indicates that a resource has been permanently redirected to another URL.

---

### 17. What does HTTP 302 mean?

**Answer:**

`302 Found` indicates a temporary redirect.

---

### 18. What does HTTP 400 mean?

**Answer:**

`400 Bad Request` means the server could not process the request because the request was invalid or malformed.

---

### 19. What does HTTP 401 mean?

**Answer:**

`401 Unauthorized` generally means the request requires valid authentication credentials.

---

### 20. What does HTTP 403 mean?

**Answer:**

`403 Forbidden` means the server understood the request but refuses to authorize access.

---

### 21. What does HTTP 404 mean?

**Answer:**

`404 Not Found` means the requested resource could not be found.

---

### 22. What does HTTP 500 mean?

**Answer:**

`500 Internal Server Error` indicates a server-side application error.

---

### 23. What does HTTP 502 mean?

**Answer:**

`502 Bad Gateway` commonly occurs when a gateway or reverse proxy receives an invalid response from an upstream server.

Example:

```text
Client
  ↓
Nginx
  ↓
Application ❌
```

---

### 24. What does HTTP 503 mean?

**Answer:**

`503 Service Unavailable` means the server is currently unable to handle the request.

Possible causes:

* Application unavailable
* Backend unhealthy
* No available service endpoints
* Temporary overload
* Maintenance

---

### 25. What does HTTP 504 mean?

**Answer:**

`504 Gateway Timeout` means a gateway or proxy did not receive a timely response from the upstream server.

---

# HTTP Headers

### 26. What are HTTP headers?

**Answer:**

HTTP headers contain metadata about an HTTP request or response.

Example:

```text
Content-Type: application/json
Authorization: Bearer <TOKEN>
Cache-Control: no-cache
```

---

### 27. What is Content-Type?

**Answer:**

`Content-Type` tells the receiver what type of data is being sent.

Examples:

```text
Content-Type: text/html
Content-Type: application/json
Content-Type: text/plain
```

---

### 28. What is the Host header?

**Answer:**

The `Host` header identifies the hostname requested by the client.

Example:

```text
Host: example.com
```

It is especially important when multiple websites are hosted on the same server or IP.

---

### 29. What is Authorization header?

**Answer:**

The `Authorization` header is commonly used to send authentication credentials.

Example:

```text
Authorization: Bearer <TOKEN>
```

---

# HTTPS and TLS

### 30. What is TLS?

**Answer:**

TLS stands for **Transport Layer Security**.

It protects network communication by providing:

* Encryption
* Integrity
* Authentication

---

### 31. What is an SSL certificate?

**Answer:**

In modern systems, HTTPS certificates are generally **TLS certificates**, although people still commonly call them SSL certificates.

A certificate helps establish the identity of a server and is used during the TLS handshake.

---

### 32. What is a TLS handshake?

**Answer:**

The TLS handshake is the process through which the client and server negotiate security parameters and establish cryptographic keys for secure communication.

Simplified:

```text
Client
  ↓
ClientHello
  ↓
ServerHello + Certificate
  ↓
Key establishment
  ↓
Secure encrypted communication
```

---

### 33. Why is a TLS certificate required?

**Answer:**

A certificate helps the client verify the server's identity and establishes trust through a certificate authority chain.

It also contains information such as:

* Domain names
* Issuer
* Validity period
* Public key

---

### 34. How do you inspect a TLS certificate?

**Answer:**

Use:

```bash
openssl s_client -connect example.com:443
```

You can also inspect certificate dates:

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

---

### 35. How do you check whether a certificate has expired?

**Answer:**

Run:

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

Check the `notAfter` value.

---

# curl

### 36. What is curl?

**Answer:**

`curl` is a command-line tool used to transfer data over network protocols including HTTP and HTTPS.

DevOps engineers frequently use it for:

* API testing
* Health checks
* HTTP troubleshooting
* Connectivity testing
* Debugging services

---

### 37. How do you check HTTP response headers using curl?

```bash
curl -I https://example.com
```

---

### 38. How do you perform verbose HTTP troubleshooting?

```bash
curl -v https://example.com
```

This can show:

```text
DNS resolution
TCP connection
TLS handshake
HTTP request
HTTP response
```

---

### 39. How do you follow redirects with curl?

```bash
curl -L https://example.com
```

To inspect redirects:

```bash
curl -IL https://example.com
```

---

### 40. How do you check only the HTTP status code?

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

---

# DevOps Troubleshooting

### 41. A website is not opening. How would you troubleshoot it?

**Answer:**

I would troubleshoot layer by layer:

```text
DNS
 ↓
IP connectivity
 ↓
TCP port
 ↓
TLS
 ↓
HTTP
 ↓
Reverse Proxy / Load Balancer
 ↓
Application
```

Commands:

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

---

### 42. DNS resolves, but HTTPS does not work. What would you check?

**Answer:**

I would check:

1. TCP port 443
2. Firewall
3. Load balancer
4. TLS certificate
5. TLS handshake
6. Reverse proxy
7. Backend application

Commands:

```bash
nc -vz example.com 443
```

```bash
curl -v https://example.com
```

```bash
openssl s_client -connect example.com:443
```

---

### 43. What would you check if you get 502 Bad Gateway?

**Answer:**

I would check the upstream application.

For example:

```text
Client
 ↓
Nginx
 ↓
Backend ❌
```

I would verify:

```bash
sudo ss -ltnp
```

Then test the backend directly:

```bash
curl -v http://<BACKEND-IP>:<PORT>
```

In Kubernetes:

```bash
kubectl get pods
kubectl get svc
kubectl get endpointslice
```

---

### 44. What would you check for a 503 error in Kubernetes?

**Answer:**

I would check:

```bash
kubectl get pods
kubectl get svc
kubectl get endpointslice
```

I would verify:

* Pods are running
* Pods are Ready
* Service selector matches Pod labels
* Service has endpoints
* Application is listening on the expected port

---

### 45. What would you check for a 504 error?

**Answer:**

I would investigate timeout and upstream response problems.

I would check:

* Backend response time
* Proxy timeout
* Load balancer timeout
* Network connectivity
* Application performance
* Backend health

---

### 46. How would you troubleshoot a Kubernetes HTTP Service?

**Answer:**

First:

```bash
kubectl get pods -o wide
```

Then:

```bash
kubectl get svc
```

Then:

```bash
kubectl get endpointslice
```

Finally test from inside the cluster:

```bash
kubectl run curl-test \
  --rm -it \
  --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://<SERVICE-IP>:80
```

---

### 47. What is the difference between Service Port, TargetPort, and NodePort?

**Answer:**

Example:

```yaml
ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```

Meaning:

```text
NodePort 30080
      ↓
Service Port 80
      ↓
Pod TargetPort 80
```

* `nodePort` → Port exposed on the Kubernetes node
* `port` → Port exposed by the Service
* `targetPort` → Port where the application is listening in the Pod

---

### 48. Why might `curl localhost:30080` fail while the Kubernetes NodePort works through the node IP?

**Answer:**

In local Kubernetes environments such as Kind, the Kubernetes node itself runs inside a container network.

Therefore:

```bash
curl http://127.0.0.1:30080
```

may fail from the host if that NodePort is not published to the host loopback interface.

But:

```bash
curl http://<NODE-IP>:30080
```

may work because it reaches the Kubernetes node directly.

The exact behavior depends on the local Kubernetes networking configuration.

---

### 49. How do you verify that a Kubernetes Service has backend Pods?

**Answer:**

Use:

```bash
kubectl get endpointslice \
  -l kubernetes.io/service-name=<SERVICE-NAME>
```

If endpoint IPs are present, the Service has discovered matching backend endpoints.

---

### 50. How do you test an HTTP service from inside Kubernetes?

**Answer:**

I can launch a temporary curl container:

```bash
kubectl run curl-test \
  --rm -it \
  --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://<SERVICE-NAME>
```

This is useful because it tests connectivity from inside the cluster network.

---

# ⭐ Scenario-Based Questions

### 51. Your application is running, but the Service returns 503. What could be wrong?

**Answer:**

The Pod can be `Running` but still not be a usable backend.

I would check:

```bash
kubectl get pods
kubectl get endpointslice
```

Possible causes:

* Readiness probe failure
* Wrong Service selector
* Wrong targetPort
* Application not listening on expected port
* No ready endpoints

---

### 52. Your application returns 200 directly, but Nginx returns 502. What does that suggest?

**Answer:**

It suggests that the application may be healthy but the connection between Nginx and the upstream application is incorrect.

I would check:

* Upstream IP
* Upstream port
* DNS
* Network connectivity
* Nginx configuration
* Backend protocol

---

### 53. HTTP works but HTTPS fails. What would you investigate?

**Answer:**

I would investigate the TLS layer:

```bash
nc -vz example.com 443
```

Then:

```bash
openssl s_client -connect example.com:443
```

And:

```bash
curl -v https://example.com
```

Possible causes include:

* Port 443 blocked
* Certificate expired
* Incorrect certificate
* TLS configuration issue
* SNI/hostname issue
* Reverse proxy configuration problem

---

### 54. What is the difference between TCP connectivity and HTTP connectivity?

**Answer:**

TCP connectivity only confirms that a TCP connection can be established.

For example:

```bash
nc -vz example.com 443
```

HTTP testing goes further:

```bash
curl -v https://example.com
```

A TCP connection can succeed while the application still returns:

```text
404
500
502
503
504
```

---

### 55. Explain the complete HTTPS request flow.

**Answer:**

A simplified flow is:

```text
Client
  ↓
DNS resolution
  ↓
TCP connection to port 443
  ↓
TLS handshake
  ↓
Certificate validation
  ↓
Encrypted HTTP request
  ↓
Load Balancer / Reverse Proxy
  ↓
Application
  ↓
HTTP response
  ↓
Encrypted response
  ↓
Client
```

---

# 🚀 DevOps Interview Rapid Revision

Remember these:

```text
HTTP  → 80
HTTPS → 443

200 → OK
201 → Created
301 → Permanent redirect
302 → Temporary redirect
400 → Bad Request
401 → Authentication required
403 → Forbidden
404 → Not Found
500 → Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout
```

Important commands:

```bash
curl -I https://example.com
```

```bash
curl -v https://example.com
```

```bash
curl -IL https://example.com
```

```bash
nc -vz example.com 443
```

```bash
openssl s_client -connect example.com:443
```

```bash
dig example.com
```

```bash
ss -ltnp
```

Kubernetes:

```bash
kubectl get pods
kubectl get svc
kubectl get endpointslice
```

---

# 🏆 Interview Answer Pattern

When an interviewer gives me a networking problem, I should avoid randomly running commands.

I should explain my troubleshooting logically:

```text
First → DNS
Second → IP connectivity
Third → TCP port
Fourth → TLS
Fifth → HTTP
Sixth → Proxy / Load Balancer
Seventh → Backend
Eighth → Application
```

This demonstrates structured DevOps troubleshooting rather than only knowing commands.
