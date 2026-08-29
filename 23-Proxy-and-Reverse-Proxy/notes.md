# 🌐 Chapter 23 – Proxy and Reverse Proxy

## 1. Introduction

A **proxy server** is an intermediary between a client and a destination server.

Instead of communicating directly with the destination, the client sends the request through the proxy.

There are two major types:

1. Forward Proxy
2. Reverse Proxy

The main difference is **who the proxy represents**.

```text
Forward Proxy  → represents the CLIENT
Reverse Proxy  → represents the SERVER
```

---

# 2. What is a Proxy?

A proxy receives a request from one system and forwards it to another system.

Basic architecture:

```text
Client
   |
   | Request
   v
 Proxy
   |
   | Forwarded Request
   v
Server
```

The proxy can inspect, modify, filter, cache, or forward traffic depending on its configuration.

---

# 3. Forward Proxy

A **forward proxy** is positioned on the client side.

```text
Client
   |
   v
Forward Proxy
   |
   v
Internet
   |
   v
Web Server
```

The client explicitly uses the proxy to access external resources.

### Example

A company may configure employee computers to access the Internet through a corporate proxy.

```text
Employee Laptop
       |
       v
Corporate Proxy
       |
       v
Internet
```

---

## 3.1 Forward Proxy Use Cases

Common uses include:

* Internet access control
* Content filtering
* Monitoring
* Caching
* Restricting websites
* Corporate security policies
* Hiding internal client addresses
* Controlling outbound traffic

---

# 4. Reverse Proxy

A **reverse proxy** sits in front of one or more backend servers.

```text
                 Backend 1
                /
Client → Reverse Proxy → Backend 2
                \
                 Backend 3
```

The client communicates with the reverse proxy.

The reverse proxy decides which backend should receive the request.

---

# 5. Forward Proxy vs Reverse Proxy

| Feature         | Forward Proxy       | Reverse Proxy    |
| --------------- | ------------------- | ---------------- |
| Represents      | Client              | Server           |
| Location        | Client side         | Server side      |
| Traffic         | Outbound            | Inbound          |
| Hides           | Client              | Backend          |
| Common use      | Internet access     | Web applications |
| Load balancing  | Not primary purpose | Common           |
| SSL termination | Possible            | Common           |
| Backend routing | Usually no          | Yes              |

### Easy way to remember

```text
Forward Proxy
       ↓
For the client

Reverse Proxy
       ↓
For the server
```

---

# 6. Why Use a Reverse Proxy?

Reverse proxies are widely used in production systems.

Important functions include:

* Load balancing
* SSL/TLS termination
* Routing
* Security
* Caching
* Compression
* Authentication
* Rate limiting
* Hiding backend infrastructure

---

# 7. Load Balancing

A reverse proxy can distribute incoming requests among multiple servers.

```text
                         +--> App Server 1
                         |
Client → Reverse Proxy --+--> App Server 2
                         |
                         +--> App Server 3
```

For example, three application servers could receive traffic:

```text
Request 1 → Server 1
Request 2 → Server 2
Request 3 → Server 3
Request 4 → Server 1
```

This improves scalability and availability.

---

# 8. SSL/TLS Termination

A reverse proxy can handle HTTPS connections from clients.

```text
Client
  |
  | HTTPS
  v
Reverse Proxy
  |
  | HTTP/HTTPS
  v
Backend Application
```

The reverse proxy manages the TLS certificate.

This is called **SSL/TLS termination**.

It can simplify certificate management because backend applications do not necessarily need to handle public TLS certificates individually.

---

# 9. Request Routing

A reverse proxy can route requests based on:

* Hostname
* URL path
* Headers
* Ports
* Other request information

Example:

```text
example.com/api
       |
       v
API Server

example.com/web
       |
       v
Web Server
```

Another example:

```text
api.example.com
       ↓
API Backend

www.example.com
       ↓
Web Backend
```

---

# 10. Caching

