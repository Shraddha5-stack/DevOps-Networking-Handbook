# 🐧 Chapter 29 — Linux Networking

## 📌 Overview

Linux networking is the foundation of **DevOps, Cloud, Docker, Kubernetes, and System Administration**.

Linux provides powerful tools to configure, inspect, troubleshoot, and monitor network connectivity.

A DevOps engineer should understand how Linux handles:

* Network interfaces
* IP addresses
* Routing
* DNS
* Ports
* TCP/UDP
* Sockets
* Network namespaces
* Bridges
* Virtual interfaces
* Firewall
* Network troubleshooting
* Container networking
* Kubernetes networking

---

## 🎯 Learning Objectives

By completing this chapter, you will understand:

* How Linux networking works
* Network interfaces
* IPv4 and IPv6
* IP addresses and subnet masks
* Default gateway
* Routing tables
* DNS configuration
* `/etc/hosts`
* `/etc/resolv.conf`
* TCP and UDP ports
* Listening services
* `ss` command
* `ping`
* `traceroute` and `tracepath`
* `curl` and `wget`
* ARP/neighbour discovery
* Network namespaces
* Linux bridges
* Virtual Ethernet interfaces
* Firewall basics
* NetworkManager
* `tcpdump`
* Linux networking troubleshooting
* Docker networking
* Kubernetes networking

---

# 🏗️ Linux Networking Architecture

A simplified Linux networking flow:

```text
Application
     |
     v
Socket
     |
     v
TCP / UDP
     |
     v
IP Layer
     |
     v
Routing Table
     |
     v
Network Interface
     |
     v
Ethernet / Wi-Fi
     |
     v
Network
```

Example:

```text
curl https://example.com
        |
        v
     DNS
        |
        v
 IP Address
        |
        v
 TCP Connection
        |
        v
      TLS
        |
        v
      HTTP
        |
        v
     Internet
```

---

# 1. Network Interfaces

A network interface connects a Linux system to a network.

Common interfaces:

```text
lo      → Loopback
eth0    → Ethernet
ens33   → Ethernet
enp0s3  → Ethernet
wlan0   → Wi-Fi
wlo1    → Wi-Fi
docker0 → Docker bridge
```

View interfaces:

```bash
ip link
```

View IP addresses:

```bash
ip addr
```

Short form:

```bash
ip a
```

Example:

```text
wlo1:
    inet 192.168.1.5/24
```

This means the system has IPv4 address:

```text
192.168.1.5
```

---

# 2. Loopback Interface

The loopback interface is normally:

```text
lo
```

Its IPv4 address is:

```text
127.0.0.1
```

It refers to the local machine.

Test it:

```bash
ping 127.0.0.1
```

or:

```bash
ping localhost
```

Example:

```text
Application
    |
    v
127.0.0.1
    |
    v
Same Linux machine
```

---

# 3. IP Address

An IP address identifies a device/interface on an IP network.

Example:

```text
192.168.1.5
```

Private IPv4 ranges include:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Example:

```text
192.168.1.5/24
```

Here:

```text
IP address → 192.168.1.5
Prefix     → /24
```

---

# 4. IPv4

IPv4 uses 32-bit addresses.

Example:

```text
192.168.1.10
```

IPv4 contains four octets:

```text
192 . 168 . 1 . 10
```

Each octet ranges from:

```text
0 - 255
```

---

# 5. IPv6

IPv6 uses 128-bit addresses.

Example:

```text
2001:db8::1
```

Check IPv6:

```bash
ip -6 addr
```

Test IPv6 loopback:

```bash
ping6 ::1
```

---

# 6. Subnet Prefix

Linux commonly displays the prefix after `/`.

Example:

```text
192.168.1.5/24
```

`/24` means the first 24 bits represent the network portion.

Common prefixes:

| Prefix | Approx. Addresses |
| ------ | ----------------: |
| /8     |      16.7 million |
| /16    |            65,536 |
| /24    |               256 |
| /32    |                 1 |

---

# 7. Default Gateway

