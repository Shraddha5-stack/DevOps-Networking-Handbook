# 🌐 Chapter 23 – Proxy and Reverse Proxy

## 📚 Overview

A **proxy** and a **reverse proxy** are network components that sit between clients and servers and control how network requests are handled.

They are widely used in DevOps, cloud computing, web applications, security, load balancing, and microservices.

---

## 🎯 Learning Objectives

By completing this chapter, you will understand:

* What a proxy server is
* What a reverse proxy is
* Forward proxy vs reverse proxy
* How a proxy works
* How a reverse proxy works
* Common reverse proxy servers
* Nginx as a reverse proxy
* Proxy use cases in DevOps
* Load balancing with reverse proxies
* Basic proxy troubleshooting

---

## 🔄 What is a Proxy?

A **proxy server** acts as an intermediary between a client and another server.

Instead of the client connecting directly to the destination, the request passes through the proxy.

```text
Client
   |
   v
 Proxy
   |
   v
Internet / Server
```

The proxy receives the client's request and forwards it to the destination.

---

## 🌍 Forward Proxy

A **forward proxy** represents the client.

```text
Client
   |
   v
Forward Proxy
   |
   v
Internet
```

The destination server sees the proxy as the source of the request rather than directly seeing the client.

### Common Uses

* Internet access control
* Content filtering
* Privacy
* Corporate network policies
* Caching
* Monitoring outbound traffic

---

## 🔁 Reverse Proxy

A **reverse proxy** represents the server.

```text
Client
   |
   v
Reverse Proxy
   |
   +------> Application Server 1
   |
   +------> Application Server 2
   |
   +------> Application Server 3
```

The client communicates with the reverse proxy instead of directly communicating with the backend application.

---

## 🆚 Forward Proxy vs Reverse Proxy

| Feature         | Forward Proxy   | Reverse Proxy    |
| --------------- | --------------- | ---------------- |
| Represents      | Client          | Server           |
| Main direction  | Outbound        | Inbound          |
| Hides           | Client          | Backend servers  |
| Common use      | Internet access | Web applications |
| Load balancing  | Less common     | Very common      |
| SSL termination | Possible        | Very common      |
| Caching         | Possible        | Common           |

---

## 🚀 Why Use a Reverse Proxy?

A reverse proxy can provide several important capabilities:

### 1. Load Balancing

Distributes requests across multiple backend servers.

```text
                 +--> Server 1
Client --> Proxy +--> Server 2
                 +--> Server 3
```

---

### 2. SSL/TLS Termination

The reverse proxy can handle HTTPS connections and forward requests to backend applications.

```text
Client
  |
 HTTPS
  |
  v
Reverse Proxy
  |
 HTTP
  |
  v
Application
```

---

### 3. Security

Backend servers do not need to be directly exposed to clients.

```text
Internet
   |
   v
Reverse Proxy
   |
   v
Private Backend
```

---

### 4. Routing

A reverse proxy can route requests based on the hostname or URL path.

Example:

```text
example.com/api
        ↓
API Server

example.com/web
        ↓
Web Server
```

---

### 5. Caching

A reverse proxy can cache frequently requested content and reduce backend load.

---

### 6. Compression

A reverse proxy can compress responses before sending them to clients.

---

## 🛠️ Common Reverse Proxy Software

Popular technologies include:

* Nginx
* HAProxy
* Apache HTTP Server
* Traefik
* Envoy

Nginx is widely used as a web server and reverse proxy.

---

## 🌐 Nginx Reverse Proxy Architecture

A typical architecture looks like:

```text
                 Internet
                    |
                    v
              +-----------+
              |   Nginx   |
              |  Proxy    |
              +-----------+
                    |
          +---------+---------+
          |         |         |
          v         v         v
       App 1      App 2     App 3
```

Nginx receives the client request and forwards it to the appropriate backend.

---

## 💼 DevOps Use Cases

Reverse proxies are commonly used in:

* CI/CD platforms
* Kubernetes applications
* Microservices
* Cloud applications
* API gateways
* Web applications
* Load balancing
* SSL/TLS termination
* Service routing

---

## ☸️ Reverse Proxy in Kubernetes

In Kubernetes, reverse-proxy concepts appear in technologies such as:

```text
Client
   |
   v
Ingress / Gateway
   |
   v
Kubernetes Service
   |
   v
Pods
```

The proxy or gateway routes external requests to the appropriate Kubernetes service.

---

## 🔐 Security Architecture

A reverse proxy can provide an additional security boundary:

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

The database should generally not be directly exposed to the Internet.

---

## 🧪 Practical Learning

In this chapter, we will practice:

1. Identifying proxy concepts
2. Checking proxy environment variables
3. Testing HTTP requests with `curl`
4. Running an Nginx reverse proxy
5. Forwarding traffic to a backend application
6. Checking proxy logs
7. Testing connectivity
8. Troubleshooting proxy failures

---

## 📝 Chapter Files

| File                     | Purpose                          |
| ------------------------ | -------------------------------- |
| `README.md`              | Chapter overview                 |
| `notes.md`               | Proxy and reverse proxy concepts |
| `commands.md`            | Useful commands                  |
| `practical-lab.md`       | Hands-on reverse proxy lab       |
| `interview-questions.md` | Interview preparation            |
| `screenshots/`           | Practical screenshots            |

---

## 🎯 Key Takeaways

### Proxy

A proxy generally acts on behalf of the **client**.

### Reverse Proxy

A reverse proxy generally acts on behalf of the **server**.

### Remember

```text
Forward Proxy
    ↓
Client-side intermediary

Reverse Proxy
    ↓
Server-side intermediary
```

A reverse proxy can provide:

```text
Routing
Load Balancing
SSL/TLS Termination
Caching
Security
Compression
```

These capabilities make reverse proxies an important component of modern DevOps and cloud architectures.
