# 🔐 Chapter 24 — VPN Practical Lab

## 🎯 Objective

Understand how a VPN changes Linux networking by observing:

* Network interfaces
* IP addresses
* Routing tables
* DNS configuration
* Private network connectivity
* VPN traffic
* Troubleshooting techniques

---

## 🧪 Lab 1 — Check Network Before VPN

### 1. Check interfaces

```bash
ip addr
```

### 2. Check routes

```bash
ip route
```

### 3. Check DNS

```bash
cat /etc/resolv.conf
```

### 4. Check public IP

```bash
curl -4 https://ifconfig.me
```

### Observation

Record the following:

| Item            | Before VPN            |
| --------------- | --------------------- |
| Main interface  |                       |
| IP address      |                       |
| Default gateway |                       |
| DNS server      |                       |
| Public IP       |                       |
| VPN interface   | Not present / Present |

---

# 🧪 Lab 2 — Connect to VPN

Connect using your approved VPN client.

After connection, run:

```bash
ip addr
```

Then:

```bash
ip route
```

Then:

```bash
cat /etc/resolv.conf
```

And:

```bash
curl -4 https://ifconfig.me
```

### Observation

Compare the results with the previous lab.

Look for:

* New interface
* New IP address
* New routes
* DNS changes
* Public IP changes

---

# 🧪 Lab 3 — Identify the VPN Interface

Run:

```bash
ip link show
```

Look for an interface such as:

```text
tun0
```

or:

```text
wg0
```

Check its details:

```bash
ip addr show tun0
```

or:

```bash
ip addr show wg0
```

### Observation

Record:

```text
Interface:
State:
IP address:
MTU:
```

---

# 🧪 Lab 4 — Check VPN Routing

Run:

```bash
ip route
```

Find routes associated with the VPN.

Then test a destination:

```bash
ip route get <PRIVATE-IP>
```

Example:

```bash
ip route get 10.10.0.10
```

### Observation

Record:

```text
Destination:
Interface:
Source IP:
Gateway:
```

---

# 🧪 Lab 5 — Test Private Network Connectivity

Test a known private IP:

```bash
ping -c 4 <PRIVATE-IP>
```

Example:

```bash
ping -c 4 10.10.0.10
```

### Observation

Record:

```text
Packets transmitted:
Packets received:
Packet loss:
Average latency:
```

---

# 🧪 Lab 6 — Test a TCP Port

Use `nc`:

```bash
nc -vz <PRIVATE-IP> 443
```

Example:

```bash
nc -vz 10.10.0.10 443
```

### Observation

Possible result:

```text
Connection succeeded
```

or:

```text
Connection refused
```

or:

```text
Connection timed out
```

### Meaning

| Result    | Possible Meaning                                |
| --------- | ----------------------------------------------- |
| Succeeded | Port is reachable                               |
| Refused   | Host reachable but service may not be listening |
| Timed out | Routing/firewall/connectivity issue possible    |

---

# 🧪 Lab 7 — Test HTTP/HTTPS

For HTTP:

```bash
curl -v http://<PRIVATE-IP>
```

For HTTPS:

```bash
curl -vk https://<PRIVATE-IP>
```

### Observation

Check:

* Connection
* HTTP status code
* Server
* Response time

---

# 🧪 Lab 8 — Test DNS

Test public DNS:

```bash
getent hosts google.com
```

Test an internal hostname:

```bash
getent hosts <INTERNAL-HOSTNAME>
```

Check DNS configuration:

```bash
cat /etc/resolv.conf
```

If available:

```bash
dig <INTERNAL-HOSTNAME>
```

### Observation

Determine whether:

```text
Public DNS       → Working / Not Working
Internal DNS     → Working / Not Working
```

---

# 🧪 Lab 9 — Check Active Connections

Run:

```bash
ss -tun
```

For listening services:

```bash
sudo ss -ltnup
```

### Observation

Identify:

* Local listening ports
* Established connections
* Remote addresses
* Protocols

---

# 🧪 Lab 10 — Check VPN with WireGuard

If your VPN uses WireGuard:

```bash
sudo wg show
```

Look for:

```text
interface
peer
latest handshake
transfer-rx
transfer-tx
```

### Observation

A recent handshake indicates recent communication with the peer.

---

# 🧪 Lab 11 — Check NetworkManager

If your system uses NetworkManager:

```bash
nmcli connection show
```

Check active connections:

```bash
nmcli connection show --active
```

### Observation

Identify:

```text
VPN connection:
Status:
Interface:
```

---

# 🧪 Lab 12 — Check Firewall

If UFW is installed:

```bash
sudo ufw status verbose
```

For nftables:

```bash
sudo nft list ruleset
```

### Observation

Check whether firewall rules could block:

* VPN traffic
* Private network traffic
* Required application ports

---

# 🧪 Lab 13 — Check Packet Flow

If `tcpdump` is available:

```bash
sudo tcpdump -i tun0
```

For WireGuard:

```bash
sudo tcpdump -i wg0
```

Generate traffic from another terminal:

```bash
ping -c 4 <PRIVATE-IP>
```

Stop packet capture:

```text
Ctrl + C
```

### Observation

Check whether packets are visible on the VPN interface.

---

# 🧪 Lab 14 — Full Tunnel vs Split Tunnel

Check the route table before connecting:

```bash
ip route
```

Connect to VPN.

Check again:

```bash
ip route
```

### Full Tunnel

A VPN may install or replace the default route:

```text
default → VPN
```

### Split Tunnel

Only selected private networks use the VPN:

```text
10.10.0.0/16 → VPN
default → normal gateway
```

### Observation

Identify which routing model your VPN appears to use.

---

# 🧪 Lab 15 — Complete Troubleshooting Exercise

Assume:

```text
VPN Network: 10.10.0.0/16
Server: 10.10.0.10
HTTPS Port: 443
```

Run the following in order.

### Step 1

```bash
ip addr
```

### Step 2

```bash
ip route
```

### Step 3

```bash
ip route get 10.10.0.10
```

### Step 4

```bash
ping -c 4 10.10.0.10
```

### Step 5

```bash
nc -vz 10.10.0.10 443
```

### Step 6

```bash
curl -vk https://10.10.0.10
```

### Troubleshooting flow

```text
VPN connected?
      ↓
Interface exists?
      ↓
Correct IP?
      ↓
Correct route?
      ↓
Ping works?
      ↓
Port reachable?
      ↓
Application responds?
```

---

# 📊 Lab Results

| Test            | Result | Observation |
| --------------- | ------ | ----------- |
| VPN connection  |        |             |
| VPN interface   |        |             |
| VPN IP          |        |             |
| Route           |        |             |
| Private IP ping |        |             |
| TCP port        |        |             |
| DNS             |        |             |
| HTTPS           |        |             |
| Firewall        |        |             |

---

# 🎓 What I Learned

After completing this lab, I understand:

* How VPN interfaces appear in Linux
* How VPNs affect routing
* How to identify VPN routes
* How to test private network connectivity
* How to test TCP ports
* How to troubleshoot DNS
* How to inspect firewall rules
* How to capture VPN traffic
* Difference between full-tunnel and split-tunnel VPNs
* A systematic VPN troubleshooting process

---

# ⭐ DevOps Real-World Use

VPNs are commonly used by DevOps engineers to securely access:

* Private cloud networks
* Kubernetes clusters
* Internal databases
* Private APIs
* CI/CD infrastructure
* Internal monitoring systems
* Bastion hosts
* Corporate services

A strong troubleshooting approach is:

```text
Interface
   ↓
IP
   ↓
Route
   ↓
Connectivity
   ↓
Port
   ↓
DNS
   ↓
Application
```

This approach helps identify the exact layer where connectivity fails.