A default gateway is the router used when Linux does not have a more specific route.

View routing table:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

Meaning:

```text
Destination
     |
     v
Internet
     |
     v
192.168.1.1
     |
     v
Linux machine
```

The gateway in this example is:

```text
192.168.1.1
```

---

# 8. Routing Table

Linux uses a routing table to determine where packets should go.

View it:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1
```

Useful command:

```bash
ip route get 8.8.8.8
```

This tells Linux which route/interface it would use to reach an address.

---

# 9. DNS

DNS converts domain names into IP addresses.

Example:

```text
google.com
    |
    v
DNS
    |
    v
142.250.x.x
```

Check resolver configuration:

```bash
cat /etc/resolv.conf
```

Check hostname resolution:

```bash
getent hosts google.com
```

Using `dig`:

```bash
dig google.com
```

Using `nslookup`:

```bash
nslookup google.com
```

---

# 10. `/etc/hosts`

The `/etc/hosts` file provides local hostname mappings.

View it:

```bash
cat /etc/hosts
```

Example:

```text
127.0.0.1 localhost
127.0.1.1 my-linux-machine
```

For testing, you can map a hostname to an IP address.

Example:

```text
192.168.1.20 test-server
```

Then:

```bash
ping test-server
```

---

# 11. Hostname

Display hostname:

```bash
hostname
```

Detailed information:

```bash
hostnamectl
```

Set hostname:

```bash
sudo hostnamectl set-hostname devops-machine
```

Verify:

```bash
hostnamectl
```

---

# 12. TCP and UDP

Linux supports different transport protocols.

## TCP

TCP is:

* Connection-oriented
* Reliable
* Ordered
* Uses acknowledgements
* Provides retransmission

Common TCP services:

```text
22   → SSH
80   → HTTP
443  → HTTPS
3306 → MySQL
```

## UDP

UDP is:

* Connectionless
* Lightweight
* Faster in many use cases
* Does not guarantee delivery

Common UDP use cases:

```text
DNS
DHCP
Streaming
VoIP
```

---

# 13. Ports

A port identifies a network service on a host.

Example:

```text
192.168.1.10:22
```

Means:

```text
IP address → 192.168.1.10
Port       → 22
Service    → SSH
```

Common ports:

| Port | Protocol | Service     |
| ---: | -------- | ----------- |
|   22 | TCP      | SSH         |
|   53 | TCP/UDP  | DNS         |
|   80 | TCP      | HTTP        |
|  443 | TCP      | HTTPS       |
| 3306 | TCP      | MySQL       |
| 5432 | TCP      | PostgreSQL  |
| 6379 | TCP      | Redis       |
| 8080 | TCP      | Application |

---

# 14. Sockets

A socket is an endpoint for network communication.

Example:

```text
127.0.0.1:3306
```

A process can listen on a socket.

Check listening sockets:

```bash
ss -ltn
```

Show processes:

```bash
sudo ss -ltnp
```

UDP:

```bash
ss -lun
```

All listening TCP/UDP sockets:

```bash
sudo ss -lntup
```

---

# 15. `ss` Command

`ss` is one of the most important Linux networking commands.

Basic:

```bash
ss
```

TCP:

```bash
ss -t
```

Listening TCP:

```bash
ss -lt
```

Listening TCP with processes:

```bash
sudo ss -ltnp
```

UDP:

```bash
ss -u
```

All listening sockets:

```bash
sudo ss -lntup
```

Check a specific port:

```bash
sudo ss -lntp | grep :8080
```

---

# 16. `ping`

`ping` tests IP connectivity using ICMP.

Example:

```bash
ping google.com
```

Send four packets:

```bash
ping -c 4 google.com
```

Test gateway:

```bash
ping -c 4 192.168.1.1
```

Test localhost:

```bash
ping -c 4 127.0.0.1
```

---

# 17. Traceroute

Traceroute helps identify the network path to a destination.

Install if required:

```bash
sudo apt install traceroute
```

Run:

```bash
traceroute google.com
```

Alternative:

```bash
tracepath google.com
```

It can help identify where packets stop or experience high latency.

---

# 18. ARP / Neighbour Table

Linux maintains information about nearby network devices.

View neighbour table:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr xx:xx:xx:xx:xx:xx REACHABLE
```

