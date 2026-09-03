# 🐧 Linux Networking — Detailed Notes

## 1. What is Linux Networking?

Linux networking is the set of kernel features, protocols, interfaces, services, and tools that allow a Linux system to communicate with other systems.

Linux networking is fundamental to:

* DevOps
* Cloud computing
* Docker
* Kubernetes
* System administration
* CI/CD
* Web servers
* Databases
* Monitoring
* Security

A Linux machine communicates through a networking stack.

```text
Application
     ↓
Socket
     ↓
TCP / UDP
     ↓
IP
     ↓
Network Interface
     ↓
Network Driver
     ↓
Network Hardware
     ↓
Network
```

---

# 2. Linux Networking Stack

A simplified Linux networking architecture:

```text
+---------------------------+
|       Applications        |
| curl, ssh, nginx, etc.    |
+---------------------------+
            |
            v
+---------------------------+
|          Sockets           |
+---------------------------+
            |
            v
+---------------------------+
|       TCP / UDP            |
+---------------------------+
            |
            v
+---------------------------+
|       IP Layer             |
+---------------------------+
            |
            v
+---------------------------+
|     Routing / Firewall     |
+---------------------------+
            |
            v
+---------------------------+
|    Network Interface       |
| eth0 / ens33 / wlo1        |
+---------------------------+
            |
            v
+---------------------------+
|       Network Driver       |
+---------------------------+
            |
            v
+---------------------------+
|      Physical Network      |
+---------------------------+
```

---

# 3. Network Interface

A network interface is the connection point between Linux and a network.

Examples:

```text
lo
eth0
ens33
enp0s3
wlan0
wlo1
docker0
```

Check interfaces:

```bash
ip link
```

Check addresses:

```bash
ip addr
```

Short versions:

```bash
ip l
ip a
```

---

# 4. Interface States

A network interface can have different states.

Example:

```text
UP
DOWN
UNKNOWN
```

Check:

```bash
ip link
```

An interface that is `UP` is enabled at the link level.

Bring an interface up:

```bash
sudo ip link set eth0 up
```

Bring it down:

```bash
sudo ip link set eth0 down
```

> Be careful with these commands on a remote server because disabling the active interface can disconnect you.

---

# 5. Loopback Interface

The loopback interface is:

```text
lo
```

Its standard IPv4 address is:

```text
127.0.0.1
```

IPv6 loopback:

```text
::1
```

The loopback interface allows a machine to communicate with itself.

Example:

```bash
ping 127.0.0.1
```

or:

```bash
ping localhost
```

Architecture:

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

# 6. IPv4 Addressing

IPv4 addresses are 32-bit addresses.

Example:

```text
192.168.1.10
```

They are written as four decimal octets:

```text
192 . 168 . 1 . 10
```

Each octet can contain:

```text
0 - 255
```

Example private network:

```text
192.168.1.0/24
```

Possible addresses include:

```text
192.168.1.1
192.168.1.2
192.168.1.3
...
192.168.1.254
```

---

# 7. Private IPv4 Address Ranges

The major private IPv4 ranges are:

| Range                         | CIDR             |
| ----------------------------- | ---------------- |
| 10.0.0.0 – 10.255.255.255     | `10.0.0.0/8`     |
| 172.16.0.0 – 172.31.255.255   | `172.16.0.0/12`  |
| 192.168.0.0 – 192.168.255.255 | `192.168.0.0/16` |

Private IP addresses are commonly used inside:

* Home networks
* Corporate networks
* Cloud VPCs/VNets
* Docker networks
* Kubernetes networks

---

# 8. CIDR Notation

CIDR represents an IP network using a prefix length.

Example:

```text
192.168.1.10/24
```

The `/24` indicates that 24 bits belong to the network prefix.

Common prefixes:

```text
/8
/16
/24
/32
```

For example:

```text
192.168.1.0/24
```

represents the network.

A `/32` usually represents a single IPv4 address.

---

# 9. IPv6

IPv6 uses 128-bit addresses.

Example:

```text
2001:db8::1
```

Check IPv6 addresses:

```bash
ip -6 addr
```

IPv6 loopback:

```text
::1
```

IPv6 is designed to provide a much larger address space than IPv4.

---

# 10. MAC Address

A network interface normally has a MAC address at Layer 2.

Example:

```text
aa:bb:cc:dd:ee:ff
```

