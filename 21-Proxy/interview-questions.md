# Chapter 21 — Proxy Interview Questions

## Table of Contents

1. What is a Proxy Server?
2. Why is a Proxy used?
3. What is a Forward Proxy?
4. What is a Reverse Proxy?
5. Forward Proxy vs Reverse Proxy
6. What is a Transparent Proxy?
7. What is an HTTP Proxy?
8. How does HTTPS work with a Proxy?
9. What is a Caching Proxy?
10. What is Proxy Authentication?
11. What is the difference between Proxy and NAT?
12. Proxy vs Gateway
13. Proxy vs Load Balancer
14. What is Nginx?
15. Why is Nginx used as a Reverse Proxy?
16. What is TLS Termination?
17. What is `HTTP_PROXY`?
18. What is `HTTPS_PROXY`?
19. What is `NO_PROXY`?
20. How do you check Proxy variables in Linux?
21. How do you test a Proxy using curl?
22. How do you bypass a Proxy using curl?
23. How do you check whether a Proxy port is reachable?
24. How do you troubleshoot Proxy connectivity?
25. How is Proxy used in Docker?
26. How is Proxy used in Kubernetes?
27. What happens if NO_PROXY is configured incorrectly?
28. How would you troubleshoot an application that cannot access the Internet?
29. Give a real-world Reverse Proxy example.
30. What should a DevOps Engineer remember about Proxies?

---

# 1. What is a Proxy Server?

### Answer

A Proxy Server is an intermediary between a client and a destination server.

Instead of communicating directly with the destination, the client sends the request through the Proxy.

```text
Client
   |
   ↓
Proxy
   |
   ↓
Server
```

---

# 2. Why is a Proxy used?

### Answer

A Proxy can be used for:

- Security
- Access control
- Traffic filtering
- Monitoring
- Logging
- Caching
- Authentication
- Routing
- TLS termination
- Hiding internal backend services

---

# 3. What is a Forward Proxy?

### Answer

A Forward Proxy is positioned between clients and external servers.

```text
Client
   |
   ↓
Forward Proxy
   |
   ↓
Internet
   |
   ↓
Server
```

It acts on behalf of the client.

### Example

A company can use a Forward Proxy to control employees' Internet access.

---

# 4. What is a Reverse Proxy?

### Answer

A Reverse Proxy is positioned in front of backend servers.

```text
Client
   |
   ↓
Reverse Proxy
   |
   +----→ Server 1
   |
   +----→ Server 2
```

It acts on behalf of the backend servers.

Common Reverse Proxy software includes:

- Nginx
- HAProxy
- Envoy
- Apache HTTP Server

---

# 5. Forward Proxy vs Reverse Proxy

### Answer

| Forward Proxy | Reverse Proxy |
|---|---|
| Represents clients | Represents servers |
| Controls outbound traffic | Controls inbound traffic |
| Located near clients | Located near servers |
| Common in corporate networks | Common in web applications |
| Hides clients from destinations | Hides backend servers from clients |

### Easy way to remember

```text
Forward:
Client → Proxy → Internet

Reverse:
Internet → Proxy → Server
```

---

# 6. What is a Transparent Proxy?

### Answer

A Transparent Proxy intercepts traffic without requiring explicit Proxy configuration in the client application.

It can be used for:

- Traffic filtering
- Monitoring
- Access control
- Caching

---

# 7. What is an HTTP Proxy?

### Answer

An HTTP Proxy handles HTTP traffic between clients and servers.

The client sends the request to the Proxy, and the Proxy forwards it to the destination.

---

# 8. How does HTTPS work with a Proxy?

### Answer

HTTPS traffic is encrypted using TLS.

A Forward Proxy can establish a tunnel to the destination using the HTTP `CONNECT` method.

Simplified flow:

```text
Client
   |
   | CONNECT
   ↓
Proxy
   |
   ↓
HTTPS Server
```

The exact visibility of encrypted traffic depends on the Proxy's configuration.

A TLS-intercepting Proxy can decrypt and inspect traffic when appropriately configured with trusted certificates.

---

# 9. What is a Caching Proxy?

### Answer

A Caching Proxy stores cacheable responses.

If another client requests the same cacheable resource, the Proxy may return the cached response instead of contacting the destination server again.

Benefits include:

- Faster responses
- Reduced bandwidth
- Reduced backend load

---

# 10. What is Proxy Authentication?

### Answer

Proxy Authentication requires a client or user to authenticate before the Proxy allows traffic.

It can be used for:

- Access control
- User identification
- Policy enforcement
- Auditing

---

# 11. What is the difference between Proxy and NAT?

### Answer

