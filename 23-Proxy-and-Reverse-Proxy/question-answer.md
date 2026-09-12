# 🎯 Chapter 23 – Proxy and Reverse Proxy Interview Questions

## 1. What is a Proxy Server?

A proxy server acts as an intermediary between a client and another server.

```text
Client → Proxy → Internet/Server
```

The client sends the request to the proxy, and the proxy forwards the request to the destination.

---

## 2. What is a Reverse Proxy?

A reverse proxy sits in front of backend servers and forwards client requests to the appropriate backend.

```text
Client → Reverse Proxy → Backend Server
```

Popular reverse proxy software includes:

* Nginx
* HAProxy
* Apache HTTP Server
* Traefik
* Envoy

---

## 3. What is the difference between a Forward Proxy and Reverse Proxy?

| Forward Proxy             | Reverse Proxy                       |
| ------------------------- | ----------------------------------- |
| Represents the client     | Represents the server               |
| Usually used by clients   | Usually used by servers             |
| Hides client identity     | Hides backend infrastructure        |
| Controls outbound traffic | Controls inbound traffic            |
| Client knows proxy        | Client may not know backend servers |

### Simple example

Forward proxy:

```text
Employee → Proxy → Internet
```

Reverse proxy:

```text
User → Nginx → Application
```

---

## 4. Why is a reverse proxy used?

A reverse proxy can provide:

* Load balancing
* SSL/TLS termination
* Caching
* Security
* Routing
* Compression
* Authentication
* Rate limiting
* High availability
* Centralized access logging

---

## 5. What is Nginx?

Nginx is a high-performance web server and reverse proxy server.

It can also provide:

* Load balancing
* HTTP caching
* TLS termination
* Static file serving
* Request routing

---

## 6. What is `proxy_pass` in Nginx?

`proxy_pass` tells Nginx where to forward a client request.

Example:

```nginx
location / {
    proxy_pass http://127.0.0.1:3000;
}
```

Here:

```text
Client
  ↓
Nginx :8080
  ↓
Backend :3000
```

---

## 7. What is a Proxy?

A proxy is an intermediary that forwards requests between a client and another destination.

Example:

```text
Client → Proxy → Server
```

The proxy can inspect, modify, filter, or forward traffic depending on its configuration.

---

## 8. What is a Reverse Proxy used for in DevOps?

Reverse proxies are commonly used in DevOps to:

* Expose applications
* Route traffic
* Load balance applications
* Terminate TLS
* Protect backend services
* Provide a single entry point
* Support microservices
* Perform health-based routing

---

## 9. What is Load Balancing?

Load balancing distributes traffic across multiple backend servers.

Example:

```text
             ┌──→ Backend 1
Client → Nginx├──→ Backend 2
             └──→ Backend 3
```

This improves scalability and availability.

---

## 10. Can Nginx act as a Load Balancer?

Yes.

Example:

```nginx
upstream backend {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
    server 127.0.0.1:3003;
}

server {
    listen 8080;

    location / {
        proxy_pass http://backend;
    }
}
```

Nginx can distribute requests between the backend servers.

---

# 🔥 Intermediate Questions

## 11. What is SSL/TLS termination?

SSL/TLS termination means the reverse proxy handles HTTPS encryption and forwards the request to the backend.

```text
Client
  |
  | HTTPS
  v
Nginx
  |
  | HTTP
  v
Backend
```

This allows backend applications to avoid handling TLS directly.

---

## 12. What is the `X-Forwarded-For` header?

`X-Forwarded-For` is commonly used to pass the original client IP through a proxy.

Example:

```nginx
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

Without appropriate forwarding, the backend may see the proxy's IP instead of the original client IP.

---

## 13. What is `X-Real-IP`?

`X-Real-IP` is commonly used to pass the client's IP address to the backend.

Example:

```nginx
proxy_set_header X-Real-IP $remote_addr;
```

---

## 14. What is the purpose of the `Host` header?

The `Host` header identifies the hostname requested by the client.

Example:

```text
Host: example.com
```

Nginx can forward it to the backend:

```nginx
proxy_set_header Host $host;
```

---

## 15. What is a 502 Bad Gateway?

`502 Bad Gateway` usually means that a gateway or proxy received an invalid response or could not successfully communicate with an upstream server.

For example:

```text
Client
  ↓