View MAC addresses:

```bash
ip link
```

Example:

```text
link/ether aa:bb:cc:dd:ee:ff
```

IP addresses operate at Layer 3, while MAC addresses operate at Layer 2.

---

# 11. IP Address vs MAC Address

| Feature  | IP Address         | MAC Address                       |
| -------- | ------------------ | --------------------------------- |
| Layer    | Layer 3            | Layer 2                           |
| Purpose  | Logical addressing | Link-layer addressing             |
| Example  | `192.168.1.10`     | `aa:bb:cc:dd:ee:ff`               |
| Changes  | Can change         | Usually associated with interface |
| Used for | Routing            | Local network delivery            |

---

# 12. Default Gateway

A default gateway is the router Linux uses when there is no more specific route for a destination.

Example:

```text
default via 192.168.1.1 dev wlo1
```

Here:

```text
Gateway = 192.168.1.1
Interface = wlo1
```

Check:

```bash
ip route
```

Concept:

```text
Linux
  |
  | 192.168.1.5
  v
192.168.1.1
Gateway
  |
  v
Internet
```

---

# 13. Routing Table

Linux maintains a routing table to decide where packets should go.

View it:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1
```

The kernel compares the destination IP against available routes.

The most specific matching route is generally preferred.

---

# 14. Understanding a Route

Consider:

```text
default via 192.168.1.1 dev wlo1
```

Meaning:

```text
default
```

All destinations that don't have a more specific route.

```text
via 192.168.1.1
```

Send the packet through this gateway.

```text
dev wlo1
```

Use the `wlo1` interface.

---

# 15. Route Lookup

You can ask Linux which route it would use:

```bash
ip route get 8.8.8.8
```

This is extremely useful during troubleshooting.

Example:

```text
8.8.8.8 via 192.168.1.1 dev wlo1
```

This tells you the route selected for that destination.

---

# 16. ARP

ARP stands for:

**Address Resolution Protocol**

For IPv4 local network communication, ARP helps determine the MAC address associated with an IP address.

Concept:

```text
Linux wants:
192.168.1.1

        ↓

Who has 192.168.1.1?

        ↓

Gateway replies with MAC address

        ↓

Linux sends Ethernet frame
```

Modern Linux exposes this information through the neighbour table.

Check:

```bash
ip neigh
```

---

# 17. Neighbour Table

View neighbour information:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

This tells us:

```text
IP       → 192.168.1.1
Interface → wlo1
MAC      → aa:bb:cc:dd:ee:ff
State    → REACHABLE
```

---

# 18. DNS

DNS stands for:

**Domain Name System**

DNS translates domain names into IP addresses.

Example:

```text
google.com
     |
     v
    DNS
     |
     v
IP Address
```

Without DNS, users would have to remember IP addresses instead of domain names.

---

# 19. DNS Resolution

Suppose you execute:

```bash
curl https://example.com
```

A simplified process is:

```text
curl
 |
 v
DNS Resolution
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
Web Server
```

---

# 20. `/etc/resolv.conf`

Linux systems use resolver configuration to determine DNS servers and related resolver settings.

Check:

```bash
cat /etc/resolv.conf
```

Example:

```text
nameserver 8.8.8.8
```

The exact contents depend on the Linux distribution and network management system.

On many modern Linux systems, `/etc/resolv.conf` may be managed automatically by another service.

---

# 21. `/etc/hosts`

The `/etc/hosts` file provides local hostname-to-IP mappings.

Check:

```bash
cat /etc/hosts
```

Example:

```text
127.0.0.1 localhost
127.0.1.1 my-machine
```

You can use it for local testing:

```text
192.168.1.20 test-server
```

Then:

```bash
ping test-server
```

---

# 22. Name Service Lookup

Linux can use multiple sources to resolve names.

The configuration is commonly controlled by:

```text
/etc/nsswitch.conf
```

Check:

```bash
cat /etc/nsswitch.conf
```

Look for:

```text
hosts:
```

This helps determine the order in which hostname sources are consulted.

---

# 23. DNS Troubleshooting

Useful commands:

```bash
getent hosts example.com
```

```bash
dig example.com
```

```bash
nslookup example.com
```

If DNS fails, test direct connectivity to a known IP when appropriate.

For example:

```bash
ping -c 4 8.8.8.8
```

If IP connectivity works but hostname resolution fails, DNS becomes a strong suspect.

---

# 24. TCP

TCP stands for:

**Transmission Control Protocol**

TCP provides:

* Connection-oriented communication
* Reliable delivery
* Ordered data
* Retransmission
* Flow control
* Congestion control

Common TCP applications include:

```text
SSH
HTTP
HTTPS
MySQL
PostgreSQL
```

---

# 25. UDP

UDP stands for:

**User Datagram Protocol**

UDP is connectionless and has lower protocol overhead than TCP.

It does not provide TCP-style guarantees for:

* Delivery
* Ordering
* Retransmission

Common UDP use cases include:

* DNS
* DHCP
* Streaming
* VoIP
* Some real-time applications

---

# 26. TCP Three-Way Handshake

TCP establishes a connection using a three-way handshake.

```text
Client                    Server
  |                         |
  | -------- SYN ---------> |
  |                         |
  | <------ SYN-ACK ------- |
  |                         |
  | -------- ACK ---------> |
  |                         |
  |      Connected          |