NAT translates network addresses and/or ports.

```text
Private IP
    ↓
NAT
    ↓
Public IP
```

A Proxy acts as an intermediary for requests or connections.

```text
Client
   ↓
Proxy
   ↓
Server
```

### Key difference

NAT works primarily at the network/transport level.

A Proxy commonly operates at the application or connection level, depending on its type.

---

# 12. Proxy vs Gateway

### Answer

A Gateway connects or provides a path between networks.

A Proxy acts as an intermediary for traffic between a client and destination.

```text
Gateway:

Network A
   ↓
Gateway
   ↓
Network B
```

```text
Proxy:

Client
   ↓
Proxy
   ↓
Server
```

The same infrastructure product can sometimes perform multiple roles.

---

# 13. Proxy vs Load Balancer

### Answer

A Proxy forwards traffic between clients and destinations.

A Load Balancer distributes traffic among multiple backend servers.

Example:

```text
Client
   |
   ↓
Reverse Proxy / Load Balancer
   |
   +----→ Server 1
   +----→ Server 2
   +----→ Server 3
```

A Reverse Proxy can also provide load-balancing functionality.

---

# 14. What is Nginx?

### Answer

Nginx is a high-performance web server and reverse proxy.

It can provide:

- Web serving
- Reverse Proxy
- Load balancing
- TLS termination
- Caching
- Routing

---

# 15. Why is Nginx used as a Reverse Proxy?

### Answer

Nginx is commonly used because it can efficiently handle many concurrent connections and provide features such as:

- Request routing
- TLS termination
- Load balancing
- Static content serving
- Header manipulation
- Access control

Example:

```text
Client
   |
   ↓
Nginx :80
   |
   ↓
Application :8080
```

---

# 16. What is TLS Termination?

### Answer

TLS termination means the Reverse Proxy handles the TLS connection from the client.

Example:

```text
Client
   |
 HTTPS
   ↓
Nginx
   |
 HTTP
   ↓
Backend
```

The Proxy decrypts the incoming TLS connection and forwards the request to the backend according to the configured architecture.

In production, the backend connection may also use HTTPS if end-to-end encryption is required.

---

# 17. What is HTTP_PROXY?

### Answer

`HTTP_PROXY` is an environment variable commonly used by applications and command-line tools to specify an HTTP Proxy.

Example:

```bash
export HTTP_PROXY=http://proxy.example.com:8080
```

---

# 18. What is HTTPS_PROXY?

### Answer

`HTTPS_PROXY` specifies a Proxy to use for HTTPS requests.

Example:

```bash
export HTTPS_PROXY=http://proxy.example.com:8080
```

The Proxy URL itself may use HTTP even when the destination is HTTPS, depending on the Proxy protocol and configuration.

---

# 19. What is NO_PROXY?

### Answer

`NO_PROXY` specifies destinations that should bypass the Proxy.

Example:

```bash
export NO_PROXY=localhost,127.0.0.1,.internal.example.com
```

This is especially important in:

- Docker
- Kubernetes
- Cloud environments
- Corporate networks

---

# 20. How do you check Proxy variables in Linux?

### Answer

Run:

```bash
env | grep -i proxy
```

or:

```bash
printenv | grep -i proxy
```

Individual variables can be checked with:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

---

# 21. How do you test a Proxy using curl?

### Answer

Use:

```bash
curl -v -x http://<proxy-host>:<proxy-port> https://example.com
```

Where:

```text
-v
```

enables verbose output.

And:

```text
-x
```

specifies the Proxy.

---

# 22. How do you bypass a Proxy using curl?

### Answer

Use:

```bash
curl --noproxy '*' https://example.com
```

This is useful when comparing:

```text
Proxy connection
```

with:

```text
Direct connection
```

---

# 23. How do you check whether a Proxy port is reachable?

### Answer

Use:

```bash
nc -zv <proxy-host> <proxy-port>
```

For example:

```bash
nc -zv 192.168.1.10 8080
```

If the connection succeeds, the host and port are reachable from your machine.

---

# 24. How do you troubleshoot Proxy connectivity?

### Answer

I would follow a structured approach:

```text
1. Check Proxy variables
2. Check DNS
3. Check Proxy hostname/IP
4. Check Proxy port
5. Test TCP connectivity
6. Test HTTP/HTTPS connectivity
7. Check NO_PROXY
8. Check TLS certificates
9. Check authentication
10. Check Proxy logs
11. Check application logs
```

Useful commands:

```bash
env | grep -i proxy
```

```bash
getent hosts <proxy-host>
```

```bash
nc -zv <proxy-host> <proxy-port>
```

