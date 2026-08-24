# Chapter 19 — NAT Commands

## Purpose

This file contains Linux commands used to inspect and troubleshoot NAT, routing, interfaces, firewall rules, Docker networking, and connectivity.

---

# 1. Check IP Address

```bash
ip addr
```

or:

```bash
ip a
```

### Purpose

Displays IP addresses assigned to network interfaces.

### Example

```text
wlo1:
    inet 192.168.1.10/24
```

### DevOps Use

Useful when checking:

* Server IP
* Private IP
* Network interfaces
* Container networking
* Production connectivity

---

# 2. Check Network Interfaces

```bash
ip link
```

### Purpose

Displays network interfaces and their state.

Example:

```text
lo
wlo1
docker0
```

### Check a specific interface

```bash
ip link show wlo1
```

---

# 3. Check Routing Table

```bash
ip route
```

### Purpose

Displays the routing table.

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1
```

### Important

The default route tells the system where to send traffic when there is no more specific route.

---

# 4. Check Default Gateway

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

Here:

```text
192.168.1.1
```

is the default gateway.

---

# 5. Test Internet Connectivity

```bash
ping -c 4 8.8.8.8
```

### Purpose

Tests whether the system can reach an external IP address.

If this works, basic IP connectivity is available.

---

# 6. Test DNS Resolution

```bash
ping -c 4 google.com
```

This tests both:

```text
DNS resolution
+
Network connectivity
```

If:

```bash
ping -c 4 8.8.8.8
```

works but:

```bash
ping -c 4 google.com
```

fails, investigate DNS.

---

# 7. Check DNS Configuration

```bash
cat /etc/resolv.conf
```

### Purpose

Displays DNS resolver configuration.

---

# 8. Check Open Ports

```bash
ss -tuln
```

### Options

```text
-t → TCP
-u → UDP
-l → Listening
-n → Numeric output
```

Example:

```text
LISTEN
0.0.0.0:22
0.0.0.0:80
0.0.0.0:443
```

---

# 9. Check Network Connections

```bash
ss -tunap
```

### Purpose

Displays active TCP/UDP connections and associated processes.

This is useful for troubleshooting applications that cannot connect to another service.

---

# 10. Trace Network Path

```bash
traceroute google.com
```

If traceroute is not installed:

```bash
tracepath google.com
```

### Purpose

Shows the network hops between your system and the destination.

Useful for identifying routing problems.

---

# 11. Inspect iptables NAT Rules

```bash
sudo iptables -t nat -L -n -v
```

### Explanation

```text
-t nat
```

Selects the NAT table.

```text
-L
```

Lists rules.

```text
-n
```

Shows numeric addresses and ports.

```text
-v
```

Shows detailed information.

---

# 12. Inspect NAT POSTROUTING Rules

```bash
sudo iptables -t nat -L POSTROUTING -n -v
```

### Purpose

POSTROUTING rules are commonly involved in source address translation.

---

# 13. Inspect NAT PREROUTING Rules

```bash
sudo iptables -t nat -L PREROUTING -n -v
```

### Purpose

PREROUTING rules are processed before the routing decision and are commonly involved in destination address translation.

---

# 14. Inspect iptables NAT Table

```bash
sudo iptables -t nat -S
```

### Purpose

Displays NAT rules in command-style format.

---

# 15. Check nftables

Modern Linux systems may use nftables.

Run:

```bash
sudo nft list ruleset
```

### Purpose

Displays the complete nftables configuration.

---

# 16. Check nftables NAT Rules

```bash
sudo nft list table ip nat
```

If the table exists, this displays its NAT configuration.

---

# 17. Check Docker Networks

```bash
docker network ls
```

Example:

```text
NETWORK ID     NAME      DRIVER
xxxxxx         bridge    bridge
xxxxxx         host      host
xxxxxx         none      null
```

---

# 18. Inspect Docker Bridge Network

```bash
docker network inspect bridge
```

### Purpose

Displays:

* Network subnet
* Gateway
* Containers
* IP addresses
* Network configuration

---

# 19. Check Docker Container IP

First list containers:

```bash
docker ps
```

Then:

```bash
docker inspect <container_name>
```

For only the IP address:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name>
```

---

# 20. Check Docker NAT Rules

```bash
sudo iptables -t nat -L -n -v
```