A reverse proxy can cache frequently requested content.

```text
Client
   |
   v
Reverse Proxy
   |
   +---- Cached Response
   |
   v
Backend
```

If the response is already cached, the proxy may serve it without contacting the backend.

Benefits:

* Lower backend load
* Faster responses
* Reduced network traffic

---

# 11. Compression

A reverse proxy can compress responses before sending them to clients.

```text
Backend
   |
   | Large response
   v
Reverse Proxy
   |
   | Compressed response
   v
Client
```

Compression can reduce bandwidth usage.

---

# 12. Security

A reverse proxy can act as a security boundary.

```text
Internet
    |
    v
Firewall
    |
    v
Reverse Proxy
    |
    v
Application
    |
    v
Database
```

Backend servers can be kept on private networks rather than being directly exposed.

A reverse proxy can also support:

* Access control
* Authentication
* Rate limiting
* Request filtering
* Security headers

---

# 13. Authentication

A reverse proxy can participate in authentication.

Example:

```text
Client
   |
   v
Reverse Proxy
   |
   | Authentication
   v
Application
```

The proxy may verify authentication before forwarding traffic to the application.

---

# 14. Rate Limiting

Rate limiting controls how many requests a client can make during a period.

Example:

```text
Client
   |
   | 1000 requests
   v
Reverse Proxy
   |
   | Allow limited requests
   v
Backend
```

This can help protect applications from excessive traffic.

---

# 15. Common Reverse Proxy Software

Popular technologies include:

### Nginx

Widely used as:

* Web server
* Reverse proxy
* Load balancer
* HTTP cache

### HAProxy

Commonly used for:

* Load balancing
* High-performance proxying
* TCP/HTTP traffic

### Apache HTTP Server

Can operate as a reverse proxy using modules such as `mod_proxy`.

### Traefik

Popular in:

* Containers
* Docker
* Kubernetes
* Dynamic environments

### Envoy

Common in:

* Cloud-native systems
* Service meshes
* Microservices

---

# 16. Nginx Reverse Proxy

Nginx can receive requests and forward them to a backend application.

Example architecture:

```text
Client
   |
   | HTTP
   v
Nginx
   |
   | HTTP
   v
Application Server
```

A simplified Nginx configuration looks like:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8080;
    }
}
```

Here:

```text
Client
  ↓
Nginx :80
  ↓
Application :8080
```

---

# 17. Proxy Headers

A reverse proxy may forward information about the original client.

Common headers include:

```text
X-Forwarded-For
X-Forwarded-Proto
X-Forwarded-Host
```

For example:

```text
X-Forwarded-For: client-IP
```

This helps the backend understand information about the original request.

---

# 18. Reverse Proxy Architecture in DevOps

A common production architecture is:

```text
                   Internet
                       |
                       v
                Load Balancer
                       |
                       v
                Reverse Proxy
                       |
             +---------+---------+
             |         |         |
             v         v         v
           App 1     App 2     App 3
             |         |         |
             +---------+---------+
                       |
                       v
                    Database
```

This architecture provides separation between external traffic and application infrastructure.

---

# 19. Reverse Proxy and Containers

Reverse proxies are commonly used with Docker.

Example:

```text
Internet
    |
    v
Nginx Container
    |
    +----> Web Container
    |
    +----> API Container
```

Docker networking allows containers to communicate using Docker networks.

---

# 20. Reverse Proxy and Kubernetes

In Kubernetes, reverse-proxy concepts are commonly implemented using **Ingress controllers** or newer **Gateway API** implementations.

Typical architecture:

```text
Client
   |
   v
Ingress / Gateway
   |
   v
Service
   |
   v
Pods
```

Example:

```text
example.com
     |
     v
Ingress
     |
     +----> web-service
     |
     +----> api-service
