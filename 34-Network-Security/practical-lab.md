# 🔐 Chapter 34 – Network Security — Practical Lab

## 📌 Overview

This practical lab focuses on applying Network Security concepts in a real Linux, Docker, Kubernetes, and AWS-style environment.

You will practice:

* Network inspection
* Listening-port security
* DNS security checks
* HTTP/HTTPS verification
* Linux firewall
* SSH security
* Packet capture
* Docker network isolation
* Kubernetes NetworkPolicy
* AWS Security Groups and NACLs
* Network troubleshooting
* Security auditing

> ⚠️ **Safety:** Perform firewall and SSH experiments on a local VM or disposable lab machine whenever possible. If you are connected to a remote server through SSH, do not change SSH/firewall rules until you have a safe recovery method.

---

# 1. Lab Environment

## Recommended Environment

| Tool            | Purpose                   |
| --------------- | ------------------------- |
| Ubuntu Linux    | Network security practice |
| Docker          | Container networking      |
| Kubernetes/kind | Kubernetes security       |
| AWS CLI         | AWS networking security   |
| tcpdump         | Packet analysis           |
| curl            | HTTP/HTTPS testing        |
| dig             | DNS testing               |
| ss              | Port inspection           |
| UFW             | Linux firewall            |

Check the environment:

```bash
cat /etc/os-release
```

```bash
uname -r
```

```bash
docker --version
```

```bash
kubectl version --client
```

```bash
aws --version
```

---

# 2. Lab 1 — Network Security Baseline

Before securing a system, understand its current state.

## Step 1: Check interfaces

```bash
ip addr
```

Short version:

```bash
ip -br addr
```

## Step 2: Check routes

```bash
ip route
```

## Step 3: Check listening ports

```bash
sudo ss -lntup
```

## Step 4: Check active connections

```bash
ss -ant
```

## Step 5: Check DNS configuration

```bash
cat /etc/resolv.conf
```

## Step 6: Check hostname

```bash
hostname
```

## Security Questions

Ask yourself:

* Which interfaces exist?
* Which IP addresses are configured?
* What is the default gateway?
* Which ports are listening?
* Which processes own those ports?
* Which DNS resolver is configured?

### Golden Rule

> **You cannot secure what you cannot see.**

---

# 3. Lab 2 — Find Unexpected Listening Ports

Run:

```bash
sudo ss -lntup
```

Example:

```text
tcp   LISTEN   0   128   0.0.0.0:22
tcp   LISTEN   0   511   0.0.0.0:80
tcp   LISTEN   0   128   127.0.0.1:631
```

Understand the difference:

```text
0.0.0.0:22
```

means the service may listen on all IPv4 interfaces.

```text
127.0.0.1:631
```

means the service is accessible only locally.

## Find a specific port

```bash
sudo ss -lntp | grep ':22'
```

```bash
sudo ss -lntp | grep ':80'
```

```bash
sudo ss -lntp | grep ':443'
```

## Security Exercise

Create a table:

| Port | Service | Required?       | Exposure   |
| ---- | ------- | --------------- | ---------- |
| 22   | SSH     | Yes             | Restricted |
| 80   | HTTP    | Maybe           | Public     |
| 443  | HTTPS   | Maybe           | Public     |
| 3306 | MySQL   | Usually private | Restricted |

### Question

If a database is listening on:

```text
0.0.0.0:3306
```

ask:

> Does the application really need the database exposed on every interface?

Usually, the answer should be **no**.

---

# 4. Lab 3 — DNS Security Checks

## Step 1: Check DNS resolver

```bash
cat /etc/resolv.conf
```

## Step 2: Resolve a domain

```bash
dig example.com
```

## Step 3: Get only the IP

```bash
dig +short example.com
```

## Step 4: Query a specific DNS server

```bash
dig @8.8.8.8 example.com
```

## Step 5: Check different record types

```bash
dig example.com A
```

```bash
dig example.com AAAA
```

```bash
dig example.com MX
```

```bash
dig example.com NS
```

## Step 6: Compare resolvers

```bash
dig example.com
```

```bash
dig @8.8.8.8 example.com
```

```bash
dig @1.1.1.1 example.com
```

Compare:

* Answer
* TTL
* Query time
* Resolver

### Security Learning

DNS is important because an attacker who manipulates DNS resolution can potentially redirect users to an unwanted destination.

---

# 5. Lab 4 — Test HTTPS Security

