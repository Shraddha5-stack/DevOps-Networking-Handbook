# 🎤 Chapter 27 — WebSockets Interview Questions

## 🟢 Basic Questions

### 1. What is WebSocket?

WebSocket is a communication protocol that provides a **persistent, full-duplex communication channel** between a client and server over a TCP connection.

It is commonly used for real-time applications.

---

### 2. Why are WebSockets used?

WebSockets are used when an application requires real-time, bidirectional communication.

Common examples:

* Chat applications
* Live notifications
* Real-time dashboards
* Multiplayer games
* Trading applications
* Monitoring systems

---

### 3. What is full-duplex communication?

Full-duplex means both the client and server can send data independently over the same connection.

```text
Client ─────────→ Server
Client ←───────── Server
```

---

### 4. What is the difference between HTTP and WebSocket?

| HTTP                                       | WebSocket                              |
| ------------------------------------------ | -------------------------------------- |
| Request-response                           | Persistent connection                  |
| Client normally initiates communication    | Both sides can send                    |
| Suitable for APIs/web pages                | Suitable for real-time communication   |
| Requests are independent                   | Connection remains open                |
| Higher overhead for repeated communication | Efficient for continuous communication |

---

### 5. What transport protocol does WebSocket use?

WebSockets normally operate over **TCP**.

```text
Application
    ↓
WebSocket
    ↓
TCP
    ↓
IP
```

---

### 6. What port does WebSocket use?

There is no single mandatory WebSocket port.

Common deployments use:

```text
ws://  → TCP 80
wss:// → TCP 443
```

The application can also use another port internally.

---

### 7. What is `ws://`?

`ws://` represents an unencrypted WebSocket connection.

Example:

```text
ws://example.com/socket
```

---

### 8. What is `wss://`?

`wss://` represents a WebSocket connection protected by TLS.

Example:

```text
wss://example.com/socket
```

It is commonly used in production.

---

# 🟡 Intermediate Questions

### 9. How does a WebSocket connection start?

A WebSocket connection begins with an HTTP-based handshake.

Simplified:

```text
Client
   ↓
HTTP Upgrade Request
   ↓
Server
   ↓
101 Switching Protocols
   ↓
WebSocket Connection
```

---

### 10. What is HTTP Upgrade?

HTTP Upgrade allows the client to request switching the connection from HTTP to another protocol, such as WebSocket.

Important headers include:

```text
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key
Sec-WebSocket-Version
```

---

### 11. What does HTTP status code 101 mean?

`101 Switching Protocols` means the server accepted the requested protocol upgrade.

For a successful WebSocket handshake, this indicates that the connection is transitioning to WebSocket communication.

---

### 12. What are WebSocket frames?

WebSocket communication after the handshake uses frames.

Common frame types include:

* Text
* Binary
* Ping
* Pong
* Close

---

### 13. What is a WebSocket Ping?

Ping is a WebSocket control frame that can be used to check whether a connection is responsive.

---

### 14. What is Pong?

Pong is the corresponding control response to a Ping.

```text
Ping
 ↓
Pong
```

---

### 15. Why are Ping/Pong messages useful?

They can help detect:

* Dead connections
* Broken network paths
* Unresponsive peers
* Idle connections

---

### 16. How is a WebSocket connection closed?

A WebSocket connection can be closed using a Close control frame.

```text
Client
  ↓ Close
Server
  ↓ Close
Connection Closed
```

---

### 17. What is the WebSocket lifecycle?

A typical lifecycle is:

```text
DNS
 ↓
TCP
 ↓
TLS (wss://)
 ↓
HTTP Upgrade
 ↓
101 Switching Protocols
 ↓
WebSocket Communication
 ↓
Close
```

---

### 18. What is the difference between WebSocket and polling?

With polling, the client repeatedly sends requests:

```text
Client → Request
Server → Response

Client → Request
Server → Response
```

WebSocket maintains a persistent connection:

```text
Client ═══════════ Server
       ←→ messages
```

---

### 19. What is long polling?

Long polling is an HTTP technique where the server keeps a request open until data is available or a timeout occurs.

It is different from WebSocket because WebSocket creates a persistent bidirectional communication channel.

---

### 20. What is WebSocket connection persistence?

A WebSocket connection can remain open for a long period instead of creating a new connection for every message.

---

# 🔐 Security Questions

### 21. How do you secure WebSocket communication?

Use:

```text
wss://
```

which provides TLS encryption.

Also implement:

* Authentication
* Authorization
* Input validation
* Rate limiting
* Connection limits
* Appropriate timeouts

---

### 22. What is the difference between `ws://` and `wss://`?

```text
ws://
 ↓
WebSocket
 ↓
TCP
```

```text
wss://
 ↓
WebSocket
 ↓
TLS
 ↓
TCP
```

`wss://` protects the communication using TLS.

---

### 23. Can WebSockets use authentication?

Yes.

Depending on the architecture, authentication can involve:

* Cookies
* Authorization headers during the handshake
* Tokens
* Application-level authentication

---

