# Chapter 22 – Firewall

## 1. What is a Firewall?

A firewall is a security mechanism that controls network traffic entering or leaving a system or network.

It uses predefined rules to decide whether traffic should be:

* Allowed
* Blocked
* Rejected
* Logged

Simple example:

```text
Internet
   |
   | Network Traffic
   ↓
+----------------+
|    Firewall    |
+----------------+
   |
   ↓
Server
```

The firewall acts as a security barrier between trusted and untrusted networks.

---

# 2. Why is a Firewall Important?

A firewall helps protect systems from unauthorized network access.

It can:

* Block unwanted connections
* Allow required services
* Restrict access to specific ports
* Restrict access to specific IP addresses
* Control inbound traffic
* Control outbound traffic
* Reduce attack surface
* Protect internal networks
* Log suspicious traffic

---

# 3. Firewall in DevOps

Firewalls are very important in DevOps and cloud environments.

A DevOps engineer may configure firewalls to allow:

```text
SSH       → 22
HTTP      → 80
HTTPS     → 443
Application → required application port
```

while blocking unnecessary ports.

Example:

```text
Internet
    |
    ↓
Firewall
    |
    ├── 22   → SSH       → Allowed from trusted IP
    ├── 80   → HTTP      → Allowed
    ├── 443  → HTTPS     → Allowed
    └── 3306 → MySQL     → Blocked from Internet
```

---

# 4. Types of Firewalls

Common types include:

1. Packet-filtering firewall
2. Stateful firewall
3. Stateless firewall
4. Proxy/application firewall
5. Host-based firewall
6. Network-based firewall
7. Next-generation firewall

---

# 5. Host-Based Firewall

A host-based firewall runs directly on a server or computer.

Examples:

* UFW
* firewalld
* nftables
* iptables

Example:

```text
Internet
   |
   ↓
Linux Server
   |
   └── Host Firewall
```

Ubuntu commonly uses UFW as a simpler firewall management interface.

---

# 6. Network-Based Firewall

A network firewall protects multiple systems or an entire network.

Example:

```text
Internet
    |
    ↓
Network Firewall
    |
    ├── Web Server
    ├── App Server
    └── Database Server
```

---

# 7. Inbound Traffic

Inbound traffic is traffic coming **into** a system.

Example:

```text
Client → Server
```

For example:

```text
Laptop → SSH → Server:22
```

A firewall can allow or block this traffic.

---

# 8. Outbound Traffic

Outbound traffic is traffic leaving a system.

Example:

```text
Server → Internet
```

For example:

```text
Server → HTTPS → Internet:443
```

A firewall can also control outbound traffic.

---

# 9. Firewall Rules

A firewall uses rules to determine what traffic is allowed.

A rule can consider:

* Source IP
* Destination IP
* Source port
* Destination port
* Protocol
* Interface
* Direction

Example:

```text
Source       Destination    Port    Protocol    Action
-------------------------------------------------------
Any          Server         80      TCP         Allow
Any          Server         443     TCP         Allow
Trusted IP   Server         22      TCP         Allow
Any          Server         23      TCP         Deny
```

---

# 10. Allow vs Deny vs Reject

### Allow

Permits the connection.

```text
Traffic → Firewall → Allowed → Server
```

### Deny / Drop

Blocks the traffic, often without sending a response.

```text
Traffic → Firewall → Dropped
```

### Reject

Blocks the traffic and sends a response indicating that the connection was rejected.

---

# 11. Default Policy

A firewall can have a default policy.

For example:

```text
Default inbound policy → DROP
```

This means traffic is blocked unless an explicit rule allows it.

This follows the principle:

> Allow only what is required.

---

# 12. Principle of Least Privilege

Firewall configuration should follow the principle of least privilege.

Only required traffic should be allowed.

Bad:

```text
Allow everything
```

Better:

```text
Allow TCP 443
Allow TCP 22 from trusted IP
Block unnecessary traffic
```

---

# 13. Ports and Firewalls

Firewalls commonly control traffic based on ports.

Important ports:

| Port | Protocol | Service                 |
| ---: | -------- | ----------------------- |
|   22 | TCP      | SSH                     |
|   53 | TCP/UDP  | DNS                     |
|   80 | TCP      | HTTP                    |
|  443 | TCP      | HTTPS                   |
| 3306 | TCP      | MySQL                   |
| 5432 | TCP      | PostgreSQL              |
| 6379 | TCP      | Redis                   |
| 8080 | TCP      | Common application port |