## Step 1: Check HTTP headers

```bash
curl -I https://example.com
```

## Step 2: Verbose HTTPS connection

```bash
curl -Iv https://example.com
```

Look for:

* TLS connection
* Certificate information
* HTTP status
* Server response

## Step 3: Follow redirects

```bash
curl -IL https://example.com
```

## Step 4: Check HTTP

```bash
curl -I http://example.com
```

Compare HTTP and HTTPS.

### Questions

1. Is the connection encrypted?
2. Does HTTP redirect to HTTPS?
3. What HTTP status code is returned?
4. Is TLS being used?

---

# 6. Lab 5 — Linux Firewall with UFW

> ⚠️ If you are working through SSH on a remote server, do not enable or modify UFW blindly. Use a local VM or ensure SSH access is explicitly allowed first.

## Step 1: Check status

```bash
sudo ufw status verbose
```

## Step 2: See numbered rules

```bash
sudo ufw status numbered
```

## Step 3: Allow SSH

```bash
sudo ufw allow 22/tcp
```

## Step 4: Allow HTTP

```bash
sudo ufw allow 80/tcp
```

## Step 5: Allow HTTPS

```bash
sudo ufw allow 443/tcp
```

## Step 6: Enable firewall

```bash
sudo ufw enable
```

Check:

```bash
sudo ufw status verbose
```

## Step 7: Delete a rule

```bash
sudo ufw delete allow 80/tcp
```

## Step 8: Reset lab rules

```bash
sudo ufw reset
```

> Only use reset in a lab environment where you understand the consequences.

---

# 7. Lab 6 — Create a Safe Test Web Service

Instead of modifying an important service, create a temporary local HTTP service.

Run:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

Keep the terminal running.

Open another terminal.

Check the port:

```bash
ss -lntp | grep ':8080'
```

Expected concept:

```text
127.0.0.1:8080
```

Test:

```bash
curl http://127.0.0.1:8080
```

### Security Observation

The service is bound to:

```text
127.0.0.1
```

Therefore it is not directly listening on the machine's external network interface.

This demonstrates an important security principle:

> **Bind services only to the interfaces where they are required.**

Stop the server with:

```text
Ctrl+C
```

---

# 8. Lab 7 — SSH Security Inspection

Check SSH service:

```bash
sudo systemctl status ssh
```

Some systems use:

```bash
sudo systemctl status sshd
```

Check port:

```bash
sudo ss -lntp | grep ':22'
```

Inspect effective SSH configuration:

```bash
sudo sshd -T
```

Check configuration file:

```bash
sudo grep -E '^(Port|PermitRootLogin|PasswordAuthentication|PubkeyAuthentication)' /etc/ssh/sshd_config
```

## SSH key information

Check your SSH directory:

```bash
ls -la ~/.ssh
```

Typical files include:

```text
id_ed25519
id_ed25519.pub
authorized_keys
known_hosts
```

## Check SSH logs

```bash
sudo journalctl -u ssh --since "30 minutes ago"
```

Or:

```bash
sudo journalctl -u sshd --since "30 minutes ago"
```

## Validate SSH configuration

Before restarting SSH after configuration changes:

```bash
sudo sshd -t
```

If there is no output, the configuration syntax is valid.

### Security Principles

Prefer:

* SSH keys
* Limited users
* Least privilege
* Strong authentication
* Restricted network access
* Logging
* Regular key rotation

---

# 9. Lab 8 — Packet Capture with tcpdump

Packet capture helps us understand what is happening on the network.

## Step 1: List interfaces

```bash
sudo tcpdump -D
```

## Step 2: Capture on loopback

```bash
sudo tcpdump -i lo
```

Stop with:

```text
Ctrl+C
```

## Step 3: Capture port 8080

Start the local HTTP server again:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

In another terminal:

```bash
sudo tcpdump -i lo port 8080
```

Then:

```bash
curl http://127.0.0.1:8080
```

Observe the packets.

## Step 4: Capture DNS

```bash
sudo tcpdump -i any port 53
```

Then:

```bash
dig example.com
```

## Step 5: Capture HTTPS traffic

```bash
sudo tcpdump -i any port 443
```

Then:

```bash
curl https://example.com
```

### Important

HTTPS encrypts application data in transit, so packet capture does not normally reveal the HTTP request body or response body in plaintext.

---

# 10. Lab 9 — Save a Packet Capture