### 24. What is authentication vs authorization?

Authentication:

> Who are you?

Authorization:

> What are you allowed to do?

Both may be required for a WebSocket application.

---

# 🌐 Proxy and Load Balancer Questions

### 25. Can WebSockets work through a reverse proxy?

Yes.

A reverse proxy must correctly support the WebSocket upgrade and persistent connection behavior.

Architecture:

```text
Client
  ↓
Reverse Proxy
  ↓
WebSocket Server
```

---

### 26. How does Nginx support WebSockets?

Nginx commonly uses HTTP/1.1 and forwards the WebSocket upgrade headers.

Example:

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";
```

---

### 27. What happens if the reverse proxy does not support WebSocket upgrades?

The handshake may fail.

For example:

```text
Client
  ↓
Upgrade Request
  ↓
Proxy ✗
```

The client may receive an error instead of:

```text
101 Switching Protocols
```

---

### 28. What are WebSocket timeout issues?

Because WebSockets are persistent, load balancers and proxies may close connections that remain idle for too long.

Check:

* Proxy timeout
* Load balancer idle timeout
* Application heartbeat
* Network devices

---

### 29. How would you troubleshoot a WebSocket connection that closes after 60 seconds?

I would check:

1. Load balancer timeout
2. Reverse proxy timeout
3. Ingress timeout
4. Application timeout
5. Ping/Pong or heartbeat configuration
6. Network/firewall behavior

---

### 30. What is TLS termination for WebSockets?

TLS termination means decrypting the `wss://` connection at a component such as:

* Load balancer
* Nginx
* Ingress Controller

Example:

```text
Client
  │ wss://
  ▼
Load Balancer
  │
  │ TLS Termination
  ▼
WebSocket Backend
```

---

# ☸️ Kubernetes Questions

### 31. Can WebSockets work with Kubernetes?

Yes.

A typical architecture is:

```text
Internet
   ↓
Load Balancer
   ↓
Ingress
   ↓
Service
   ↓
WebSocket Pod
```

---

### 32. What should you check when WebSockets fail in Kubernetes?

I would check:

```text
DNS
 ↓
Load Balancer
 ↓
Ingress
 ↓
TLS
 ↓
Service
 ↓
Endpoints
 ↓
Pod
 ↓
Application
```

Useful commands:

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl describe ingress <name>
kubectl logs <pod>
```

---

### 33. How do you check whether a Kubernetes Service has backend endpoints?

```bash
kubectl get endpoints <SERVICE-NAME>
```

Or:

```bash
kubectl get endpointslice
```

If there are no endpoints, the Service may not be selecting healthy Pods.

---

### 34. Why can a WebSocket connection return 502 Bad Gateway?

A `502` can indicate that a reverse proxy or gateway could not successfully communicate with its upstream backend.

Possible causes:

* Backend is down
* Incorrect Service port
* Incorrect target port
* Network connectivity problem
* Proxy configuration problem
* Application failure

---

### 35. Why can a WebSocket connection return 404?

Possible causes include:

* Incorrect WebSocket path
* Incorrect Ingress rule
* Incorrect reverse-proxy routing
* Application does not expose the requested endpoint

---

### 36. Why can a WebSocket connection return 401?

Usually because authentication failed or credentials were missing/invalid.

---

### 37. Why can a WebSocket connection return 403?

Usually because the request was authenticated but not authorized, or a proxy/security policy denied it.

---

# 🔴 Troubleshooting Questions

### 38. How would you troubleshoot a WebSocket connection from scratch?

I would troubleshoot layer by layer:

```text
1. DNS
2. TCP
3. TLS
4. HTTP Upgrade
5. 101 response
6. Load Balancer
7. Reverse Proxy
8. Ingress
9. Service
10. Pod
11. Application
```

Commands:

```bash
dig example.com
```

```bash
nc -vz example.com 443
```

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

```bash
curl -v https://example.com
```

---

### 39. How do you check TLS for a `wss://` endpoint?

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

Check:

* Certificate
* Certificate chain
* TLS version
* Cipher
* Verification result

---

### 40. How do you check if port 443 is reachable?

```bash
nc -vz example.com 443
```

If successful, TCP connectivity to port 443 is working.

---

### 41. How do you check active TCP connections?

```bash
ss -tn
```

To see processes:

```bash
sudo ss -tnp
```

---

### 42. How do you check WebSocket server logs?

For a normal Linux service:

```bash
journalctl -u <service-name>
```

For Docker:

```bash
docker logs <container-name>
```

For Kubernetes:

```bash
kubectl logs <pod-name>
```

---

### 43. How do you troubleshoot Nginx WebSocket problems?

I would check:

```bash
sudo nginx -t
```

Then:

```bash
sudo tail -f /var/log/nginx/error.log
```

And:

```bash
sudo tail -f /var/log/nginx/access.log
```

