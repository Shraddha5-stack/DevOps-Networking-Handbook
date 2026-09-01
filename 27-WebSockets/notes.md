# 🌐 Chapter 27 — WebSockets Notes

## 1. What are WebSockets?

**WebSocket** is a communication protocol that provides a persistent, full-duplex communication channel between a client and a server over a single TCP connection.

With WebSockets, both the client and server can send messages independently after the connection is established.

```text
Client
   │
   │ WebSocket Connection
   │══════════════════════│
   │                      │
   │ ───── Message ──────→│
   │ ←──── Message ───────│
   │ ───── Message ──────→│
   │ ←──── Message ───────│
   │                      │
   └──────────────────────┘
```

---

# 2. Why Do We Need WebSockets?

Traditional HTTP is primarily request-response based.

For example:

```text
Client → Request → Server
Client ← Response ← Server
```

If the server needs to send new information to the client, additional mechanisms are often required, such as polling or server-sent events.

WebSockets allow the server to send data to the client immediately over an existing persistent connection.

---

# 3. WebSocket Characteristics

WebSockets provide:

* Persistent connection
* Full-duplex communication
* Low communication overhead after connection establishment
* Real-time data exchange
* Server-to-client communication
* Client-to-server communication

---

# 4. What Does Full-Duplex Mean?

Full-duplex means both sides can communicate independently at the same time.

```text
Client ───────────────→ Server
Client ←─────────────── Server
```

The client does not need to wait for a new HTTP request before the server can send a WebSocket message.

---

# 5. WebSocket vs HTTP

| HTTP                                  | WebSocket                           |
| ------------------------------------- | ----------------------------------- |
| Request-response model                | Persistent communication            |
| Client normally initiates requests    | Both sides can send messages        |
| Connection may be short-lived         | Connection stays open               |
| Higher overhead for repeated requests | Efficient for ongoing communication |
| Common for REST APIs                  | Common for real-time applications   |

---

# 6. WebSocket Connection

A WebSocket connection starts with an HTTP-based handshake.

Simplified flow:

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

After the successful upgrade, the connection uses the WebSocket protocol.

---

# 7. HTTP Upgrade

The initial WebSocket handshake uses HTTP headers to request a protocol upgrade.

Example:

```http
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: <key>
Sec-WebSocket-Version: 13
```

The server can accept the upgrade with:

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
```

The exact handshake includes additional protocol-defined headers.

---

# 8. Status Code 101

HTTP status code:

```text
101 Switching Protocols
```

indicates that the server is switching protocols as requested by the client.

For WebSockets, a successful handshake results in a WebSocket connection.

---

# 9. WebSocket URL Schemes

WebSockets have two common URL schemes.

## `ws://`

Unencrypted WebSocket communication.

```text
ws://example.com/chat
```

## `wss://`

WebSocket communication protected by TLS.

```text
wss://example.com/chat
```

Think of:

```text
ws://  → WebSocket
wss:// → WebSocket + TLS
```

---

# 10. WebSocket and TCP

WebSockets normally operate over TCP.

Simplified protocol stack:

```text
Application
    ↓
WebSocket
    ↓
TCP
    ↓
IP
```

For secure WebSockets:

```text
Application
    ↓
WebSocket
    ↓
TLS
    ↓
TCP
    ↓
IP
```

---

# 11. WebSocket Frames

After the connection is established, WebSocket communication uses **frames**.

Frames can carry different types of information.

Important frame types include:

* Text
* Binary
* Ping
* Pong
* Close

---

# 12. Text Frames

Text frames carry UTF-8 encoded text data.

Example:

```text
Hello
```

or:

```json
{"message":"Hello"}
```

---

# 13. Binary Frames

Binary frames are used for binary data.

Examples:

* Images
* Audio
* Files
* Binary application data

---

# 14. Ping and Pong

WebSockets support control frames such as:

```text
Ping
  ↓
Pong
```

They can be used to help determine whether the connection is still responsive.

Applications and infrastructure may also implement their own heartbeat mechanisms.

---

# 15. Close Frame

A WebSocket connection can be closed using a close control frame.

Simplified:

```text
Client
   │
   │ Close
   ▼
Server
   │
   │ Close
   ▼
Connection Closed
```

---

# 16. WebSocket Connection Lifecycle

A typical lifecycle is:

```text
1. DNS Resolution
       ↓
2. TCP Connection
       ↓
3. TLS Connection (for wss://)
       ↓
4. HTTP Upgrade Request
       ↓
5. 101 Switching Protocols
       ↓
6. WebSocket Communication
       ↓
7. Close
```

---

# 17. WebSocket Through a Proxy

A WebSocket connection may pass through:

```text
Client
   ↓
Load Balancer
   ↓
Reverse Proxy
   ↓
Application
```

The proxy must correctly support the WebSocket upgrade and connection behavior.

---

# 18. WebSocket and Reverse Proxy

A reverse proxy must generally preserve the required upgrade semantics.

For example, Nginx commonly uses:

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";
```

The exact configuration depends on the proxy and application architecture.

---

# 19. Nginx WebSocket Architecture

Example:

```text
Client
   │
   │ wss://
   ▼
