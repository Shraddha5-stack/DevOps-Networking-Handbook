# Linux Networking — Interview Questions & Answers

## 📌 Introduction

Linux networking is an important skill for DevOps, Cloud, SRE, and System Administration roles.

This document contains:

* Linux networking fundamentals
* Important commands
* IP addressing
* Routing
* DNS
* Ports
* TCP/UDP
* Network troubleshooting
* Network namespaces
* veth
* Docker networking
* Kubernetes networking
* Real-world DevOps scenarios

---

# 🟢 Beginner-Level Questions

## 1. What is Linux networking?

Linux networking is the set of features and tools used by Linux to communicate with other systems over a network.

It includes:

* Network interfaces
* IP addresses
* MAC addresses
* Routing
* DNS
* TCP/UDP
* Ports
* Firewalls
* Network namespaces
* Packet capture

---

## 2. How do you check network interfaces in Linux?

Use:

```bash
ip link
```

or:

```bash
ip addr
```

`ip link` mainly shows interfaces and their state, while `ip addr` also shows IP addresses.

---

## 3. How do you check the IP address?

```bash
ip addr
```

IPv4:

```bash
ip -4 addr
```

IPv6:

```bash
ip -6 addr
```

Another simple command:

```bash
hostname -I
```

---

## 4. What is a network interface?

A network interface is a software or hardware interface through which a system sends and receives network traffic.

Examples:

```text
eth0
ens33
wlo1
lo
docker0
```

---

## 5. What is the loopback interface?

The loopback interface allows a system to communicate with itself.

The standard loopback address is:

```text
127.0.0.1
```

Interface:

```text
lo
```

Test it:

```bash
ping -c 4 127.0.0.1
```

---

## 6. What is a MAC address?

A MAC address is a Layer 2 hardware/link-layer address associated with a network interface.

Example:

```text
52:54:00:12:34:56
```

Check it:

```bash
ip link
```

---

## 7. What is an IP address?

An IP address identifies a device or network interface at the network layer.

Example IPv4 address:

```text
192.168.1.10
```

IPv6 example:

```text
2001:db8::10
```

---

## 8. What is the difference between private and public IP addresses?

### Private IP

Used inside private networks.

Common IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

### Public IP

A publicly routable address used to communicate across the internet.

---

## 9. How do you check the routing table?

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1
```

---

## 10. What is a default gateway?

A default gateway is the router used when the destination does not match a more specific route in the routing table.

Check it:

```bash
ip route | grep default
```

---

# 🟡 Intermediate-Level Questions

## 11. What is routing?

Routing is the process of determining where network packets should be sent to reach their destination.

Linux uses the routing table to make this decision.

Check:

```bash
ip route
```

---

## 12. How does Linux decide where to send a packet?

Linux examines the destination IP and performs a route lookup.

For example:

```bash
ip route get 8.8.8.8
```

The output can show:

```text
8.8.8.8 via 192.168.1.1 dev wlo1
```

This tells us the selected gateway and interface.

---

## 13. What is ARP?

ARP stands for Address Resolution Protocol.

In IPv4 networks, ARP is used to discover the MAC address associated with an IP address on the local network.

Check the neighbour table:

```bash
ip neigh
```

---

## 14. What is the Linux neighbour table?

It stores information about neighbouring systems, including link-layer addresses.

Check:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr xx:xx:xx:xx:xx:xx REACHABLE
```

---

## 15. What is DNS?

DNS stands for Domain Name System.

It translates domain names into IP addresses.

Example:

```text
google.com
     ↓
IP address
```

Test:

```bash
dig google.com
```

---

## 16. How do you troubleshoot DNS problems?

I would check:

```bash
getent hosts google.com
```

Then:

```bash
dig google.com
```

Then:

```bash
cat /etc/resolv.conf
```

I would also compare direct DNS queries:

```bash
dig @8.8.8.8 google.com
```

---

## 17. What is `/etc/hosts`?

`/etc/hosts` provides local hostname-to-IP mappings.

Example:

```text
127.0.0.1 localhost
192.168.1.10 server1
```

Check:

```bash
cat /etc/hosts
```

---

## 18. What is `/etc/resolv.conf`?

It contains DNS resolver configuration used by the system.

Check:

```bash
cat /etc/resolv.conf
```

It may contain nameserver entries such as:

```text
nameserver 8.8.8.8
```

---

## 19. What is `/etc/nsswitch.conf`?

It controls how Linux performs several types of name and information lookups.

