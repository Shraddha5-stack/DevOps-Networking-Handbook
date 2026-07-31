# 🛠️ Troubleshooting – Network Devices

Network troubleshooting is the process of identifying and fixing problems related to network connectivity, communication, and services.

DevOps engineers use networking knowledge and Linux commands to quickly identify issues in production environments.

---

# 🎯 Common Network Problems

Common issues include:

- No network connectivity
- Wrong IP configuration
- DNS resolution failure
- Routing problems
- Firewall blocking traffic
- Application port not accessible
- Network interface failure

---

# 1️⃣ Network Interface Not Working

## Problem

The system cannot communicate with the network.

## Check Interface Status

Command:

```bash
ip link show
```

Example:

```
wlo1: <UP,LOWER_UP>
```

## Solution

If interface is down:

```bash
sudo ip link set <interface> up
```

---

# 2️⃣ IP Address Problem

## Problem

Device does not have a valid IP address.

## Check IP Address

Command:

```bash
ip addr show
```

Check:

- IP address
- Interface status
- Network configuration

## Solution

Restart network service:

```bash
sudo systemctl restart NetworkManager
```

---

# 3️⃣ Routing Problem

## Problem

System cannot reach another network.

## Check Routing Table

Command:

```bash
ip route
```

Example:

```
default via 192.168.1.1
```

## Solution

Verify:

- Default gateway
- Route configuration

---

# 4️⃣ DNS Resolution Problem

## Problem

Website name cannot be resolved.

Example:

```
ping google.com
```

fails but:

```
ping 8.8.8.8
```

works.

## Check DNS Configuration

Command:

```bash
cat /etc/resolv.conf
```

## Solution

Verify DNS servers.

Example:

```
nameserver 8.8.8.8
```

---

# 5️⃣ Connectivity Issue

## Problem

Unable to communicate with another host.

## Test Connectivity

Command:

```bash
ping google.com
```

Check:

- Packet loss
- Response time

---

# 6️⃣ Port Not Accessible

## Problem

Application is running but users cannot access it.

## Check Listening Ports

Command:

```bash
ss -tuln
```

Example:

```
0.0.0.0:8080
```

## Check:

- Application status
- Firewall rules
- Port configuration

---

# 7️⃣ Firewall Blocking Traffic

## Problem

Traffic is blocked by security rules.

## Check Firewall

Linux:

```bash
sudo ufw status
```

## Solution

Allow required ports.

Example:

```bash
sudo ufw allow 80
sudo ufw allow 443
```

---

# 8️⃣ Docker Networking Issue

## Problem

Containers cannot communicate.

## Check Networks

Command:

```bash
docker network ls
```

Inspect network:

```bash
docker network inspect bridge
```

Check:

- Container connection
- Network configuration

---

# 9️⃣ Load Balancer Troubleshooting

## Problem

Users cannot access application through Load Balancer.

Check:

1. Backend server health.
2. Security rules.
3. Target group status.
4. Application port.

Architecture:

```
User
 |
Load Balancer
 |
Application Server
```

---

# 🔟 Network Troubleshooting Workflow

Follow this order:

```
1. Check Physical Connection
          |
2. Check Network Interface
          |
3. Check IP Address
          |
4. Check Routing
          |
5. Check DNS
          |
6. Check Firewall
          |
7. Check Application Port
```

---

# 💼 DevOps Troubleshooting Commands

## Interface

```bash
ip link show
```

## IP Configuration

```bash
ip addr show
```

## Routing

```bash
ip route
```

## Connectivity

```bash
ping <host>
```

## DNS

```bash
cat /etc/resolv.conf
```

## Ports

```bash
ss -tuln
```

## Docker Network

```bash
docker network ls
```

---

# 🎤 Interview Scenario

## Question:

Your application is running on a server, but users cannot access it. How will you troubleshoot?

## Answer:

I will troubleshoot step by step:

1. Check network interface status.

```bash
ip link show
```

2. Verify IP address.

```bash
ip addr show
```

3. Check routing.

```bash
ip route
```

4. Verify firewall rules.

5. Check application port.

```bash
ss -tuln
```

6. Test connectivity.

```bash
ping <server-ip>
```

---

# 🔑 Key Takeaways

- Always troubleshoot from lower layers to higher layers.
- Check connectivity before application issues.
- Verify IP, routing, DNS, and firewall.
- Linux networking commands are essential for DevOps engineers.
- Understanding network devices helps identify failures faster.

> **Remember:** Troubleshooting is not guessing; it is a systematic process of finding where communication breaks.
