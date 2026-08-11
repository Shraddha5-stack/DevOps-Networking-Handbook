# 🌐 Chapter 15 – Ports & Protocols: Real-World Use Cases

## 1. SSH Server Administration

### Scenario

A DevOps engineer needs to connect to a Linux server remotely.

SSH commonly uses:

```text
TCP 22
```

Flow:

```text
Developer Laptop
      |
      | TCP 22
      ↓
Linux Server
      |
      ↓
SSH Service
```

Command:

```bash
ssh user@server-ip
```

### DevOps Use

SSH is commonly used for:

* Server administration
* Troubleshooting
* Log inspection
* Configuration
* Secure file transfer
* Automation

---

# 2. Web Application – HTTP/HTTPS

A typical web application uses:

```text
HTTP  → 80
HTTPS → 443
```

Production traffic generally uses HTTPS.

Architecture:

```text
User
 ↓
HTTPS :443
 ↓
Load Balancer
 ↓
Application Server
```

Example:

```bash
curl -I https://example.com
```

### DevOps Use

Ports 80 and 443 are commonly involved in:

* Web servers
* Load balancers
* Reverse proxies
* Ingress controllers
* Cloud deployments

---

# 3. Application Server on Port 8080

Many applications use a non-default application port such as `8080`.

Example:

```text
User
  ↓
Load Balancer :443
  ↓
Application :8080
```

The application may listen on:

```text
0.0.0.0:8080
```

Check:

```bash
sudo ss -tulpn | grep :8080
```

Test:

```bash
curl http://localhost:8080
```

### DevOps Use

Port `8080` is commonly encountered with:

* Java applications
* Development servers
* Internal APIs
* Jenkins installations
* Application containers

---

# 4. Database Connectivity

An application may need to communicate with a database.

Common database ports:

```text
MySQL      → 3306
PostgreSQL → 5432
Redis      → 6379
```

Architecture:

```text
Internet
   ↓
Load Balancer
   ↓
Application
   ↓
Database
```

The database should normally be placed in a private network rather than directly exposed to the Internet.

---

# 5. AWS Security Groups

In AWS, Security Groups control inbound and outbound traffic associated with resources such as EC2 instances.

Example:

```text
Security Group
│
├── TCP 22   → SSH
├── TCP 80   → HTTP
└── TCP 443  → HTTPS
```

A production architecture may allow:

```text
Internet
   ↓
443
   ↓
Load Balancer
   ↓
Application
```

while restricting database access to trusted application resources.

### DevOps Importance

When an application works locally but not remotely, checking the relevant AWS Security Group is an important troubleshooting step.

---

# 6. Docker Port Mapping

Docker can expose a container service through a host port.

Example:

```bash
docker run -p 8080:80 nginx
```

Architecture:

```text
Host
8080
  ↓
Container
80
  ↓
Nginx
```

Check:

```bash
docker ps
```

Example output may contain:

```text
0.0.0.0:8080->80/tcp
```

This means host port `8080` maps to container port `80`.

---

# 7. Docker Compose

A Compose application can define port mappings.

Example:

```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80"
```

Flow:

```text
localhost:8080
       ↓
Container:80
       ↓
Nginx
```

### DevOps Use

Port mapping is important when running:

* Local development environments
* Multi-container applications
* Testing environments
* CI/CD integration tests

---

# 8. Kubernetes Service Ports

Kubernetes applications commonly use Services to expose Pods.

Example concept:

```text
Client
  ↓
Service :80
  ↓
targetPort :8080
  ↓
Pod
```

The application inside the Pod can listen on `8080`, while the Service exposes port `80`.

Useful commands:

```bash
kubectl get svc
```

```bash
kubectl describe svc <service-name>
```

### DevOps Importance

Incorrect `port` or `targetPort` configuration can cause an application to appear unreachable even when the Pod itself is running.

---

# 9. Load Balancer

A load balancer can accept traffic on one port and forward it to another port.

Example:

```text
Internet
   ↓
HTTPS :443
   ↓
Load Balancer
   ↓
HTTP :8080
   ↓
Application
```

This allows the public endpoint and internal application port to be different.

---

# 10. Reverse Proxy

A reverse proxy such as Nginx can listen on standard web ports and forward requests to an application.

Example:

```text
Client
  ↓
HTTPS :443
  ↓
Nginx
  ↓
Application :8080
```

Check Nginx listening ports:

```bash
sudo ss -tulpn | grep nginx
```

### DevOps Use

Reverse proxies are commonly used for:

* TLS termination
* Routing
* Load balancing
* Security controls
* Serving static content

---

# 11. Firewall Troubleshooting

Suppose an application listens on:

```text
8080
```

but users cannot access it.

First check:

```bash
sudo ss -tulpn | grep :8080
```

If the service is listening, check firewall rules:

```bash
sudo ufw status
```

Then test locally:

```bash
nc -zv localhost 8080
```

Then test remotely:

```bash
nc -zv <server-ip> 8080
```