Modern Linux uses the term **neighbour discovery/table** for both IPv4 and IPv6 mechanisms.

---

# 19. Network Statistics

View interface statistics:

```bash
ip -s link
```

You can inspect:

```text
RX packets
TX packets
RX errors
TX errors
dropped packets
```

These statistics are useful for troubleshooting network problems.

---

# 20. NetworkManager

Many Linux distributions use NetworkManager.

Check status:

```bash
systemctl status NetworkManager
```

List connections:

```bash
nmcli connection show
```

List devices:

```bash
nmcli device status
```

Show active connections:

```bash
nmcli connection show --active
```

---

# 21. Network Namespaces

A network namespace provides an isolated network environment.

Network namespaces are heavily used by:

* Containers
* Docker
* Kubernetes
* CNI plugins

List namespaces:

```bash
ip netns list
```

Create one:

```bash
sudo ip netns add test-ns
```

Run a command inside it:

```bash
sudo ip netns exec test-ns ip addr
```

Delete it:

```bash
sudo ip netns delete test-ns
```

Concept:

```text
Linux Host
│
├── Network Namespace A
│   ├── Interface
│   ├── Routing
│   └── Ports
│
└── Network Namespace B
    ├── Interface
    ├── Routing
    └── Ports
```

---

# 22. Virtual Ethernet Pair

A veth pair connects two network namespaces.

Concept:

```text
Namespace A
    |
   veth
    |
    |
   veth
    |
Namespace B
```

Create one:

```bash
sudo ip link add veth0 type veth peer name veth1
```

View:

```bash
ip link
```

Veth pairs are fundamental to container networking.

---

# 23. Linux Bridge

A bridge connects network interfaces at Layer 2.

View bridges:

```bash
ip link
```

Docker commonly creates:

```text
docker0
```

Inspect:

```bash
ip addr show docker0
```

Example:

```text
docker0
   |
   +--- container
   |
   +--- container
   |
   +--- container
```

---

# 24. `curl`

`curl` is one of the most important DevOps networking tools.

Test a website:

```bash
curl https://example.com
```

Headers only:

```bash
curl -I https://example.com
```

Verbose mode:

```bash
curl -v https://example.com
```

Check HTTP status:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Check response time:

```bash
curl -o /dev/null -s -w "Time: %{time_total}s\n" https://example.com
```

---

# 25. `wget`

`wget` is commonly used to download files.

Example:

```bash
wget https://example.com/file.txt
```

Useful for testing HTTP connectivity:

```bash
wget --spider https://example.com
```

---

# 26. `tcpdump`

`tcpdump` captures network packets.

Install:

```bash
sudo apt install tcpdump
```

List interfaces:

```bash
sudo tcpdump -D
```

Capture packets:

```bash
sudo tcpdump -i wlo1
```

Capture ICMP:

```bash
sudo tcpdump -i wlo1 icmp
```

Capture traffic on port 80:

```bash
sudo tcpdump -i wlo1 port 80
```

Capture DNS:

```bash
sudo tcpdump -i wlo1 port 53
```

Write capture to a file:

```bash
sudo tcpdump -i wlo1 -w capture.pcap
```

Read capture:

```bash
tcpdump -r capture.pcap
```

---

# 27. Linux Firewall

Linux systems can use firewall technologies such as:

```text
nftables
iptables
ufw
```

Check UFW:

```bash
sudo ufw status
```

Example:

```text
Status: active
```

Allow SSH:

```bash
sudo ufw allow 22/tcp
```

Allow HTTP:

```bash
sudo ufw allow 80/tcp
```

Allow HTTPS:

```bash
sudo ufw allow 443/tcp
```

> Always understand existing rules before changing a firewall, especially on a remote server.

---

# 28. `iptables` and `nftables`

