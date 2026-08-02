# 🛠️ Troubleshooting – TCP/IP Model

The TCP/IP Model provides a practical method for identifying and resolving networking problems.

DevOps engineers troubleshoot issues by checking each layer from the network connection to the application service.

---

# 📊 TCP/IP Troubleshooting Flow

```
Application Layer
        ▲
        |
Transport Layer
        ▲
        |
Internet Layer
        ▲
        |
Network Access Layer
```

---

# 1️⃣ Network Access Layer Troubleshooting

## Common Problems

- Network interface is down
- Wi-Fi/Ethernet disconnected
- Faulty network adapter
- MAC communication failure

---

## Check Interface Status

Command:

```bash
ip link show
```

### Verify:

- Interface exists
- Interface is UP
- Network adapter is working

---

## Check MAC Address Communication

Command:

```bash
ip neigh
```

### Verify:

- IP-to-MAC mapping
- Local device communication

---

## Solutions

- Enable network interface
- Restart network service
- Check physical connection
- Verify switch/Wi-Fi connection

---

# 2️⃣ Internet Layer Troubleshooting

## Common Problems

- Wrong IP address
- Incorrect subnet
- Missing gateway
- Routing failure

---

## Check IP Address

Command:

```bash
ip addr show
```

Verify:

- IP address
- Network interface
- Subnet information

---

## Check Routing Table

Command:

```bash
ip route
```

Verify:

- Default gateway
- Available routes

Example:

```text
default via 192.168.1.1
```

---

## Test Connectivity

Command:

```bash
ping google.com
```

Checks:

- Packet transmission
- Network reachability

---

## Solutions

- Correct IP configuration
- Update routing table
- Check gateway settings
- Verify firewall rules

---

# 3️⃣ Transport Layer Troubleshooting

## Common Problems

- Port blocked
- Application not listening
- Firewall blocking traffic
- TCP connection failure

---

## Check Listening Ports

Command:

```bash
ss -tuln
```

Example:

```text
LISTEN 0 128 0.0.0.0:22
```

---

## Test Port Connectivity

Command:

```bash
nc -zv server-ip port
```

Example:

```bash
nc -zv google.com 443
```

---

## Solutions

- Start required service
- Open firewall ports
- Check security group rules
- Verify application configuration

---

# 4️⃣ Application Layer Troubleshooting

## Common Problems

- Website unavailable
- DNS failure
- API error
- Web server stopped

---

## Test HTTP Service

Command:

```bash
curl -I https://google.com
```

Verify:

- HTTP response
- Server availability

---

## Check DNS

Commands:

```bash
nslookup google.com
```

or

```bash
dig google.com
```

Verify:

- DNS resolution
- DNS server response

---

## Check DNS Configuration

Command:

```bash
cat /etc/resolv.conf
```

---

## Solutions

- Restart application service
- Fix DNS configuration
- Check web server logs
- Verify application settings

---

# ☁️ DevOps Troubleshooting Examples

---

# Example 1: EC2 Server Not Reachable

## Problem

Unable to SSH into AWS EC2 instance.

## Troubleshooting

### Check Network

```bash
ping instance-ip
```

### Check Port

```bash
nc -zv instance-ip 22
```

### Verify AWS Settings

- Security Group
- Network ACL
- Route Table
- Internet Gateway

---

# Example 2: Docker Container Cannot Communicate

## Problem

Frontend container cannot reach backend container.

## Check:

```bash
docker ps
```

```bash
docker network ls
```

```bash
docker inspect container-name
```

Verify:

- Container network
- Container IP
- Exposed ports

---

# Example 3: Kubernetes Service Not Working

## Problem

Pod cannot access another service.

## Check:

```bash
kubectl get pods -o wide
```

```bash
kubectl get svc
```

```bash
kubectl describe service service-name
```

Verify:

- Pod IP
- Service endpoint
- Network policies

---

# 🧰 Quick Troubleshooting Checklist

| Problem | Command |
|---|---|
| Interface issue | `ip link show` |
| MAC issue | `ip neigh` |
| IP issue | `ip addr show` |
| Routing issue | `ip route` |
| Connectivity issue | `ping` |
| Port issue | `ss -tuln` |
| DNS issue | `nslookup` / `dig` |
| Web issue | `curl` |

---

# 💡 Best Practices

- Start troubleshooting from the lowest layer.
- Verify simple issues first.
- Collect evidence using commands.
- Check logs after network validation.
- Document the root cause and solution.

---

# ✅ Summary

The TCP/IP Model provides a structured way to troubleshoot network problems.

By understanding each layer and using Linux networking commands, DevOps engineers can quickly identify issues in:

- Linux servers
- Cloud infrastructure
- Docker containers
- Kubernetes clusters
- Web applications

A strong understanding of TCP/IP is essential for modern infrastructure and DevOps operations.