```

The three packets are:

```text
SYN
SYN-ACK
ACK
```

---

# 27. TCP Connection States

Common TCP states include:

```text
LISTEN
SYN-SENT
SYN-RECEIVED
ESTABLISHED
FIN-WAIT
TIME-WAIT
CLOSE-WAIT
```

Check TCP connections:

```bash
ss -tan
```

Check listening ports:

```bash
ss -ltn
```

---

# 28. Ports

A port identifies a service endpoint on a host.

Example:

```text
192.168.1.10:22
```

Means:

```text
IP   → 192.168.1.10
Port → 22
```

Common ports:

| Port | Service                 |
| ---: | ----------------------- |
|   22 | SSH                     |
|   53 | DNS                     |
|   80 | HTTP                    |
|  443 | HTTPS                   |
| 3306 | MySQL                   |
| 5432 | PostgreSQL              |
| 6379 | Redis                   |
| 8080 | Common application port |

---

# 29. Sockets

A socket is an endpoint used by an application for network communication.

For example:

```text
127.0.0.1:8080
```

An application can bind to a socket and listen for connections.

Check sockets:

```bash
ss -lntup
```

---

# 30. The `ss` Command

`ss` is one of the most important Linux networking tools.

Check TCP:

```bash
ss -t
```

Check UDP:

```bash
ss -u
```

Listening TCP:

```bash
ss -lt
```

Listening TCP with numbers:

```bash
ss -ltn
```

Listening sockets with processes:

```bash
sudo ss -lntup
```

Check port 8080:

```bash
sudo ss -lntp | grep :8080
```

---

# 31. `netstat`

`netstat` was traditionally used for network statistics and sockets.

On modern Linux systems, `ss` is generally preferred.

Old command:

```bash
netstat -lntp
```

Modern alternative:

```bash
ss -lntp
```

---

# 32. `lsof` for Network Connections

`lsof` can show which process owns a network socket.

Example:

```bash
sudo lsof -i
```

Specific port:

```bash
sudo lsof -i :8080
```

This is useful when you need to identify which application is using a port.

---

# 33. `ping`

`ping` is commonly used to test IP connectivity using ICMP.

Example:

```bash
ping google.com
```

Limit the number of packets:

```bash
ping -c 4 google.com
```

Test localhost:

```bash
ping -c 4 127.0.0.1
```

Test gateway:

```bash
ping -c 4 192.168.1.1
```

Important:

A failed ping does not always mean the application is unreachable. ICMP may be filtered while TCP/HTTPS still works.

---

# 34. `traceroute` and `tracepath`

These tools help identify the network path toward a destination.

```bash
traceroute google.com
```

Alternative:

```bash
tracepath google.com
```

They are useful for identifying:

* Routing problems
* Network hops
* Latency changes
* Where connectivity appears to stop

---

# 35. `curl`

`curl` is essential for DevOps networking.

Test an HTTP endpoint:

```bash
curl https://example.com
```

Headers:

```bash
curl -I https://example.com
```

Verbose output:

```bash
curl -v https://example.com
```

Follow redirects:

```bash
curl -L https://example.com
```

Check status code:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Check response time:

```bash
curl -o /dev/null -s -w "%{time_total}\n" https://example.com
```

---

# 36. `wget`

`wget` is commonly used for downloading files.

Example:

```bash
wget https://example.com/file.txt
```

Test without downloading:

```bash
wget --spider https://example.com
```

---

# 37. `nc` — Netcat

Netcat is useful for testing TCP/UDP connectivity.

Test whether a TCP port is reachable:

```bash
nc -vz example.com 443
```

Local testing:

```bash
nc -vz 127.0.0.1 8080
```

It can be useful when you want to test a port without depending on an application-level protocol such as HTTP.

---

# 38. `tcpdump`

`tcpdump` captures packets from a network interface.

Install:

```bash
sudo apt install tcpdump
```

List interfaces:

```bash
sudo tcpdump -D
```

Capture traffic:

```bash
sudo tcpdump -i any
```

Capture on a specific interface:

```bash
sudo tcpdump -i wlo1
```

Capture ICMP:

```bash
sudo tcpdump -i wlo1 icmp
```

Capture port 8080:

```bash
sudo tcpdump -i any port 8080
```

Capture DNS:

```bash
sudo tcpdump -i any port 53
```

Save packets:

```bash
sudo tcpdump -i any -w capture.pcap
```

Read packets:

```bash
tcpdump -r capture.pcap
```

---

# 39. Network Interface Statistics

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
RX dropped
TX dropped
```