For hostname resolution, the `hosts` entry can define the lookup order.

Check:

```bash
cat /etc/nsswitch.conf
```

---

## 20. What is a port?

A port is a logical endpoint used to identify network services on a host.

Examples:

| Port | Common Service          |
| ---: | ----------------------- |
|   22 | SSH                     |
|   53 | DNS                     |
|   80 | HTTP                    |
|  443 | HTTPS                   |
| 3306 | MySQL                   |
| 5432 | PostgreSQL              |
| 8080 | Common application port |

---

## 21. How do you check listening ports?

Use:

```bash
sudo ss -lntup
```

For TCP only:

```bash
sudo ss -lntp
```

---

## 22. What does `LISTEN` mean?

`LISTEN` means a TCP socket is waiting for incoming connections.

Example:

```text
LISTEN 0 128 0.0.0.0:8080
```

An application is waiting for TCP connections on port 8080.

---

## 23. What is the difference between `127.0.0.1` and `0.0.0.0`?

`127.0.0.1` means localhost.

A service bound to:

```text
127.0.0.1:8080
```

normally accepts connections only through the local host interface.

A service bound to:

```text
0.0.0.0:8080
```

listens on all IPv4 interfaces.

---

## 24. How do you find which process is using a port?

Using `ss`:

```bash
sudo ss -lntp | grep :8080
```

Using `lsof`:

```bash
sudo lsof -i :8080
```

---

## 25. What is `ping`?

`ping` is used to test IP-level reachability using ICMP Echo Request and Echo Reply messages.

Example:

```bash
ping -c 4 8.8.8.8
```

---

## 26. Does ping test whether an application is working?

No.

A successful ping generally shows IP-level reachability, but it does not prove that a particular TCP port or application is working.

For example:

```bash
ping server
```

does not prove:

```text
TCP 443
HTTP
Application
```

are working.

---

## 27. What is `traceroute` or `tracepath`?

These tools help identify the network path between the local system and a destination.

Example:

```bash
tracepath google.com
```

or:

```bash
traceroute google.com
```

---

## 28. What is `ss`?

`ss` stands for socket statistics.

It is used to inspect:

* Listening ports
* TCP connections
* UDP sockets
* Network sockets
* Connection states

Example:

```bash
ss -tuln
```

---

## 29. What is `netstat`?

`netstat` is an older networking utility.

It can display:

* Network connections
* Routing tables
* Listening ports
* Interface statistics

Modern Linux systems generally prefer:

```bash
ss
```

---

## 30. What is `curl` used for in networking?

`curl` is commonly used to test HTTP/HTTPS endpoints and APIs.

Example:

```bash
curl https://example.com
```

Check headers:

```bash
curl -I https://example.com
```

Verbose mode:

```bash
curl -v https://example.com
```

---

# 🟠 Advanced Questions

## 31. What is TCP?

TCP stands for Transmission Control Protocol.

It is:

* Connection-oriented
* Reliable
* Ordered
* Designed for reliable byte-stream delivery

Common applications include:

* HTTP/HTTPS
* SSH
* Database connections

---

## 32. What is UDP?

UDP stands for User Datagram Protocol.

It is:

* Connectionless
* Lightweight
* Faster in many use cases
* Does not provide TCP-style delivery guarantees

Common uses include:

* DNS
* Streaming
* VoIP
* Gaming
* Some monitoring protocols

---

## 33. TCP vs UDP?

| TCP                    | UDP                                 |
| ---------------------- | ----------------------------------- |
| Connection-oriented    | Connectionless                      |
| Reliable delivery      | No TCP-style reliability            |
| Ordered stream         | Datagram based                      |
| More protocol overhead | Lower overhead                      |
| HTTP/HTTPS, SSH        | DNS and many real-time applications |

---

## 34. Explain the TCP three-way handshake.

The TCP connection establishment process is:

```text
Client                    Server

  SYN  -------------------->
       <-------------------- SYN-ACK
  ACK  -------------------->
```

After this, the TCP connection can carry application data.

---

## 35. What is `nc`?

`nc` or netcat is a networking utility used for testing TCP/UDP connections and transferring data.

Test a port:

```bash
nc -vz example.com 443
```

Test localhost:

```bash
nc -vz 127.0.0.1 8080
```

---

## 36. What is `tcpdump`?

`tcpdump` is a command-line packet analyzer.

Example:

```bash
sudo tcpdump -i any
```

Capture HTTP test traffic:

```bash
sudo tcpdump -i any port 8080
```

