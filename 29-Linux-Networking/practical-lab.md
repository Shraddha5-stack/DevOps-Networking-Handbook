# 🧪 Linux Networking — Practical Lab

## 📌 Objective

In this practical lab, we will practice Linux networking from basic to advanced concepts.

We will work with:

1. Network interfaces
2. IP addresses
3. MAC addresses
4. Routing
5. Default gateway
6. ARP/neighbour table
7. DNS
8. Ping
9. Tracepath
10. Ports and sockets
11. Local HTTP server
12. `curl`
13. `nc`
14. `tcpdump`
15. Network namespaces
16. veth pairs
17. Linux bridge concepts
18. Firewall inspection
19. Docker networking
20. Kubernetes networking
21. Network troubleshooting

---

# 1. Check Your Network Interfaces

Run:

```bash
ip link
```

Short form:

```bash
ip l
```

### Expected

You should see interfaces such as:

```text
lo
wlo1
docker0
```

The exact interface names depend on your system.

### Understand

| Interface | Purpose                    |
| --------- | -------------------------- |
| `lo`      | Loopback                   |
| `wlo1`    | Wireless interface example |
| `eth0`    | Ethernet interface example |
| `docker0` | Docker bridge              |
| `veth*`   | Virtual Ethernet           |

---

# 2. Check IP Addresses

Run:

```bash
ip addr
```

or:

```bash
ip a
```

IPv4 only:

```bash
ip -4 addr
```

IPv6 only:

```bash
ip -6 addr
```

Find your IP:

```bash
hostname -I
```

Example:

```text
192.168.1.5
```

---

# 3. Identify Your Active Interface

Run:

```bash
ip route
```

Look for:

```text
default via 192.168.1.1 dev wlo1
```

Here:

```text
default
   |
   +---- gateway: 192.168.1.1
   |
   +---- interface: wlo1
```

Find only the active interface:

```bash
ip route | awk '/default/ {print $5}'
```

---

# 4. Check MAC Address

Run:

```bash
ip link
```

Look for:

```text
link/ether xx:xx:xx:xx:xx:xx
```

You can also run:

```bash
cat /sys/class/net/$(ip route | awk '/default/ {print $5}')/address
```

---

# 5. Check the Routing Table

Run:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1
172.17.0.0/16 dev docker0
```

### Understand

```text
Destination       Gateway        Interface
------------------------------------------------
default           192.168.1.1    wlo1
192.168.1.0/24    directly       wlo1
172.17.0.0/16     directly       docker0
```

---

# 6. Find the Route to a Destination

Run:

```bash
ip route get 8.8.8.8
```

Example:

```text
8.8.8.8 via 192.168.1.1 dev wlo1
```

This tells Linux:

```text
Destination
     |
     v
8.8.8.8
     |
     v
Gateway
192.168.1.1
     |
     v
Interface
wlo1
```

---

# 7. Test Your Loopback Interface

Run:

```bash
ping -c 4 127.0.0.1
```

Also:

```bash
ping -c 4 localhost
```

Expected:

```text
4 packets transmitted
4 received
0% packet loss
```

### What does this test?

It checks whether local networking and the loopback interface are functioning.

---

# 8. Test Your Default Gateway

First find the gateway:

```bash
ip route | awk '/default/ {print $3}'
```

Suppose it returns:

```text
192.168.1.1
```

Test it:

```bash
ping -c 4 192.168.1.1
```

Or automatically:

```bash
ping -c 4 "$(ip route | awk '/default/ {print $3}')"
```

---

# 9. Test Internet Connectivity

Test an IP:

```bash
ping -c 4 8.8.8.8
```

Then test a hostname:

```bash
ping -c 4 google.com
```

### Important observation

If:

```bash
ping -c 4 8.8.8.8
```

works but:

```bash
ping -c 4 google.com
```

fails,

there may be a DNS resolution problem.

---

# 10. Test DNS

Run:

```bash
getent hosts google.com
```

Then:

```bash
dig google.com
```

Short output:

```bash
dig +short google.com
```

If `dig` is not installed:

```bash
sudo apt update
sudo apt install dnsutils
```

Then:

```bash
dig +short google.com
```

---

# 11. Check DNS Configuration

Run:

```bash
cat /etc/resolv.conf
```

Also inspect:

```bash
cat /etc/hosts
```

And:

```bash
cat /etc/nsswitch.conf
```

### Understand

A simplified resolution path can involve:

```text
Application
     |
     v