These statistics can help identify interface-level problems.

---

# 40. NetworkManager

NetworkManager manages network connections on many Linux distributions.

Check service:

```bash
systemctl status NetworkManager
```

List devices:

```bash
nmcli device status
```

List connections:

```bash
nmcli connection show
```

Show active connections:

```bash
nmcli connection show --active
```

---

# 41. Network Namespace

A network namespace provides an isolated network environment.

Each namespace can have its own:

* Interfaces
* IP addresses
* Routing table
* Ports
* Network devices
* Firewall/network configuration

Create a namespace:

```bash
sudo ip netns add dev-ns
```

List:

```bash
ip netns list
```

Run a command inside:

```bash
sudo ip netns exec dev-ns ip addr
```

Delete:

```bash
sudo ip netns delete dev-ns
```

---

# 42. Why Network Namespaces Matter in DevOps

Network namespaces are fundamental to containers.

Conceptually:

```text
Linux Host
│
├── Host Network Namespace
│
├── Container Namespace A
│
├── Container Namespace B
│
└── Container Namespace C
```

Docker containers use Linux networking features to isolate and connect container network environments.

Kubernetes pods also use Linux network namespaces.

---

# 43. Virtual Ethernet — veth

A veth pair is a pair of connected virtual network interfaces.

Concept:

```text
Namespace A
     |
   veth0
     |
     |
   veth1
     |
Namespace B
```

Create:

```bash
sudo ip link add veth0 type veth peer name veth1
```

View:

```bash
ip link
```

One end can be moved into another namespace.

---

# 44. Linux Bridge

A Linux bridge behaves similarly to a Layer 2 switch.

Concept:

```text
          Linux Bridge
          /    |    \
         /     |     \
       Host   VM   Container
```

Docker commonly creates a bridge named:

```text
docker0
```

Check:

```bash
ip addr show docker0
```

Docker network information:

```bash
docker network ls
```

---

# 45. `127.0.0.1` vs `0.0.0.0`

This is one of the most important concepts for DevOps engineers.

If an application listens on:

```text
127.0.0.1:8080
```

it normally accepts connections through the local loopback interface only.

If it listens on:

```text
0.0.0.0:8080
```

it listens on all IPv4 interfaces, subject to firewall and application configuration.

Example:

```text
Application
    |
    +---- 127.0.0.1:8080
             |
             v
        Local machine
```

Versus:

```text
Application
    |
    +---- 0.0.0.0:8080
             |
       +-----+------+
       |            |
     eth0         wlan0
```

This explains many:

> "It works on localhost but not from another machine"

problems.

---

# 46. Firewall

A firewall controls network traffic according to configured rules.

Linux networking may involve:

```text
nftables
iptables
ufw
```

Check UFW:

```bash
sudo ufw status
```

Check nftables:

```bash
sudo nft list ruleset
```

Check iptables where applicable:

```bash
sudo iptables -L -n -v
```

---

# 47. Firewall Troubleshooting

Suppose:

```bash
curl http://localhost:8080
```

works, but:

```bash
curl http://SERVER-IP:8080
```

