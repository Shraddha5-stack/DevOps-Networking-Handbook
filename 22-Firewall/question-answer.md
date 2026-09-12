# 🔥 Chapter 22 – Firewall Interview Questions

## 🟢 Basic Questions

### 1. What is a firewall?

A firewall is a security mechanism that controls incoming and outgoing network traffic based on predefined rules.

It can allow or block traffic based on factors such as:

* IP address
* Port
* Protocol
* Source
* Destination

---

### 2. Why is a firewall important in DevOps?

Firewalls help protect servers and applications from unauthorized network access.

In DevOps, firewalls are commonly used to:

* Protect production servers
* Restrict SSH access
* Allow only required application ports
* Protect databases
* Control network communication
* Reduce the attack surface

---

### 3. What is inbound traffic?

Inbound traffic is network traffic coming **into** a server or system.

Example:

```text
Client → Server:443
```

This represents incoming HTTPS traffic.

---

### 4. What is outbound traffic?

Outbound traffic is network traffic leaving a server or system.

Example:

```text
Server → Internet:443
```

This represents outgoing HTTPS traffic.

---

### 5. What is a firewall rule?

A firewall rule defines what network traffic should be allowed or denied.

Example:

```text
Allow TCP port 22
Deny TCP port 23
```

---

## 🟡 UFW Questions

### 6. What is UFW?

UFW stands for **Uncomplicated Firewall**.

It provides a simpler command-line interface for managing firewall rules on Linux systems.

Example:

```bash
sudo ufw status
```

---

### 7. How do you check UFW status?

```bash
sudo ufw status
```

For more details:

```bash
sudo ufw status verbose
```

---

### 8. How do you allow SSH through UFW?

```bash
sudo ufw allow 22/tcp
```

Or:

```bash
sudo ufw allow ssh
```

---

### 9. How do you allow HTTP and HTTPS?

HTTP:

```bash
sudo ufw allow 80/tcp
```

HTTPS:

```bash
sudo ufw allow 443/tcp
```

---

### 10. How do you block a port using UFW?

```bash
sudo ufw deny 8080/tcp
```

This blocks incoming TCP traffic on port 8080.

---

### 11. How do you delete a UFW rule?

First check numbered rules:

```bash
sudo ufw status numbered
```

Then delete the required rule:

```bash
sudo ufw delete <rule-number>
```

---

### 12. How do you allow traffic from a specific IP?

```bash
sudo ufw allow from 192.168.1.10
```

This allows traffic from that IP address.

---

### 13. How do you allow SSH only from a specific IP?

```bash
sudo ufw allow from 192.168.1.10 to any port 22 proto tcp
```

This is more restrictive than allowing SSH from everywhere.

---

### 14. How do you enable UFW?

```bash
sudo ufw enable
```

⚠️ Before enabling UFW on a remote server, make sure SSH access is allowed.

---

### 15. How do you disable UFW?

```bash
sudo ufw disable
```

---

## 🟠 iptables and nftables Questions

### 16. What is iptables?

`iptables` is a Linux firewall tool used to configure packet-filtering rules.

Example:

```bash
sudo iptables -L -n -v
```

---

### 17. What is nftables?

`nftables` is the modern Linux packet-filtering framework and is intended to replace the older iptables framework.

Example:

```bash
sudo nft list ruleset
```

---

### 18. What is the difference between UFW and iptables?

| UFW                                      | iptables                             |
| ---------------------------------------- | ------------------------------------ |
| Easier to use                            | More advanced                        |
| Simplified interface                     | Low-level firewall management        |
| Beginner-friendly                        | Requires deeper networking knowledge |
| Uses underlying Linux firewall framework | Direct rule management               |

---

## 🔵 Ports and Firewall Questions

### 19. How do you check which ports are listening?

```bash
sudo ss -ltnp
```

For TCP and UDP:

```bash
sudo ss -tulnp
```

---

### 20. How do you check whether port 22 is listening?

```bash
sudo ss -ltnp | grep :22
```

---

### 21. What is the difference between an open port and an allowed firewall port?

A **listening port** means an application is waiting for connections.

A **firewall-allowed port** means the firewall permits traffic to that port.

For successful communication, both may be required.

```text
Application listening
        +
Firewall allows traffic
        ↓
Connection can succeed
```

---

## 🔴 Troubleshooting Questions

### 22. An application is running but users cannot access it. What would you check?

I would troubleshoot layer by layer:

```text
1. Is the application running?
2. Is the expected port listening?
3. Is the service bound to the correct IP?
4. Is the firewall allowing the port?
5. Is routing correct?
6. Is DNS resolving correctly?
7. Is there a cloud firewall/security group?
8. Is the remote client able to reach the server?
```

Useful commands:

```bash
sudo ss -ltnp
sudo ufw status verbose
ip addr
ip route
ping <server-ip>
curl http://<server-ip>:<port>
```