Name Service Switch
/etc/nsswitch.conf
     |
     +---- /etc/hosts
     |
     +---- DNS
             |
             v
       DNS Resolver
```

---

# 12. Test Different DNS Servers

Google DNS:

```bash
dig @8.8.8.8 google.com
```

Cloudflare DNS:

```bash
dig @1.1.1.1 google.com
```

Short result:

```bash
dig +short @8.8.8.8 google.com
```

---

# 13. Reverse DNS Lookup

Run:

```bash
dig -x 8.8.8.8
```

This asks:

```text
IP Address
    |
    v
Reverse DNS
    |
    v
Hostname
```

---

# 14. Inspect the ARP/Neighbour Table

Run:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr xx:xx:xx:xx:xx:xx REACHABLE
```

The neighbour table maps local IP information to link-layer information such as MAC addresses.

---

# 15. Check Network Statistics

Run:

```bash
ip -s link
```

Look for:

```text
RX packets
RX errors
RX dropped

TX packets
TX errors
TX dropped
```

This is useful when investigating:

* Packet loss
* Interface errors
* Dropped packets
* Network performance problems

---

# 16. Check Open Ports

Run:

```bash
sudo ss -lntup
```

Example:

```text
LISTEN 0 128 0.0.0.0:22
LISTEN 0 128 127.0.0.1:3306
```

Understand:

```text
0.0.0.0:22
```

means the service is listening on all IPv4 interfaces.

Whereas:

```text
127.0.0.1:3306
```

means it is listening only on the local machine.

---

# 17. Check a Specific Port

Check port 22:

```bash
sudo ss -lntp | grep :22
```

Check port 80:

```bash
sudo ss -lntp | grep :80
```

Check port 8080:

```bash
sudo ss -lntp | grep :8080
```

---

# 18. Find Process Using a Port

Install `lsof` if necessary:

```bash
sudo apt update
sudo apt install lsof
```

Find port 8080:

```bash
sudo lsof -i :8080
```

Alternative:

```bash
sudo ss -lntp | grep :8080
```

---

# 19. Test a TCP Port

Use netcat:

```bash
nc -vz google.com 443
```

Test localhost:

```bash
nc -vz 127.0.0.1 22
```

If you have a local application on port 8080:

```bash
nc -vz 127.0.0.1 8080
```

---

# 20. Create a Local HTTP Server

Python provides a simple HTTP server for testing.

Create a directory:

```bash
mkdir -p ~/linux-networking-lab
cd ~/linux-networking-lab
```

Create a test file:

```bash
echo "Linux Networking Lab" > index.html
```

Start server:

```bash
python3 -m http.server 8080
```

You should see something similar to:

```text
Serving HTTP on 0.0.0.0 port 8080
```

Keep this terminal running.

---

# 21. Test the HTTP Server

Open another terminal.

Run:

```bash
curl http://127.0.0.1:8080
```

Expected:

```text
Linux Networking Lab
```

Check headers:

```bash
curl -I http://127.0.0.1:8080
```

Verbose:

```bash
curl -v http://127.0.0.1:8080
```

---

# 22. Check the Listening Port

While Python is running:

```bash
sudo ss -lntp | grep :8080
```

You should see a listener.

You can also use:

```bash
sudo lsof -i :8080
```

---

# 23. Test with Netcat

Run:

```bash
nc -vz 127.0.0.1 8080
```

Expected:

```text
Connection to 127.0.0.1 8080 port [tcp/*] succeeded!
```

---

# 24. Observe Traffic with tcpdump

Find interfaces:

```bash
sudo tcpdump -D
```

Capture traffic:

```bash
sudo tcpdump -i any port 8080
```