Nginx
   │
   │ WebSocket Proxy
   ▼
Application
```

Nginx can:

* Accept the client connection
* Terminate TLS if configured to do so
* Forward WebSocket traffic
* Route requests to backend applications

---

# 20. WebSocket Through Kubernetes

A common architecture is:

```text
Internet
    │
    │ wss://
    ▼
Load Balancer
    │
    ▼
Ingress Controller
    │
    ▼
Service
    │
    ▼
WebSocket Pod
```

Kubernetes itself does not define the WebSocket application protocol. The application and the networking components must support persistent upgraded connections.

---

# 21. WebSocket and Kubernetes Service

A Kubernetes Service provides a stable network endpoint for the application.

```text
Client
   ↓
Ingress
   ↓
Service
   ↓
Pod
```

The Service forwards traffic to healthy matching Pods.

---

# 22. WebSocket and TLS

For production applications, encrypted WebSockets are normally preferred.

```text
ws://
```

does not provide TLS encryption.

```text
wss://
```

uses TLS.

Architecture:

```text
Client
   │
   │ wss://
   ▼
TLS
   │
   ▼
WebSocket
   │
   ▼
Application
```

---

# 23. WebSocket Authentication

WebSockets can use authentication mechanisms supported by the application and surrounding infrastructure.

Common approaches include:

* Cookies
* Authorization headers during the handshake
* Tokens
* Application-level authentication

The authentication design depends on the application.

---

# 24. WebSocket Authorization

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to do?

A WebSocket application should validate both when required.

Example:

```text
Client
  ↓
Authentication
  ↓
Authorization
  ↓
WebSocket Connection
```

---

# 25. WebSocket Scaling

Persistent connections create different scaling considerations compared with ordinary short-lived HTTP requests.

Example:

```text
                Load Balancer
                /           \
               /             \
              ▼               ▼
        WebSocket Pod 1   WebSocket Pod 2
```

A client connection remains attached to a particular backend connection until it closes or is otherwise moved.

---

# 26. Connection Persistence

WebSocket connections can remain open for a long time.

Therefore infrastructure should consider:

* Idle timeouts
* Connection limits
* Resource usage
* Load balancer timeouts
* Proxy timeouts
* Application heartbeat behavior

---

# 27. WebSocket Heartbeats

Long-lived connections may use ping/pong or application-level heartbeat mechanisms.

Example:

```text
Client
   │
   │ Ping
   ▼
Server
   │
   │ Pong
   ▼
Client
```

This can help detect broken or inactive connections.

---

# 28. WebSocket Timeouts

A proxy or load balancer may close an idle WebSocket connection.

Example:

```text
Client
   │
   │ WebSocket
   ▼
Proxy
   │
   │ Idle for too long
   X
Connection closed
```

When troubleshooting, check timeout settings at every layer.

---

# 29. WebSocket Load Balancing

WebSocket connections can be load-balanced across multiple application instances.

```text
                   Load Balancer
                  /      |      \
                 ▼       ▼       ▼
                Pod1    Pod2    Pod3
```

Each WebSocket connection is established with one backend.

---

# 30. Session State and WebSockets

If the application stores connection-specific state only in local memory, scaling can become difficult.

Example:

```text
User A
  ↓
Pod 1
  ↓
Session State
```

If another request or connection reaches Pod 2, Pod 2 may not have that local state.

Possible solutions include:

* Shared databases
* Redis
* Distributed messaging systems
* Application-level synchronization

The correct design depends on the application.

---

# 31. WebSocket vs Polling

## Polling

The client repeatedly asks:

```text
Client → Are there new messages?
Server → No
Client → Are there new messages?
Server → No
Client → New message?
Server → Yes
```

This can create unnecessary requests.

## WebSocket

```text
Client ═════════ Server
          │
          │ Message
          │──────→
          │
          │ Message
          │←──────
```

The persistent connection allows real-time communication.

---

# 32. WebSocket vs Long Polling

Long polling keeps an HTTP request open until the server has data or a timeout occurs.

WebSockets instead establish a persistent upgraded connection designed for bidirectional communication.

---

# 33. WebSocket Use Cases

### Chat

```text
User A
  │
  ▼
WebSocket Server
  │
  ▼
User B
```

### Real-Time Dashboard

```text
Monitoring System
       ↓
WebSocket
       ↓
Dashboard
```

### Notifications

```text
Backend
   ↓
WebSocket
   ↓
Browser
```

---

# 34. WebSockets in DevOps

DevOps engineers may need to troubleshoot WebSocket communication across:

```text
DNS
 ↓
Firewall
 ↓
Load Balancer
 ↓
Reverse Proxy
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```

---

# 35. WebSocket Troubleshooting

When a WebSocket connection fails, troubleshoot layer by layer.

## Step 1 — DNS

```bash
dig example.com
```

## Step 2 — TCP

```bash
nc -vz example.com 443
```

## Step 3 — TLS

For `wss://`:

```bash
openssl s_client -connect example.com:443 -servername example.com
```