Capture traffic into a file:

```bash
sudo tcpdump -i any port 443 -w https-test.pcap
```

Generate traffic:

```bash
curl https://example.com
```

Stop tcpdump:

```text
Ctrl+C
```

Check file:

```bash
ls -lh https-test.pcap
```

Read the capture:

```bash
tcpdump -r https-test.pcap
```

This is useful for:

* Incident investigation
* Network troubleshooting
* Protocol analysis
* Security analysis

---

# 11. Lab 10 — Docker Network Isolation

Check Docker networks:

```bash
docker network ls
```

Inspect the default bridge:

```bash
docker network inspect bridge
```

## Create a private lab network

```bash
docker network create security-lab
```

Check:

```bash
docker network ls
```

## Start a web container

```bash
docker run -d \
  --name security-web \
  --network security-lab \
  nginx
```

## Start a client container

```bash
docker run -d \
  --name security-client \
  --network security-lab \
  nginx
```

Inspect:

```bash
docker network inspect security-lab
```

You should see both containers attached to the same network.

---

# 12. Lab 11 — Docker Container-to-Container Communication

The containers can communicate through the Docker network.

Get the web container IP:

```bash
docker inspect security-web \
  --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
```

For a more convenient test, start a temporary curl container:

```bash
docker run --rm \
  --network security-lab \
  curlimages/curl \
  http://security-web
```

Docker's embedded DNS resolves:

```text
security-web
```

to the container's network address.

### Security Observation

Containers attached to the same Docker network can communicate according to network configuration.

Network segmentation can therefore reduce unnecessary communication.

---

# 13. Lab 12 — Docker Network Separation

Create another network:

```bash
docker network create isolated-lab
```

Run another container:

```bash
docker run -d \
  --name isolated-web \
  --network isolated-lab \
  nginx
```

Inspect:

```bash
docker network inspect isolated-lab
```

Now the networks are separate:

```text
security-lab
    ├── security-web
    └── security-client

isolated-lab
    └── isolated-web
```

### Security Concept

This demonstrates basic network segmentation.

> Containers should communicate only when communication is required.

---

# 14. Lab 13 — Docker Published Ports

Run:

```bash
docker run -d \
  --name public-web \
  -p 8081:80 \
  nginx
```

Check:

```bash
docker ps
```

Test:

```bash
curl http://127.0.0.1:8081
```

Inspect:

```bash
docker port public-web
```

Understand:

```text
Host Port 8081
       ↓
Container Port 80
```

## Security consideration

Published ports expose container services through the host.

Do not publish ports unnecessarily.

---

# 15. Lab 14 — Kubernetes Network Security

> ⚠️ Kubernetes `NetworkPolicy` requires a network plugin/CNI that actually enforces NetworkPolicy. The YAML object can exist even when the installed CNI does not enforce the desired policy.

Create namespace:

```bash
kubectl create namespace networking-security-lab
```

Set it as the current context namespace:

```bash
kubectl config set-context --current \
  --namespace=networking-security-lab
```

---

# 16. Create Backend Deployment

Create:

```bash
kubectl create deployment backend \
  --image=nginx \
  --replicas=2
```

Check:

```bash
kubectl get pods -o wide
```

Check labels:

```bash
kubectl get pods --show-labels
```

---

# 17. Create Backend Service

Expose the Deployment:

```bash
kubectl expose deployment backend \
  --port=80 \
  --target-port=80
```

Check:

```bash
kubectl get svc
```

Check endpoints:

```bash
kubectl get endpoints
```

Or:

```bash
kubectl get endpointslices
```

---

# 18. Create a Client Pod

Run:

```bash
kubectl run client \
  --image=busybox:1.36 \
  --restart=Never \
  -- sleep 3600
```

Check:

```bash
kubectl get pods -o wide
```

Test DNS:

```bash
kubectl exec client -- nslookup backend
```

If `nslookup` is unavailable in the image, use another diagnostic image or test service connectivity with a suitable client container.

---

# 19. Test Backend Connectivity

Get service information:

```bash
kubectl get svc backend
```

Test from the client:

```bash
kubectl exec client -- wget -qO- http://backend
```

Expected result should contain nginx HTML.

This demonstrates:

```text
Client Pod
    |
    | DNS
    ↓
backend Service
    |
    ↓
Backend Pods
```

---

# 20. Lab 15 — Kubernetes Default-Deny NetworkPolicy