In another terminal:

```bash
curl http://127.0.0.1:8080
```

Then stop tcpdump:

```text
Ctrl + C
```

---

# 25. Capture Only TCP Traffic

Run:

```bash
sudo tcpdump -i any tcp port 8080
```

Then:

```bash
curl http://127.0.0.1:8080
```

You may observe packets associated with:

```text
TCP connection
SYN
SYN-ACK
ACK
HTTP request
HTTP response
FIN
```

---

# 26. Capture ICMP Traffic

Start:

```bash
sudo tcpdump -i any icmp
```

In another terminal:

```bash
ping -c 4 8.8.8.8
```

Observe the ICMP packets.

Stop:

```text
Ctrl + C
```

---

# 27. Capture DNS Traffic

Run:

```bash
sudo tcpdump -i any port 53
```

In another terminal:

```bash
dig google.com
```

Stop:

```text
Ctrl + C
```

---

# 28. Save a Packet Capture

Run:

```bash
sudo tcpdump -i any port 8080 -w linux-networking.pcap
```

Generate traffic:

```bash
curl http://127.0.0.1:8080
```

Stop:

```text
Ctrl + C
```

Check the file:

```bash
ls -lh linux-networking.pcap
```

Read it:

```bash
tcpdump -r linux-networking.pcap
```

---

# 29. Network Namespace Lab

Network namespaces provide isolated network environments.

Create:

```bash
sudo ip netns add lab-ns
```

Check:

```bash
ip netns list
```

Expected:

```text
lab-ns
```

---

# 30. Inspect the New Namespace

Run:

```bash
sudo ip netns exec lab-ns ip addr
```

You will normally see only the namespace's loopback interface.

Check:

```bash
sudo ip netns exec lab-ns ip route
```

---

# 31. Enable Loopback in Namespace

```bash
sudo ip netns exec lab-ns ip link set lo up
```

Test:

```bash
sudo ip netns exec lab-ns ping -c 2 127.0.0.1
```

---

# 32. Create a veth Pair

Create:

```bash
sudo ip link add veth-host type veth peer name veth-ns
```

Check:

```bash
ip link
```

You should see:

```text
veth-host
veth-ns
```

A veth pair behaves like a virtual cable:

```text
Host
 |
veth-host
 |
======== virtual cable ========
 |
veth-ns
 |
Namespace
```

---

# 33. Move One veth Interface into Namespace

```bash
sudo ip link set veth-ns netns lab-ns
```

Check host:

```bash
ip link
```

Check namespace:

```bash
sudo ip netns exec lab-ns ip link
```

---

# 34. Configure Host Side

Assign an IP:

```bash
sudo ip addr add 10.10.0.1/24 dev veth-host
```

Bring it up:

```bash
sudo ip link set veth-host up
```

Verify:

```bash
ip addr show veth-host
```

---

# 35. Configure Namespace Side

Bring loopback up:

```bash
sudo ip netns exec lab-ns ip link set lo up
```

Assign IP:

```bash
sudo ip netns exec lab-ns ip addr add 10.10.0.2/24 dev veth-ns
```

Bring interface up:

```bash
sudo ip netns exec lab-ns ip link set veth-ns up
```

Verify:

```bash
sudo ip netns exec lab-ns ip addr
```

---

# 36. Test Host-to-Namespace Connectivity

From the host:

```bash
ping -c 4 10.10.0.2
```

Expected:

```text
4 packets transmitted
4 received
0% packet loss
```

Now test from the namespace:

```bash
sudo ip netns exec lab-ns ping -c 4 10.10.0.1
```

You have now created communication between:

```text
Host
10.10.0.1
   |
   | veth pair
   |
10.10.0.2
Namespace
```

---

# 37. Run a Server Inside the Namespace

Run:

```bash
sudo ip netns exec lab-ns python3 -m http.server 8080 --bind 10.10.0.2
```

Keep it running.

From the host, open another terminal:

```bash
curl http://10.10.0.2:8080
```

This demonstrates application communication between a host and a network namespace.

---

# 38. Check Namespace Port