doesn't work from another machine.

Possible causes include:

```text
Application binding
Firewall
Cloud security group
Network route
Service configuration
```

Always check the application listener first:

```bash
sudo ss -lntp | grep :8080
```

---

# 48. Linux Networking Files

Important files:

| File                 | Purpose                           |
| -------------------- | --------------------------------- |
| `/etc/hosts`         | Local hostname mappings           |
| `/etc/resolv.conf`   | Resolver configuration            |
| `/etc/hostname`      | Hostname                          |
| `/etc/nsswitch.conf` | Name-service lookup configuration |
| `/proc/net/`         | Kernel network information        |
| `/sys/class/net/`    | Network interface information     |

---

# 49. `/proc/net`

The `/proc` filesystem exposes kernel information.

Examples:

```bash
cat /proc/net/dev
```

```bash
cat /proc/net/route
```

These can provide low-level networking information.

For most daily administration tasks, however, modern tools such as:

```bash
ip
ss
```

are easier to use.

---

# 50. `/sys/class/net`

This directory contains information about network interfaces.

List interfaces:

```bash
ls /sys/class/net/
```

Example:

```text
lo
wlo1
docker0
```

Check interface state:

```bash
cat /sys/class/net/wlo1/operstate
```

---

# 51. Linux Networking Troubleshooting Method

Use a systematic approach.

```text
1. Interface
      ↓
2. IP address
      ↓
3. Route
      ↓
4. Gateway
      ↓
5. DNS
      ↓
6. Port
      ↓
7. Service
      ↓
8. Firewall
      ↓
9. Packet capture
      ↓
10. Application
```

---

# 52. Step 1 — Check Interface

```bash
ip link
```

Check whether the expected interface exists and is operational.

---

# 53. Step 2 — Check IP Address

```bash
ip addr
```

Confirm that the interface has an appropriate IP address.

---

# 54. Step 3 — Check Routing

```bash
ip route
```

Look for:

```text
default via ...
```

Also test a specific destination:

```bash
ip route get 8.8.8.8
```

---

# 55. Step 4 — Check Gateway

Test the gateway:

```bash
ping -c 4 <gateway-ip>
```

If the gateway is unreachable, investigate the local network, interface, address, or route.

---

# 56. Step 5 — Check DNS

Test:

```bash
getent hosts example.com
```

Then:

```bash
dig example.com
```

If DNS fails but direct IP connectivity works, investigate DNS configuration.

---

# 57. Step 6 — Check Port

Check local listening ports:

```bash
sudo ss -lntup
```

Specific port:

```bash
sudo ss -lntp | grep :8080
```

---

# 58. Step 7 — Test the Service

For HTTP:

```bash
curl -v http://127.0.0.1:8080
```

For TCP:

```bash
nc -vz 127.0.0.1 8080
```

---

# 59. Step 8 — Check Firewall

```bash
sudo ufw status
```

If using nftables:

```bash
sudo nft list ruleset
```

Do not change firewall rules blindly on production systems.

---

# 60. Step 9 — Capture Packets

Use:

```bash
sudo tcpdump -i any port 8080
```

Then generate traffic:

```bash
curl http://127.0.0.1:8080
```

Observe whether packets are:

* Leaving
* Arriving
* Being answered
* Being retransmitted
* Being rejected

---

# 61. Step 10 — Check Application

Finally check the application itself.

For example:

```bash
systemctl status nginx
```

Logs:

```bash
journalctl -u nginx
```

Or application-specific logs.

---

# 62. Docker Networking

Docker relies on Linux networking features.

Common Docker network types include:

```text
bridge
host
none
overlay
```

List networks:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect bridge
```

Typical bridge architecture:

```text
Linux Host
    |
 docker0
    |
 +--+----------+
 |             |
 v             v
Container A  Container B
```

---

# 63. Docker Port Publishing

Example:

```bash
docker run -d -p 8080:80 nginx
```

Meaning:

```text
Host port 8080
      |
      v
Container port 80
```

Traffic flow:

```text
Client
  |
  v
Host:8080
  |
  v
Docker networking
  |
  v
Container:80
```

---

# 64. Kubernetes Networking

Kubernetes builds on Linux networking concepts.

Important components include:

```text
Network Namespace
veth
Routing
CNI
Pod network
Service
ClusterIP
NodePort
LoadBalancer
Ingress
```

Basic architecture:

```text
Client
  |
  v