Nginx
  ↓
Backend DOWN
```

Nginx may return:

```text
502 Bad Gateway
```

---

## 16. What is an upstream server?

An upstream server is a backend server that receives requests from a reverse proxy.

Example:

```nginx
upstream backend {
    server 127.0.0.1:3000;
}
```

Here, the application on port `3000` is an upstream server.

---

## 17. What is the difference between a web server and reverse proxy?

A web server can directly serve content.

Example:

```text
Client → Nginx → HTML file
```

A reverse proxy forwards requests to another application.

```text
Client → Nginx → Application
```

Nginx can perform both roles.

---

## 18. What happens if the backend server goes down?

The reverse proxy may return an error such as:

```text
502 Bad Gateway
```

or:

```text
504 Gateway Timeout
```

depending on the failure and configuration.

---

## 19. What is a 504 Gateway Timeout?

A `504 Gateway Timeout` occurs when a gateway or proxy does not receive a timely response from an upstream server.

Example:

```text
Client
  ↓
Nginx
  ↓
Backend
  ↓
Too slow/no response
```

Nginx may return:

```text
504 Gateway Timeout
```

---

## 20. What is caching in a reverse proxy?

A reverse proxy can cache responses so that repeated requests can be served without contacting the backend every time.

```text
First request:
Client → Proxy → Backend

Later request:
Client → Proxy → Cache
```

This can reduce backend load and improve response time.

---

# 🚀 DevOps Interview Questions

## 21. Why would you put Nginx in front of an application?

A strong answer:

> I would use Nginx as a reverse proxy to provide a single entry point for the application, handle TLS termination, route requests, perform load balancing, manage headers, and improve security and performance.

---

## 22. How would you troubleshoot a 502 error?

Follow this sequence:

### Step 1 — Check the backend

```bash
curl http://127.0.0.1:3000
```

### Step 2 — Check the backend port

```bash
sudo ss -ltnp | grep ':3000'
```

### Step 3 — Check Nginx

```bash
sudo systemctl status nginx
```

### Step 4 — Validate configuration

```bash
sudo nginx -t
```

### Step 5 — Check error logs

```bash
sudo tail -n 50 /var/log/nginx/error.log
```

### Step 6 — Test the proxy

```bash
curl -v http://127.0.0.1:8080
```

---

## 23. How do you check whether Nginx is listening?

Run:

```bash
sudo ss -ltnp | grep nginx
```

Or:

```bash
sudo ss -ltnp | grep ':8080'
```

---

## 24. How do you check Nginx configuration?

Run:

```bash
sudo nginx -t
```

Expected:

```text
syntax is ok
test is successful
```

---

## 25. How do you reload Nginx without stopping it?

Run:

```bash
sudo systemctl reload nginx
```

This allows Nginx to reload its configuration without completely stopping the service.

---

## 26. What is the difference between reload and restart?

### Reload

```bash
sudo systemctl reload nginx
```

Reloads configuration while keeping the service running.

### Restart

```bash
sudo systemctl restart nginx
```

Stops and starts the service.

A reload is generally preferred for configuration changes when possible.

---

## 27. How do you view Nginx access logs?

Run:

```bash
sudo tail -f /var/log/nginx/access.log
```

---

## 28. How do you view Nginx error logs?

Run:

```bash
sudo tail -f /var/log/nginx/error.log
```

---

## 29. What is rate limiting?

Rate limiting controls how many requests a client can make during a period.

It can help protect applications from:

* Excessive traffic
* Abuse
* Brute-force attempts
* Resource exhaustion

---

## 30. How does a reverse proxy improve security?

A reverse proxy can:

* Hide backend IP addresses
* Restrict direct backend access
* Terminate TLS
* Apply rate limits
* Filter requests
* Add authentication
* Centralize security policies

---

# ☸️ Kubernetes Questions

## 31. Is a Kubernetes Ingress a reverse proxy?

Ingress is an API resource that defines HTTP/HTTPS routing rules.

An Ingress Controller implements those rules and commonly acts as a reverse proxy.

Example:

```text
Internet
   |
   v
Ingress Controller
   |
   +----→ Service A
   |
   +----→ Service B