Capture ICMP:

```bash
sudo tcpdump -i any icmp
```

---

## 37. How do you capture packets into a file?

```bash
sudo tcpdump -i any -w capture.pcap
```

Read the capture:

```bash
tcpdump -r capture.pcap
```

---

## 38. How would you troubleshoot a slow network?

I would check:

```bash
ip -s link
```

for errors and dropped packets.

Then:

```bash
ping
```

for latency and packet loss.

Then:

```bash
tracepath
```

for the network path.

Then:

```bash
ss
```

for connection state.

Finally:

```bash
tcpdump
```

for packet-level analysis.

I would also check CPU, memory, disk I/O, application logs, and network device metrics.

---

## 39. How would you troubleshoot a connection refused error?

I would check whether the application is listening:

```bash
sudo ss -lntp | grep :8080
```

Then test:

```bash
nc -vz 127.0.0.1 8080
```

Then check:

```bash
systemctl status <service>
```

and:

```bash
journalctl -u <service>
```

If necessary, I would inspect firewall rules and packet captures.

---

## 40. How would you troubleshoot a connection timeout?

I would check:

1. IP address
2. Routing
3. Gateway
4. Firewall
5. Security groups
6. Network ACLs
7. Service availability
8. Packet capture

Useful commands:

```bash
ip addr
ip route
ping <host>
nc -vz <host> <port>
sudo ss -lntup
sudo tcpdump -i any
```

---

# 🔴 DevOps Scenario-Based Questions

## 41. A server has internet access by IP but not by hostname. What is wrong?

This strongly suggests a DNS resolution problem.

I would test:

```bash
ping -c 4 8.8.8.8
```

Then:

```bash
getent hosts google.com
```

Then:

```bash
dig google.com
```

Then inspect:

```bash
cat /etc/resolv.conf
```

---

## 42. An application works on localhost but not from another machine. What would you check?

First check the listening address:

```bash
sudo ss -lntp | grep :8080
```

If it shows:

```text
127.0.0.1:8080
```

the application is restricted to localhost.

I would then check:

* Application bind address
* Firewall
* Cloud security group
* Network ACL
* Routing
* Load balancer
* Container port mapping

---

## 43. An application is listening on port 8080, but users cannot connect. What would you check?

I would check:

```bash
sudo ss -lntp | grep :8080
```

Then:

```bash
nc -vz <server-ip> 8080
```

Then:

```bash
sudo ufw status
```

Then investigate:

```text
Cloud Security Group
Network ACL
Load Balancer
Routing
Application configuration
Container networking
Kubernetes Service
```

---

## 44. How would you troubleshoot HTTP 502 Bad Gateway?

A 502 generally indicates that a proxy or gateway could not get a valid response from its upstream.

I would check:

```text
Client
  ↓
Load Balancer / Reverse Proxy
  ↓
Application
  ↓
Backend
```

Then verify:

```bash
curl -v http://backend:port
```

Check listening ports:

```bash
ss -lntp
```

Check application logs:

```bash
journalctl -u <service>
```

Also inspect reverse-proxy and load-balancer logs.

---

## 45. How would you troubleshoot HTTP 504 Gateway Timeout?

A 504 commonly indicates that a gateway/proxy waited too long for an upstream response.

I would check:

* Application response time
* Backend availability
* Network connectivity
* Firewall
* Routing
* DNS
* Load balancer timeout
* Reverse proxy timeout
* Database latency

Useful tests:

```bash
curl -v http://backend:port
```

```bash
nc -vz backend port
```

```bash
ping backend
```

---

# 🐳 Docker Networking Questions

## 46. What networking does Docker use?

Docker commonly uses:

* Network namespaces
* Virtual Ethernet pairs
* Linux bridges
* NAT
* Routing

---

## 47. How do you list Docker networks?

```bash
docker network ls
```

---

## 48. How do you inspect a Docker network?

```bash
docker network inspect bridge
```

---

## 49. What is the Docker bridge network?

The default Docker bridge network provides networking for containers connected to it.

On the host, you commonly see:

```bash
ip addr show docker0
```

Conceptually:

```text
Host
 |
docker0 bridge
 |
Container
```

---

## 50. How do you check a container's network configuration?

```bash
docker inspect <container>
```

You can also retrieve the container IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>
```

---

## 51. What does `-p 8080:80` mean in Docker?

Example:

```bash
docker run -d -p 8080:80 nginx
```

It maps:

```text
Host port 8080
      ↓
