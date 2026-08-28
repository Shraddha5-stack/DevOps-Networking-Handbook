# 🔥 Chapter 22 – Firewall Practical Lab

## 🎯 Objective

In this practical lab, I will learn how to:

* Check firewall status
* Inspect firewall rules
* Check listening ports
* Understand INPUT, OUTPUT and FORWARD traffic
* Test network connectivity
* Inspect iptables and nftables
* Understand Docker and Kubernetes networking from a firewall perspective
* Troubleshoot a blocked network connection

---

# 🧪 Lab 1 – Check UFW Status

### Command

```bash
sudo ufw status
```

### Observation

Record the output:

```text
Status:
```

### What I learned

UFW (Uncomplicated Firewall) provides an easy way to manage firewall rules on Linux.

---

# 🧪 Lab 2 – Check Detailed UFW Status

### Command

```bash
sudo ufw status verbose
```

### Observation

Record:

```text
Status:
Default incoming policy:
Default outgoing policy:
Default routed policy:
```

### What I learned

The verbose output shows the firewall state and its default traffic policies.

---

# 🧪 Lab 3 – Check UFW Rules

### Command

```bash
sudo ufw status numbered
```

### Observation

Record the rules shown by the system:

```text
Rules:
```

### What I learned

Numbered rules make it easier to identify and delete individual firewall rules.

---

# 🧪 Lab 4 – Check Listening Ports

### Command

```bash
sudo ss -ltnp
```

### Observation

Look for services listening on ports such as:

```text
22
80
443
3306
8080
```

Only record ports that actually exist on my system.

### What I learned

`ss` helps identify services that are listening for incoming TCP connections.

---

# 🧪 Lab 5 – Check SSH Port

### Command

```bash
sudo ss -ltnp | grep :22
```

### Observation

If SSH is running, a listening entry for port 22 should appear.

### What I learned

Port 22 is commonly used by SSH for remote administration.

---

# 🧪 Lab 6 – Check HTTP Port

### Command

```bash
sudo ss -ltnp | grep :80
```

### Observation

Check whether a web server is listening on port 80.

### What I learned

Port 80 is normally used for HTTP traffic.

---

# 🧪 Lab 7 – Inspect iptables

### Command

```bash
sudo iptables -L -n -v
```

### Observation

Look for:

* INPUT
* FORWARD
* OUTPUT
* Policy
* Packet counters
* Byte counters

### What I learned

iptables can inspect and manage packet-filtering rules.

---

# 🧪 Lab 8 – Inspect NAT Rules

### Command

```bash
sudo iptables -t nat -L -n -v
```

### Observation

Check for NAT and forwarding-related rules.

### What I learned

NAT rules are especially useful when troubleshooting Docker, Kubernetes, and port forwarding.

---

# 🧪 Lab 9 – Inspect nftables

### Command

```bash
sudo nft list ruleset
```

### Observation

Check whether an active nftables ruleset is present.

```text
Observation:
```

### What I learned

nftables is the modern Linux packet-filtering framework.

---

# 🧪 Lab 10 – Test Local HTTP Connectivity

### Command

```bash
curl -I http://127.0.0.1
```

### Observation

A successful HTTP response indicates that a local web server is reachable.

Example:

```text
HTTP/1.1 200 OK
```

### What I learned

`curl` can test whether an application is reachable through HTTP.

---

# 🧪 Lab 11 – Test a TCP Port

### Command

```bash
nc -vz 127.0.0.1 22
```

### Observation

A successful connection means that port 22 is reachable locally.

### What I learned

`nc` (netcat) can be used to test TCP connectivity.

---

# 🧪 Lab 12 – Check Network Interfaces

### Command

```bash
ip addr show
```

### Observation

Record the important interfaces:

```text
Interface:
IP address:
```

### What I learned

Firewall troubleshooting requires knowing which network interfaces and IP addresses are involved.

---

# 🧪 Lab 13 – Check Routing Table

### Command

```bash
ip route
```

### Observation

Record:

```text
Default gateway:
Interface:
Route:
```

### What I learned

A firewall may be configured correctly, but traffic can still fail because of routing problems.

---

# 🧪 Lab 14 – Test DNS Resolution

### Command

```bash
getent hosts example.com
```

### Observation

If an IP address is returned, DNS resolution is working.

### What I learned

DNS problems can sometimes look like network or firewall problems, so DNS should also be checked during troubleshooting.

---

# 🧪 Lab 15 – Test HTTPS Connectivity

### Command

```bash
curl -I https://example.com
```

### Observation

A successful response such as:

```text
HTTP/2 200
```

shows that HTTPS connectivity is working.

### What I learned

This tests DNS resolution, TCP connectivity, TLS negotiation and HTTP communication together.

---

# 🐳 Lab 16 – Check Docker Networks

### Command

```bash
docker network ls
```

### Observation

Check for networks such as:

```text
bridge
host
none
```

### What I learned

Docker creates virtual networks that allow containers to communicate.

---

# 🐳 Lab 17 – Check Docker Containers

### Command

```bash
docker ps -a
```

### Observation

Record:

```text
Running containers:
Stopped containers:
```

### What I learned

A container may be stopped even though Docker-related firewall or networking processes are still present.

---

# 🐳 Lab 18 – Check Docker Port Mappings

### Command

```bash
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Names}}"
```

### Observation

Look for mappings such as:

```text
0.0.0.0:8080->80/tcp
```

### What I learned

A port mapping forwards traffic from a host port to a container port.

---

# ☸️ Lab 19 – Check Kubernetes Services

### Command

```bash
kubectl get svc -A
```

### Observation

Identify:

* ClusterIP
* NodePort
* LoadBalancer

### What I learned

Kubernetes Services provide stable networking endpoints for applications.

