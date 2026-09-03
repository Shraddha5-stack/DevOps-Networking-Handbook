# 🐧 Linux Networking — Commands Reference

## 📌 Overview

This file contains commonly used Linux networking commands for:

* Network interface management
* IP addressing
* Routing
* DNS troubleshooting
* Ports and sockets
* Connectivity testing
* TCP/UDP troubleshooting
* Network namespaces
* Virtual Ethernet
* Linux bridges
* Packet capture
* Firewall inspection
* NetworkManager
* Docker networking
* Kubernetes networking
* DevOps troubleshooting

---

# 1. Check Linux Network Interfaces

## `ip link`

Displays network interfaces.

```bash
ip link
```

Short form:

```bash
ip l
```

Example output:

```text
1: lo: <LOOPBACK,UP,LOWER_UP>
2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP>
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP>
```

---

## Show a Specific Interface

```bash
ip link show wlo1
```

Example:

```bash
ip link show lo
```

---

## Bring an Interface Up

```bash
sudo ip link set eth0 up
```

Verify:

```bash
ip link show eth0
```

---

## Bring an Interface Down

```bash
sudo ip link set eth0 down
```

> ⚠️ Do not run this on your active remote interface unless you intentionally want to disconnect the system.

---

# 2. IP Address Commands

## Show All IP Addresses

```bash
ip addr
```

Short form:

```bash
ip a
```

---

## Show IPv4 Addresses

```bash
ip -4 addr
```

---

## Show IPv6 Addresses

```bash
ip -6 addr
```

---

## Show IP Address of One Interface

```bash
ip addr show wlo1
```

Example:

```bash
ip addr show lo
```

---

## Add an IP Address

Temporary configuration:

```bash
sudo ip addr add 192.168.1.50/24 dev eth0
```

Verify:

```bash
ip addr show eth0
```

---

## Remove an IP Address

```bash
sudo ip addr del 192.168.1.50/24 dev eth0
```

> These `ip` changes are generally runtime configuration and may not persist after reboot.

---

# 3. MAC Address

## Display MAC Addresses

```bash
ip link
```

Look for:

```text
link/ether aa:bb:cc:dd:ee:ff
```

---

## Show MAC Address of One Interface

```bash
ip link show wlo1
```

---

## Read MAC Address Directly

```bash
cat /sys/class/net/wlo1/address
```

---

# 4. Loopback

Check loopback:

```bash
ip addr show lo
```

Test:

```bash
ping -c 4 127.0.0.1
```

or:

```bash
ping -c 4 localhost
```

IPv6:

```bash
ping6 -c 4 ::1
```

---

# 5. Routing Commands

## Show Routing Table

```bash
ip route
```

Short form:

