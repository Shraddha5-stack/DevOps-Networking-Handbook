# 🌐 Chapter 25 — HTTP & HTTPS

## 📖 Overview

HTTP and HTTPS are fundamental application-layer protocols used for communication between clients and servers.

As a DevOps engineer, understanding HTTP/HTTPS is essential because web applications, APIs, reverse proxies, load balancers, Kubernetes Ingress, CI/CD systems, monitoring tools, and cloud services depend heavily on them.

---

## 🎯 Learning Objectives

By completing this chapter, I will understand:

* What HTTP is
* What HTTPS is
* How HTTP request/response works
* HTTP methods
* HTTP status codes
* HTTP headers
* HTTP cookies
* HTTP sessions
* HTTP authentication basics
* Difference between HTTP and HTTPS
* TLS basics
* HTTP/1.1, HTTP/2, and HTTP/3
* HTTP troubleshooting
* HTTP commands used by DevOps engineers
* Real-world HTTP/HTTPS architecture

---

## 📚 Chapter Contents

### 1. HTTP Fundamentals

* What is HTTP?
* Client and server
* Request and response
* HTTP request structure
* HTTP response structure
* HTTP URL structure

### 2. HTTP Methods

* GET
* POST
* PUT
* PATCH
* DELETE
* HEAD
* OPTIONS

### 3. HTTP Status Codes

* 1xx — Informational
* 2xx — Success
* 3xx — Redirection
* 4xx — Client Errors
* 5xx — Server Errors

Important examples:

```text
200 OK
201 Created
204 No Content
301 Moved Permanently
302 Found
304 Not Modified
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
408 Request Timeout
409 Conflict
429 Too Many Requests
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

### 4. HTTP Headers

Learn commonly used headers:

```text
Host
Content-Type
Content-Length
Authorization
Accept
User-Agent
Cookie
Set-Cookie
Cache-Control
Location
Connection
X-Forwarded-For
X-Forwarded-Proto
```

### 5. Cookies and Sessions

Understand:

* Cookies
* Session identifiers
* Set-Cookie
* Cookie
* Secure cookies
* HttpOnly cookies
* SameSite cookies

### 6. HTTPS

Learn:

* What HTTPS means
* Why HTTPS is required
* TLS
* Certificates
* Certificate authorities
* Public/private keys
* TLS handshake
* Certificate validation

### 7. HTTP Versions

Understand the major versions:

```text
HTTP/1.1
HTTP/2
HTTP/3
```

### 8. DevOps Applications

HTTP/HTTPS is used with:

* Nginx
* Apache
* Docker
* Kubernetes
* Ingress
* Reverse proxies
* Load balancers
* REST APIs
* CI/CD systems
* Cloud services
* Monitoring systems

---

## 🧪 Practical Work

The practical labs will include commands such as:

```bash
curl
wget
ss
openssl
dig
ping
```

Example:

```bash
curl -I https://example.com
```

Verbose HTTP request:

```bash
curl -v https://example.com
```

Check TLS certificate:

```bash
openssl s_client -connect example.com:443
```

---

## 🔧 Real-World Architecture

A typical web application can look like:

```text
                    Internet
                       |
                       v
                +-------------+
                |   Client    |
                +-------------+
                       |
                    HTTPS
                       |
                       v
                +-------------+
                | Load        |
                | Balancer    |
                +-------------+
                       |
                       v
                +-------------+
                | Reverse     |
                | Proxy/Nginx |
                +-------------+
                       |
                       v
                +-------------+
                | Application |
                +-------------+
                       |
                       v
                +-------------+
                |  Database   |
                +-------------+
```

---

## 🧠 Key DevOps Concepts

A DevOps engineer should be able to troubleshoot:

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
Application
  ↓
Database
```

For example, if an application returns:

```text
502 Bad Gateway
```

the problem may be between a reverse proxy/load balancer and the upstream application.

If it returns:

```text
404 Not Found
```

the server may be reachable but the requested resource may not exist.

---

## 📁 Chapter Files

This chapter will contain:

```text
25-HTTP-HTTPS/
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

---

## 🎓 Expected Outcome

After completing Chapter 25, I should be able to:

* Explain HTTP and HTTPS clearly
* Understand request/response communication
* Identify HTTP methods
* Interpret HTTP status codes
* Inspect HTTP headers
* Use `curl` for troubleshooting
* Understand basic TLS and certificates
* Troubleshoot common HTTP/HTTPS problems
* Explain HTTP/HTTPS architecture in a DevOps interview

---

## 🚀 DevOps Connection

HTTP/HTTPS knowledge connects directly with:

```text
Linux
  ↓
Networking
  ↓
DNS
  ↓
TCP/IP
  ↓
HTTP/HTTPS
  ↓
Nginx
  ↓
Docker
  ↓
Kubernetes
  ↓
Ingress
  ↓
Cloud
  ↓
CI/CD
```

**Goal:** Build a strong networking foundation that can be applied to real-world DevOps infrastructure.