Container port 80
```

Users connect to:

```text
host:8080
```

and traffic is forwarded to port 80 inside the container.

---

# ☸️ Kubernetes Networking Questions

## 52. How does Kubernetes networking work at a high level?

Kubernetes provides networking for:

* Pod-to-Pod communication
* Pod-to-Service communication
* Service-to-Pod communication
* External-to-Service communication
* DNS-based service discovery

---

## 53. What is a Pod IP?

A Pod normally receives an IP address from the cluster's Pod network.

Check:

```bash
kubectl get pods -o wide
```

---

## 54. What is a Kubernetes Service?

A Service provides a stable network endpoint for a group of Pods.

It allows clients to communicate with Pods without depending on individual Pod IPs.

---

## 55. Why do we need Kubernetes Services?

Pod IPs can change when Pods are recreated.

A Service provides a stable endpoint.

Conceptually:

```text
Client
  |
  v
Service
  |
  +---- Pod
  |
  +---- Pod
  |
  +---- Pod
```

---

## 56. How do you check Kubernetes Services?

```bash
kubectl get svc
```

Detailed information:

```bash
kubectl describe svc <service-name>
```

---

## 57. How do you check Service endpoints?

```bash
kubectl get endpoints
```

Or:

```bash
kubectl get endpointslices
```

---

## 58. How do you test Kubernetes DNS?

From a Pod:

```bash
nslookup <service-name>
```

For example:

```bash
nslookup nginx-service
```

---

## 59. What is Kubernetes DNS used for?

Kubernetes DNS provides service discovery.

Instead of directly using a changing Pod IP, applications can use a Service DNS name.

Conceptually:

```text
Application
     |
     v
nginx-service
     |
     v
Kubernetes DNS
     |
     v
Service IP
     |
     v
Pod
```

---

## 60. How do you inspect networking inside a Pod?

Run:

```bash
kubectl exec -it <pod> -- ip addr
```

Routes:

```bash
kubectl exec -it <pod> -- ip route
```

DNS:

```bash
kubectl exec -it <pod> -- cat /etc/resolv.conf
```

---

# 🧠 Network Namespace Questions

## 61. What is a network namespace?

A network namespace provides an isolated network environment.

It can have its own:

* Network interfaces
* IP addresses
* Routing table
* ARP/neighbour table
* Ports
* Network configuration

---

## 62. How do you create a network namespace?

```bash
sudo ip netns add lab-ns
```

List:

```bash
ip netns list
```

---

## 63. How do you execute a command inside a namespace?

```bash
sudo ip netns exec lab-ns ip addr
```

---

## 64. What is a veth pair?

A veth pair is a pair of virtual Ethernet devices connected together like a virtual cable.

Example:

```text
Host
 |
veth-host
 |
=========
 |
veth-ns
 |
Namespace
```

---

## 65. Why are network namespaces important in DevOps?

They are fundamental to container networking.

Containers commonly use isolated network namespaces, while virtual interfaces connect those namespaces to bridges and other networking components.

---

# 🔥 Important Troubleshooting Questions

## 66. What commands do you use first when troubleshooting networking?

My basic sequence is:

```bash
ip addr
ip route
ip neigh
ping
getent hosts
dig
ss
nc
curl
tcpdump
```

---

## 67. What is your Linux network troubleshooting methodology?

I follow a layered approach:

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
6. TCP port
       ↓
7. Firewall
       ↓
8. HTTP/HTTPS
       ↓
9. Application
```

This prevents randomly changing configurations.

---

## 68. What would you check if a server cannot reach another server?

I would check:

```bash
ip addr
ip route
ping <destination>
```

Then:

```bash
nc -vz <destination> <port>
```

Then:

```bash
sudo tcpdump -i any
```

I would also investigate firewall rules and cloud networking.

---

## 69. How do you troubleshoot packet loss?

First:

```bash
ping -c 20 <destination>
```

Then:

```bash
ip -s link
```

Then:

```bash
tracepath <destination>
```

Then capture traffic:

```bash
sudo tcpdump -i any icmp
```

I would also check interface errors, network congestion, MTU, routing, and intermediate network devices.

---

## 70. What is MTU?

MTU stands for Maximum Transmission Unit.

It defines the largest packet size that can normally be transmitted over a network interface without fragmentation at that layer.

Check:

```bash
ip link
```

You may see:

```text
mtu 1500
```

---

# 💻 Practical Command Round

## 71. Show all IP addresses

```bash
ip addr
```

## 72. Show routing table

