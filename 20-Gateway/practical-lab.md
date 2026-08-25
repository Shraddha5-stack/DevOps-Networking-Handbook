# Chapter 20 — Gateway Practical Lab

## Objective

In this practical lab, I will learn how to identify and troubleshoot a Gateway on a Linux system.

I will practically check:

- IP address
- Network interfaces
- Routing table
- Default Gateway
- Route to a destination
- Gateway reachability
- Neighbor/ARP information
- Internet connectivity
- DNS resolution
- Network path
- Listening ports
- Network statistics

---

# Lab Environment

### Operating System

```bash
cat /etc/os-release
```

### Kernel

```bash
uname -r
```

### Hostname

```bash
hostname
```

---

# Lab 1 — Check IP Address

Run:

```bash
ip addr
```

Short form:

```bash
ip a
```

### What to observe

Find the active network interface.

For example:

```text
wlo1
```

Look for:

```text
inet 192.168.1.10/24
```

### Record

```text
Interface:
IP Address:
Subnet:
```

### Observation

The `ip addr` command displays the IP addresses assigned to the system's network interfaces.

---

# Lab 2 — Check Network Interfaces

Run:

```bash
ip link
```

### What to observe

Look for interfaces such as:

```text
lo
wlo1
docker0
```

Check whether the active interface shows:

```text
state UP
```

### Observation

The active network interface is responsible for sending and receiving network traffic.

---

# Lab 3 — Check Routing Table

Run:

```bash
ip route
```

### Example

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1 proto kernel scope link src 192.168.1.10
```

### What to observe

Find:

```text
default via <gateway-ip>
```

### Record

```text
Default Gateway:
Network:
Interface:
Source IP:
```

### Observation

The routing table tells Linux where packets should be sent.

---

# Lab 4 — Find Only the Default Gateway

Run:

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

### Record

```text
Gateway IP:
192.168.1.1

Interface:
wlo1
```

Use your actual output instead of the example.

### Observation

The IP address after `via` is the default Gateway.

---

# Lab 5 — Find the Exact Route to a Destination

Run:

```bash
ip route get 8.8.8.8
```

Example:

```text
8.8.8.8 via 192.168.1.1 dev wlo1 src 192.168.1.10
```

### Record

```text
Destination:
8.8.8.8

Gateway:

Interface:

Source IP:
```

### Observation

This command shows the exact route Linux will use to reach the destination.

---

# Lab 6 — Check Neighbor / ARP Information

Run:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

### Look for

Your Gateway IP.

### Record

```text
Gateway IP:

Gateway MAC:

Interface:

State:
```

### Observation

The neighbor table contains information about nearby devices.

For IPv4 Ethernet networks, this commonly includes the IP-to-MAC mapping learned through ARP.

---

# Lab 7 — Test Gateway Connectivity

First find your Gateway:

```bash
ip route | grep default
```

Then test it:

```bash
ping -c 4 <gateway-ip>
```

Example:

```bash
ping -c 4 192.168.1.1
```

### Expected result

You should receive replies similar to:

```text
64 bytes from 192.168.1.1
```

### Record

```text
Gateway:
Packets Sent:
Packets Received:
Packet Loss:
```

### Observation

A successful ping shows that the local system can reach the Gateway.

---

# Lab 8 — Test Internet Connectivity by IP

Run:

```bash
ping -c 4 8.8.8.8
```

### Record

```text
Packets Sent:
Packets Received:
Packet Loss:
Average Latency:
```

### Observation

This tests Internet connectivity without depending on DNS name resolution.

---

# Lab 9 — Test DNS Resolution

Run:

```bash
getent hosts google.com
```

You can also run:

```bash
nslookup google.com
```

If installed:

```bash
dig google.com
```

### Observation

If the hostname resolves to an IP address, DNS resolution is working.

---

# Lab 10 — Compare IP Connectivity and DNS

Run:

```bash
ping -c 4 8.8.8.8
```

Then:

```bash
ping -c 4 google.com
```

### Understand the difference

If:

```text
8.8.8.8 → works
google.com → works
```

Then basic IP connectivity and DNS are likely working.

If:

```text
8.8.8.8 → works
google.com → fails
```

Investigate DNS.

---

# Lab 11 — Trace the Network Path

Run:

```bash
tracepath google.com
```

If unavailable, try:

```bash
traceroute google.com
```

### What to observe

Look at the network hops between your machine and the destination.

Example:

```text
1   <local-gateway>
2   <next-router>
3   ...
```

### Observation

The first hop is often the local Gateway.

---

# Lab 12 — Check Network Statistics

Run:

```bash
ip -s link
```

### Look for

```text
RX packets
TX packets
errors
dropped
```

### Record

```text
Interface:

RX packets:

TX packets:

RX errors:

TX errors:

RX dropped:

TX dropped:
```

### Observation

Network statistics help identify packet errors and dropped packets.

---

# Lab 13 — Check Listening Ports

Run:

```bash
ss -tuln
```

### What to observe

Look for ports such as:

```text
22
80
443
```

### Explanation

```text
22  → SSH
80  → HTTP
443 → HTTPS
```

### Observation

The command shows TCP and UDP ports that are listening on the system.

---

# Lab 14 — Check Processes Using Ports

Run:

```bash
sudo ss -ltnp
```

### What to observe

You may see:

```text
users:(("sshd",pid=...,fd=...))
```

### Observation

This command helps identify which process is listening on a TCP port.

---

# Lab 15 — Test HTTPS Connectivity

Run:

```bash
curl -I https://google.com
```

For detailed information:

```bash
curl -v https://google.com
```

### What to observe

Look for:

```text
Connected
HTTP response
TLS information
```

### Observation

`curl` helps test connectivity at the application layer.

---

# Lab 16 — Test TCP Port Connectivity

Run:

```bash
nc -zv google.com 443
```

### Expected result

You may see:

```text
Connection to google.com 443 port [tcp/https] succeeded!
```

### Observation

This tests whether TCP port `443` is reachable.

---

# Lab 17 — Check Public IP

Run:

```bash
curl ifconfig.me
```

Or:

```bash
curl https://api.ipify.org
```

### Record

```text
Public IP:
```

### Observation

The returned address is the public IP visible to the external service.

This can help demonstrate the difference between private and public addressing.

---

# Lab 18 — Check NetworkManager

Run:

```bash
nmcli device status
```

### Example

```text
DEVICE   TYPE      STATE
wlo1     wifi      connected
lo       loopback  connected
```

### Observation

This command shows the current state of NetworkManager-managed interfaces.

---

# Lab 19 — Check Network Connections

Run:

```bash
nmcli connection show
```

### Observation

This displays configured NetworkManager connections.

---

# Lab 20 — Check Firewall

Run:

```bash
sudo ufw status
```

For more details:

```bash
sudo ufw status verbose
```

### Observation

Record whether UFW is:

```text
active
```

or:

```text
inactive
```

Do not change firewall rules during this lab unless you understand the impact.

---

# Lab 21 — Check NAT Rules

Run:

```bash
sudo iptables -t nat -L -n -v
```

### Look for

```text
SNAT
DNAT
MASQUERADE
```

If your system uses nftables, also run:

```bash
sudo nft list ruleset
```

### Observation

NAT rules can be important when troubleshooting traffic between private and public networks.

---

# Lab 22 — Docker Gateway

If Docker is installed, run:

```bash
docker network ls
```

Then:

```bash
docker network inspect bridge
```

### Look for

```text
Subnet
Gateway
Containers
```

Example:

```text
Subnet:
172.17.0.0/16

Gateway:
172.17.0.1
```

### Observation

Docker bridge networks have their own network configuration and Gateway.

---

# Lab 23 — Inspect a Docker Container

First list containers:

```bash
docker ps
```

Then:

```bash
docker inspect <container-name>
```

Example:

```bash
docker inspect nginx
```

### Observation

Look at the container's network configuration.

---

# Lab 24 — Find Docker Container IP

Run:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-name>
```

Example:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx
```

### Record

```text
Container:

Container IP:

Docker Network:

Gateway:
```

---

# Lab 25 — Complete Gateway Troubleshooting Test

Now perform the complete troubleshooting sequence.

## Step 1

```bash
ip addr
```

Check:

```text
IP address
```

## Step 2

```bash
ip link
```

Check:

```text
Interface state
```

## Step 3

```bash
ip route
```

Check:

```text
Routing table
```

## Step 4

```bash
ip route | grep default
```

Check:

```text
Default Gateway
```

## Step 5

```bash
ip route get 8.8.8.8
```

Check:

```text
Gateway
Interface
Source IP
```

## Step 6

```bash
ip neigh
```

Check:

```text
Gateway MAC
```

## Step 7

```bash
ping -c 4 <gateway-ip>
```

Check:

```text
Gateway connectivity
```

## Step 8

```bash
ping -c 4 8.8.8.8
```

Check:

```text
Internet connectivity
```

## Step 9

```bash
getent hosts google.com
```

Check:

```text
DNS resolution
```

## Step 10

```bash
curl -I https://google.com
```

Check:

```text
Application connectivity
```

---

# Practical Observation Table

After completing the lab, fill this table with your actual results.

| Check | Command | Result |
|---|---|---|
| IP Address | `ip addr` | |
| Interface | `ip link` | |
| Routing Table | `ip route` | |
| Default Gateway | `ip route \| grep default` | |
| Destination Route | `ip route get 8.8.8.8` | |
| Neighbor Table | `ip neigh` | |
| Gateway Ping | `ping -c 4 <gateway-ip>` | |
| Internet Ping | `ping -c 4 8.8.8.8` | |
| DNS | `getent hosts google.com` | |
| Network Path | `tracepath google.com` | |
| Listening Ports | `ss -tuln` | |
| HTTPS | `curl -I https://google.com` | |
| Public IP | `curl ifconfig.me` | |
| Firewall | `sudo ufw status` | |