This helps isolate whether the problem is:

```text
Application
     ↓
Local network
     ↓
Firewall
     ↓
Remote network
```

---

# 12. CI/CD Server

DevOps tools often expose web interfaces on specific ports.

For example, a CI/CD server may run on:

```text
8080
```

Architecture:

```text
Developer
   ↓
HTTPS
   ↓
Reverse Proxy
   ↓
CI/CD Server :8080
```

The exact port depends on the application's configuration.

### DevOps Importance

Port knowledge helps when:

* Installing CI/CD tools
* Configuring reverse proxies
* Creating firewall rules
* Setting cloud security groups
* Troubleshooting connectivity

---

# 13. Monitoring Systems

Monitoring tools communicate over network ports.

For example:

```text
Monitoring Server
       ↓
Exporter / Agent
       ↓
Metrics Port
```

A monitoring engineer may need to verify whether the expected metrics endpoint is listening.

Useful command:

```bash
sudo ss -tulpn
```

And for HTTP-based metrics:

```bash
curl http://localhost:<port>/metrics
```

---

# 14. Microservices Architecture

In a microservices environment, different services can listen on different ports.

Example:

```text
Frontend
   ↓
:3000
   ↓
API Gateway
   ↓
:8080
   ↓
User Service
   ↓
:8081
   ↓
Order Service
   ↓
:8082
```

Each service has its own network endpoint.

### DevOps Challenge

A wrong port configuration can prevent one microservice from communicating with another.

---

# 15. DNS Troubleshooting

DNS commonly uses port:

```text
53
```

Check DNS:

```bash
nslookup example.com
```

or:

```bash
dig example.com
```

DNS can use both UDP and TCP depending on the situation.

### DevOps Importance

If DNS resolution fails, applications may appear unreachable even when the network itself is functioning.

---

# 16. DHCP

DHCP commonly uses:

```text
UDP 67 → Server
UDP 68 → Client
```

Basic process:

```text
Client
  ↓
Discover
  ↓
Server
  ↓
Offer
  ↓
Client
  ↓
Request
  ↓
Server
  ↓
ACK
```

DHCP provides network configuration such as:

* IP address
* Subnet mask
* Gateway
* DNS server

---

# 17. Port Scanning During Security Audits

Administrators may inspect which ports are exposed on a system.

For local inspection:

```bash
sudo ss -tulpn
```

For a controlled test environment, tools such as `nmap` can be used to identify exposed services.

Example:

```bash
nmap <server-ip>
```

### Security Principle

Only required services should be exposed.

Unused services increase the attack surface.

---

# 18. "Ping Works but Application Doesn't"

This is a common troubleshooting scenario.

Suppose:

```text
ping server-ip
```

works, but:

```bash
nc -zv server-ip 443
```

fails.

This can happen because:

```text
ICMP
 ↓
Allowed

TCP 443
 ↓
Blocked / unavailable
```

Possible causes:

* Firewall
* Security Group
* Service not listening
* Network policy
* Wrong port

Therefore:

> Successful ping does not prove application-port connectivity.

---

# 19. "Application Works Locally but Not Remotely"

Suppose:

```bash
curl http://localhost:8080
```

works.

But:

```bash
curl http://server-ip:8080
```

fails from another machine.

Check:

```bash
sudo ss -tulpn | grep :8080
```

If the service is bound to:

```text
127.0.0.1:8080
```

it is only listening on the loopback interface.

A service intended to accept remote traffic must listen on an appropriate interface, subject to firewall and security controls.

---

# 20. Real-World Troubleshooting Flow

When a user reports:

> "The application is down."

Use:

```text
DNS
 ↓
IP Address
 ↓
Routing
 ↓
Firewall
 ↓
Listening Port
 ↓
Process
 ↓
Application
 ↓
Response
```

Useful commands:

```bash
nslookup example.com
```

```bash
ip route
```

```bash
sudo ss -tulpn
```

```bash
nc -zv <host> <port>
```

```bash
curl -v <url>
```

```bash
sudo ufw status
```

---

# 💼 DevOps Interview Scenario

### Question

> A developer says the application is running on port 8080, but users cannot access it. What will you do?

### Answer

> First, I would verify that the application process is running and listening on port 8080 using `ss -tulpn`. Then I would test the port locally using `nc`. If local connectivity works, I would test it remotely. If remote access fails, I would check the host firewall, cloud Security Group, network ACLs, routing, and whether the application is bound to the correct interface. Finally, I would use `curl` to determine whether the issue is network-level or application-level.

---

# 🎯 Key Takeaways

```text
IP Address
   ↓
Identifies host

Port
   ↓
Identifies service endpoint

Protocol
   ↓
Defines communication rules

Firewall
   ↓
Controls allowed traffic

Service
   ↓
Listens on a port

Application
   ↓
Processes the request
```

Understanding this flow is essential for Linux, AWS, Docker, Kubernetes, and CI/CD troubleshooting.
