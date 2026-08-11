# 🛠️ Chapter 15 – Ports & Protocols Commands

## 1. Show Listening Ports

```bash
ss -tuln
```

### Options

```text
-t → TCP
-u → UDP
-l → Listening
-n → Numeric addresses and ports
```

Useful for checking which ports are listening on the system.

---

## 2. Show Listening Ports with Processes

```bash
sudo ss -tulpn
```

Additional options:

```text
-p → Show process information
```

This helps identify which application owns a port.

Example:

```text
LISTEN  0  128  0.0.0.0:22
```

---

## 3. Show TCP Connections

```bash
ss -tn
```

Useful for viewing active TCP connections.

---

## 4. Show UDP Sockets

```bash
ss -un
```

Useful for checking UDP sockets.

---

## 5. Show Only Listening TCP Ports

```bash
ss -ltn
```

---

## 6. Show Only Listening UDP Ports

```bash
ss -lun
```

---

## 7. Check a Specific Port

```bash
sudo ss -tulpn | grep :22
```

Example for HTTPS:

```bash
sudo ss -tulpn | grep :443
```

Example for port 8080:

```bash
sudo ss -tulpn | grep :8080
```

---

# 8. Test a Local TCP Port with Netcat

```bash
nc -zv localhost 22
```

Options:

```text
-z → Scan without sending data
-v → Verbose output
```

Successful connection indicates that something accepted the TCP connection.

---

# 9. Test a Remote TCP Port

```bash
nc -zv example.com 443
```

This tests whether TCP port `443` is reachable.

---

# 10. Test Multiple Ports

```bash
nc -zv localhost 22 80 443
```

You can use this to test several ports.

---

# 11. Port Range Scan with Netcat

```bash
nc -zv localhost 20-30
```

This checks a range of TCP ports.

---

# 12. Check HTTP Port with curl

```bash
curl -I http://example.com
```

`-I` requests response headers.

Useful for checking:

* HTTP connectivity
* HTTP status code
* Response headers
* Web-server availability

---

# 13. Check HTTPS Port

```bash
curl -I https://example.com
```

This tests an HTTPS connection.

It involves:

```text
DNS
 ↓
TCP 443
 ↓
TLS
 ↓
HTTP
```

---

# 14. Show Detailed curl Information

```bash
curl -v https://example.com
```

`-v` means verbose.

It can show details such as:

* DNS connection
* TCP connection
* TLS handshake
* Request headers
* Response headers

---

# 15. Check Only HTTP Status Code

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```

Example:

```text
200
```

Common status codes:

```text
200 → OK
301 → Redirect
302 → Temporary Redirect
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
```

---

# 16. Check DNS Before Testing a Port

```bash
nslookup example.com
```

or:

```bash
dig example.com
```

This confirms that the hostname can be resolved.

---

# 17. Check the Route to a Host

```bash
ip route
```

For a specific destination:

```bash
ip route get 8.8.8.8
```

This helps determine which interface and gateway Linux will use.

---

# 18. Check Connectivity with ping

```bash
ping -c 4 8.8.8.8
```

This tests IP-level reachability using ICMP.

Important:

> Successful ping does not prove that a TCP/UDP service port is reachable.

---

# 19. Check a Port with telnet

If installed:

```bash
telnet example.com 443
```

However, `telnet` is generally not preferred for secure administration.

For simple TCP connectivity testing, `nc` is usually more useful.

---

# 20. Find a Process Using a Port

```bash
sudo lsof -i :22
```

Example:

```bash
sudo lsof -i :80
```

This can show the process listening on the specified port.

---

# 21. Find Processes Listening on Network Ports

```bash
sudo lsof -i -P -n
```

Options:

```text
-P → Show port numbers instead of service names
-n → Do not resolve hostnames
```

---

# 22. Using netstat

If `net-tools` is installed:

```bash
netstat -tuln
```

With process information:

```bash
sudo netstat -tulpn
```

Modern Linux systems generally prefer:

```bash
ss
```

over `netstat`.

---

# 23. Check Firewall Rules

If UFW is installed:

```bash
sudo ufw status
```

Detailed output:

```bash
sudo ufw status verbose
```

This helps determine whether firewall rules may be blocking traffic.

---

# 24. Check a Docker Port

```bash
docker ps
```

Look at the `PORTS` column.

Example:

```text
0.0.0.0:8080->80/tcp
```

Meaning:

```text
Host port 8080
      ↓
Container port 80
```

---

# 25. Check Docker Listening Ports

```bash
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

Useful when troubleshooting containerized applications.

---

# 26. Kubernetes Port Inspection

```bash
kubectl get svc
```

Detailed information:

```bash
kubectl describe svc <service-name>
```

Check pods:

```bash
kubectl get pods
```

Check pod details:

```bash
kubectl describe pod <pod-name>
```

---

# 27. Common Port Troubleshooting Sequence

When an application is unreachable:

### Step 1 — Check the service

```bash
sudo systemctl status <service>
```

### Step 2 — Check listening ports

```bash
sudo ss -tulpn
```

### Step 3 — Test locally

```bash
nc -zv localhost <port>
```

### Step 4 — Test remotely

```bash
nc -zv <server-ip> <port>
```

### Step 5 — Test the application

```bash
curl -v http://<server-ip>:<port>
```

### Step 6 — Check firewall

```bash
sudo ufw status
```

### Step 7 — Check routing

```bash
ip route
```

---

# 🎯 Most Important Commands

For interviews and real DevOps work, remember these:

```bash
ss -tuln
```

```bash
sudo ss -tulpn
```

```bash
nc -zv localhost 22
```

```bash
nc -zv example.com 443
```

```bash
curl -I https://example.com
```

```bash
curl -v https://example.com
```

```bash
sudo lsof -i :22
```

```bash
ip route
```

```bash
sudo ufw status
```

```bash
docker ps
```

```bash
kubectl get svc
```

---

# 🧠 Quick Cheat Sheet

| Command            | Purpose                           |
| ------------------ | --------------------------------- |
| `ss -tuln`         | Show listening TCP/UDP ports      |
| `ss -tulpn`        | Show ports + processes            |
| `nc -zv host port` | Test TCP connectivity             |
| `curl -I URL`      | Check HTTP headers                |
| `curl -v URL`      | Detailed HTTP/TLS troubleshooting |
| `lsof -i :PORT`    | Find process using port           |
| `ip route`         | Show routing table                |
| `ufw status`       | Check UFW firewall                |
| `docker ps`        | Check container port mappings     |
| `kubectl get svc`  | Check Kubernetes services         |
| `netstat -tuln`    | Legacy port inspection            |

---

# 💡 DevOps Tip

When someone says:

> "The application is not reachable."

Don't immediately restart the server.

Follow:

```text
DNS
 ↓
IP
 ↓
Route
 ↓
Firewall
 ↓
Port
 ↓
Process
 ↓
Application
```

Use the appropriate command at each layer.