```bash
curl -v https://example.com
```

---

# 25. How is Proxy used in Docker?

### Answer

Docker containers may require a Proxy for outbound Internet access.

Proxy variables can be passed into containers:

```bash
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

Example:

```bash
docker run --rm \
-e HTTP_PROXY="$HTTP_PROXY" \
-e HTTPS_PROXY="$HTTPS_PROXY" \
-e NO_PROXY="$NO_PROXY" \
ubuntu env | grep -i proxy
```

---

# 26. How is Proxy used in Kubernetes?

### Answer

Pods may use Proxy environment variables for outbound traffic.

Example:

```bash
kubectl exec <pod-name> -- env | grep -i proxy
```

Important variables include:

```bash
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

`NO_PROXY` should be configured carefully so internal Kubernetes traffic does not unnecessarily go through an external Proxy.

---

# 27. What happens if NO_PROXY is configured incorrectly?

### Answer

Internal traffic may accidentally go through the Proxy.

This can cause:

- Connection failures
- Increased latency
- Authentication errors
- DNS problems
- Unexpected routing
- Service-to-service communication issues

This is particularly important in Kubernetes and cloud environments.

---

# 28. How would you troubleshoot an application that cannot access the Internet?

### Answer

I would troubleshoot layer by layer.

### Step 1 — Check IP

```bash
ip addr
```

### Step 2 — Check route

```bash
ip route
```

### Step 3 — Check DNS

```bash
getent hosts example.com
```

### Step 4 — Check Proxy

```bash
env | grep -i proxy
```

### Step 5 — Check Proxy port

```bash
nc -zv <proxy-host> <proxy-port>
```

### Step 6 — Test HTTPS

```bash
curl -v https://example.com
```

### Step 7 — Test without Proxy

```bash
curl --noproxy '*' -v https://example.com
```

### Step 8 — Check firewall and application logs

This allows me to determine whether the issue is related to:

```text
Network
DNS
Proxy
TLS
Firewall
Application
```

---

# 29. Give a real-world Reverse Proxy example.

### Answer

Suppose a company has three application servers:

```text
Application Server 1
Application Server 2
Application Server 3
```

Instead of exposing all three directly to users, the company can place Nginx in front of them:

```text
             ┌──→ App Server 1
             |
Internet → Nginx
             |
             ├──→ App Server 2
             |
             └──→ App Server 3
```

Nginx can provide:

- TLS termination
- Routing
- Load balancing
- Access control
- Logging

This makes Nginx a central entry point for the application.

---

# 30. What should a DevOps Engineer remember about Proxies?

### Answer

A DevOps Engineer should understand:

```text
Forward Proxy
Reverse Proxy
HTTP Proxy
HTTPS Proxy
Transparent Proxy
Caching
Authentication
TLS termination
Proxy environment variables
NO_PROXY
Nginx
Docker Proxy
Kubernetes Proxy
Proxy troubleshooting
```

The most important mental model is:

```text
Forward Proxy:

Client → Proxy → Internet


Reverse Proxy:

Internet → Proxy → Backend
```

---

# Quick Interview Revision

### Q: What is a Proxy?

**Answer:**

> A Proxy is an intermediary that forwards traffic between a client and a destination according to its configuration and policies.

### Q: Forward Proxy?

**Answer:**

> A Forward Proxy represents the client and is commonly used to control outbound traffic.

### Q: Reverse Proxy?

**Answer:**

> A Reverse Proxy represents backend servers and is commonly used for routing, TLS termination, load balancing, and security.

### Q: What is NO_PROXY?

**Answer:**

> `NO_PROXY` defines destinations that should bypass the configured Proxy.

### Q: How do you check Proxy configuration?

**Answer:**

```bash
env | grep -i proxy
```

### Q: How do you test a Proxy?

**Answer:**

```bash
curl -v -x http://<proxy-host>:<proxy-port> https://example.com
```

### Q: How do you bypass a Proxy?

**Answer:**

```bash
curl --noproxy '*' https://example.com
```

### Q: How do you test a Proxy port?

**Answer:**

```bash
nc -zv <proxy-host> <proxy-port>
```

---

# Interview Tip

When answering Proxy questions, don't only give a definition.

Use this structure:

```text
Definition
   ↓
Purpose
   ↓
Example
   ↓
DevOps use case
```

For example:

> A Reverse Proxy is a server placed in front of backend servers. It receives client requests and forwards them to the appropriate backend. In DevOps, Nginx is commonly used as a Reverse Proxy for TLS termination, routing, and load balancing.

This gives a much stronger interview answer than only saying:

> "A Reverse Proxy forwards requests."