---

### 23. SSH is not working. How would you troubleshoot it?

I would check:

```bash
sudo systemctl status ssh
```

Then:

```bash
sudo ss -ltnp | grep :22
```

Then check the firewall:

```bash
sudo ufw status
```

I would also verify:

* Server IP
* Network connectivity
* SSH configuration
* Firewall rules
* Cloud security groups
* Whether port 22 is reachable

---

### 24. Port 80 is listening, but the website is not reachable. What could be wrong?

Possible causes include:

* Firewall blocking port 80
* Application bound only to localhost
* Incorrect IP address
* Routing problem
* Cloud security group blocking port 80
* Network ACL blocking traffic
* Reverse proxy configuration issue

I would check:

```bash
sudo ss -ltnp | grep :80
sudo ufw status
curl http://127.0.0.1
curl http://<server-ip>
```

---

### 25. How would you check whether a firewall is blocking traffic?

First check firewall configuration:

```bash
sudo ufw status verbose
```

Then check listening ports:

```bash
sudo ss -ltnp
```

For lower-level rules:

```bash
sudo iptables -L -n -v
```

or:

```bash
sudo nft list ruleset
```

I would also test connectivity using:

```bash
curl
nc
ping
```

depending on the protocol being tested.

---

## 🟣 DevOps Scenario Questions

### 26. A production server should allow SSH only from the company's IP. How would you configure it?

I would restrict SSH to the trusted source IP:

```bash
sudo ufw allow from <trusted-ip> to any port 22 proto tcp
```

Then I would ensure there is no broader SSH allow rule.

I would verify:

```bash
sudo ufw status numbered
```

---

### 27. A web server needs HTTP and HTTPS, but SSH should be restricted. What firewall rules would you use?

Conceptually:

```text
22/tcp  → Allow only trusted administration IPs
80/tcp  → Allow
443/tcp → Allow
Everything else → Deny by default
```

This follows the principle of least privilege.

---

### 28. What is the principle of least privilege in firewall security?

It means allowing only the network traffic that is actually required.

For example, if a server only needs:

```text
SSH
HTTPS
```

there is no reason to expose unnecessary ports.

---

### 29. What is "deny by default"?

Deny by default means incoming traffic is blocked unless a specific rule allows it.

Example:

```bash
sudo ufw default deny incoming
```

Then explicitly allow required services.

---

### 30. What is the difference between a host firewall and a cloud security group?

A **host firewall** runs inside the operating system.

Examples:

```text
UFW
iptables
nftables
```

A **cloud security group** is a cloud-provider network security control applied outside the operating system.

In production, both may be used together.

---

## 🧠 Scenario-Based Interview Answer

### 31. A developer says: "The application works on localhost but not from another machine." What would you check?

I would check whether the application is listening only on localhost.

For example:

```text
127.0.0.1:8080
```

is accessible only from the same machine.

Whereas:

```text
0.0.0.0:8080
```

can listen on all IPv4 interfaces.

I would check:

```bash
sudo ss -ltnp | grep :8080
```

Then I would check:

```bash
sudo ufw status
ip addr
ip route
```

and any external/cloud firewall rules.

---

### 32. How would you troubleshoot a blocked Kubernetes application?

I would check:

```text
Pod
 ↓
Service
 ↓
NodePort / LoadBalancer
 ↓
Node network
 ↓
Host firewall
 ↓
Cloud firewall/security group
```

Useful Kubernetes commands include:

```bash
kubectl get pods -o wide
kubectl get svc
kubectl describe svc <service-name>
kubectl get endpointslice
```

Then test connectivity with:

```bash
curl
```

from an appropriate network location.

---

### 33. What is the difference between firewall and antivirus?

A **firewall** controls network traffic.

An **antivirus** detects and removes malicious software.

They provide different layers of security.

---

### 34. Can a firewall stop all attacks?

No.

A firewall is only one security layer.

A secure production environment should use multiple controls such as:

```text
Firewall
+
Authentication
+
Encryption
+
Patch management
+
Access control
+
Monitoring
+
Logging
```

---

# 🎯 Quick Interview Revision

Remember these commands:

```bash
sudo ufw status
sudo ufw status verbose
sudo ufw status numbered

sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

sudo ufw deny 8080/tcp
sudo ufw delete <rule-number>

sudo ss -ltnp
sudo ss -tulnp

sudo iptables -L -n -v
sudo nft list ruleset
```

## ⭐ Most Important Interview Points

* Firewall controls network traffic.
* Inbound = traffic coming into the server.
* Outbound = traffic leaving the server.
* UFW is a simplified firewall management tool.
* `ss` checks listening ports.
* `iptables` provides low-level firewall management.
* `nftables` is the modern Linux packet-filtering framework.
* Use least privilege.
* Prefer deny-by-default for incoming traffic where appropriate.
* Always consider host firewall + cloud firewall/security groups in production.
