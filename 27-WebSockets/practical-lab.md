# 🧪 Chapter 27 — WebSockets Practical Lab

## 🎯 Lab Objective

In this lab, I will:

* Understand a WebSocket connection
* Create a simple WebSocket server
* Connect to it using a WebSocket client
* Test `ws://`
* Inspect network connections
* Test WebSocket traffic through Nginx
* Understand `wss://`
* Troubleshoot WebSocket connectivity
* Understand how WebSockets work with DevOps infrastructure

---

# Part 1 — Check Required Tools

Check whether Python is installed:

```bash
python3 --version
```

Check `curl`:

```bash
curl --version
```

Check OpenSSL:

```bash
openssl version
```

Check networking tools:

```bash
ss --version
```

Optional:

```bash
which websocat
```

### Observation

Record the versions installed on your system.

---

# Part 2 — Create a Simple WebSocket Server

Create a working directory:

```bash
mkdir -p ~/websocket-lab
cd ~/websocket-lab
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the WebSocket library:

```bash
pip install websockets
```

Verify:

```bash
pip show websockets
```

---

# Part 3 — Create the WebSocket Server

Create:

```bash
nano server.py
```

Add:

```python
import asyncio
import websockets

async def handler(websocket):
    print("Client connected")

    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Server received: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket server listening on port 8765")
        await asyncio.Future()

asyncio.run(main())
```

Save and exit.

---

# Part 4 — Start the Server

Run:

```bash
python3 server.py
```

Expected output:

```text
WebSocket server listening on port 8765
```

The server is now listening on:

```text
0.0.0.0:8765
```

Keep this terminal running.

---

# Part 5 — Check the Listening Port

Open another terminal.

Run:

```bash
ss -ltnp | grep 8765
```

Expected result should show a listening TCP socket.

Example:

```text
LISTEN ... 0.0.0.0:8765
```

### Observation

Record:

* IP address
* Port
* Process

---

# Part 6 — Test with WebSocket Client

If `websocat` is installed:

```bash
websocat ws://localhost:8765
```

Type:

```text
Hello WebSocket
```

Expected response:

```text
Server received: Hello WebSocket
```

Try another message:

```text
Hello DevOps
```

Expected:

```text
Server received: Hello DevOps
```

---

# Part 7 — Observe the Server

Look at the server terminal.

You should see something similar to:

```text
Client connected
Received: Hello WebSocket
Received: Hello DevOps
```

This demonstrates bidirectional communication.

---

# Part 8 — Understand the Connection

The architecture is:

```text
WebSocket Client
       │
       │ ws://
       ▼
localhost:8765
       │
       ▼