```bash
ip r
```

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1
```

---

## Show IPv4 Routes

```bash
ip -4 route
```

---

## Show IPv6 Routes

```bash
ip -6 route
```

---

## Find Route to a Destination

```bash
ip route get 8.8.8.8
```

Example:

```text
8.8.8.8 via 192.168.1.1 dev wlo1
```

This tells you which gateway and interface Linux would use.

---

## Add a Route

Example:

```bash
sudo ip route add 10.10.0.0/16 via 192.168.1.1
```

Verify:

```bash
ip route
```

---

## Delete a Route

```bash
sudo ip route del 10.10.0.0/16
```

> ⚠️ Routing changes can break connectivity. Understand the route before modifying it.

---

# 6. Default Gateway

Find the default gateway:

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

Extract only the gateway:

```bash
ip route | awk '/default/ {print $3}'
```

Test the gateway:

```bash
ping -c 4 192.168.1.1
```

---

# 7. ARP / Neighbour Commands

## Show Neighbour Table

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

---

## Show Neighbours for One Interface

```bash
ip neigh show dev wlo1
```

---

## Flush Neighbour Entries

```bash
sudo ip neigh flush dev wlo1
```

> Use carefully. The system will relearn neighbour information as needed.

---

# 8. DNS Commands

## Check `/etc/resolv.conf`

```bash
cat /etc/resolv.conf
```

---

## Check `/etc/hosts`

```bash
cat /etc/hosts
```

---

## Check Name Service Configuration

```bash
cat /etc/nsswitch.conf
```

---

## Resolve a Host Using `getent`

```bash
getent hosts google.com
```

Example:

```text
142.250.x.x google.com
```

---

## DNS Lookup Using `dig`

```bash
dig google.com
```

Short answer:

```bash
dig +short google.com
```

---

## Query a Specific DNS Server

```bash
dig @8.8.8.8 google.com
```

Another public resolver:

```bash
dig @1.1.1.1 google.com
```

---

## Check DNS Records

A record:

```bash
dig example.com A
```

AAAA record:

```bash
dig example.com AAAA
```

MX record:

```bash
dig example.com MX
```

NS record:

```bash
dig example.com NS
```

TXT record:

```bash
dig example.com TXT
```

---

## Reverse DNS Lookup

```bash
dig -x 8.8.8.8
```

---

## `nslookup`

Basic:

```bash
nslookup google.com
```

Specific DNS server:

```bash
nslookup google.com 8.8.8.8
```

---

# 9. Hostname Commands

## Show Hostname

```bash
hostname
```

---

## Detailed Hostname Information

```bash
hostnamectl
```

---

## Show FQDN

```bash
hostname -f
```

---

## Resolve Hostname

```bash
getent hosts $(hostname)
```

---

# 10. Connectivity Testing

## Ping a Host

```bash
ping google.com
```

---

## Send Four Packets

```bash
ping -c 4 google.com
```

---

## Ping an IP

```bash
ping -c 4 8.8.8.8
```

---

## Ping the Gateway

```bash
ping -c 4 192.168.1.1
```

---

## Test Localhost

```bash
ping -c 4 127.0.0.1
```

---

## Set Ping Timeout

```bash
ping -W 2 -c 4 google.com
```

---

# 11. Traceroute

Install:

```bash
sudo apt update
sudo apt install traceroute
```

Run:

```bash
traceroute google.com
```

---

## Trace to an IP

```bash
traceroute 8.8.8.8
```

---

# 12. `tracepath`

Often available without additional configuration:

```bash
tracepath google.com
```

Example:

```bash
tracepath 8.8.8.8
```

Useful for:

* Routing analysis
* Hop discovery
* MTU-related troubleshooting
* Network path investigation

---

# 13. Ports and Sockets

## Show Listening TCP Ports

```bash
ss -ltn
```

---

## Show Listening UDP Ports

```bash
ss -lun
```

---

## Show All Listening TCP/UDP Ports

```bash
ss -lntup
```

Use `sudo` to see more process information:

```bash
sudo ss -lntup
```

---

## Show Established Connections

```bash
ss -tn state established
```

---

## Show TCP Connections

```bash
ss -tn
```

---

## Show UDP Connections

```bash
ss -un
```

---

## Find Port 8080

```bash
sudo ss -lntp | grep :8080
```

---

## Find Port 22

```bash
sudo ss -lntp | grep :22
```

---

## Find HTTPS Port

```bash
sudo ss -lntp | grep :443
```

---

# 14. `lsof` Networking Commands

## Show Network Files/Sockets

```bash
sudo lsof -i
```

---

## Find Process Using Port 8080

```bash
sudo lsof -i :8080
```

---

## Find TCP Port

```bash
sudo lsof -iTCP:8080 -sTCP:LISTEN
```

---

## Find UDP Port

```bash
sudo lsof -iUDP:53
```

---

# 15. `netstat`

Older systems may use:

```bash
netstat -lntp
```

Modern Linux generally prefers:

```bash
ss -lntp
```

Check whether installed:

```bash
which netstat
```

---

# 16. TCP Testing with Netcat

## Test a TCP Port

```bash
nc -vz google.com 443
```

Example:

```bash
nc -vz 127.0.0.1 8080
```

Successful output may look similar to:

```text
Connection to 127.0.0.1 8080 port [tcp/*] succeeded!
```

---

## Test SSH Port

```bash
nc -vz server.example.com 22
```

---

## Test HTTPS Port

```bash
nc -vz server.example.com 443
```

---

# 17. HTTP Testing with `curl`

## Basic GET

```bash
curl https://example.com
```

---

## Show HTTP Headers

```bash
curl -I https://example.com
```

---

## Verbose Mode

```bash
curl -v https://example.com
```

Useful for inspecting:

* DNS
* TCP connection
* TLS
* HTTP request
* HTTP response

---

## Follow Redirects

```bash
curl -L https://example.com
```

---

## Show Only HTTP Status Code

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

---

## Show Response Time

```bash
curl -o /dev/null -s -w "%{time_total}\n" https://example.com
```

---

## Show Detailed Timing

```bash
curl -o /dev/null -s \
-w "DNS: %{time_namelookup}s\nConnect: %{time_connect}s\nTLS: %{time_appconnect}s\nStart Transfer: %{time_starttransfer}s\nTotal: %{time_total}s\n" \
https://example.com
```

---

# 18. HTTP Headers

Request specific headers:

```bash
curl -H "Accept: application/json" https://example.com
```

Send User-Agent:

```bash
curl -H "User-Agent: DevOps-Test" https://example.com
```

---

## POST Request

```bash
curl -X POST https://example.com/api
```

JSON:

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"Shraddha"}' \
https://example.com/api
```

---

# 19. `wget`

Download:

```bash
wget https://example.com/file.txt
```

Save with a custom filename:

```bash
wget -O output.txt https://example.com/file.txt
```

Test without downloading:

```bash
wget --spider https://example.com
```

---

# 20. Interface Statistics

## Show RX/TX Statistics

```bash
ip -s link
```

Example information:

```text
RX packets
RX errors
RX dropped
TX packets
TX errors
TX dropped
```

---

## Show Statistics for One Interface

```bash
ip -s link show wlo1
```

---

# 21. NetworkManager Commands

Check service:

```bash
systemctl status NetworkManager
```

List network devices:

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

Show details for a device:

```bash
nmcli device show wlo1
```

---

# 22. Network Namespace Commands

## List Namespaces

```bash
ip netns list
```

---

## Create Namespace

```bash
sudo ip netns add test-ns
```

Verify:

```bash
ip netns list
```

---

## Execute Command Inside Namespace

```bash
sudo ip netns exec test-ns ip addr
```

Check routes:

```bash
sudo ip netns exec test-ns ip route
```

Check interfaces:

```bash
sudo ip netns exec test-ns ip link
```

---

## Delete Namespace

```bash
sudo ip netns delete test-ns
```

---

# 23. Create a veth Pair

Create:

```bash
sudo ip link add veth0 type veth peer name veth1
```

Check:

```bash
ip link
```

Delete:

```bash
sudo ip link delete veth0
```

Deleting one side removes the pair.

---

# 24. Move veth into a Namespace

Create namespace:

```bash
sudo ip netns add test-ns
```

Create veth pair:

```bash
sudo ip link add veth-host type veth peer name veth-ns
```

Move one side:

```bash
sudo ip link set veth-ns netns test-ns
```

Check host:

```bash
ip link
```

Check namespace:

```bash
sudo ip netns exec test-ns ip link
```

---

# 25. Configure Namespace Interface

Inside namespace:

```bash
sudo ip netns exec test-ns ip link set lo up
```

Configure interface:

```bash
sudo ip netns exec test-ns ip addr add 10.10.0.2/24 dev veth-ns
```

Bring it up:

```bash
sudo ip netns exec test-ns ip link set veth-ns up
```

---

# 26. Configure Host Side

```bash
sudo ip addr add 10.10.0.1/24 dev veth-host
```

Bring it up:

```bash
sudo ip link set veth-host up
```

Then test:

```bash
ping -c 4 10.10.0.2
```

---

# 27. Linux Bridge Commands

List links:

```bash
ip link
```

Inspect Docker bridge:

```bash
ip addr show docker0
```

If bridge utilities are installed:

```bash
bridge link
```

Show forwarding database:

```bash
bridge fdb show
```

---

# 28. Packet Capture with `tcpdump`

## List Interfaces

```bash
sudo tcpdump -D
```

---

## Capture on One Interface

```bash
sudo tcpdump -i wlo1
```

---

## Capture on All Interfaces

```bash
sudo tcpdump -i any
```

---

## Capture ICMP

```bash
sudo tcpdump -i any icmp
```

Then in another terminal:

```bash
ping -c 4 8.8.8.8
```

---

## Capture Port 8080

```bash
sudo tcpdump -i any port 8080
```

Then:

```bash
curl http://127.0.0.1:8080
```

---

## Capture Port 443

```bash
sudo tcpdump -i any port 443
```

---

## Capture DNS

```bash
sudo tcpdump -i any port 53
```

---

## Capture TCP

```bash
sudo tcpdump -i any tcp
```

---

## Capture UDP

```bash
sudo tcpdump -i any udp
```

---

## Save Capture

```bash
sudo tcpdump -i any -w network.pcap
```

Stop with:

```text
Ctrl + C
```

---

## Read Capture

```bash
tcpdump -r network.pcap
```

---

## Capture Specific Host

```bash
sudo tcpdump -i any host 8.8.8.8
```

---

## Capture Specific Source

```bash
sudo tcpdump -i any src host 192.168.1.10
```

---

## Capture Specific Destination

```bash
sudo tcpdump -i any dst host 192.168.1.10
```

---

# 29. Firewall — UFW

Check status:

```bash
sudo ufw status
```

Detailed status:

```bash
sudo ufw status verbose
```

List numbered rules:

```bash
sudo ufw status numbered
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

Allow a custom port:

```bash
sudo ufw allow 8080/tcp
```

Delete a rule:

```bash
sudo ufw delete allow 8080/tcp
```

> ⚠️ Be especially careful with firewall changes on remote servers. Incorrect rules can lock you out.

---

# 30. nftables

Show rules:

```bash
sudo nft list ruleset
```

List tables:

```bash
sudo nft list tables
```

List chains:

```bash
sudo nft list chains
```

Check whether nftables is available:

```bash
which nft
```

---

# 31. iptables

List rules:

```bash
sudo iptables -L
```

Numeric output:

```bash
sudo iptables -L -n
```

Verbose:

```bash
sudo iptables -L -n -v
```

Show NAT rules:

```bash
sudo iptables -t nat -L -n -v
```

> On modern Linux systems, nftables is the underlying framework on many distributions, and `iptables` may be provided through a compatibility layer.

---

# 32. Check Network Services

Check a service:

```bash
systemctl status nginx
```

Check SSH:

```bash
systemctl status ssh
```

Restart a service:

```bash
sudo systemctl restart nginx
```

> Restart only when you understand the impact, especially on production systems.

---

# 33. Check Listening Service

Example:

```bash
sudo ss -lntp | grep :80
```

If nginx is listening:

```text
LISTEN ... 0.0.0.0:80
```

Check application port:

```bash
sudo ss -lntp | grep :8080
```

---

# 34. Check Which Process Uses a Port

Using `ss`:

```bash
sudo ss -lntp | grep :8080
```

Using `lsof`:

```bash
sudo lsof -i :8080
```

Using `fuser`:

```bash
sudo fuser -n tcp 8080
```

---

# 35. Process and Network Troubleshooting

Find process:

```bash
ps aux | grep nginx
```

Find a process by name:

```bash
pgrep nginx
```

Find open network files:

```bash
sudo lsof -i
```

---

# 36. Check Network Kernel Information

Interface statistics:

```bash
cat /proc/net/dev
```

Routing information:

```bash
cat /proc/net/route
```

List network-related proc entries:

```bash
ls /proc/net/
```

---

# 37. Inspect `/sys/class/net`

List interfaces:

```bash
ls /sys/class/net/
```

Check interface state:

```bash
cat /sys/class/net/wlo1/operstate
```

Check MAC:

```bash
cat /sys/class/net/wlo1/address
```

Check MTU:

```bash
cat /sys/class/net/wlo1/mtu
```

---

# 38. MTU

MTU means:

**Maximum Transmission Unit**

Check:

```bash
ip link show wlo1
```

You may see:

```text
mtu 1500
```

Check specific interface:

```bash
ip link show dev wlo1
```

---

# 39. Check DNS + Connectivity Together

First:

```bash
getent hosts google.com
```

Then:

```bash
ping -c 4 google.com
```

Then:

```bash
curl -I https://google.com
```

This separates:

```text
DNS
 ↓
ICMP connectivity
 ↓
HTTP/HTTPS
```

---

# 40. Check TCP Connectivity

```bash
nc -vz example.com 443
```

Then:

```bash
curl -I https://example.com
```

This helps distinguish basic TCP connectivity from HTTP-level problems.

---

# 41. Check HTTPS/TLS

Using curl:

```bash
curl -v https://example.com
```

Using OpenSSL:

```bash
openssl s_client -connect example.com:443
```

Check certificate information:

```bash
openssl s_client -connect example.com:443 </dev/null
```

Useful for diagnosing:

* TLS handshake problems
* Certificate issues
* Protocol negotiation

---

# 42. Docker Networking

List Docker networks:

```bash
docker network ls
```

Inspect bridge network:

```bash
docker network inspect bridge
```

Show Docker interfaces:

```bash
ip link
```

Check Docker bridge:

```bash
ip addr show docker0
```

---

# 43. Docker Container IP

List running containers:

```bash
docker ps
```

Inspect container:

```bash
docker inspect <container-name>
```

Extract IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-name>
```

---

# 44. Docker Port Mapping

Run nginx:

```bash
docker run -d --name nginx-test -p 8080:80 nginx
```

Check:

```bash
docker ps
```

Test:

```bash
curl http://localhost:8080
```

Check listening port:

```bash
sudo ss -lntp | grep :8080
```

---

# 45. Docker Network Inspection

```bash
docker network inspect bridge
```

Look for:

* Containers
* Subnet
* Gateway
* IP addresses
* Network configuration

---

# 46. Kubernetes Networking Commands

List pods with IPs:

```bash
kubectl get pods -o wide
```

List services:

```bash
kubectl get svc
```

Detailed service:

```bash
kubectl describe svc <service-name>
```

List endpoints:

```bash
kubectl get endpoints
```

Modern Kubernetes may also expose endpoint slices:

```bash
kubectl get endpointslices
```

---

# 47. Test Pod Networking

Get a shell:

```bash
kubectl exec -it <pod-name> -- sh
```

Inside the pod:

```bash
ip addr
```

Check routes:

```bash
ip route
```

Check DNS:

```bash
cat /etc/resolv.conf
```

Test service:

```bash
curl http://<service-name>:<port>
```

---

# 48. Kubernetes Pod IP

```bash
kubectl get pod <pod-name> -o wide
```

Example information:

```text
NAME     READY   STATUS    IP          NODE
nginx    1/1     Running   10.244.x.x  node
```

---

# 49. Kubernetes Service IP

```bash
kubectl get svc
```

Detailed:

```bash
kubectl describe svc <service-name>
```

---

# 50. Kubernetes DNS Test

From a pod:

```bash
kubectl exec -it <pod-name> -- nslookup kubernetes.default
```

If `nslookup` is unavailable inside the image, use another diagnostic container/image that contains DNS tools.

---

# 51. Kubernetes Port Forwarding

Forward local port 8080 to a pod:

```bash
kubectl port-forward pod/<pod-name> 8080:80
```

Then:

```bash
curl http://127.0.0.1:8080
```

This is useful for local debugging.

---

# 52. Kubernetes Service Port Forwarding

```bash
kubectl port-forward svc/<service-name> 8080:80
```

Then:

```bash
curl http://127.0.0.1:8080
```

---

# 53. Kubernetes Logs

```bash
kubectl logs <pod-name>
```

Follow logs:

```bash
kubectl logs -f <pod-name>
```

Describe pod:

```bash
kubectl describe pod <pod-name>
```

These are useful when network connectivity appears correct but the application is unhealthy.

---

# 54. Linux Networking Troubleshooting Commands

A good troubleshooting sequence:

```bash
ip link
```

```bash
ip addr
```

```bash
ip route
```

```bash
ip neigh
```

```bash
ping -c 4 <gateway>
```

```bash
getent hosts <hostname>
```

```bash
dig <hostname>
```

```bash
sudo ss -lntup
```

```bash
nc -vz <host> <port>
```

```bash
curl -v <URL>
```

```bash
sudo ufw status
```

```bash
sudo tcpdump -i any
```

---

# 55. Troubleshooting: Interface Problem

### Problem

No network connectivity.

### Check:

```bash
ip link
```

Then:

```bash
ip addr
```

Look for:

```text
UP
```

and a valid IP address.

---

# 56. Troubleshooting: No Default Route

Check:

```bash
ip route
```

Look for:

```text
default via <gateway>
```

Find route to destination:

```bash
ip route get 8.8.8.8
```

---

# 57. Troubleshooting: DNS Problem

Test:

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

If direct IP connectivity works but DNS resolution fails, investigate DNS configuration.

---

# 58. Troubleshooting: Port Problem

Check:

```bash
sudo ss -lntp | grep :8080
```

If there is no output, nothing may be listening on that port.

Check the application:

```bash
systemctl status <service>
```

Check logs:

```bash
journalctl -u <service>
```

---

# 59. Troubleshooting: Localhost Works but Remote Fails

Check:

```bash
sudo ss -lntp | grep :8080
```

If you see:

```text
127.0.0.1:8080
```

the service is listening on loopback only.

If appropriate for the application, configure it to listen on:

```text
0.0.0.0:8080
```

Then check:

```bash
sudo ss -lntp | grep :8080
```

Also investigate:

```text
Linux firewall
Cloud firewall/security group
Routing
Application configuration
Load balancer
```

---

# 60. Troubleshooting: HTTP Problem

Check DNS:

```bash
getent hosts example.com
```

Check TCP:

```bash
nc -vz example.com 443
```

Check HTTPS:

```bash
curl -v https://example.com
```

Check TLS:

```bash
openssl s_client -connect example.com:443
```

---

# 61. Troubleshooting: Packet Level

Start capture:

```bash
sudo tcpdump -i any port 8080
```

Generate traffic:

```bash
curl http://127.0.0.1:8080
```

Look for:

```text
Request
Response
Retransmissions
RST
No response
```

---

# 62. Useful One-Liners

## Show IP Address

```bash
hostname -I
```

---

## Show Default Gateway

```bash
ip route | awk '/default/ {print $3}'
```

---

## Show Listening Ports

```bash
sudo ss -lntup
```

---

## Find Port 8080

```bash
sudo ss -lntp | grep :8080
```

---

## Find Process on Port 8080

```bash
sudo lsof -i :8080
```

---

## Test Port 8080

```bash
nc -vz 127.0.0.1 8080
```

---

## Test HTTP Status

```bash
curl -o /dev/null -s -w "%{http_code}\n" http://127.0.0.1:8080
```

---

## Resolve DNS

```bash
dig +short google.com
```

---

## Show Default Interface

```bash
ip route | awk '/default/ {print $5}'
```

---

## Show All Network Interfaces

```bash
ls /sys/class/net/
```

---

# 63. Practical Command Sequence

Use this sequence when investigating a Linux server:

```bash
echo "=== Interfaces ==="
ip link

echo "=== IP Addresses ==="
ip addr

echo "=== Routes ==="
ip route

echo "=== Neighbours ==="
ip neigh

echo "=== Listening Ports ==="
sudo ss -lntup

echo "=== Hostname ==="
hostname

echo "=== DNS ==="
cat /etc/resolv.conf
```

---

# 64. Complete Network Health Check

```bash
echo "===== HOST ====="
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

echo "===== CONNECTIVITY ====="
ping -c 2 8.8.8.8

echo "===== HTTPS ====="
curl -I --max-time 5 https://example.com
```

---

# 65. Command Cheat Sheet

| Task                   | Command                    |
| ---------------------- | -------------------------- |
| Show interfaces        | `ip link`                  |
| Show IP addresses      | `ip addr`                  |
| Show IPv4              | `ip -4 addr`               |
| Show IPv6              | `ip -6 addr`               |
| Show routes            | `ip route`                 |
| Route lookup           | `ip route get <IP>`        |
| Show neighbours        | `ip neigh`                 |
| Show hostname          | `hostname`                 |
| Hostname details       | `hostnamectl`              |
| DNS lookup             | `dig <domain>`             |
| Short DNS lookup       | `dig +short <domain>`      |
| Host lookup            | `nslookup <domain>`        |
| Name resolution        | `getent hosts <domain>`    |
| Test connectivity      | `ping <host>`              |
| Trace path             | `tracepath <host>`         |
| TCP/UDP sockets        | `ss -lntup`                |
| Process using port     | `lsof -i :<port>`          |
| TCP port test          | `nc -vz <host> <port>`     |
| HTTP test              | `curl -I <URL>`            |
| Detailed HTTP test     | `curl -v <URL>`            |
| Download               | `wget <URL>`               |
| Packet capture         | `tcpdump`                  |
| NetworkManager         | `nmcli`                    |
| Firewall               | `ufw`                      |
| nftables               | `nft`                      |
| Network namespace      | `ip netns`                 |
| Docker networks        | `docker network ls`        |
| Kubernetes pod network | `kubectl get pods -o wide` |
| Kubernetes services    | `kubectl get svc`          |

---

# 🎯 DevOps Troubleshooting Flow

Memorize this:

```text
             Network Problem
                    |
                    v
              ip link
                    |
                    v
              ip addr
                    |
                    v
              ip route
                    |
                    v
               ip neigh
                    |
                    v
                ping
                    |
                    v
             DNS / getent
                    |
                    v
                 dig
                    |
                    v
                  ss
                    |
                    v
                  nc
                    |
                    v
                 curl
                    |
                    v
               Firewall
                    |
                    v
              tcpdump
                    |
                    v
             Application
```

---

# 🧠 Most Important Commands to Memorize

If you remember only these commands, start here:

```bash
ip addr
ip link
ip route
ip neigh
ss -lntup
ping
tracepath
getent hosts
dig
curl
nc
tcpdump
nmcli
ufw
```

These commands cover a large part of everyday Linux networking troubleshooting.