I would also verify:

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";
```

---

### 44. What does `TCP connectivity successful` prove?

It proves that a TCP connection can be established to the specified host and port.

It does **not** prove that:

* TLS works
* WebSocket handshake works
* Authentication works
* Application works

---

# 🏗️ Scenario-Based Questions

### 45. WebSocket works locally but fails through Nginx. What do you check?

I would compare:

```text
Local:
Client → WebSocket Server

Production:
Client → Nginx → WebSocket Server
```

Then check:

* Upgrade headers
* HTTP version
* Proxy configuration
* Proxy timeout
* Backend connectivity
* Nginx logs

---

### 46. WebSocket works through HTTP but fails through HTTPS. What would you investigate?

I would investigate the TLS layer.

Check:

```text
Certificate
Certificate chain
Hostname
SNI
TLS version
Port 443
Load balancer
```

Command:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

---

### 47. WebSocket connects successfully but disconnects frequently. What could cause it?

Possible causes:

* Idle timeout
* Load balancer timeout
* Proxy timeout
* Firewall timeout
* Network instability
* Application errors
* Missing heartbeat
* Resource exhaustion

---

### 48. Kubernetes Pods are healthy but WebSocket connections fail. What would you check?

I would not assume the Pods are the problem.

I would check the entire path:

```text
Client
 ↓
DNS
 ↓
Load Balancer
 ↓
Ingress
 ↓
Service
 ↓
Endpoints
 ↓
Pod
```

Then check application logs.

---

### 49. Service exists but WebSocket traffic does not reach Pods. What would you check?

Check:

```bash
kubectl get svc
```

```bash
kubectl describe svc <SERVICE-NAME>
```

```bash
kubectl get endpoints <SERVICE-NAME>
```

Also verify:

* Selector
* TargetPort
* Pod labels
* Pod readiness

---

# 🎯 DevOps Interview Questions

### 50. Explain WebSockets as a DevOps engineer.

A strong answer:

> WebSocket is a protocol that provides persistent, full-duplex communication between a client and server. It starts with an HTTP Upgrade handshake and, after a successful `101 Switching Protocols` response, the connection becomes a WebSocket connection. In DevOps, WebSockets are important because they need to work correctly through load balancers, reverse proxies, Nginx, Kubernetes Ingress, Services, firewalls, and TLS termination. For secure production communication, `wss://` is normally used. I troubleshoot WebSocket issues layer by layer, starting with DNS and TCP, then TLS, HTTP upgrade, proxy or Ingress configuration, Service endpoints, and finally the application.

---

# 🧠 Rapid-Fire Revision

| Question               | Answer                          |
| ---------------------- | ------------------------------- |
| WebSocket?             | Persistent full-duplex protocol |
| Transport?             | TCP                             |
| `ws://`?               | Unencrypted WebSocket           |
| `wss://`?              | WebSocket over TLS              |
| HTTPS port?            | Commonly 443                    |
| WebSocket handshake?   | HTTP Upgrade                    |
| Successful status?     | 101 Switching Protocols         |
| Data format?           | WebSocket frames                |
| Ping?                  | Control/heartbeat mechanism     |
| Pong?                  | Response to Ping                |
| Reverse proxy support? | Yes                             |
| Nginx support?         | Yes                             |
| Kubernetes support?    | Yes                             |
| TLS?                   | Use `wss://`                    |
| Persistent connection? | Yes                             |
| Full duplex?           | Yes                             |
| 502?                   | Gateway/upstream problem        |
| 404?                   | Routing/path problem            |
| 401?                   | Authentication problem          |
| 403?                   | Authorization/security denial   |

---

# 🏆 Final Interview Checklist

Before completing Chapter 27, I should be able to explain:

```text
[ ] What is WebSocket?
[ ] Why use WebSockets?
[ ] HTTP vs WebSocket
[ ] Full-duplex communication
[ ] WebSocket over TCP
[ ] ws://
[ ] wss://
[ ] WebSocket handshake
[ ] HTTP Upgrade
[ ] 101 Switching Protocols
[ ] WebSocket frames
[ ] Ping/Pong
[ ] Connection lifecycle
[ ] Authentication
[ ] Authorization
[ ] TLS termination
[ ] Reverse proxy
[ ] Nginx WebSockets
[ ] Load balancer
[ ] Kubernetes WebSockets
[ ] Ingress
[ ] Service
[ ] Endpoint troubleshooting
[ ] Timeout problems
[ ] 401/403/404/502 errors
[ ] DNS/TCP/TLS troubleshooting
```

---

# 🎯 Final Mental Model

```text
                         WebSocket
                             │
                             ▼
                    HTTP Upgrade Request
                             │
                             ▼
                    101 Switching Protocols
                             │
                             ▼
                   Persistent TCP Connection
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
                 Client             Server
                    ↕                 ↕
                    └──── Messages ───┘
                             │
                             ▼
                  Reverse Proxy / Ingress
                             │
                             ▼
                         Service
                             │
                             ▼
                            Pod
```

> **Interview key point:** WebSockets are persistent, full-duplex connections. The most important DevOps troubleshooting path is **DNS → TCP → TLS → HTTP Upgrade → 101 → Proxy/Ingress → Service → Pod → Application**.