A firewall can allow or block these ports.

---

# 14. TCP and UDP

Firewalls can distinguish between protocols.

Example:

```text
TCP 22
UDP 53
TCP 443
```

A rule may specify:

```text
Allow TCP port 443
```

while blocking other traffic.

---

# 15. UFW

UFW stands for:

**Uncomplicated Firewall**

It provides a simpler interface for managing Linux firewall rules.

Check status:

```bash
sudo ufw status
```

Detailed status:

```bash
sudo ufw status verbose
```

---

# 16. UFW Basic Rule Example

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

Enable UFW:

```bash
sudo ufw enable
```

Check:

```bash
sudo ufw status
```

---

# 17. Important SSH Warning

Before enabling UFW on a remote server, make sure SSH access is allowed.

For example:

```bash
sudo ufw allow 22/tcp
```

Then:

```bash
sudo ufw enable
```

Otherwise, you could accidentally lock yourself out of the server.

In production, this is extremely important.

---

# 18. UFW Rules by Service

Instead of specifying the port directly, you can use a service name.

Example:

```bash
sudo ufw allow ssh
```

HTTP:

```bash
sudo ufw allow http
```

HTTPS:

```bash
sudo ufw allow https
```

---

# 19. Restrict SSH to a Specific IP

Instead of allowing SSH from everywhere:

```bash
sudo ufw allow 22/tcp
```

you can restrict it:

```bash
sudo ufw allow from 192.168.1.10 to any port 22 proto tcp
```

This improves security when the trusted source IP is known.

---

# 20. Deny a Port

Example:

```bash
sudo ufw deny 23/tcp
```

This blocks Telnet traffic.

---

# 21. Delete a UFW Rule

List numbered rules:

```bash
sudo ufw status numbered
```

Then delete a rule:

```bash
sudo ufw delete NUMBER
```

Example:

```bash
sudo ufw delete 2
```

---

# 22. UFW Reset

To remove UFW rules:

```bash
sudo ufw reset
```

Be careful with this command on production systems.

---

# 23. iptables

`iptables` is a traditional Linux firewall management tool.

It works with the Linux kernel's Netfilter framework.

Example:

```bash
sudo iptables -L
```

Verbose output:

```bash
sudo iptables -L -v
```

Numeric output:

```bash
sudo iptables -L -n
```

---

# 24. iptables Chains

Common iptables chains include:

### INPUT

Controls incoming traffic to the local system.

```text
Network → INPUT → Local Server
```

### OUTPUT

Controls traffic leaving the local system.

```text
Local Server → OUTPUT → Network
```

### FORWARD

Controls traffic being routed through the system.

```text
Network → FORWARD → Network
```

---

# 25. nftables

nftables is the modern Linux packet-filtering framework.

Check rules:

```bash
sudo nft list ruleset
```

Check tables:

```bash
sudo nft list tables
```

It is increasingly used as the underlying firewall framework on modern Linux systems.

---

# 26. firewalld

`firewalld` is another Linux firewall management solution.

Check status:

```bash
sudo firewall-cmd --state
```

List zones:

```bash
sudo firewall-cmd --get-active-zones
```

List allowed services:

```bash
sudo firewall-cmd --list-services
```

---

# 27. Firewall Zones

firewalld uses zones to apply different trust levels.

Examples:

```text
public
internal
external
trusted
dmz
```

Different interfaces can be assigned to different zones.

---

# 28. Stateful Firewall

A stateful firewall tracks the state of network connections.

For example:

```text
Client → Server
       SYN
       ↓
Server → Client
       SYN-ACK
       ↓
Client → Server
       ACK
```

The firewall understands that these packets belong to the same connection.

---

# 29. Stateless Firewall

A stateless firewall evaluates packets individually.

It does not maintain connection state in the same way as a stateful firewall.

Rules are generally based on packet characteristics such as:

* Source IP
* Destination IP
* Port
* Protocol

---

# 30. Firewall vs Router

A router primarily forwards packets between networks.

A firewall primarily controls whether network traffic should be allowed or blocked according to security rules.

Some devices perform both functions.

---

# 31. Firewall vs Security Group