Run:

```bash
sudo ip netns exec lab-ns ss -lntp
```

You should see port:

```text
10.10.0.2:8080
```

---

# 39. Capture Namespace Traffic

On the host:

```bash
sudo tcpdump -i veth-host port 8080
```

Then:

```bash
curl http://10.10.0.2:8080
```

Observe the traffic.

---

# 40. Cleanup Namespace Lab

Stop the Python server with:

```text
Ctrl + C
```

Delete the namespace:

```bash
sudo ip netns delete lab-ns
```

Verify:

```bash
ip netns list
```

The namespace should no longer appear.

---

# 41. Docker Networking Lab

Check Docker:

```bash
docker version
```

List networks:

```bash
docker network ls
```

You may see:

```text
bridge
host
none
```

---

# 42. Inspect Docker Bridge

Run:

```bash
ip addr show docker0
```

Then:

```bash
docker network inspect bridge
```

Look for:

```text
Subnet
Gateway
Containers
IP addresses
```

---

# 43. Run a Docker Container

Run nginx:

```bash
docker run -d --name networking-nginx -p 8080:80 nginx
```

Check:

```bash
docker ps
```

Test:

```bash
curl http://127.0.0.1:8080
```

---

# 44. Check Docker Port Mapping

Run:

```bash
docker port networking-nginx
```

Expected output will show the container's port 80 mapped to the host's port 8080.

Also:

```bash
sudo ss -lntp | grep :8080
```

---

# 45. Inspect Docker Container Networking

Run:

```bash
docker inspect networking-nginx
```

Or:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' networking-nginx
```

---

# 46. Inspect Docker Network

```bash
docker network inspect bridge
```

Understand:

```text
Host
 |
docker0 bridge
 |
Container
 |
eth0
```

Docker uses Linux networking primitives such as:

* Network namespaces
* Virtual Ethernet interfaces
* Bridges
* Routing
* NAT

---

# 47. Docker Cleanup

Stop:

```bash
docker stop networking-nginx
```

Remove:

```bash
docker rm networking-nginx
```

Verify:

```bash
docker ps -a
```

---

# 48. Kubernetes Networking Lab

Check cluster:

```bash
kubectl get nodes
```

List pods:

```bash
kubectl get pods -A
```

Create a test namespace:

```bash
kubectl create namespace networking-lab
```

---

# 49. Create an Nginx Pod

```bash
kubectl run nginx \
  --image=nginx \
  --port=80 \
  -n networking-lab
```

Check:

```bash
kubectl get pods -n networking-lab -o wide
```

You should see the Pod IP.

---

# 50. Inspect the Pod Network

Run:

```bash
kubectl exec -n networking-lab nginx -- ip addr
```

Check routes:

```bash
kubectl exec -n networking-lab nginx -- ip route
```

Check DNS:

```bash
kubectl exec -n networking-lab nginx -- cat /etc/resolv.conf
```

---

# 51. Create a Kubernetes Service

```bash
kubectl expose pod nginx \
  --name=nginx-service \
  --port=80 \
  --target-port=80 \
  -n networking-lab
```

Check:

```bash
kubectl get svc -n networking-lab
```

---

# 52. Check Service Endpoints

```bash
kubectl get endpoints -n networking-lab
```

If supported by your Kubernetes version:

```bash
kubectl get endpointslices -n networking-lab
```

The endpoint should point toward the Pod.

---

# 53. Test Kubernetes Service

Port-forward:

```bash
kubectl port-forward \
  -n networking-lab \
  svc/nginx-service 8080:80
```

Keep it running.

Open another terminal:

```bash
curl http://127.0.0.1:8080
```

You should receive the nginx response.

---

# 54. Test Networking from Inside a Pod

Open a shell:

```bash
kubectl exec -it -n networking-lab nginx -- sh
```

Inside:

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

Exit:

```bash
exit
```

---

# 55. Kubernetes DNS Test

Create a temporary diagnostic pod if your cluster does not have suitable networking tools:

```bash
kubectl run network-test \
  --image=busybox:1.36 \
  --restart=Never \
  -n networking-lab \
  -- sleep 3600