```bash
ip route
```

## 73. Show neighbour table

```bash
ip neigh
```

## 74. Show listening ports

```bash
sudo ss -lntup
```

## 75. Test DNS

```bash
dig google.com
```

## 76. Test TCP port

```bash
nc -vz <host> <port>
```

## 77. Test HTTP

```bash
curl -v http://<host>:<port>
```

## 78. Capture packets

```bash
sudo tcpdump -i any
```

## 79. Check interface statistics

```bash
ip -s link
```

## 80. Check firewall

```bash
sudo ufw status
```

---

# 🎯 Real-World DevOps Scenario

## Scenario

A production web application is not accessible.

You are given:

```text
URL:
https://example.com
```

### Step 1 — DNS

```bash
dig example.com
```

Check whether DNS returns the expected address.

### Step 2 — Network connectivity

```bash
ping <resolved-ip>
```

Remember that ICMP may be blocked, so ping failure alone does not prove the server is down.

### Step 3 — TCP

```bash
nc -vz <resolved-ip> 443
```

### Step 4 — HTTPS

```bash
curl -v https://example.com
```

### Step 5 — TLS

```bash
openssl s_client -connect example.com:443
```

### Step 6 — Server

On the server:

```bash
sudo ss -lntp | grep :443
```

### Step 7 — Firewall

```bash
sudo ufw status
```

### Step 8 — Packet capture

```bash
sudo tcpdump -i any port 443
```

### Step 9 — Application logs

Check the web server, reverse proxy, and application logs.

---

# 🏆 Top 20 Commands to Memorize

```bash
ip addr
ip link
ip route
ip route get <destination>
ip neigh
ping <host>
tracepath <host>
getent hosts <host>
dig <host>
cat /etc/resolv.conf
ss -lntup
sudo lsof -i :<port>
nc -vz <host> <port>
curl -v <url>
wget <url>
tcpdump
ip -s link
nmcli
docker network ls
kubectl get pods -o wide
```

---

# 🎤 Interview Answer Template

When an interviewer asks:

> "How do you troubleshoot a networking issue in Linux?"

A strong answer is:

**"First, I check the network interface and IP address using `ip addr`. Then I check the routing table using `ip route` and verify the default gateway. I test connectivity with `ping`, and if the issue appears to be DNS-related, I use `getent` or `dig`. For application connectivity, I check listening ports with `ss` and test the TCP port using `nc`. I then test the application using `curl`. If the problem is still unclear, I use `tcpdump` to inspect packets. Finally, I check firewall rules, service logs, and cloud or Kubernetes networking components depending on the environment."**

---

# 🧠 Final Revision Map

```text
                 Linux Networking
                        |
        +---------------+---------------+
        |               |               |
     Interface        Routing           DNS
        |               |               |
     ip link         ip route           dig
     ip addr         gateway            getent
        |
        +-------------------------------+
        |
      Connectivity
        |
     ping / tracepath
        |
        +-------------------------------+
        |
       Ports
        |
      ss / nc / lsof
        |
        +-------------------------------+
        |
     Applications
        |
      curl / wget
        |
        +-------------------------------+
        |
     Packet Analysis
        |
      tcpdump
        |
        +-------------------------------+
        |
    Container Networking
        |
   Docker / Namespaces
        |
        +-------------------------------+
        |
   Kubernetes Networking
        |
   Pod / Service / DNS
```

---

# ✅ Chapter 29 Interview Preparation Checklist

* [ ] Explain Linux networking
* [ ] Explain network interfaces
* [ ] Explain IP addresses
* [ ] Explain MAC addresses
* [ ] Explain routing
* [ ] Explain default gateway
* [ ] Explain ARP
* [ ] Explain DNS
* [ ] Explain ports
* [ ] Explain TCP vs UDP
* [ ] Explain TCP handshake
* [ ] Use `ip`
* [ ] Use `ping`
* [ ] Use `dig`
* [ ] Use `ss`
* [ ] Use `nc`
* [ ] Use `curl`
* [ ] Use `tcpdump`
* [ ] Troubleshoot DNS
* [ ] Troubleshoot connection refused
* [ ] Troubleshoot timeout
* [ ] Troubleshoot packet loss
* [ ] Explain network namespaces
* [ ] Explain veth pairs
* [ ] Explain Docker networking
* [ ] Explain Kubernetes networking
* [ ] Explain Kubernetes Services
* [ ] Explain Kubernetes DNS
* [ ] Explain a complete network troubleshooting flow
