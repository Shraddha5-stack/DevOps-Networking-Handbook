# Chapter 21 — Proxy

## Table of Contents

1. [What is a Proxy?](#1-what-is-a-proxy)
2. [How a Proxy Works](#2-how-a-proxy-works)
3. [Why Do We Use a Proxy?](#3-why-do-we-use-a-proxy)
4. [Client, Proxy and Server](#4-client-proxy-and-server)
5. [Forward Proxy](#5-forward-proxy)
6. [Reverse Proxy](#6-reverse-proxy)
7. [Forward Proxy vs Reverse Proxy](#7-forward-proxy-vs-reverse-proxy)
8. [HTTP Proxy](#8-http-proxy)
9. [HTTPS Proxy](#9-https-proxy)
10. [Transparent Proxy](#10-transparent-proxy)
11. [Anonymous Proxy](#11-anonymous-proxy)
12. [Caching Proxy](#12-caching-proxy)
13. [Proxy Authentication](#13-proxy-authentication)
14. [Proxy and DNS](#14-proxy-and-dns)
15. [Proxy and NAT](#15-proxy-and-nat)
16. [Proxy vs Gateway](#16-proxy-vs-gateway)
17. [Proxy vs Load Balancer](#17-proxy-vs-load-balancer)
18. [Reverse Proxy in DevOps](#18-reverse-proxy-in-devops)
19. [Nginx as a Reverse Proxy](#19-nginx-as-a-reverse-proxy)
20. [Proxy in Docker](#20-proxy-in-docker)
21. [Proxy in Kubernetes](#21-proxy-in-kubernetes)
22. [Proxy in Cloud Environments](#22-proxy-in-cloud-environments)
23. [Common Proxy Problems](#23-common-proxy-problems)
24. [Production Example](#24-production-example)
25. [Key Takeaways](#25-key-takeaways)

---

# 1. What is a Proxy?

A **Proxy Server** is an intermediary between a client and a destination server.

Instead of the client communicating directly with the destination, the client sends the request to the proxy.

The proxy then communicates with the destination server.

Basic flow:

```text
Client
   |
   ↓
Proxy
   |
   ↓
Destination Server
```

### Simple Definition

> A proxy is a server that acts as an intermediary between a client and another server.

---

# 2. How a Proxy Works

Without a proxy:

```text
Client
   |
   ↓
Internet
   |
   ↓
Server
```

With a proxy:

```text
Client
   |
   ↓
Proxy
   |
   ↓
Internet
   |
   ↓
Server
```

The client sends a request to the proxy.

The proxy processes or forwards the request.

The destination server responds to the proxy.

The proxy then sends the response back to the client.

---

# 3. Why Do We Use a Proxy?

Proxies are used for many purposes.

Common uses include:

- Security
- Access control
- Caching
- Monitoring
- Traffic filtering
- Authentication
- Hiding internal services
- Internet access control
- Routing application traffic
- SSL/TLS termination
- Load balancing

In DevOps, proxies are commonly used in front of applications and services.

---

# 4. Client, Proxy and Server

Consider:

```text
User
 |
 ↓
Browser
 |
 ↓
Proxy
 |
 ↓
Web Server
```

The browser is the client.

The proxy is the intermediary.

The web server is the destination.

The proxy can inspect, modify, filter, cache, or forward traffic depending on its configuration.

---

# 5. Forward Proxy

A **Forward Proxy** is positioned on the client side.

The client sends requests through the proxy to external servers.

Architecture:

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
Web Server
```

### Example

A company may configure employee computers to access the Internet through a corporate proxy.

```text
Employee Laptop
       |
       ↓
Corporate Proxy
       |
       ↓
Internet
```

The organization can use the proxy for:

- Access control
- Logging
- Filtering
- Monitoring
- Caching

---

# 6. Reverse Proxy

A **Reverse Proxy** is positioned in front of servers.

Clients communicate with the reverse proxy instead of directly communicating with backend servers.

Architecture:

```text
Client
   |
   ↓
Reverse Proxy
   |
   +------→ Application Server 1
   |
   +------→ Application Server 2
   |
   +------→ Application Server 3
```

Popular reverse proxy software includes:

- Nginx
- HAProxy
- Apache HTTP Server
- Envoy

---

# 7. Forward Proxy vs Reverse Proxy

| Feature | Forward Proxy | Reverse Proxy |
|---|---|---|
| Represents | Client | Server |
| Located near | Client/network | Server/application |
| Main purpose | Control outbound traffic | Control inbound traffic |
| Common use | Internet access | Application delivery |
| Hides | Client from destination | Backend servers from clients |
| Example | Corporate proxy | Nginx |

### Easy way to remember

```text
Forward Proxy
Client → Proxy → Internet

Reverse Proxy
Internet → Proxy → Servers
```

---

# 8. HTTP Proxy

An HTTP proxy handles HTTP traffic.

Example:

```text
Client
   |
   ↓
HTTP Proxy
   |
   ↓
HTTP Server
```

A proxy can receive an HTTP request and forward it to the destination.

It can also apply:

- Authentication
- Filtering
- Logging
- Caching

---

# 9. HTTPS Proxy

HTTPS traffic uses TLS encryption.

A proxy can interact with HTTPS traffic in different ways depending on its configuration.

One common mechanism is the HTTP `CONNECT` method.

Simplified flow:

```text
Client
   |
   | CONNECT
   ↓
Proxy
   |
   ↓
Destination
```

The proxy may establish a TCP tunnel between the client and destination.

### Important

HTTPS traffic is encrypted, so a normal forwarding proxy does not automatically see the encrypted HTTP contents.

Inspection of encrypted traffic requires specific proxy/TLS interception configurations and appropriate trust certificates.

---

# 10. Transparent Proxy

A **Transparent Proxy** intercepts traffic without requiring the client application to be explicitly configured to use a proxy.

Example:

```text
Client
   |
   ↓
Network
   |
   ↓
Transparent Proxy
   |
   ↓
Internet
```

The client may not know that its traffic is being proxied.

Transparent proxies are commonly used for:

- Network filtering
- Monitoring
- Access control
- Caching

---

# 11. Anonymous Proxy

An anonymous proxy can reduce the amount of client identity information exposed to the destination.

However, anonymity depends on the specific proxy configuration and network architecture.

A proxy should not automatically be considered a complete privacy or anonymity solution.

---

# 12. Caching Proxy

A caching proxy stores responses so they can potentially be reused for later requests.

Example:

```text
Client 1
   |
   ↓
Proxy
   |
   ↓
Internet
   |
   ↓
Server
```

The proxy caches the response.

Later:

```text
Client 2
   |
   ↓
Proxy
   |
   ↓
Cached Response
```

### Benefits

- Reduced bandwidth usage
- Faster responses for cacheable content
- Reduced load on destination servers

Caching depends on HTTP caching rules and proxy configuration.

---

# 13. Proxy Authentication

A proxy can require users or applications to authenticate before forwarding requests.

Example:

```text
Client
   |
   ↓
Proxy
   |
   | Authentication
   ↓
Internet
```

Authentication can help organizations control who can use the proxy.

Possible mechanisms depend on the proxy and environment.

---

# 14. Proxy and DNS

DNS and proxying are separate concepts.

DNS resolves names:

```text
example.com
     ↓
IP Address
```

A proxy handles traffic between the client and destination.

Depending on the proxy type and configuration, DNS resolution may happen:

```text
Client side
```

or:

```text
Proxy side
```

This distinction can matter when troubleshooting.

---

# 15. Proxy and NAT

Proxy and NAT are different.

### NAT

NAT changes or translates network addresses and/or ports.

```text
Private IP
   ↓
NAT
   ↓
Public IP
```

### Proxy

A proxy acts as an intermediary at the application or connection level.

```text
Client
   ↓
Proxy
   ↓
Server
```

A network can use both.

Example:

```text
Client
   |
   ↓
Forward Proxy
   |
   ↓
NAT Gateway
   |
   ↓
Internet
```

---

# 16. Proxy vs Gateway

A Gateway is a network entry/exit point between networks.

A Proxy is an intermediary that handles requests or connections on behalf of a client or server.

### Gateway

```text
Network A
    |
    ↓
Gateway
    |
    ↓
Network B
```

### Proxy

```text
Client
    |
    ↓
Proxy
    |
    ↓
Server
```

### Important

The terms can overlap in real-world products, but they describe different networking roles.

---

# 17. Proxy vs Load Balancer

A load balancer distributes traffic across multiple backend servers.

A reverse proxy can also perform load balancing.

Example:

```text
Client
   |
   ↓
Reverse Proxy / Load Balancer
   |
   +------→ Server 1
   |
   +------→ Server 2
   |
   +------→ Server 3
```

### Difference

A proxy is primarily an intermediary.

A load balancer's primary purpose is distributing traffic among backend resources.

Many modern products perform both functions.

---

# 18. Reverse Proxy in DevOps

Reverse proxies are extremely common in DevOps.

A typical architecture:

```text
Internet
   |
   ↓
DNS
   |
   ↓
Reverse Proxy
   |
   +--------→ Frontend
   |
   +--------→ Backend API
   |
   +--------→ Microservice
```

A reverse proxy can provide:

- TLS termination
- Routing
- Load balancing
- Authentication
- Rate limiting
- Security controls
- Header manipulation
- Logging

---

# 19. Nginx as a Reverse Proxy

Nginx is commonly used as a reverse proxy.

Example:

```text
Client
   |
   ↓
Nginx
   |
   ↓
Application
```

A simplified Nginx configuration can look like:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8080;
    }
}
```

In this example:

```text
Client
   |
   ↓
Nginx :80
   |
   ↓
Application :8080
```

The client does not need to access port `8080` directly.

---

# 20. Proxy in Docker

Containers may need proxies for outbound Internet access.

For example:

```text
Container
   |
   ↓
Docker Network
   |
   ↓
Proxy
   |
   ↓
Internet
```

Proxy environment variables commonly include:

```bash
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

Example:

```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
```

`NO_PROXY` is used to specify destinations that should bypass the proxy.

Example:

```bash
export NO_PROXY=localhost,127.0.0.1
```

---

# 21. Proxy in Kubernetes

Kubernetes environments can use proxies for both inbound and outbound traffic.

For example:

```text
Internet
   |
   ↓
Ingress / Gateway / Reverse Proxy
   |
   ↓
Service
   |
   ↓
Pod
```

For outbound traffic:

```text
Pod
 |
 ↓
Proxy
 |
 ↓
Internet
```

Proxy configuration can be provided through environment variables or application-specific configuration.

Common variables include:

```bash
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

### Important Kubernetes consideration

The `NO_PROXY` configuration often needs to include internal cluster destinations so internal traffic does not unnecessarily go through an external proxy.

---

# 22. Proxy in Cloud Environments

Cloud environments commonly use proxies for:

- Security
- Outbound Internet control
- Application routing
- Private network access
- Monitoring
- Traffic inspection

Example:

```text
Private Server
      |
      ↓
Corporate Proxy
      |
      ↓
NAT Gateway
      |
      ↓
Internet
```

A proxy can provide application-level control, while the NAT Gateway provides network-level address translation.

---

# 23. Common Proxy Problems

## Problem 1 — Proxy Unreachable

Symptoms:

```text
Connection refused
Timeout
```

Check:

```bash
ping <proxy-ip>
```

and:

```bash
nc -zv <proxy-host> <proxy-port>
```

---

## Problem 2 — Wrong Proxy Configuration

Check:

```bash
env | grep -i proxy
```

Look for:

```text
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

---

## Problem 3 — NO_PROXY Incorrect

An internal service may incorrectly go through the proxy.

Check:

```bash
echo $NO_PROXY
```

Ensure required internal domains, hosts, or IP ranges are configured according to the environment.

---

## Problem 4 — DNS Problem

Check:

```bash
getent hosts <domain>
```

---

## Problem 5 — TLS Certificate Problem

If a proxy performs TLS interception, certificate trust configuration can become important.

Test:

```bash
curl -v https://example.com
```

Look for certificate errors.

---

## Problem 6 — Authentication Failure

The proxy may require authentication.

Check application/proxy logs and authentication configuration.

Do not expose credentials in logs or commands.

---

# 24. Production Example

Consider a company with many private servers.

The company does not want every server to have unrestricted direct Internet access.

Architecture:

```text
Private Server
      |
      ↓
Forward Proxy
      |
      ↓
Firewall
      |
      ↓
NAT Gateway
      |
      ↓
Internet
```

The proxy can control:

```text
Which destinations are allowed
Which users/applications can connect
What traffic should be logged
```

The firewall provides network-level security.

The NAT Gateway provides address translation.

Each component has a different responsibility.

---

# 25. Key Takeaways

### Proxy

A proxy acts as an intermediary between a client and destination.

### Forward Proxy

Represents clients.

```text
Client → Forward Proxy → Internet
```

### Reverse Proxy

Represents backend servers.

```text
Internet → Reverse Proxy → Backend
```

### Common DevOps Uses

```text
TLS termination
Routing
Load balancing
Caching
Authentication
Security
Logging
Access control
```

### Common Tools

```text
Nginx
HAProxy
Envoy
Apache HTTP Server
Squid
```

### Common Proxy Environment Variables

```bash
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

### Important Troubleshooting Commands

```bash
env | grep -i proxy
```

```bash
curl -v https://example.com
```

```bash
nc -zv <proxy-host> <proxy-port>
```

```bash
getent hosts <domain>
```

---

# Final Mental Model

Remember:

```text
FORWARD PROXY

Client
  |
  ↓
Proxy
  |
  ↓
Internet
  |
  ↓
Server
```

The proxy acts **on behalf of the client**.

And:

```text
REVERSE PROXY

Client
  |
  ↓
Internet
  |
  ↓
Reverse Proxy
  |
  +------→ Backend 1
  |
  +------→ Backend 2
  |
  +------→ Backend 3
```

The reverse proxy acts **in front of the servers**.

---

# One-Line Definition

> **A proxy is an intermediary that receives traffic from one side and forwards it to another side according to its configuration and policies.**