`iptables` is a traditional Linux firewall tool.

`nftables` is the modern packet-filtering framework.

Check nftables:

```bash
sudo nft list ruleset
```

Check iptables:

```bash
sudo iptables -L -n -v
```

For modern Linux systems, understand **nftables** conceptually even when working with tools such as UFW.

---

# 29. Linux Networking and Docker

Docker creates its own networking components.

Common Docker networks:

```bash
docker network ls
```

Inspect a network:

```bash
docker network inspect bridge
```

Typical architecture:

```text
Host
 |
docker0
 |
 +---- Container A
 |
 +---- Container B
```

Docker networking concepts include:

* Bridge
* Host
* None
* Overlay
* Port publishing
* Container DNS
* Network isolation

Example:

```bash
docker run -d -p 8080:80 nginx
```

Meaning:

```text
Host :8080
     |
     v
Container :80
```

---

# 30. Linux Networking and Kubernetes

Kubernetes networking relies heavily on Linux networking.

Important concepts:

```text
Pod
Service
ClusterIP
NodePort
LoadBalancer
CNI
Network Namespace
veth
Bridge
iptables/nftables
Routing
```

Conceptually:

```text
Pod
 |
veth
 |
Node Network
 |
CNI
 |
Kubernetes Network
```

Kubernetes pods normally receive their own network identity.

Useful commands:

```bash
kubectl get pods -o wide
```

```bash
kubectl get svc
```

Inside a pod:

```bash
kubectl exec -it <pod-name> -- ip addr
```

Test connectivity:

```bash
kubectl exec -it <pod-name> -- curl <service-name>
```

---

# 31. Linux Networking Troubleshooting

A practical troubleshooting sequence:

```text
1. Check interface
       ↓
2. Check IP address
       ↓
3. Check route
       ↓
4. Check gateway
       ↓
5. Check DNS
       ↓
6. Check port
       ↓
7. Check service
       ↓
8. Check firewall
       ↓
9. Capture packets
       ↓
10. Check application
```

Useful commands:

```bash
ip link
ip addr
ip route
ip neigh
ping
ss
dig
curl
nc
tcpdump
```

---

# 32. Example Troubleshooting

Suppose an application is not reachable on port `8080`.

### Step 1 — Check interface

```bash
ip link
```

### Step 2 — Check IP

```bash
ip addr
```

### Step 3 — Check route

```bash
ip route
```

### Step 4 — Check listening port

```bash
sudo ss -lntp | grep :8080
```

### Step 5 — Test locally

```bash
curl http://127.0.0.1:8080
```

### Step 6 — Test using server IP

```bash
curl http://<SERVER-IP>:8080
```

### Step 7 — Check firewall

```bash
sudo ufw status
```

### Step 8 — Capture traffic

```bash
sudo tcpdump -i any port 8080
```

This helps determine where the connection is failing.

---

# 33. `127.0.0.1` vs `0.0.0.0`

This is extremely important in DevOps.

If an application listens on:

```text
127.0.0.1:8080
```

it accepts connections only from the local machine.

If it listens on:

```text
0.0.0.0:8080
```

it listens on all IPv4 interfaces.

Example:

```text
127.0.0.1:8080
      ↓
Local access only
```

Versus:

```text
0.0.0.0:8080
      ↓
All IPv4 interfaces
```

This is a common reason why an application works locally but cannot be accessed from another machine or container.

---

# 34. Important Linux Networking Files

| File                 | Purpose                       |
| -------------------- | ----------------------------- |
| `/etc/hosts`         | Local hostname mappings       |
| `/etc/resolv.conf`   | DNS resolver configuration    |
| `/etc/hostname`      | System hostname               |
| `/etc/nsswitch.conf` | Name-service lookup order     |
| `/proc/net/`         | Kernel network information    |
| `/sys/class/net/`    | Network interface information |

Check:

```bash
cat /etc/hosts
```

```bash
cat /etc/resolv.conf
```

```bash
cat /etc/nsswitch.conf
```

---

