# 🛠️ Chapter 27 — WebSockets Commands

## 1. Check DNS Resolution

```bash
dig example.com
```

### Observation

Check the `ANSWER SECTION` and identify the IP address returned for the domain.

---

## 2. Check TCP Port 80

```bash
nc -vz example.com 80
```

### Observation

Port 80 is commonly used for unencrypted HTTP traffic.

---

## 3. Check TCP Port 443

```bash
nc -vz example.com 443
```

### Observation

Port 443 is commonly used for HTTPS and secure WebSocket (`wss://`) connections.

---

## 4. Check HTTPS Connectivity

```bash
curl -I https://example.com
```

### Observation

Check the HTTP response status.

Example:

```text
HTTP/2 200
```

---

# 🔄 WebSocket Handshake Commands

## 5. Send a WebSocket Upgrade Request with curl

```bash
curl -i \
-H "Connection: Upgrade" \
-H "Upgrade: websocket" \
-H "Sec-WebSocket-Version: 13" \
-H "Sec-WebSocket-Key: SGVsbG9XZWJTb2NrZXQ=" \
https://example.com/
```

### Observation

A real WebSocket endpoint should respond appropriately to a valid upgrade request.

A successful handshake normally contains:

```text
101 Switching Protocols
```

A normal HTTP endpoint may instead return another HTTP status.

---

## 6. Inspect TLS for WSS

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

### Observe

Check:

```text
Protocol
Cipher
Certificate
Verify return code
```

---

## 7. Test TLS 1.2

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-tls1_2
```

### Observation

Record whether the TLS handshake succeeds.

---

## 8. Test TLS 1.3

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-tls1_3
```

### Observation

Record whether the TLS handshake succeeds.

---

# 🔐 Certificate Commands

## 9. Check Certificate Dates

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -dates
```

Look for:

```text
notBefore
notAfter
```

---

## 10. Check Certificate Issuer

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -issuer
```

---

## 11. Check Certificate Subject

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -subject
```

---

## 12. Check Certificate SAN

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -text |
grep -A1 "Subject Alternative Name"
```

### Observation

Verify that the hostname is included in the certificate's SAN entries.

---

# 🌐 HTTP Debugging

## 13. Verbose curl

```bash
curl -v https://example.com
```

Useful for observing:

* DNS resolution
* TCP connection
* TLS negotiation
* HTTP request
* HTTP response

---

## 14. Show Only HTTP Status

```bash
curl -o /dev/null -s \
-w "%{http_code}\n" \
https://example.com
```

---

## 15. Check Response Headers

```bash
curl -I https://example.com
```

---

# 🔌 WebSocket Client Tools

## 16. Check if `websocat` is Installed

```bash
which websocat
```

Or:

```bash
websocat --version
```

If installed, it can be used as a command-line WebSocket client.

---

## 17. Connect to a WebSocket Endpoint

Example:

```bash
websocat ws://localhost:8080
```

For secure WebSockets:

```bash
websocat wss://example.com/socket
```

### Observation

After connecting, type a message and observe whether the server responds.

---

# 🐳 Docker WebSocket Troubleshooting

## 18. Check Running Containers

```bash
docker ps
```

---

## 19. Check Container Ports