```

Check:

```bash
kubectl get pods -n networking-lab
```

Enter:

```bash
kubectl exec -it -n networking-lab network-test -- sh
```

Inside:

```bash
nslookup nginx-service
```

Then:

```bash
wget -qO- http://nginx-service
```

Exit:

```bash
exit
```

---

# 56. Kubernetes Pod-to-Service Flow

Understand the traffic:

```text
network-test Pod
      |
      | DNS lookup
      v
nginx-service
      |
      | Service routing
      v
nginx Pod
      |
      v
nginx container
```

---

# 57. Kubernetes Cleanup

Delete the test namespace:

```bash
kubectl delete namespace networking-lab
```

Verify:

```bash
kubectl get namespaces
```

---

# 58. Firewall Check

Check UFW:

```bash
sudo ufw status
```

Detailed:

```bash
sudo ufw status verbose
```

If UFW is inactive, do not enable it just for this lab unless you understand the effect on your system.

---

# 59. Complete Linux Network Health Check

Run:

```bash
echo "===== HOSTNAME ====="
hostname

echo "===== INTERFACES ====="
ip link

echo "===== IP ADDRESSES ====="
ip addr

echo "===== ROUTES ====="
ip route

echo "===== NEIGHBOURS ====="
ip neigh

echo "===== LISTENING PORTS ====="
sudo ss -lntup

echo "===== DNS ====="
getent hosts google.com

echo "===== INTERNET ====="
ping -c 2 8.8.8.8

echo "===== HTTPS ====="
curl -I --max-time 5 https://example.com
```

---

# 60. Troubleshooting Scenario 1 — No Internet

### Problem

You cannot access the internet.

### Step 1

Check interface:

```bash
ip link
```

### Step 2

Check IP:

```bash
ip addr
```

### Step 3

Check route:

```bash
ip route
```

### Step 4

Check gateway:

```bash
ping -c 4 "$(ip route | awk '/default/ {print $3}')"
```

### Step 5

Check internet IP:

```bash
ping -c 4 8.8.8.8
```

### Step 6

Check DNS:

```bash
getent hosts google.com
```

---

# 61. Troubleshooting Scenario 2 — DNS Failure

Test:

```bash
ping -c 4 8.8.8.8
```

If this works:

```bash
getent hosts google.com
```

If this fails:

```bash
dig google.com
```

Check:

```bash
cat /etc/resolv.conf
```

Compare DNS servers:

```bash
dig @8.8.8.8 google.com
```

and:

```bash
dig @1.1.1.1 google.com
```

---

# 62. Troubleshooting Scenario 3 — Application Port Not Working

Suppose application should run on port 8080.

Check:

```bash
sudo ss -lntp | grep :8080
```

If no output:

```text
Nothing is listening on port 8080.
```

Check application:

```bash
ps aux | grep <application>
```

Check service:

```bash
systemctl status <service>
```

Check logs:

```bash
journalctl -u <service>
```

---

# 63. Troubleshooting Scenario 4 — Localhost Works but Remote Does Not

Check binding:

```bash
sudo ss -lntp | grep :8080
```

If:

```text
127.0.0.1:8080
```

the application is bound only to localhost.

If the application is intended to be remotely reachable, configure it appropriately to listen on the required interface/address, often:

```text
0.0.0.0:8080
```

Then check firewall:

```bash
sudo ufw status
```

Also check:

```text
Cloud security group
Cloud network ACL
Load balancer
Routing
Application configuration
```

---

# 64. Troubleshooting Scenario 5 — HTTP Connection Refused

Run:

```bash
nc -vz 127.0.0.1 8080
```

Then:

```bash
curl -v http://127.0.0.1:8080
```

Check:

```bash
sudo ss -lntp | grep :8080
```

If the port is not listening, investigate the application.

---

# 65. Troubleshooting Scenario 6 — Packet Loss

Start:

```bash
ping -c 20 8.8.8.8
```

Then inspect:

```bash
ip -s link
```

Check path:

```bash
tracepath 8.8.8.8
```

Capture packets:

```bash
sudo tcpdump -i any icmp
```

Investigate:

```text
Interface errors
Packet drops
Routing
Gateway
Firewall
Network congestion
MTU
Remote endpoint
```

---

# 66. Troubleshooting Scenario 7 — TCP Connection Problem

Test:

```bash
nc -vz <host> <port>
```

Then:

```bash
sudo ss -ant
```

For packet-level analysis:

```bash
sudo tcpdump -i any host <host> and port <port>
```

Look for:

```text
SYN
SYN-ACK
ACK
RST
Retransmissions
```

---

# 67. DevOps Network Troubleshooting Flow

Use this order:

```text
              Application Problem
                      |
                      v
                 DNS Check
                      |
                      v
                IP Connectivity
                      |
                      v
                    Route
                      |
                      v
                  TCP Port
                      |
                      v
                  Firewall
                      |
                      v
                   HTTP
                      |
                      v
                  TLS/SSL
                      |
                      v
                Application
                      |
                      v
                 Database