In cloud environments, you may have both host-level and cloud-level controls.

Example:

```text
Internet
   |
   ↓
Cloud Security Group
   |
   ↓
Server
   |
   ↓
Host Firewall
   |
   ↓
Application
```

Both layers can control traffic.

---

# 32. AWS Security Groups

In AWS, a Security Group acts as a virtual firewall for resources such as EC2 instances.

Example:

```text
Inbound:
TCP 22  → Trusted IP
TCP 80  → 0.0.0.0/0
TCP 443 → 0.0.0.0/0
```

A database port such as `3306` should generally not be exposed publicly unless there is a specific security requirement.

---

# 33. Firewall and Kubernetes

Kubernetes networking can involve multiple layers of traffic control.

Example:

```text
Internet
   |
   ↓
Cloud Firewall / Security Group
   |
   ↓
Node
   |
   ↓
Kubernetes Network
   |
   ↓
Service
   |
   ↓
Pod
```

Kubernetes NetworkPolicies can also control pod-to-pod traffic.

---

# 34. Firewall and Docker

Docker creates network interfaces and rules to allow container networking.

Check interfaces:

```bash
ip link
```

Check routes:

```bash
ip route
```

Check firewall rules when troubleshooting Docker networking:

```bash
sudo iptables -L -n -v
```

or:

```bash
sudo nft list ruleset
```

---

# 35. Firewall Troubleshooting

When an application cannot be reached, check:

### Step 1 – Is the service running?

```bash
sudo systemctl status nginx
```

### Step 2 – Is the port listening?

```bash
sudo ss -ltnp
```

### Step 3 – Is the firewall blocking it?

For UFW:

```bash
sudo ufw status
```

For iptables:

```bash
sudo iptables -L -n -v
```

For nftables:

```bash
sudo nft list ruleset
```

### Step 4 – Test connectivity

```bash
curl http://server-ip:80
```

or:

```bash
nc -zv server-ip 80
```

---

# 36. Firewall Troubleshooting Flow

```text
Client
  |
  ↓
DNS
  |
  ↓
Network Route
  |
  ↓
Firewall
  |
  ↓
Server Port
  |
  ↓
Application
```

When troubleshooting, check each layer.

---

# 37. Real-World Example

Suppose an application runs on:

```text
Server IP: 10.0.0.10
Application Port: 8080
```

The client cannot connect.

Check:

```bash
sudo ss -ltnp | grep :8080
```

If the application is listening, check the firewall:

```bash
sudo ufw status
```

If port 8080 is blocked:

```bash
sudo ufw allow 8080/tcp
```

Then test:

```bash
curl http://10.0.0.10:8080
```

---

# 38. Security Best Practices

For production environments:

1. Deny unnecessary traffic.
2. Allow only required ports.
3. Restrict SSH access.
4. Avoid exposing databases directly to the Internet.
5. Use multiple security layers.
6. Monitor firewall logs.
7. Review firewall rules regularly.
8. Use least privilege.
9. Document firewall changes.
10. Test changes before production deployment.

---

# 39. Important Firewall Commands

### UFW

```bash
sudo ufw status
sudo ufw status verbose
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw deny 23/tcp
sudo ufw status numbered
```

### iptables

```bash
sudo iptables -L
sudo iptables -L -n
sudo iptables -L -n -v
```

### nftables

```bash
sudo nft list ruleset
sudo nft list tables
```

### firewalld

```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-services
```

---

# 40. DevOps Interview Summary

Remember:

```text
Firewall
   ↓
Controls network traffic
   ↓
Inbound + Outbound
   ↓
IP + Port + Protocol + Rules
   ↓
Allow / Drop / Reject
```

Important concepts:

```text
UFW         → Simple Linux firewall interface
iptables    → Traditional Linux firewall tool
nftables    → Modern Linux packet filtering framework
firewalld   → Dynamic firewall manager
INPUT       → Incoming traffic
OUTPUT      → Outgoing traffic
FORWARD     → Routed traffic
Stateful    → Tracks connections
Stateless   → Evaluates packets individually
```

## Production mindset

When troubleshooting a network problem, don't immediately blame the firewall.

Check:

```text
1. DNS
2. Routing
3. Network connectivity
4. Firewall
5. Listening port
6. Application
```

A firewall is only one layer of the network path.