Python WebSocket Server
```

The connection remains open while the client is connected.

---

# Part 9 — Check the Connection with `ss`

While `websocat` is connected, run:

```bash
ss -tnp | grep 8765
```

You should see an established TCP connection.

Look for:

```text
ESTAB
```

This confirms that the WebSocket connection is using an established TCP connection underneath.

---

# Part 10 — Test Multiple Messages

From the WebSocket client:

```text
Message 1
Message 2
Message 3
Message 4
```

Observe that the same connection can carry multiple messages.

### Observation

Unlike repeated short HTTP requests, the WebSocket connection remains open while communication continues.

---

# Part 11 — Test Multiple Clients

Open another terminal and connect:

```bash
websocat ws://localhost:8765
```

Send:

```text
Client 2 connected
```

The server should accept multiple connections.

Check:

```bash
ss -tnp | grep 8765
```

### Observation

You should see multiple established connections if both clients remain connected.

---

# Part 12 — Close the Connection

Exit the WebSocket client.

Depending on the client, use:

```text
Ctrl + C
```

Check:

```bash
ss -tnp | grep 8765
```

The established connection should disappear after the connection closes.

---

# Part 13 — Test HTTP Port vs WebSocket Port

The WebSocket server is listening on:

```text
8765
```

Try:

```bash
curl http://localhost:8765
```

The response may not be a normal HTTP page because this endpoint is intended for WebSocket communication.

### Observation

A WebSocket endpoint is not automatically a normal REST/HTTP endpoint.

---

# Part 14 — Check TCP Connectivity

Run:

```bash
nc -vz localhost 8765
```

Expected:

```text
Connection to localhost 8765 port [tcp/*] succeeded!
```

This confirms TCP connectivity.

Remember:

```text
TCP connectivity ≠ successful WebSocket handshake
```

---

# Part 15 — WebSocket Handshake Concept

The WebSocket connection begins with an HTTP Upgrade request.

Conceptually:

```text
Client
  │
  │ GET / HTTP/1.1
  │ Upgrade: websocket
  │ Connection: Upgrade
  ▼
Server
  │
  │ 101 Switching Protocols
  ▼
WebSocket Connection
```

After the successful upgrade, WebSocket frames are exchanged.

---

# Part 16 — Install Nginx

If Nginx is not installed:

```bash
sudo apt update
sudo apt install nginx -y
```

Check:

```bash
nginx -v
```

---

# Part 17 — Create Nginx WebSocket Proxy

Create a configuration:

```bash
sudo nano /etc/nginx/sites-available/websocket
```

Add:

```nginx
server {
    listen 8080;

    location / {
        proxy_pass http://127.0.0.1:8765;

        proxy_http_version 1.1;

        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
    }
}
```

Save and exit.

---

# Part 18 — Enable the Nginx Configuration

Create the symbolic link:

```bash
sudo ln -s /etc/nginx/sites-available/websocket \
/etc/nginx/sites-enabled/websocket
```

Check configuration:

```bash
sudo nginx -t
```

Expected:

```text
syntax is ok
test is successful
```

---

# Part 19 — Restart Nginx

```bash
sudo systemctl restart nginx
```

Check status:

```bash
sudo systemctl status nginx
```

---

# Part 20 — Check Nginx Port

Run:

```bash
ss -ltnp | grep 8080
```

Expected:

```text
LISTEN ... :8080
```

Architecture:

```text
WebSocket Client
       │
       │ ws://localhost:8080
       ▼
      Nginx
       │
       │ proxy
       ▼
Python WebSocket Server
       │
       │ :8765
```

---

# Part 21 — Test WebSocket Through Nginx

Connect:

```bash
websocat ws://localhost:8080
```

Send:

```text
Hello through Nginx
```

Expected:

```text
Server received: Hello through Nginx
```

### Observation

Nginx successfully forwards the WebSocket connection to the backend.

---

# Part 22 — Verify Backend Connection

While the client is connected:

```bash
ss -tnp | grep -E '8080|8765'
```

You should observe connections involving:

```text
Client → Nginx
Nginx → Python WebSocket Server
```

This demonstrates proxying of a persistent WebSocket connection.

---

# Part 23 — Check Nginx Logs

Access log:

```bash
sudo tail -f /var/log/nginx/access.log
```

Error log:

```bash
sudo tail -f /var/log/nginx/error.log
```

Connect with:

```bash
websocat ws://localhost:8080
```

Send a message.

Observe the logs.

---

# Part 24 — Test Failure Scenario

Stop the Python WebSocket server.

Go to the server terminal and press:

```text
Ctrl + C
```

Now try:

```bash
websocat ws://localhost:8080
```

The connection should fail because Nginx cannot reach the backend.

Check:

```bash
sudo tail -f /var/log/nginx/error.log
```

### Observation

This demonstrates a common:

```text
502 Bad Gateway
```

type failure when a reverse proxy cannot successfully reach its upstream.

---

# Part 25 — Restart the Backend

Start the Python server again:

```bash
cd ~/websocket-lab
source venv/bin/activate
python3 server.py
```

Test again:

```bash
websocat ws://localhost:8080
```

Send:

```text
Backend is back
```

Expected:

```text
Server received: Backend is back
```

---

# Part 26 — Kubernetes WebSocket Architecture

A production-style architecture can look like:

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
              ┌────────┼────────┐
              ▼        ▼        ▼
            Pod 1    Pod 2    Pod 3
              │        │        │
              └────────┼────────┘
                       ▼
                WebSocket App
```

---

# Part 27 — Check Kubernetes

Check cluster:

```bash
kubectl get nodes
```

Check Pods:

```bash
kubectl get pods
```

Check Services:

```bash
kubectl get svc
```

Check Ingress:

```bash
kubectl get ingress
```

---

# Part 28 — WebSocket Troubleshooting

Use the following order:

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

# Part 29 — DNS Test

```bash
dig example.com
```

### Observation

Check whether DNS returns the expected IP address.

---

# Part 30 — TCP Test

For secure WebSockets:

```bash
nc -vz example.com 443
```

### Observation

A successful TCP connection confirms network reachability to port 443.

---

# Part 31 — TLS Test

For `wss://`:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

Check:

```text
Protocol
Cipher
Certificate
Verify return code
```

---

# Part 32 — HTTPS Test

```bash
curl -v https://example.com
```

Observe:

```text
DNS
TCP
TLS
HTTP
```

---

# Part 33 — Certificate Expiration Test

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -dates
```

Check:

```text
notBefore
notAfter
```

---

# Part 34 — Kubernetes WebSocket Troubleshooting

Check:

```bash
kubectl get pods
```

Then:

```bash
kubectl get svc
```

Then:

```bash
kubectl get ingress
```

Describe the Ingress:

```bash
kubectl describe ingress <INGRESS-NAME>
```

Check application logs:

```bash
kubectl logs <POD-NAME>
```

---

# Part 35 — Common Failure Scenarios

## Scenario 1 — DNS Failure

```text
Domain
  ↓
DNS Failure
  ↓
Client cannot find server
```

Check:

```bash
dig example.com
```

---

## Scenario 2 — TCP Failure

```text
DNS works
   ↓
TCP 443 blocked
   ↓
Connection fails
```

Check:

```bash
nc -vz example.com 443
```

---

## Scenario 3 — TLS Failure

```text
TCP works
   ↓
TLS handshake fails
```

Check:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

---

## Scenario 4 — WebSocket Upgrade Failure

```text
TCP ✓
TLS ✓
HTTP ✓
Upgrade ✗
```

Check:

* Upgrade header
* Connection header
* Reverse proxy configuration
* Application endpoint

---

## Scenario 5 — Backend Failure

```text
Client
  ↓
Nginx
  ↓
Backend ✗
```

Check:

```bash
sudo tail -f /var/log/nginx/error.log
```

and:

```bash
ss -ltnp
```

---

# Part 36 — Cleanup

Stop the WebSocket server:

```text
Ctrl + C
```

Deactivate the Python virtual environment:

```bash
deactivate
```

If you want to remove the lab:

```bash
rm -rf ~/websocket-lab
```

Remove the Nginx configuration:

```bash
sudo rm /etc/nginx/sites-enabled/websocket
sudo rm /etc/nginx/sites-available/websocket
```

Test Nginx:

```bash
sudo nginx -t
```

Restart:

```bash
sudo systemctl restart nginx
```

---

# 📊 Lab Observation Table

| Test              | Command                        | Expected Result     | Observation |
| ----------------- | ------------------------------ | ------------------- | ----------- |
| Python            | `python3 --version`            | Python installed    |             |
| WebSocket library | `pip show websockets`          | Package information |             |
| Server            | `python3 server.py`            | Server starts       |             |
| Port              | `ss -ltnp \| grep 8765`        | Port listening      |             |
| TCP               | `nc -vz localhost 8765`        | Connection succeeds |             |
| WebSocket         | `websocat ws://localhost:8765` | Connection succeeds |             |
| Messages          | Send text                      | Echo received       |             |
| Nginx             | `nginx -t`                     | Configuration valid |             |
| Proxy             | `websocat ws://localhost:8080` | Connection succeeds |             |
| Logs              | `tail -f nginx logs`           | Requests visible    |             |
| Kubernetes        | `kubectl get pods`             | Pods visible        |             |

---

# 🧠 What I Learned

After completing this lab, I understand:

```text
[✓] WebSocket basics
[✓] Persistent connections
[✓] Full-duplex communication
[✓] WebSocket handshake
[✓] 101 Switching Protocols
[✓] ws://
[✓] wss://
[✓] WebSocket over TCP
[✓] WebSocket through Nginx
[✓] Reverse proxy configuration
[✓] TCP troubleshooting
[✓] TLS troubleshooting
[✓] Kubernetes WebSocket architecture
[✓] WebSocket failure scenarios
```

---

# 🏆 Final Architecture

```text
                         Client
                           │
                           │ wss://
                           ▼
                     Load Balancer
                           │
                           ▼
                    Nginx / Ingress
                           │
                           │ WebSocket
                           ▼
                        Service
                           │
                           ▼
                    WebSocket Pods
                           │
                           ▼
                     Application
```

> **Key lesson:** A WebSocket connection starts with an HTTP Upgrade handshake and then becomes a persistent, full-duplex connection. In DevOps, successful WebSocket communication depends not only on the application but also on DNS, TCP, TLS, load balancers, reverse proxies, Ingress, Services, timeouts, and firewall rules.