Look for Docker-related chains such as:

```text
DOCKER
DOCKER-USER
```

---

# 21. Check ARP / Neighbor Information

```bash
ip neigh
```

### Purpose

Displays neighboring devices known to the system.

This is useful when troubleshooting local network communication.

---

# 22. Check MAC Address

```bash
ip link show
```

Look for:

```text
link/ether
```

Example:

```text
link/ether aa:bb:cc:dd:ee:ff
```

---

# 23. Check Hostname

```bash
hostname
```

or:

```bash
hostnamectl
```

Useful when identifying servers during production troubleshooting.

---

# 24. Check Network Statistics

```bash
ip -s link
```

### Purpose

Displays network interface statistics such as:

* RX packets
* TX packets
* Errors
* Dropped packets

---

# 25. Check Active Connections

```bash
ss -tunap
```

This is one of the most useful commands for production network troubleshooting.

---

# 26. Check Which Process Uses a Port

```bash
sudo ss -ltnp
```

Example:

```text
LISTEN 0 128 0.0.0.0:8080
```

The process information can help identify which application owns the port.

---

# 27. Check Connectivity to a Specific Port

Using netcat:

```bash
nc -zv <host> <port>
```

Example:

```bash
nc -zv google.com 443
```

This tests whether a TCP connection can be established to the specified port.

---

# 28. Check HTTP Connectivity

```bash
curl -I https://google.com
```

### Purpose

Tests HTTP/HTTPS connectivity.

Useful when:

* DNS works
* Network connectivity works
* But an application cannot reach an HTTP endpoint

---

# 29. Check Public IP

You can query an external service:

```bash
curl ifconfig.me
```

or:

```bash
curl https://api.ipify.org
```

### Purpose

Helps identify the public IP seen by an external service.

This can be useful when investigating NAT behavior.

---

# 30. Production NAT Troubleshooting Flow

When a private server cannot access the Internet:

```text
1. Check IP
   ↓
ip addr

2. Check interface
   ↓
ip link

3. Check route
   ↓
ip route

4. Check gateway
   ↓
ip route | grep default

5. Test IP connectivity
   ↓
ping 8.8.8.8

6. Test DNS
   ↓
ping google.com

7. Check ports
   ↓
ss -tuln

8. Check NAT
   ↓
sudo iptables -t nat -L -n -v

9. Check nftables
   ↓
sudo nft list ruleset

10. Trace path
   ↓
traceroute google.com
```

---

# 31. Most Important Commands for DevOps

These commands should become familiar:

```bash
ip addr
ip link
ip route
ip neigh
ss -tuln
ss -tunap
ping
traceroute
tracepath
curl
nc
sudo iptables -t nat -L -n -v
sudo nft list ruleset
docker network ls
docker network inspect bridge
```

---

# 32. Quick Memory Table

| Command                  | Purpose                     |
| ------------------------ | --------------------------- |
| `ip addr`                | Check IP addresses          |
| `ip link`                | Check interfaces            |
| `ip route`               | Check routing               |
| `ip neigh`               | Check neighbors/ARP         |
| `ss -tuln`               | Check listening ports       |
| `ss -tunap`              | Check connections/processes |
| `ping`                   | Test connectivity           |
| `traceroute`             | Trace network path          |
| `tracepath`              | Trace network path          |
| `curl`                   | Test HTTP/HTTPS             |
| `nc`                     | Test port connectivity      |
| `iptables -t nat`        | Inspect NAT rules           |
| `nft list ruleset`       | Inspect nftables            |
| `docker network ls`      | List Docker networks        |
| `docker network inspect` | Inspect Docker network      |

---

# 33. Important Warning

Do not modify production NAT or firewall rules unless you understand the impact.

Commands such as:

```bash
iptables
nft
```

can affect network connectivity.

For learning and troubleshooting, prefer read-only commands such as:

```bash
sudo iptables -t nat -L -n -v
sudo nft list ruleset
ip addr
ip route
ss -tuln
```

---

# DevOps Interview Memory

Remember:

```text
IP Address
    ↓
Routing
    ↓
NAT
    ↓
Firewall
    ↓
Port
    ↓
Application
```

When troubleshooting connectivity, do not randomly run commands.

Follow the network path and identify where communication stops.