Service
  |
  v
Pod
  |
  v
Container
```

---

# 65. Kubernetes Pod Networking

Pods use network namespaces.

Conceptually:

```text
Kubernetes Node
      |
      +---- Pod Network Namespace
      |          |
      |        eth0
      |          |
      |       Pod IP
      |
      +---- Pod Network Namespace
                 |
               eth0
                 |
              Pod IP
```

Check pod IPs:

```bash
kubectl get pods -o wide
```

---

# 66. Kubernetes Service Networking

A Service provides a stable network endpoint for a group of pods.

Example:

```text
Client
   |
   v
Service
   |
   +---- Pod 1
   |
   +---- Pod 2
   |
   +---- Pod 3
```

Useful command:

```bash
kubectl get svc
```

---

# 67. Network Namespaces and Containers

The relationship can be summarized as:

```text
Linux Kernel
     |
     +--- Network Namespace
              |
              +--- Interface
              +--- IP
              +--- Routes
              +--- Ports
```

Containers are therefore not using a completely separate networking system from Linux. They use Linux kernel networking primitives.

---

# 68. Network Security

Linux networking security includes:

* Firewall
* SSH security
* Port management
* TLS
* Network segmentation
* Least privilege
* Monitoring
* Packet inspection
* Access control

A good security practice is to expose only required ports.

Example:

```text
Required:
22    → SSH
443   → HTTPS

Not required:
3306  → Database should not normally be publicly exposed
```

---

# 69. Common DevOps Networking Problems

### Problem 1: DNS failure

Symptoms:

```text
curl: Could not resolve host
```

Check:

```bash
getent hosts example.com
cat /etc/resolv.conf
dig example.com
```

---

### Problem 2: Port not listening

Check:

```bash
sudo ss -lntp | grep :8080
```

If nothing appears, the application may not be listening.

---

### Problem 3: Localhost works but remote access fails

Check:

```bash
sudo ss -lntp | grep :8080
```

If:

```text
127.0.0.1:8080
```

the application may only be reachable locally.

---

### Problem 4: Firewall blocks traffic

Check:

```bash
sudo ufw status
```

---

### Problem 5: Wrong route

Check:

```bash
ip route
```

and:

```bash
ip route get <destination-ip>
```

---

# 70. Important Linux Networking Commands

### Interface

```bash
ip link
ip addr
```

### Routing

```bash
ip route
ip route get <destination>
```

### Neighbour

```bash
ip neigh
```

### Ports

```bash
ss -lntup
```

### Processes

```bash
sudo lsof -i
```

### Connectivity

```bash
ping
tracepath
traceroute
```

### DNS

```bash
getent
dig
nslookup
```

### HTTP

```bash
curl
wget
```

### TCP testing

```bash
nc
```

### Packet capture

```bash
tcpdump
```

### Firewall

```bash
ufw
nft
iptables
```

### NetworkManager

```bash
nmcli
```

---

# 71. Linux Networking and DevOps

Linux networking knowledge is required when working with:

### Git

Git communicates with remote repositories using protocols such as:

```text
HTTPS
SSH
```

### CI/CD

CI/CD runners need network connectivity to:

```text
Git repository
Artifact repository
Container registry
Cloud APIs
Kubernetes API
Deployment servers
```

### Docker

Docker requires networking for:

```text
Container-to-container communication
Host-to-container communication
Container-to-internet communication
```

### Kubernetes

Kubernetes networking enables:

```text
Pod-to-pod
Pod-to-service
Pod-to-internet
External-to-service
```

### Cloud

Cloud VMs communicate through:

```text
VPC/VNet
Subnet
Route Table
Security Group
Firewall
Gateway
Load Balancer
```

---

# 72. Real-World Example

Suppose a DevOps engineer deploys an application on Linux:

```text
Application
    |
    | Port 8080
    v
Linux Server
    |
    | 443
    v
Load Balancer
    |
    v
Users
```

The engineer must verify:

```bash
ip addr
ip route
sudo ss -lntp
curl localhost:8080
sudo ufw status
```

If remote connectivity fails, investigate:

```text
Application binding
      ↓
Linux firewall
      ↓
Cloud firewall/security group
      ↓
Route
      ↓
Load balancer
      ↓
