# 🔥 Chapter 22 – Firewall Commands

## 1. Check Firewall Status with UFW

### Command

```bash
sudo ufw status
```

### Purpose

Checks whether the UFW firewall is active and displays configured rules.

### Observation

Example:

```text
Status: inactive
```

If it shows `inactive`, UFW is currently not enabled.

---

## 2. Check Detailed UFW Status

### Command

```bash
sudo ufw status verbose
```

### Purpose

Displays detailed firewall status, including:

* Firewall state
* Default incoming policy
* Default outgoing policy
* Configured rules

### Observation

Example:

```text
Status: inactive
```

---

## 3. Check UFW Version

### Command

```bash
sudo ufw version
```

### Purpose

Displays the installed UFW version.

### Observation

This confirms that UFW is installed and shows its version.

---

## 4. Check Firewall Rules

### Command

```bash
sudo ufw status numbered
```

### Purpose

Displays firewall rules with numbers.

### Observation

Example:

```text
Status: inactive
```

If rules exist and UFW is active, they will be displayed with rule numbers.

---

## 5. Check iptables Rules

### Command

```bash
sudo iptables -L -n -v
```

### Purpose

Displays Linux firewall rules managed through iptables.

### Options

* `-L` → List rules
* `-n` → Don't resolve hostnames
* `-v` → Verbose output

### Observation

Look for chains such as:

```text
Chain INPUT
Chain FORWARD
Chain OUTPUT
```

These represent traffic entering, passing through, and leaving the system.

---

## 6. Check iptables NAT Rules

### Command

```bash
sudo iptables -t nat -L -n -v
```

### Purpose

Displays NAT-related firewall rules.

### Observation

Useful when troubleshooting:

* Docker networking
* Port forwarding
* NAT
* Kubernetes networking

---

## 7. Check nftables Rules

### Command

```bash
sudo nft list ruleset
```

### Purpose

Displays the complete nftables ruleset.

### Observation

Modern Linux distributions commonly use nftables as the underlying firewall framework.

---

## 8. Check Listening Ports

### Command

```bash
sudo ss -ltnp
```

### Purpose

Shows TCP ports currently listening on the system.

### Observation

Example:

```text
LISTEN 0 4096 0.0.0.0:22
LISTEN 0 4096 0.0.0.0:8080
```

This helps identify services that may need firewall protection.

---

## 9. Check a Specific Port

### Command

```bash
sudo ss -ltnp | grep :22
```

### Purpose

Checks whether SSH is listening on port `22`.

### Observation

If SSH is running, you should see a listening entry for port 22.

---

## 10. Check Firewall Service

### Command

```bash
sudo systemctl status ufw
```

### Purpose

Checks the status of the UFW service.

### Observation

Depending on the Linux distribution, UFW may be managed primarily through the `ufw` command rather than as a traditional systemd service.

---

# 🧪 Hands-On Firewall Lab

## Lab 1 – Check Current Firewall State

### Step 1

```bash
sudo ufw status verbose
```

### Step 2

Record the output.

### Observation

Write your actual output here:

```text
Status:
Default:
Rules:
```

---

## Lab 2 – Check Listening Services

### Command

```bash
sudo ss -ltnp
```

### Observation

Identify important ports.

Example:

| Port | Service       | Purpose                 |
| ---- | ------------- | ----------------------- |
| 22   | SSH           | Remote administration   |
| 80   | HTTP          | Web traffic             |
| 443  | HTTPS         | Secure web traffic      |
| 3306 | MariaDB/MySQL | Database                |
| 8080 | Application   | Web/application service |

Only include ports that actually appear on your system.

---

## Lab 3 – Check iptables

### Command

```bash
sudo iptables -L -n -v
```

### Observation

Check:

* INPUT chain
* FORWARD chain
* OUTPUT chain
* Default policies
* Packet counters
* Byte counters

Record anything relevant to your system.

---

## Lab 4 – Check nftables

### Command

```bash
sudo nft list ruleset
```

### Observation

Check whether your system has an active nftables ruleset.

---

# 🔐 Safe UFW Rule Examples

> ⚠️ Do not blindly enable or change firewall rules on a remote production server. Always make sure you have an alternative access method before changing SSH rules.

## Allow SSH

```bash
sudo ufw allow 22/tcp
```

### Purpose

Allows incoming SSH connections on TCP port 22.

---

## Allow HTTP

```bash
sudo ufw allow 80/tcp
```

### Purpose

Allows incoming HTTP traffic.

---

## Allow HTTPS

```bash
sudo ufw allow 443/tcp
```

### Purpose

Allows incoming HTTPS traffic.

---

## Allow a Specific Port

```bash
sudo ufw allow 8080/tcp
```

### Purpose

Allows TCP traffic to port 8080.

---

## Deny a Port

```bash
sudo ufw deny 8080/tcp
```

### Purpose

Blocks incoming TCP connections to port 8080.

---

## Delete a Rule

First check numbered rules:

```bash
sudo ufw status numbered
```

Then delete the required rule:

```bash
sudo ufw delete <rule-number>
```

Example:

```bash
sudo ufw delete 2
```

---

# 🌐 Test Network Access

## Test Local HTTP Service

```bash
curl -I http://127.0.0.1
```

### Observation

A successful HTTP response indicates that the local web service is reachable.

---

## Test a Specific Port

```bash
nc -vz 127.0.0.1 22
```

### Purpose

Tests whether TCP port 22 is reachable.

### Observation

A successful connection indicates that the port is accepting connections.

---

## Test HTTP Port

```bash
nc -vz 127.0.0.1 80
```

### Observation

Useful for checking whether a web server is listening on port 80.

---

# 🔎 Firewall Troubleshooting Commands

## Check Routing

```bash
ip route
```

### Observation

Confirms the system's routing table and default gateway.

---

## Check IP Addresses

```bash
ip addr show
```

### Observation

Shows network interfaces and assigned IP addresses.

---

## Check DNS

```bash
cat /etc/resolv.conf
```

### Observation

Shows configured DNS resolver information.

---

## Test DNS Resolution

```bash
getent hosts example.com
```

### Observation

If an IP address is returned, DNS resolution is working.

---

## Test HTTPS Connectivity

```bash
curl -I https://example.com
```

### Observation

A successful HTTP response such as:

```text
HTTP/2 200
```

indicates that HTTPS connectivity is working.

---

# 🐳 Firewall and Docker

Docker can create its own networking and firewall rules.

### Check Docker Networks

```bash
docker network ls
```

### Observation

Look for networks such as:

```text
bridge
host
none
```

---

### Check Docker Containers

```bash
docker ps -a
```

### Observation

Shows running and stopped containers.

---

### Check Docker Port Mappings

```bash
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Names}}"
```

### Observation

Look for mappings such as:

```text
0.0.0.0:8080->80/tcp
```

This means host port `8080` forwards traffic to container port `80`.

---

# ☸️ Firewall and Kubernetes

Kubernetes networking can also interact with Linux firewall and packet-filtering systems.

### Check Kubernetes Services

```bash
kubectl get svc -A
```

### Observation

Look for service types such as:

* ClusterIP
* NodePort
* LoadBalancer

---

### Check Kubernetes Nodes

```bash
kubectl get nodes -o wide
```

### Observation

Record:

* Node IP
* Kubernetes version
* Container runtime

---

### Check Kubernetes Network Components

```bash
sudo ss -ltnp
```

### Observation

Look for Kubernetes-related ports and processes.

---

# 🧠 Important Firewall Concepts

| Concept  | Meaning                                    |
| -------- | ------------------------------------------ |
| Firewall | Controls network traffic                   |
| UFW      | User-friendly firewall interface           |
| iptables | Linux packet filtering framework           |
| nftables | Modern Linux packet filtering framework    |
| INPUT    | Incoming traffic                           |
| OUTPUT   | Outgoing traffic                           |
| FORWARD  | Traffic passing through the host           |
| Allow    | Permit traffic                             |
| Deny     | Block traffic                              |
| Port     | Logical endpoint for network communication |
| Rule     | Firewall condition/action                  |
| NAT      | Network Address Translation                |

---

# 🎯 Production Troubleshooting Flow

When an application cannot be reached:

```text
Application
    ↓
Process running?
    ↓
Port listening?
    ↓
Local connectivity?
    ↓
Firewall rules?
    ↓
Routing?
    ↓
Network connectivity?
    ↓
DNS?
    ↓
Remote firewall/security group?
```

Useful commands:

```bash
ps aux
sudo ss -ltnp
sudo ufw status verbose
sudo iptables -L -n -v
sudo nft list ruleset
ip addr
ip route
getent hosts example.com
curl -v http://<IP>:<PORT>
```

---

# 📝 My Observations

## UFW

```text
Status:
Observation:
```

## Listening Ports

```text
Important ports:
Observation:
```

## iptables

```text
Observation:
```

## nftables

```text
Observation:
```

## Docker

```text
Observation:
```

## Kubernetes

```text
Observation:
```

---

# 💼 Real-World DevOps Use

A DevOps engineer uses firewall knowledge to:

* Secure Linux servers
* Allow only required ports
* Protect SSH
* Troubleshoot blocked applications
* Secure web servers
* Understand Docker networking
* Troubleshoot Kubernetes networking
* Investigate connectivity failures
* Reduce unnecessary network exposure
* Work with cloud security groups and network ACLs

---

# ⭐ Key Takeaways

1. A firewall controls network traffic.
2. UFW provides a simple interface for Linux firewall management.
3. `iptables` and `nftables` can be used to inspect packet-filtering rules.
4. `ss -ltnp` helps identify listening services.
5. Firewall troubleshooting should be combined with routing and connectivity checks.
6. Docker and Kubernetes can introduce additional networking and firewall behavior.
7. Never expose unnecessary ports.
8. Always protect SSH carefully before modifying firewall rules on remote systems.
9. In production, follow least-privilege networking.
10. A firewall is one layer of a larger security architecture.