## Step 4 — HTTP Upgrade

Check whether the server returns:

```text
101 Switching Protocols
```

## Step 5 — Proxy

Check:

* Upgrade headers
* Connection headers
* Proxy version
* Proxy timeout
* Idle timeout

## Step 6 — Application

Check:

* Application logs
* Authentication
* Authorization
* Connection limits
* Application errors

---

# 36. Common WebSocket Problems

## Problem 1 — 400 Bad Request

Possible causes:

* Incorrect handshake
* Missing required headers
* Invalid request

---

## Problem 2 — 401 Unauthorized

Possible cause:

```text
Authentication failure
```

---

## Problem 3 — 403 Forbidden

Possible cause:

```text
Authorization failure
```

---

## Problem 4 — 404 Not Found

Possible causes:

* Incorrect WebSocket path
* Incorrect routing
* Wrong backend

---

## Problem 5 — 502 Bad Gateway

Possible causes:

* Backend unavailable
* Incorrect Service configuration
* Proxy cannot connect to backend
* Application failure

---

## Problem 6 — Connection Closes After a Period

Possible causes:

* Idle timeout
* Proxy timeout
* Load balancer timeout
* Application heartbeat failure
* Network interruption

---

# 37. WebSocket Security

Security considerations include:

* Use `wss://` in production
* Validate authentication
* Validate authorization
* Validate message input
* Apply rate limits
* Limit connection counts
* Protect against resource exhaustion
* Configure appropriate timeouts
* Monitor abnormal connections

---

# 38. WebSocket and Firewall

A firewall normally needs to allow the underlying transport connection.

For secure WebSockets, commonly:

```text
TCP 443
```

For non-TLS WebSockets, commonly:

```text
TCP 80
```

The exact port depends on the deployment.

---

# 39. WebSocket Monitoring

Important metrics include:

* Active connections
* New connections
* Closed connections
* Connection duration
* Messages per second
* Errors
* Authentication failures
* Backend latency
* CPU usage
* Memory usage

---

# 40. WebSocket Logging

Useful logs include:

```text
Connection established
Authentication successful
Authentication failed
Connection closed
Message received
Message sent
Backend error
Timeout
```

Logs help identify where a persistent connection is failing.

---

# 41. WebSocket Architecture Example

```text
                         Internet
                            │
                            │ wss://
                            ▼
                     Load Balancer
                            │
                            ▼
                    Nginx / Ingress
                            │
                            ▼
                       Kubernetes
                         Service
                            │
                ┌───────────┼───────────┐
                ▼           ▼           ▼
              Pod 1       Pod 2       Pod 3
                │           │           │
                └───────────┼───────────┘
                            ▼
                     WebSocket App
```

---

# 42. Important Commands

### DNS

```bash
dig example.com
```

### TCP

```bash
nc -vz example.com 443
```

### TLS

```bash
openssl s_client -connect example.com:443 -servername example.com
```

### HTTPS headers

```bash
curl -I https://example.com
```

### Kubernetes Pods

```bash
kubectl get pods
```

### Kubernetes Services

```bash
kubectl get svc
```

### Kubernetes Ingress

```bash
kubectl get ingress
```

---

# 43. WebSocket Mental Model

Remember:

```text
HTTP Request
      ↓
Upgrade Request
      ↓
101 Switching Protocols
      ↓
WebSocket Connection
      ↓
Full-Duplex Communication
      ↓
Close
```

---

# 44. Key Takeaways

```text
WebSocket
   ↓
Persistent connection
   ↓
Full-duplex communication
   ↓
Client ↔ Server
```

Important terms:

```text
ws://   → WebSocket
wss://  → WebSocket over TLS
101     → Switching Protocols
Ping    → Connection health/control
Pong    → Response to Ping
Close   → Connection termination
```

---

# 45. DevOps Troubleshooting Mental Model

```text
WebSocket Failure
       │
       ▼
     DNS?
       │
       ▼
   TCP reachable?
       │
       ▼
    TLS works?
       │
       ▼
HTTP Upgrade?
       │
       ▼
101 response?
       │
       ▼
Proxy configured?
       │
       ▼
Timeout correct?
       │
       ▼
Backend healthy?
       │
       ▼
Application logs
```

---

# 🧠 Final Revision

### What is WebSocket?

A protocol that provides persistent, full-duplex communication between a client and server.

### What is `wss://`?

WebSocket communication protected by TLS.

### What does 101 mean?

`101 Switching Protocols` indicates a successful HTTP protocol upgrade.

### What is full-duplex communication?

Both client and server can send data independently.

### What is a WebSocket frame?

A protocol-defined unit used to carry WebSocket data or control information.

### Why is WebSocket useful?

It is useful when an application needs persistent, real-time, bidirectional communication.

### What should I check when WebSockets fail?

```text
DNS → TCP → TLS → HTTP Upgrade → Proxy → Timeout → Backend → Application
```

> **Core idea:** WebSockets begin with an HTTP upgrade handshake and then maintain a persistent connection that allows both client and server to communicate in real time.
