# 🌐 Chapter 27 — WebSockets

## 📚 Overview

WebSockets provide a persistent, full-duplex communication channel between a client and a server over a single TCP connection.

Unlike traditional HTTP request-response communication, WebSockets allow both the client and server to send messages independently after the connection is established.

---

## 🎯 Objectives

In this chapter, I will learn:

* What WebSockets are
* How WebSockets work
* WebSocket vs HTTP
* WebSocket handshake
* Full-duplex communication
* WebSocket frames
* `ws://` and `wss://`
* WebSocket connection lifecycle
* WebSocket status codes
* Reverse proxy support
* Nginx WebSocket configuration
* Kubernetes WebSocket networking
* WebSocket troubleshooting
* DevOps use cases

---

## 🔄 Traditional HTTP

HTTP normally follows a request-response model:

```text
Client
  │
  │ HTTP Request
  ▼
Server
  │
  │ HTTP Response
  ▼
Client
```

The client normally initiates the communication.

---

## ⚡ WebSocket Communication

WebSockets maintain a persistent connection:

```text
Client
   │
   │ WebSocket Connection
   │══════════════════════│
   │                      │
   │ ←──── Message ───────│
   │ ───── Message ──────→│
   │ ←──── Message ───────│
   │ ───── Message ──────→│
   │                      │
   └──────────────────────┘
```

Both sides can send messages.

---

## 🔑 Important Concepts

| Concept               | Meaning                                        |
| --------------------- | ---------------------------------------------- |
| WebSocket             | Persistent, full-duplex communication protocol |
| `ws://`               | WebSocket without TLS                          |
| `wss://`              | WebSocket over TLS                             |
| Handshake             | Initial HTTP-based upgrade process             |
| Frame                 | Unit used to carry WebSocket data              |
| Full-duplex           | Both sides can communicate independently       |
| Persistent connection | Connection remains open until closed           |

---

## 🤝 WebSocket Handshake

WebSockets begin with an HTTP request that asks the server to upgrade the connection.

Simplified:

```text
Client
   │
   │ HTTP Upgrade Request
   ▼
Server
   │
   │ 101 Switching Protocols
   ▼
WebSocket Connection
```

After the successful upgrade, communication uses the WebSocket protocol.

---

## 🔐 WebSocket URLs

Unencrypted:

```text
ws://example.com
```

Encrypted:

```text
wss://example.com
```

`wss://` is WebSocket communication protected by TLS.

---

## 🌍 Common Use Cases

WebSockets are useful for applications requiring real-time communication:

* Chat applications
* Live notifications
* Real-time dashboards
* Online collaboration
* Multiplayer games
* Live monitoring
* Trading applications
* IoT applications

---

## ☁️ DevOps Relevance

WebSockets are important for DevOps because infrastructure may need to support persistent connections through:

* Nginx
* Reverse proxies
* Load balancers
* Kubernetes Ingress
* Cloud load balancers
* Firewalls
* TLS termination

---

## 🏗️ Typical Architecture

```text
User
 │
 │ wss://
 ▼
Load Balancer
 │
 ▼
Reverse Proxy / Ingress
 │
 ▼
Service
 │
 ▼
WebSocket Application
```

---

## 🧪 Troubleshooting Flow

When WebSockets are not working:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP Upgrade
 ↓
101 Switching Protocols
 ↓
WebSocket Connection
 ↓
Application
```

Useful tools include:

```bash
curl
openssl
ss
kubectl
```

---

## 📂 Chapter Contents

```text
27-WebSockets/
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

---

## 🎓 Expected Outcome

After completing this chapter, I should be able to:

* Explain WebSockets
* Explain HTTP Upgrade
* Explain the WebSocket handshake
* Understand `ws://` and `wss://`
* Understand persistent connections
* Troubleshoot WebSocket connectivity
* Understand reverse-proxy WebSocket support
* Understand WebSockets in Kubernetes

---

## 🏆 Goal

> Understand how WebSockets provide real-time, persistent, full-duplex communication and learn how to support and troubleshoot them in DevOps environments.