# 35. Important Commands

### Interfaces

```bash
ip link
ip addr
```

### Routing

```bash
ip route
ip route get 8.8.8.8
```

### Neighbours

```bash
ip neigh
```

### Ports

```bash
ss -lntup
```

### DNS

```bash
dig google.com
nslookup google.com
getent hosts google.com
```

### Connectivity

```bash
ping google.com
tracepath google.com
```

### HTTP

```bash
curl -I https://example.com
```

### Packet capture

```bash
sudo tcpdump -i any
```

### Firewall

```bash
sudo ufw status
```

---

# 36. DevOps Use Cases

Linux networking is used daily in DevOps.

### CI/CD

```text
CI Runner
   |
   v
Git Repository
   |
   v
Artifact Repository
   |
   v
Deployment Server
```

### Docker

```text
Host
 |
Docker Bridge
 |
Containers
```

### Kubernetes

```text
Pod
 |
Service
 |
Ingress
 |
Load Balancer
```

### Cloud

```text
Linux EC2/VM
 |
Private IP
 |
Route Table
 |
Gateway
 |
Internet / Other Networks
```

---

# 37. Real-World DevOps Scenario

### Problem

Application is running but users cannot access it.

### Investigation

Check:

```bash
sudo ss -lntp
```

Suppose the application is:

```text
127.0.0.1:8080
```

The service is bound only to localhost.

Change the application configuration to listen on:

```text
0.0.0.0:8080
```

Then verify:

```bash
sudo ss -lntp | grep :8080
```

Test:

```bash
curl http://localhost:8080
```

Then test using the server IP:

```bash
curl http://<SERVER-IP>:8080
```

This is a common Linux networking issue in Docker, Kubernetes, and cloud environments.

---

# 38. Interview-Ready Questions

You should be able to answer:

1. What is a network interface?
2. What is the loopback interface?
3. What is `127.0.0.1`?
4. What is `0.0.0.0`?
5. What is an IP address?
6. What is a subnet?
7. What is a default gateway?
8. What is a routing table?
9. How do you check the routing table?
10. How do you check listening ports?
11. What is the difference between TCP and UDP?
12. What is DNS?
13. How do you troubleshoot DNS?
14. What is `/etc/hosts`?
15. What is `/etc/resolv.conf`?
16. What is ARP?
17. What is `ip neigh`?
18. What is `ss`?
19. What is `tcpdump`?
20. What is a network namespace?
21. What is a veth pair?
22. What is a Linux bridge?
23. How does Docker use Linux networking?
24. How does Kubernetes use Linux networking?
25. How would you troubleshoot an unreachable application?
26. Why does an application work on localhost but not remotely?
27. How do you check whether port 8080 is listening?
28. How do you test HTTP connectivity?
29. How do you check DNS resolution?
30. How do you inspect network traffic?

---

# 🧠 Quick Revision

Remember this flow:

```text
Interface
    ↓
IP Address
    ↓
Subnet
    ↓
Routing Table
    ↓
Gateway
    ↓
DNS
    ↓
TCP / UDP
    ↓
Port
    ↓
Service
    ↓
Firewall
    ↓
Application
```

Most important commands:

```bash
ip addr
ip link
ip route
ip neigh
ss
ping
tracepath
dig
nslookup
curl
wget
tcpdump
ufw
nmcli
```

---

# 🎯 Chapter Goal

After completing Chapter 29, you should be able to:

* Inspect Linux network interfaces
* Understand IP addresses
* Read routing tables
* Identify the default gateway
* Troubleshoot DNS
* Check listening ports
* Understand TCP and UDP
* Test connectivity
* Inspect neighbour information
* Capture network packets
* Understand network namespaces
* Understand Linux bridges and veth
* Troubleshoot application connectivity
* Understand Docker networking foundations
* Understand Kubernetes networking foundations

---

## 🚀 Next

The next files for this chapter are:

```text
29-Linux-Networking/
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

Complete the practical work in `commands.md` and `practical-lab.md` before moving to the next chapter.
