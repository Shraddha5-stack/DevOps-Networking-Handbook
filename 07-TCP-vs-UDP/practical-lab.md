# 🧪 TCP vs UDP Practical Lab

## 🎯 Objective

The objective of this lab is to understand how TCP and UDP work in Linux by using common networking commands. You will inspect listening ports, identify active connections, test remote services, and compare TCP and UDP behavior.

---

# 📋 Prerequisites

- Ubuntu/Linux system
- Internet connection
- Terminal access
- `ss` command
- `netstat` (net-tools package)
- `nc` (Netcat)
- `curl`

Verify the required tools:

```bash
ss --version
netstat --version
nc -h
curl --version
```

---

# 🧪 Lab 1 – View Listening TCP and UDP Ports

## Command

```bash
ss -tuln
```

### Expected Result

A list of services currently listening on TCP and UDP ports.

### Learning Outcome

Understand which applications are accepting network connections.

---

# 🧪 Lab 2 – View Active TCP Connections

## Command

```bash
ss -tan
```

### Expected Result

Displays listening and established TCP connections.

### Learning Outcome

Learn how TCP maintains reliable connections.

---

# 🧪 Lab 3 – View Active UDP Sockets

## Command

```bash
ss -uan
```

### Expected Result

Shows UDP sockets currently in use.

### Learning Outcome

Observe that UDP is connectionless.

---

# 🧪 Lab 4 – Display Listening Ports Using netstat

## Command

```bash
netstat -tuln
```

### Expected Result

Displays all listening TCP and UDP ports.

### Learning Outcome

Compare `netstat` with `ss`.

---

# 🧪 Lab 5 – Test HTTP Port

## Command

```bash
nc -zv google.com 80
```

### Expected Result

```text
Connection to google.com 80 port [tcp/http] succeeded!
```

### Learning Outcome

Verify that a remote TCP service is reachable.

---

# 🧪 Lab 6 – Test HTTPS Port

## Command

```bash
nc -zv google.com 443
```

### Expected Result

```text
Connection to google.com 443 port [tcp/https] succeeded!
```

### Learning Outcome

Understand how HTTPS uses TCP.

---

# 🧪 Lab 7 – Retrieve HTTP Headers

## Command

```bash
curl -I https://google.com
```

### Expected Result

Displays HTTP response headers.

### Learning Outcome

Understand how web servers respond to HTTP requests.

---

# 📊 Observation Table

| Lab | Command | Status |
|------|---------|--------|
| 1 | `ss -tuln` | ✅ Completed |
| 2 | `ss -tan` | ✅ Completed |
| 3 | `ss -uan` | ✅ Completed |
| 4 | `netstat -tuln` | ✅ Completed |
| 5 | `nc -zv google.com 80` | ✅ Completed |
| 6 | `nc -zv google.com 443` | ✅ Completed |
| 7 | `curl -I https://google.com` | ✅ Completed |

---

# 💡 Real-World Scenario

Imagine a web application is not accessible.

A DevOps engineer can use:

- `ss -tuln` to check if the application is listening.
- `netstat -tuln` to verify open ports.
- `nc` to test connectivity to the application.
- `curl` to verify the web server response.

These commands help identify whether the issue is related to the application, firewall, network, or web server.

---

# 🎯 Key Learnings

- TCP is reliable and connection-oriented.
- UDP is fast and connectionless.
- `ss` is the modern replacement for `netstat`.
- `nc` is useful for testing remote ports.
- `curl` is commonly used to verify web services and APIs.
- These tools are widely used in Linux administration, DevOps, Kubernetes, Docker, and cloud environments.

---

# ✅ Lab Summary

In this lab, you practiced essential Linux networking commands to inspect TCP and UDP connections, test remote services, and verify HTTP communication. These practical skills are fundamental for troubleshooting applications and infrastructure in real-world DevOps environments.