```

The Service then forwards traffic to the appropriate Pods.

---

# 21. Proxy vs Load Balancer

A reverse proxy and load balancer can overlap in functionality, but they are not exactly the same concept.

### Reverse Proxy

Primarily acts as an intermediary between clients and backend servers.

### Load Balancer

Primarily distributes traffic among multiple backend servers.

A reverse proxy can also perform load balancing.

```text
Reverse Proxy
      +
Load Balancing
      =
Common Production Architecture
```

---

# 22. Proxy vs API Gateway

An API Gateway is a specialized entry point for APIs.

It can provide:

* Routing
* Authentication
* Authorization
* Rate limiting
* Request transformation
* API management

A reverse proxy can provide some of these functions, but an API gateway usually offers more API-specific capabilities.

---

# 23. Proxy Environment Variables

Linux applications may use environment variables to configure proxies.

Common variables include:

```bash
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

You can inspect them with:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

Lowercase versions may also exist:

```bash
echo $http_proxy
echo $https_proxy
echo $no_proxy
```

Environment variable names are case-sensitive on Linux.

---

# 24. curl and Proxy Testing

`curl` can be used to test HTTP/HTTPS connectivity.

Basic request:

```bash
curl -I https://example.com
```

Verbose request:

```bash
curl -v https://example.com
```

Bypass proxy settings for a request:

```bash
curl --noproxy '*' -I https://example.com
```

This is useful when troubleshooting whether a proxy is involved in a connection.

---

# 25. Proxy Troubleshooting

When a proxy is not working, check the following:

### Step 1 — Check environment variables

```bash
env | grep -i proxy
```

### Step 2 — Test DNS

```bash
getent hosts example.com
```

### Step 3 — Test connectivity

```bash
curl -I https://example.com
```

### Step 4 — Use verbose mode

```bash
curl -v https://example.com
```

### Step 5 — Bypass proxy

```bash
curl --noproxy '*' -I https://example.com
```

Compare the results.

---

# 26. Important Networking Terms

### Client

The system making the request.

### Backend

The application or server processing the request.

### Proxy

An intermediary forwarding network requests.

### Reverse Proxy

A proxy positioned in front of backend servers.

### Upstream

A backend server to which a proxy forwards requests.

### Downstream

The client-facing side of a proxy connection.

### Load Balancing

Distributing traffic among multiple backend servers.

### TLS Termination

Decrypting HTTPS traffic at the proxy.

---

# 27. Real-World Example

Suppose an application has three backend servers:

```text
App Server 1 → 10.0.0.11
App Server 2 → 10.0.0.12
App Server 3 → 10.0.0.13
```

A reverse proxy is exposed publicly:

```text
Public IP
    |
    v
Reverse Proxy
    |
    +----> 10.0.0.11
    |
    +----> 10.0.0.12
    |
    +----> 10.0.0.13
```

Users only need to know the public endpoint.

The backend servers can remain private.

---

# 28. DevOps Importance

Understanding reverse proxies is important for DevOps engineers because they frequently appear in:

* CI/CD infrastructure
* Docker environments
* Kubernetes
* Cloud architecture
* Microservices
* Web applications
* API infrastructure
* Load balancing
* HTTPS deployments

A DevOps engineer should understand how traffic flows from:

```text
Client
   ↓
DNS
   ↓
Load Balancer / Reverse Proxy
   ↓
Application
   ↓
Database
```

---

# 29. Key Takeaways

Remember these five points:

```text
1. Forward Proxy → represents the client

2. Reverse Proxy → represents the server

3. Reverse Proxy → can route traffic

4. Reverse Proxy → can perform load balancing

5. Reverse Proxy → can terminate TLS
```

### Final Architecture

```text
                    Internet
                       |
                       v
                    DNS
                       |
                       v
              Reverse Proxy
               /     |     \
              /      |      \
             v       v       v
          App 1    App 2    App 3
             \       |       /
              \      |      /
               \     |     /
                    Database
```

A reverse proxy provides a controlled entry point between clients and backend infrastructure, making it an important building block for modern DevOps and cloud systems.