```

---

## 32. What is the difference between NodePort and a reverse proxy?

NodePort exposes a Kubernetes Service on a port on the node.

Example:

```text
Client → NodeIP:30080 → Service → Pod
```

A reverse proxy provides application-layer routing and can route based on hostnames or paths.

Example:

```text
Client
  ↓
Nginx
  ├── /app1 → App 1
  └── /app2 → App 2
```

---

## 33. How can Nginx route traffic to multiple applications?

Using different locations:

```nginx
server {
    listen 80;

    location /app1 {
        proxy_pass http://127.0.0.1:3001;
    }

    location /app2 {
        proxy_pass http://127.0.0.1:3002;
    }
}
```

Traffic is routed according to the request path.

---

## 34. What is path-based routing?

Path-based routing sends requests to different backends based on the URL path.

Example:

```text
/app1 → Application 1
/app2 → Application 2
/api  → API Server
```

---

## 35. What is host-based routing?

Host-based routing sends requests to different backends based on the hostname.

Example:

```text
app.example.com → App 1
api.example.com → API
admin.example.com → Admin App
```

---

# 🧠 Scenario-Based Questions

## 36. Your application works on port 3000 but Nginx returns 502. What would you check?

I would check:

```bash
curl http://127.0.0.1:3000
```

Then:

```bash
sudo ss -ltnp | grep ':3000'
```

Then:

```bash
sudo nginx -t
```

Finally:

```bash
sudo tail -n 50 /var/log/nginx/error.log
```

I would verify the `proxy_pass` address and confirm that the backend is reachable from the Nginx process.

---

## 37. Your Nginx configuration is correct but the application returns 504. What could be wrong?

Possible causes include:

* Backend is slow
* Backend is overloaded
* Network connectivity problem
* Incorrect upstream address
* Backend dependency is unavailable
* Timeout settings are too short

I would inspect Nginx logs and test the upstream directly.

---

## 38. Why should backend servers sometimes not be exposed directly to the Internet?

Keeping backends behind a reverse proxy can:

* Reduce the attack surface
* Centralize TLS
* Apply security controls
* Hide internal infrastructure
* Control routing
* Provide consistent logging

---

## 39. How would you design a production reverse-proxy architecture?

A simple architecture could be:

```text
                  Internet
                     |
                     v
              Load Balancer
                     |
                     v
             Reverse Proxy
              /          \
             /            \
            v              v
        App Server 1    App Server 2
             \            /
              \          /
               Database
```

For higher availability, multiple proxy instances can also be deployed.

---

## 40. Explain reverse proxy in simple words.

A simple interview answer:

> A reverse proxy is a server that sits between users and backend servers. Users send requests to the reverse proxy, and the reverse proxy forwards those requests to the appropriate backend. It can also provide load balancing, TLS termination, security, caching, and routing.

---

# ⭐ Quick Revision

Remember these five concepts:

```text
Forward Proxy
    ↓
Represents the client

Reverse Proxy
    ↓
Represents the server

proxy_pass
    ↓
Forwards requests to backend

502
    ↓
Bad/failed upstream communication

504
    ↓
Upstream response timeout
```

## 🔥 Most Important Commands

```bash
nginx -v
```

```bash
sudo nginx -t
```

```bash
sudo systemctl status nginx
```

```bash
sudo systemctl reload nginx
```

```bash
sudo ss -ltnp
```

```bash
curl -v http://127.0.0.1:8080
```

```bash
sudo tail -f /var/log/nginx/access.log
```

```bash
sudo tail -f /var/log/nginx/error.log
```

---

# 🎯 Interview Practice

Try answering these **without looking at the notes**:

1. What is a reverse proxy?
2. Forward proxy vs reverse proxy?
3. Why is Nginx used as a reverse proxy?
4. What does `proxy_pass` do?
5. What is `502 Bad Gateway`?
6. What is `504 Gateway Timeout`?
7. What is load balancing?
8. What is SSL/TLS termination?
9. What is `X-Forwarded-For`?
10. How would you troubleshoot a 502 error?
11. How does reverse proxying improve security?
12. How does Kubernetes Ingress relate to reverse proxies?

**Goal:** Answer each question in your own words in **30–60 seconds**.