Create:

```bash
cat > default-deny.yaml <<'EOF'
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}
  policyTypes:
    - Ingress
EOF
```

Apply:

```bash
kubectl apply -f default-deny.yaml
```

Check:

```bash
kubectl get networkpolicy
```

Describe:

```bash
kubectl describe networkpolicy default-deny-ingress
```

### Concept

The policy selects all Pods in the namespace and establishes default-deny ingress behavior.

---

# 21. Lab 16 — Allow Client → Backend

First inspect labels:

```bash
kubectl get pods --show-labels
```

The client Pod should have:

```text
run=client
```

Create:

```bash
cat > allow-client-to-backend.yaml <<'EOF'
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-client-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              run: client
      ports:
        - protocol: TCP
          port: 80
EOF
```

Apply:

```bash
kubectl apply -f allow-client-to-backend.yaml
```

Check:

```bash
kubectl get networkpolicy
```

Test:

```bash
kubectl exec client -- wget -qO- http://backend
```

### Security Model

```text
Client
  |
  | TCP/80
  ↓
Backend
```

Allowed because:

```text
Source: run=client
Destination: app=backend
Port: 80/TCP
```

Other ingress traffic remains restricted by the default-deny policy.

> If traffic is not actually blocked/allowed as expected, check whether your CNI supports and enforces NetworkPolicy.

---

# 22. Lab 17 — Kubernetes Security Inspection

Check NetworkPolicies:

```bash
kubectl get networkpolicy
```

Check Pods:

```bash
kubectl get pods -o wide
```

Check Services:

```bash
kubectl get svc
```

Check EndpointSlices:

```bash
kubectl get endpointslices
```

Check events:

```bash
kubectl get events --sort-by=.lastTimestamp
```

Describe a Pod:

```bash
kubectl describe pod <pod-name>
```

Check labels:

```bash
kubectl get pods --show-labels
```

### Troubleshooting Questions

If traffic fails:

1. Does the Service exist?
2. Does the Service have endpoints?
3. Are selectors correct?
4. Is DNS resolving?
5. Is the Pod ready?
6. Is NetworkPolicy blocking traffic?
7. Does the CNI enforce NetworkPolicy?

---

# 23. Lab 18 — AWS Security Group Inspection

Make sure AWS CLI is configured.

Check identity:

```bash
aws sts get-caller-identity
```

List security groups:

```bash
aws ec2 describe-security-groups
```

List only IDs and names:

```bash
aws ec2 describe-security-groups \
  --query 'SecurityGroups[*].[GroupId,GroupName]' \
  --output table
```

Inspect one Security Group:

```bash
aws ec2 describe-security-groups \
  --group-ids <security-group-id>
```

### Questions

Check:

* Which inbound ports are open?
* Which sources are allowed?
* Is SSH open to `0.0.0.0/0`?
* Is a database port publicly accessible?
* Are outbound rules restricted?

### Security Principle

Avoid unnecessarily broad rules such as:

```text
0.0.0.0/0
```

for sensitive services.

---

# 24. Lab 19 — AWS NACL Inspection

List NACLs:

```bash
aws ec2 describe-network-acls
```

Get IDs:

```bash
aws ec2 describe-network-acls \
  --query 'NetworkAcls[*].NetworkAclId' \
  --output table
```

Inspect a NACL:

```bash
aws ec2 describe-network-acls \
  --network-acl-ids <network-acl-id>
```

Review:

* Rule number
* Protocol
* Port range
* Source/destination
* Allow/Deny
* Inbound/Outbound

### Remember

Security Groups are:

```text
Stateful
```

NACLs are:

```text
Stateless
```

---

# 25. Lab 20 — Public vs Private Subnet Security

Understand the architecture:

```text
Internet
    |
    ↓
Internet Gateway
    |
    ↓
Public Subnet
    |
    ↓
Load Balancer / Bastion
    |
    ↓
Private Subnet
    |
    ↓
Application
    |
    ↓
Database
```

A secure architecture commonly keeps sensitive workloads in private subnets.

Example:

```text
Public:
- Load Balancer
- Bastion (if required)

Private:
- Application servers
- Kubernetes worker nodes
- Databases
```

---

# 26. Lab 21 — Security Audit

Create a security audit table.