DNS
```

---

# 73. Golden Troubleshooting Checklist

When an application is unreachable:

```text
[ ] Is the interface UP?
[ ] Does the server have an IP?
[ ] Is the route correct?
[ ] Is the gateway reachable?
[ ] Does DNS resolve?
[ ] Is the port listening?
[ ] Is the application healthy?
[ ] Is the application bound correctly?
[ ] Is the Linux firewall allowing traffic?
[ ] Is the cloud firewall allowing traffic?
[ ] Is the service reachable?
[ ] Do packet captures show traffic?
[ ] Are application logs showing errors?
```

---

# 74. Interview Answer — What is Linux Networking?

**Interview-ready answer:**

> Linux networking is the collection of kernel networking capabilities, protocols, interfaces, routing, firewall mechanisms, and tools that allow Linux systems to communicate over networks. As a DevOps engineer, I use tools such as `ip`, `ss`, `ping`, `dig`, `curl`, `tcpdump`, and `nmcli` to configure and troubleshoot networking. Linux networking is also the foundation of Docker and Kubernetes networking.

---

# 75. Interview Answer — How Do You Troubleshoot Network Connectivity?

**Interview-ready answer:**

> I troubleshoot networking layer by layer. First I check the network interface using `ip link`, then verify the IP address using `ip addr`, check routes using `ip route`, test the gateway and connectivity using `ping`, verify DNS using `dig` or `getent`, check listening ports using `ss`, test the application using `curl` or `nc`, inspect firewall rules, and finally use `tcpdump` when packet-level analysis is required.

---

# 76. Interview Answer — Why Does an Application Work on Localhost but Not Remotely?

**Interview-ready answer:**

> The application may be bound only to the loopback address, such as `127.0.0.1`, which allows only local connections. I would check the listening address using `ss -lntp`. If necessary, I would configure the application to listen on an appropriate non-loopback address such as `0.0.0.0`, while also checking Linux firewalls, cloud security rules, routing, and application configuration.

---

# 77. Interview Answer — What is `ss`?

**Interview-ready answer:**

> `ss` is a Linux command used to inspect sockets and network connections. I commonly use `ss -lntup` to identify listening TCP and UDP ports and the processes using them. It is generally preferred over the older `netstat` command on modern Linux systems.

---

# 78. Interview Answer — What is a Network Namespace?

**Interview-ready answer:**

> A network namespace provides an isolated networking environment with its own interfaces, IP addresses, routes, and sockets. Linux containers use network namespaces to isolate their networking, and Kubernetes networking also relies heavily on Linux network namespaces and virtual Ethernet interfaces.

---

# 79. Interview Answer — What is `tcpdump`?

**Interview-ready answer:**

> `tcpdump` is a command-line packet capture and network analysis tool. I use it when higher-level tools such as `ping`, `curl`, or `ss` are not enough to determine what is happening at the packet level. For example, I can use `tcpdump -i any port 8080` to inspect traffic to an application running on port 8080.

---

# 80. Quick Revision

Remember this Linux networking flow:

```text
Interface
   ↓
IP Address
   ↓
Subnet
   ↓
Route
   ↓
Gateway
   ↓
DNS
   ↓
TCP/UDP
   ↓
Port
   ↓
Socket
   ↓
Service
   ↓
Firewall
   ↓
Application
```

Most important commands:

```bash
ip link
ip addr
ip route
ip neigh
ss
ping
tracepath
dig
nslookup
getent
curl
wget
nc
tcpdump
nmcli
ufw
nft
```

---

# 🎯 Chapter 29 Key Takeaways

You should now understand:

* Linux networking architecture
* Network interfaces
* Loopback
* IPv4
* IPv6
* CIDR
* MAC addresses
* Default gateways
* Routing tables
* ARP/neighbour tables
* DNS
* `/etc/hosts`
* `/etc/resolv.conf`
* TCP
* UDP
* Ports
* Sockets
* `ss`
* `ping`
* `traceroute`
* `tracepath`
* `curl`
* `wget`
* `nc`
* `tcpdump`
* NetworkManager
* Network namespaces
* veth pairs
* Linux bridges
* Linux firewall
* Docker networking
* Kubernetes networking
* Network troubleshooting

The most important DevOps lesson is:

> **When a service cannot communicate, troubleshoot from the network interface upward instead of guessing.**