```

Useful commands:

```bash
getent hosts <host>
dig <host>
ip addr
ip route
ping <host>
nc -vz <host> <port>
ss -lntup
curl -v <url>
openssl s_client -connect <host>:443
tcpdump
```

---

# 68. Final Practical Checklist

Complete each task:

* [ ] `ip link`
* [ ] `ip addr`
* [ ] `ip route`
* [ ] `ip route get`
* [ ] `ip neigh`
* [ ] `ping`
* [ ] `getent`
* [ ] `dig`
* [ ] `nslookup`
* [ ] `tracepath`
* [ ] `ss`
* [ ] `lsof`
* [ ] `nc`
* [ ] `curl`
* [ ] Python HTTP server
* [ ] `tcpdump`
* [ ] Packet capture
* [ ] Network namespace
* [ ] veth pair
* [ ] Namespace-to-host communication
* [ ] Docker bridge
* [ ] Docker container networking
* [ ] Kubernetes Pod IP
* [ ] Kubernetes Service
* [ ] Kubernetes DNS
* [ ] Kubernetes port-forward
* [ ] Firewall inspection
* [ ] Network troubleshooting

---

# 🎯 Interview Practice

After completing the lab, answer these without looking at your notes:

### 1. How do you check an IP address?

```bash
ip addr
```

### 2. How do you check the routing table?

```bash
ip route
```

### 3. How do you find the default gateway?

```bash
ip route | grep default
```

### 4. How do you check listening ports?

```bash
sudo ss -lntup
```

### 5. How do you find which process uses port 8080?

```bash
sudo lsof -i :8080
```

### 6. How do you test a TCP port?

```bash
nc -vz <host> <port>
```

### 7. How do you troubleshoot DNS?

```bash
getent hosts example.com
dig example.com
cat /etc/resolv.conf
```

### 8. How do you capture network packets?

```bash
sudo tcpdump -i any
```

### 9. What is a network namespace?

A network namespace provides an isolated network environment with its own interfaces, routes, neighbour table, and network configuration.

### 10. What is a veth pair?

A veth pair is a pair of virtual network interfaces that act like a virtual cable between network namespaces or networking components.

---

# 🧠 Final Revision

Remember:

```text
ip link    → Interfaces
ip addr    → IP addresses
ip route   → Routing
ip neigh   → ARP/Neighbours
ping       → Connectivity
dig        → DNS
ss         → Sockets/Ports
nc         → TCP/UDP connectivity testing
curl       → HTTP/API testing
tcpdump    → Packet capture
nmcli      → NetworkManager
ufw        → Firewall
ip netns   → Network namespaces
docker     → Container networking
kubectl    → Kubernetes networking
```

The core Linux networking troubleshooting sequence is:

```text
Interface
   ↓
IP Address
   ↓
Route
   ↓
Gateway
   ↓
DNS
   ↓
Port
   ↓
TCP
   ↓
HTTP/HTTPS
   ↓
Application
```

This sequence should become a daily DevOps troubleshooting habit.