| Check               | Command                            | Result |
| ------------------- | ---------------------------------- | ------ |
| Interfaces          | `ip addr`                          |        |
| Routes              | `ip route`                         |        |
| Listening ports     | `sudo ss -lntup`                   |        |
| DNS                 | `dig example.com`                  |        |
| Firewall            | `sudo ufw status`                  |        |
| SSH                 | `systemctl status ssh`             |        |
| Logs                | `journalctl`                       |        |
| Docker networks     | `docker network ls`                |        |
| Kubernetes policies | `kubectl get networkpolicy`        |        |
| AWS SG              | `aws ec2 describe-security-groups` |        |
| AWS NACL            | `aws ec2 describe-network-acls`    |        |

---

# 27. Lab 22 — Find the Attack Surface

Run:

```bash
sudo ss -lntup
```

For every exposed service, answer:

### Question 1

What service is running?

### Question 2

Why is it running?

### Question 3

Who needs access?

### Question 4

From where should access be allowed?

### Question 5

Can the service be restricted to:

```text
127.0.0.1
```

or a private interface?

### Question 6

Does it require encryption?

### Question 7

Is authentication required?

---

# 28. Lab 23 — Troubleshooting Scenario: Connection Refused

Test:

```bash
curl http://127.0.0.1:9999
```

You may receive:

```text
Connection refused
```

Troubleshoot:

```bash
sudo ss -lntup | grep ':9999'
```

Check service status:

```bash
sudo systemctl status <service>
```

Check logs:

```bash
sudo journalctl -u <service>
```

### Mental Model

```text
Client
  |
  ↓
DNS
  |
  ↓
IP
  |
  ↓
Route
  |
  ↓
Firewall
  |
  ↓
Port
  |
  ↓
Service
```

---

# 29. Lab 24 — Troubleshooting Scenario: Timeout

A timeout is different from connection refused.

Test:

```bash
curl -v http://<server-ip>:<port>
```

Check:

```bash
ip route
```

```bash
ping -c 4 <server-ip>
```

```bash
nc -vz <server-ip> <port>
```

Check firewall:

```bash
sudo ufw status verbose
```

Check listening service:

```bash
sudo ss -lntup
```

For AWS, inspect:

* Security Group
* NACL
* Route Table
* Internet Gateway
* NAT Gateway
* Subnet
* Network interface

---

# 30. Lab 25 — Troubleshooting DNS Failure

Test:

```bash
dig example.com
```

Then:

```bash
getent hosts example.com
```

Check:

```bash
cat /etc/resolv.conf
```

Test direct DNS:

```bash
dig @8.8.8.8 example.com
```

If direct DNS works but normal resolution does not, investigate:

* Resolver configuration
* Local DNS service
* Network access to DNS
* Firewall
* DNS search domains

---

# 31. Lab 26 — Troubleshooting HTTPS Failure

Run:

```bash
curl -Iv https://example.com
```

Check DNS:

```bash
dig example.com
```

Check route:

```bash
ip route
```

Check port:

```bash
nc -vz example.com 443
```

Check packet traffic:

```bash
sudo tcpdump -i any port 443
```

Think through:

```text
DNS
 ↓
IP
 ↓
Route
 ↓
TCP/443
 ↓
TLS
 ↓
HTTP
```

---

# 32. Lab 27 — Security Logging

View recent system logs:

```bash
sudo journalctl -n 100
```

Follow logs:

```bash
sudo journalctl -f
```

SSH logs:

```bash
sudo journalctl -u ssh
```

Firewall-related logs:

```bash
sudo journalctl | grep -i ufw
```

Kernel messages:

```bash
dmesg | grep -i network
```

Look for:

* Failed logins
* Unexpected connections
* Service failures
* Firewall blocks
* Interface errors
* Network configuration changes

---

# 33. Lab 28 — Least Privilege Exercise

For each service, define the minimum required access.

Example:

| Service | Source        | Destination   | Port | Protocol |
| ------- | ------------- | ------------- | ---- | -------- |
| SSH     | Admin network | Server        | 22   | TCP      |
| HTTP    | Internet      | Load Balancer | 80   | TCP      |
| HTTPS   | Internet      | Load Balancer | 443  | TCP      |
| App     | Load Balancer | App           | 8080 | TCP      |
| DB      | App           | Database      | 3306 | TCP      |

Avoid:

```text
Any → Any → Any
```

Prefer:

```text
Specific Source
      ↓
Specific Destination
      ↓
Specific Port
      ↓
Specific Protocol
```

---

# 34. Lab 29 — Defense in Depth