---

# Troubleshooting Scenario

## Scenario

You are working on a Linux server.

The application cannot connect to an external API.

### Question

How would you investigate?

### Answer

I would follow this sequence:

```text
1. Check IP address
       ↓
2. Check interface
       ↓
3. Check routing table
       ↓
4. Check default Gateway
       ↓
5. Check Gateway reachability
       ↓
6. Check Internet connectivity
       ↓
7. Check DNS
       ↓
8. Check destination port
       ↓
9. Check firewall
       ↓
10. Check NAT
       ↓
11. Check application
```

Commands:

```bash
ip addr
ip link
ip route
ip route | grep default
ip route get <destination-ip>
ip neigh
ping -c 4 <gateway-ip>
ping -c 4 8.8.8.8
getent hosts <domain>
nc -zv <host> <port>
curl -v https://<host>
sudo ufw status
sudo iptables -t nat -L -n -v
```

---

# Screenshots to Capture

For the handbook, capture screenshots of important practical commands.

Recommended screenshots:

### Screenshot 1 — IP Address

```bash
ip addr
```

Suggested filename:

```text
01-ip-address.png
```

### Screenshot 2 — Routing Table

```bash
ip route
```

### My Actual Observation

My routing table shows:

```text
Default Gateway: 192.168.1.1
Network Interface: wlo1
Local IP: 192.168.1.5
Local Network: 192.168.1.0/24


Suggested filename:

```text
02-routing-table.png
```

### Screenshot 3 — Default Gateway

```bash
ip route | grep default
```

Suggested filename:

```text
03-default-gateway.png
```

### Screenshot 4 — Exact Route

```bash
ip route get 8.8.8.8
```

Suggested filename:

```text
04-route-to-destination.png
```

### Screenshot 5 — Neighbor Table

```bash
ip neigh
```

Suggested filename:

```text
05-neighbor-table.png
```

### Screenshot 6 — Gateway Ping

```bash
ping -c 4 <gateway-ip>
```

Suggested filename:

```text
06-gateway-ping.png
```

### Screenshot 7 — Internet Connectivity

```bash
ping -c 4 8.8.8.8
```

Suggested filename:

```text
07-internet-connectivity.png
```

### Screenshot 8 — DNS

```bash
getent hosts google.com
```

Suggested filename:

```text
08-dns-resolution.png
```

### Screenshot 9 — Network Path

```bash
tracepath google.com
```

Suggested filename:

```text
09-network-path.png
```

### Screenshot 10 — Docker Gateway

If Docker is installed:

```bash
docker network inspect bridge
```

Suggested filename:

```text
10-docker-gateway.png
```

---

# Lab Summary

In this lab, I practically checked how my Linux system communicates with other networks through a Gateway.

I used:

```bash
ip addr
ip link
ip route
ip route | grep default
ip route get 8.8.8.8
ip neigh
ping
tracepath
ss
curl
nmcli
```

I also explored:

```text
Firewall
NAT
Docker Gateway
```

The most important troubleshooting flow I learned is:

```text
IP
 ↓
Interface
 ↓
Route
 ↓
Gateway
 ↓
NAT / Firewall
 ↓
DNS
 ↓
Destination Port
 ↓
Application
```

---

# Key Learning

A Gateway is not something I should troubleshoot in isolation.

When a server cannot communicate with another network, I should verify the complete path:

```text
Source
  ↓
Network Interface
  ↓
IP Address
  ↓
Routing Table
  ↓
Default Gateway
  ↓
NAT / Firewall
  ↓
Destination
```

This practical troubleshooting approach is useful for Linux, Docker, cloud environments, and DevOps production systems.