```bash
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

---

## 20. Inspect a Container

```bash
docker inspect <container-name>
```

---

## 21. Check Container Logs

```bash
docker logs <container-name>
```

Follow logs:

```bash
docker logs -f <container-name>
```

### Observation

Look for:

```text
connection
upgrade
timeout
error
```

---

# ☸️ Kubernetes WebSocket Commands

## 22. Check Pods

```bash
kubectl get pods
```

---

## 23. Check Services

```bash
kubectl get svc
```

---

## 24. Check Service Details

```bash
kubectl describe svc <SERVICE-NAME>
```

Check:

```text
Selector
Port
TargetPort
Endpoints
```

---

## 25. Check Endpoints

```bash
kubectl get endpoints <SERVICE-NAME>
```

---

## 26. Check EndpointSlices

```bash
kubectl get endpointslice
```

For a specific Service:

```bash
kubectl get endpointslice \
-l kubernetes.io/service-name=<SERVICE-NAME> \
-o wide
```

---

## 27. Check Ingress

```bash
kubectl get ingress
```

---

## 28. Describe Ingress

```bash
kubectl describe ingress <INGRESS-NAME>
```

Check:

```text
Rules
Hosts
Paths
Backends
TLS
Events
```

---

## 29. Check Ingress Controller

```bash
kubectl get pods -A | grep ingress
```

---

## 30. Check Ingress Controller Logs

First find the controller Pod:

```bash
kubectl get pods -A | grep ingress
```

Then:

```bash
kubectl logs -n <NAMESPACE> <INGRESS-POD>
```

Follow logs:

```bash
kubectl logs -n <NAMESPACE> <INGRESS-POD> -f
```

---

# 🔐 Kubernetes TLS Commands

## 31. List Secrets

```bash
kubectl get secrets
```

---

## 32. Check TLS Secret

```bash
kubectl get secret <TLS-SECRET-NAME>
```

---

## 33. Describe TLS Secret

```bash
kubectl describe secret <TLS-SECRET-NAME>
```

Check the Secret type:

```text
kubernetes.io/tls
```

---

## 34. Check Ingress TLS Configuration

```bash
kubectl describe ingress <INGRESS-NAME>
```

Look for:

```text
TLS:
  SecretName:
```

---

# 🔎 Network Troubleshooting

## 35. Check Listening Ports

```bash
ss -ltn
```

---

## 36. Show Listening Processes

```bash
sudo ss -ltnp
```

---

## 37. Check Established TCP Connections

```bash
ss -tn
```

---

## 38. Watch TCP Connections

```bash
watch -n 1 'ss -tn'
```

Press:

```text
Ctrl + C
```

to stop.

---

# 📊 WebSocket Troubleshooting Commands

## 39. Complete DNS → TCP → TLS Test

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
openssl s_client \
-connect example.com:443 \
-servername example.com
```

### HTTP

```bash
curl -v https://example.com
```

---

# 🚨 Common HTTP Status Codes

| Status | Meaning               |
| ------ | --------------------- |
| 101    | Switching Protocols   |
| 200    | OK                    |
| 400    | Bad Request           |
| 401    | Unauthorized          |
| 403    | Forbidden             |
| 404    | Not Found             |
| 408    | Request Timeout       |
| 429    | Too Many Requests     |
| 500    | Internal Server Error |
| 502    | Bad Gateway           |
| 503    | Service Unavailable   |
| 504    | Gateway Timeout       |

---

# 🧪 Practical Observation Table

| Test       | Command                        | Expected Result           | Observation |
| ---------- | ------------------------------ | ------------------------- | ----------- |
| DNS        | `dig example.com`              | IP returned               |             |
| TCP 80     | `nc -vz example.com 80`        | Connection succeeds/fails |             |
| TCP 443    | `nc -vz example.com 443`       | Connection succeeds/fails |             |
| HTTPS      | `curl -I https://example.com`  | HTTP response             |             |
| TLS        | `openssl s_client ...`         | TLS handshake             |             |
| TLS 1.2    | `openssl s_client ... -tls1_2` | Handshake result          |             |
| TLS 1.3    | `openssl s_client ... -tls1_3` | Handshake result          |             |
| Kubernetes | `kubectl get pods`             | Running Pods              |             |
| Service    | `kubectl get svc`              | Service available         |             |
| Ingress    | `kubectl get ingress`          | Ingress available         |             |

---

# 🧠 Troubleshooting Order

Always troubleshoot WebSockets systematically:

```text
1. DNS
   ↓
2. TCP
   ↓
3. TLS
   ↓
4. HTTP Upgrade
   ↓
5. 101 Switching Protocols
   ↓
6. Reverse Proxy
   ↓
7. Load Balancer
   ↓
8. Kubernetes Ingress
   ↓
9. Service
   ↓
10. Pod
   ↓
11. Application
```

---

# 🎯 Key Commands to Remember

```bash
dig example.com
```

```bash
nc -vz example.com 443
```

```bash
curl -v https://example.com
```

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

```bash
kubectl get pods
```

```bash
kubectl get svc
```

```bash
kubectl get ingress
```

```bash
kubectl describe ingress <INGRESS-NAME>
```

```bash
ss -tn
```

> **Key lesson:** For WebSocket troubleshooting, verify the connection layer by layer: **DNS → TCP → TLS → HTTP Upgrade → Proxy/Ingress → Service → Pod → Application**.