Build a security model using multiple layers:

```text
                    Internet
                       |
                       ↓
                     WAF
                       |
                       ↓
                Load Balancer
                       |
                       ↓
               Security Group
                       |
                       ↓
                Private Subnet
                       |
                       ↓
               NetworkPolicy
                       |
                       ↓
                 Application
                       |
                       ↓
                Authentication
                       |
                       ↓
                   Database
```

Possible controls:

* Firewall
* Security Groups
* NACLs
* NetworkPolicy
* TLS
* Authentication
* Authorization
* Logging
* Monitoring
* Secrets management
* Network segmentation

---

# 35. Lab 30 — Final Network Security Checklist

## Host Security

* [ ] Unnecessary services disabled
* [ ] Listening ports reviewed
* [ ] Firewall configured
* [ ] SSH secured
* [ ] Logs monitored
* [ ] Software updated

## Network Security

* [ ] Network segmentation implemented
* [ ] Private networks used where appropriate
* [ ] Least privilege applied
* [ ] Unnecessary ports blocked
* [ ] DNS monitored
* [ ] TLS used for sensitive traffic

## Docker Security

* [ ] Unnecessary ports not published
* [ ] Networks separated where required
* [ ] Container communication restricted
* [ ] Images trusted and updated

## Kubernetes Security

* [ ] NetworkPolicies considered
* [ ] CNI enforcement verified
* [ ] Services exposed only when required
* [ ] Namespaces used for organization/isolation
* [ ] Cluster API access protected

## AWS Security

* [ ] Security Groups reviewed
* [ ] NACLs reviewed
* [ ] Public exposure minimized
* [ ] Private subnets used for sensitive workloads
* [ ] NAT/VPC endpoints understood
* [ ] IAM least privilege applied

---

# 36. Final Practical Challenge

Build this architecture mentally and explain every security layer:

```text
                         Internet
                            |
                            ↓
                          WAF
                            |
                            ↓
                     Load Balancer
                            |
                            ↓
                    Public Subnet
                            |
                            ↓
                   Private App Tier
                     /          \
                    /            \
                   ↓              ↓
             Kubernetes       Application
                Pods              |
                   |              |
                   └──────┬───────┘
                          ↓
                       Database
```

Answer:

### 1. Which components should be public?

### 2. Which components should be private?

### 3. Where would you use TLS?

### 4. Where would you use a firewall?

### 5. Where would you use Security Groups?

### 6. Where would you use NetworkPolicy?

### 7. Which ports should be open?

### 8. Which traffic should be denied?

### 9. How would you monitor suspicious traffic?

### 10. How would you troubleshoot if the application cannot reach the database?

---

# 37. Network Security Troubleshooting Flow

Use this flow in real DevOps work:

```text
1. Identify the source
        ↓
2. Identify the destination
        ↓
3. Resolve DNS
        ↓
4. Check IP address
        ↓
5. Check routing
        ↓
6. Check firewall
        ↓
7. Check Security Group/NACL
        ↓
8. Check port
        ↓
9. Check service
        ↓
10. Check authentication
        ↓
11. Check TLS
        ↓
12. Check logs
        ↓
13. Capture packets if necessary
        ↓
14. Fix the smallest required layer
        ↓
15. Retest
```

---

# 🎯 Chapter 34 Practical Goals

After completing this lab, you should be able to:

* Inspect Linux network security
* Find exposed ports
* Analyze DNS
* Test HTTP/HTTPS
* Configure a basic Linux firewall safely
* Inspect SSH security
* Capture packets using tcpdump
* Understand Docker network isolation
* Understand published Docker ports
* Create Kubernetes NetworkPolicies
* Understand CNI dependency
* Inspect AWS Security Groups
* Inspect AWS NACLs
* Understand public/private subnet security
* Apply least privilege
* Apply defense in depth
* Troubleshoot network-security failures

---

# 🧠 Interview Mental Model

When asked:

> **"How do you secure a network?"**

Think:

```text
Visibility
   ↓
Authentication
   ↓
Authorization
   ↓
Least Privilege
   ↓
Segmentation
   ↓
Firewall
   ↓
Encryption
   ↓
Monitoring
   ↓
Logging
   ↓
Detection
   ↓
Response
```

## Golden Rule

> 🔐 **Allow only the traffic that is required, from the source that is authorized, to the destination that is needed, using the required protocol and port — and monitor it.**