---

# ☸️ Lab 20 – Check Kubernetes Nodes

### Command

```bash
kubectl get nodes -o wide
```

### Observation

Record:

```text
Node:
Internal IP:
Status:
Container Runtime:
```

### What I learned

The node IP is important when troubleshooting NodePort and other external connectivity.

---

# ☸️ Lab 21 – Test Kubernetes Service

### Command

```bash
kubectl get svc
```

Find the service and its port.

For example:

```text
web-app-nodeport   NodePort   80:30080/TCP
```

Then test the NodePort using the node IP:

```bash
curl http://<NODE-IP>:30080
```

### Observation

A successful response means the request reached the Kubernetes Service and backend Pod.

### What I learned

A NodePort exposes a Kubernetes Service on a port of the node.

---

# 🔍 Lab 22 – Compare Localhost and Node IP

Test:

```bash
curl http://127.0.0.1:30080
```

Then:

```bash
curl http://<NODE-IP>:30080
```

### Observation

Record both results:

```text
127.0.0.1:
Result:

NODE-IP:
Result:
```

### What I learned

In environments such as Kind running through Docker, a NodePort may not be directly exposed on the host's `127.0.0.1`.

The node's reachable IP may work instead.

---

# 🔎 Lab 23 – Check Kubernetes Endpoints

### Command

```bash
kubectl get endpointslice -l kubernetes.io/service-name=<SERVICE-NAME>
```

Example:

```bash
kubectl get endpointslice -l kubernetes.io/service-name=web-app-nodeport
```

### Observation

Check the backend Pod IP addresses.

### What I learned

EndpointSlices show the actual backend endpoints selected by a Service.

---

# 🔎 Lab 24 – Test Service from Inside Kubernetes

### Command

```bash
kubectl run network-test --rm -it --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://<CLUSTER-IP>:80
```

### Observation

A successful HTTP response indicates that:

```text
Pod
 ↓
Service
 ↓
Backend Pod
```

networking is working inside the cluster.

---

# 🔥 Lab 25 – Understand Firewall Traffic Chains

Linux firewall traffic can be understood using:

```text
              Incoming Traffic
                     ↓
                  INPUT
                     ↓
                 Application


Application
     ↓
   OUTPUT
     ↓
Outgoing Traffic


Incoming Traffic
      ↓
   FORWARD
      ↓
Another Network
```

### What I learned

* INPUT → traffic destined for the local machine
* OUTPUT → traffic generated by the local machine
* FORWARD → traffic passing through the machine

---

# 🧠 Lab 26 – Firewall Troubleshooting Scenario

## Problem

An application cannot be reached.

### Step 1 – Check the process

```bash
ps aux
```

### Step 2 – Check listening ports

```bash
sudo ss -ltnp
```

### Step 3 – Check firewall

```bash
sudo ufw status verbose
```

### Step 4 – Check iptables

```bash
sudo iptables -L -n -v
```

### Step 5 – Check nftables

```bash
sudo nft list ruleset
```

### Step 6 – Check IP address

```bash
ip addr
```

### Step 7 – Check routing

```bash
ip route
```

### Step 8 – Test connectivity

```bash
curl -v http://<IP>:<PORT>
```

### What I learned

Firewall troubleshooting should not be done in isolation. I need to check:

```text
Process
   ↓
Port
   ↓
Firewall
   ↓
IP
   ↓
Route
   ↓
Network
   ↓
Application
```

---

# ⚠️ Important Safety Rule

Never enable or modify firewall rules blindly on a remote production server.

Before changing SSH firewall rules:

1. Confirm the SSH port.
2. Make sure SSH access is allowed.
3. Keep an alternative access method if possible.
4. Test the rule carefully.
5. Avoid locking yourself out of the server.

---

# 📊 Final Lab Summary

| Area       | Command                         | Purpose                       |
| ---------- | ------------------------------- | ----------------------------- |
| UFW        | `sudo ufw status`               | Check firewall status         |
| UFW        | `sudo ufw status verbose`       | Detailed firewall information |
| UFW        | `sudo ufw status numbered`      | Show numbered rules           |
| Ports      | `sudo ss -ltnp`                 | Find listening services       |
| iptables   | `sudo iptables -L -n -v`        | Inspect firewall rules        |
| NAT        | `sudo iptables -t nat -L -n -v` | Inspect NAT rules             |
| nftables   | `sudo nft list ruleset`         | Inspect nftables              |
| Interfaces | `ip addr`                       | Check IP addresses            |
| Routing    | `ip route`                      | Check routes                  |
| DNS        | `getent hosts example.com`      | Test DNS                      |
| HTTP       | `curl -I http://127.0.0.1`      | Test HTTP                     |
| TCP        | `nc -vz 127.0.0.1 22`           | Test TCP port                 |
| Docker     | `docker network ls`             | Check Docker networks         |
| Kubernetes | `kubectl get svc -A`            | Check Services                |
| Kubernetes | `kubectl get nodes -o wide`     | Check node networking         |

---

# 📝 My Final Observations

### UFW

```text
Status:
```

### Listening Ports

```text
Important ports:
```

### iptables

```text
Observation:
```

### nftables

```text
Observation:
```

### Docker Networking

```text
Observation:
```

### Kubernetes Networking

```text
Observation:
```

### Troubleshooting Lesson

```text
The most important thing I learned:
```

---

# ⭐ Key Takeaway

A firewall is not just about blocking ports.

As a DevOps engineer, I need to understand the complete traffic path:

```text
Client
  ↓
DNS
  ↓
IP Address
  ↓
Routing
  ↓
Firewall
  ↓
Port
  ↓
Application
```

When troubleshooting connectivity, I should check each layer systematically instead of assuming that the firewall is always the problem.
