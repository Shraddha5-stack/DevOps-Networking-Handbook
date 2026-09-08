# 🔄 CI/CD Networking — Detailed Notes

## Chapter 33 — CI/CD Networking

CI/CD networking is the networking foundation behind automated software delivery.

A CI/CD pipeline does not work in isolation. It continuously communicates with external and internal systems such as:

```text
Developer
    ↓
Git Repository
    ↓
CI/CD Runner
    ↓
Package Repository
    ↓
Container Registry
    ↓
Cloud
    ↓
Kubernetes
    ↓
Application
```

Every arrow represents network communication.

---

# 1. What is CI/CD?

## CI — Continuous Integration

Continuous Integration means frequently integrating code changes into a shared repository and automatically:

* Building code
* Running tests
* Performing code checks
* Generating artifacts

Example:

```text
Developer
    ↓
git push
    ↓
Git Repository
    ↓
CI Pipeline
    ↓
Build
    ↓
Test
```

---

# 2. What is CD?

CD can mean:

### Continuous Delivery

The software is automatically built, tested, and prepared for release.

### Continuous Deployment

The software is automatically deployed to the target environment.

Example:

```text
Code
 ↓
Build
 ↓
Test
 ↓
Package
 ↓
Deploy
 ↓
Production
```

---

# 3. Why Networking Matters in CI/CD

Suppose a pipeline contains:

```bash
git clone ...
docker pull ...
docker push ...
kubectl apply ...
```

Every operation may require network communication.

For example:

```text
git clone
   ↓
HTTPS/SSH
   ↓
Git server
```

```text
docker push
   ↓
HTTPS
   ↓
Container Registry
```

```text
kubectl apply
   ↓
HTTPS
   ↓
Kubernetes API Server
```

Therefore:

> CI/CD failures can be caused by networking even when the application code is correct.

---

# 4. Basic CI/CD Network Flow

A simple pipeline:

```text
                  Developer
                      |
                      | HTTPS
                      v
               Git Repository
                      |
                   Webhook
                      |
                      v
                 CI Runner
                      |
          +-----------+-----------+
          |                       |
          v                       v
       Build                    Test
          |
          v
      Docker Build
          |
          v
  Container Registry
          |
          v
       Kubernetes
          |
          v
      Application
```

---

# 5. Important CI/CD Components

## 5.1 Git Repository

Stores source code.

Examples:

* GitHub
* GitLab
* Bitbucket

Communication commonly uses:

```text
HTTPS
SSH
```

---

## 5.2 CI/CD Server

Responsible for coordinating pipeline execution.

Examples:

* GitHub Actions
* GitLab CI/CD
* Jenkins

The CI/CD platform may:

* Receive events
* Start jobs
* Manage workflows
* Store logs
* Trigger deployments

---

## 5.3 Runner

A runner executes pipeline commands.

Example:

```text
CI Server
    |
    v
Runner
    |
    +--- git
    +--- docker
    +--- kubectl
    +--- aws
```

The runner needs network access to whatever services the job uses.

---

# 6. Hosted Runner

A hosted runner is managed by the CI/CD provider.

Architecture:

```text
Git Provider
     |
     v
Managed Runner
     |
     +--- Internet
     |
     +--- Public Services
```

Advantages:

* Easy to use
* No server maintenance
* Quick setup
* Provider-managed infrastructure

---

# 7. Self-Hosted Runner

A self-hosted runner is infrastructure managed by your organization.

Example:

```text
                 Git Provider
                      |
                      | HTTPS
                      v
               Self-Hosted Runner
                 Private Network
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       AWS VPC    Kubernetes   Internal API
```

Self-hosted runners are useful when pipelines need access to:

* Private servers
* Internal APIs
* Private Kubernetes clusters
* Private databases
* Internal package repositories

---

# 8. Runner Network Requirements

A runner may need access to:

```text
Git
Container Registry
Cloud APIs
Package Repositories
Kubernetes API
Artifact Repository
Deployment Servers
```

Typical protocol:

```text
HTTPS : 443
```

Other ports depend on the application.

---

# 9. Git Networking

Git communicates with remote repositories using protocols such as:

```text
HTTPS
SSH
```

### HTTPS

Example:

```bash
git clone https://github.com/user/project.git
```

Usually uses:

```text
TCP 443
```

### SSH

Example:

```bash
git clone git@github.com:user/project.git
```

Commonly uses:

```text
TCP 22
```

---

# 10. DNS in CI/CD

DNS converts names into IP addresses or other DNS records.

Example:

```text
registry.example.com
        |
        v
      DNS
        |
        v
    IP Address
```

If DNS fails:

```text
CI Runner
    |
    X
DNS Resolution
```

The pipeline may fail before it even reaches the destination.

Useful command:

```bash
dig registry.example.com
```

---

# 11. TCP in CI/CD

TCP provides reliable transport for many CI/CD connections.

Example:

```text
Runner
  |
  | TCP 443
  |
  v
Git Server
```

TCP provides:

* Connection establishment
* Reliable delivery
* Ordering
* Retransmission

---

# 12. HTTPS in CI/CD

HTTPS is one of the most common protocols in modern CI/CD systems.

Used for:

* Git repositories
* Cloud APIs
* Container registries
* Webhooks
* Kubernetes API
* Package repositories

Typical port:

```text
443
```

---

# 13. Container Registry Networking

A CI/CD system commonly builds a container:

```bash
docker build -t myapp:1.0 .
```

Then pushes it:

```bash
docker push registry.example.com/myapp:1.0
```

Network flow:

```text
CI Runner
    |
    | HTTPS
    v
Container Registry
```

During deployment:

```text
Kubernetes Node
      |
      | HTTPS
      v
Container Registry
      |
      v
Docker Image
```

---

# 14. Docker Registry Authentication

A registry normally requires authentication before pushing private images.

Example:

```text
CI Runner
    |
    | Authentication
    v
Registry
    |
    | Authorized
    v
docker push
```

Credentials should be stored securely.

Never put credentials directly in source code.

---

# 15. Package Repository Networking

Build systems frequently download dependencies.

Examples:

```text
npm
pip
Maven
Gradle
apt
yum/dnf
```

Example:

```text
CI Runner
    |
    | HTTPS
    v
Package Repository
    |
    v
Dependencies
```

If package downloads fail, investigate:

* DNS
* Internet access
* Proxy
* Firewall
* Repository availability
* Authentication

---

# 16. Webhooks

A webhook allows one system to notify another system about an event.

Example:

```text
Developer
    |
    v
git push
    |
    v
GitHub
    |
    | HTTPS webhook
    v
CI/CD Server
    |
    v
Pipeline
```

Webhook events can include:

* Push
* Pull Request
* Release
* Tag

---

# 17. Webhook Inbound vs Outbound Traffic

This distinction is important.

### Outbound

Runner connects to external services:

```text
Runner → Git
Runner → Registry
Runner → AWS
```

### Inbound

External service connects to your CI/CD server:

```text
GitHub → Webhook Endpoint
```

A self-hosted CI/CD server may need special firewall or reverse-proxy configuration for inbound webhooks.

---

# 18. Proxy in CI/CD

Organizations sometimes require Internet traffic to go through a proxy.

Architecture:

```text
CI Runner
    |
    v
Corporate Proxy
    |
    v
Internet
```

Environment variables may look like:

```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
```

Exceptions can be configured with:

```bash
export NO_PROXY=localhost,127.0.0.1
```

Exact values depend on the environment.

---

# 19. Why Proxy Causes CI/CD Failures

Suppose:

```text
git clone
```

works on your laptop but fails on the CI runner.

Possible reason:

```text
Laptop
   |
Internet
   |
GitHub
```

but:

```text
CI Runner
   |
Corporate Proxy
   |
Firewall
   |
GitHub
```

The proxy may:

* Block the destination
* Require authentication
* Inspect TLS
* Restrict domains
* Modify traffic behavior

---

# 20. Firewall in CI/CD

Firewalls control network traffic.

Possible firewall layers:

```text
Internet Firewall
       ↓
Cloud Security Group
       ↓
NACL
       ↓
Host Firewall
       ↓
Container Firewall/Policy
       ↓
Application
```

A blocked connection may appear as:

```text
Connection timeout
```

---

# 21. AWS Security Groups and CI/CD

Suppose a CI runner needs to connect to an EC2 application server.

Example:

```text
CI Runner
    |
    | TCP 22 / 443 / custom port
    v
EC2
```

The EC2 Security Group must allow the required traffic from an appropriate source.

Avoid:

```text
0.0.0.0/0
```

for administrative access whenever possible.

---

# 22. Kubernetes API Networking

`kubectl` communicates with the Kubernetes API server.

Typical API endpoint:

```text
https://<kubernetes-api>:6443
```

Flow:

```text
CI Runner
    |
    | HTTPS
    v
Kubernetes API Server
    |
    v
Cluster
```

The runner requires:

* Network connectivity
* Authentication
* Authorization/RBAC

---

# 23. Kubernetes NetworkPolicy

After a deployment reaches Kubernetes, Pod-to-Pod communication may be controlled by NetworkPolicies.

Example:

```text
Frontend Pod
     |
     | Allowed
     v
Backend Pod
     |
     | Allowed
     v
Database
```

A restrictive policy can block expected application traffic.

Therefore deployment troubleshooting may involve both:

```text
CI/CD networking
+
Kubernetes networking
```

---

# 24. AWS Private Subnet and CI/CD

Suppose a self-hosted runner is inside a private subnet.

Architecture:

```text
              AWS VPC
                 |
          Private Subnet
                 |
          Self-Hosted Runner
                 |
          +------+------+
          |             |
          v             v
       AWS APIs      Internet
                       |
                    NAT Gateway
                       |
                  Internet Gateway
```

The runner may need:

* NAT Gateway
* VPC Endpoints
* DNS
* Route Tables
* Security Groups
* NACLs

---

# 25. VPC Endpoints for CI/CD

Private workloads often need access to AWS services.

Instead of sending traffic through the public Internet path, supported AWS services can be reached using VPC endpoints.

Example:

```text
Private Runner
      |
      v
VPC Endpoint
      |
      v
AWS Service
```

Benefits can include:

* Private connectivity
* Reduced Internet dependency
* Better network control

---

# 26. VPN in CI/CD

A runner may need access to a private corporate network.

Example:

```text
CI/CD Runner
      |
      | VPN
      v
Corporate Network
      |
      +--- Internal API
      |
      +--- Private Server
      |
      +--- Private Kubernetes
```

VPN provides encrypted connectivity between networks.

---

# 27. CI/CD and SSH

SSH is commonly used for:

* Remote server administration
* Git operations
* Deployment to Linux servers
* Secure file transfer

Typical port:

```text
22
```

Example:

```bash
ssh user@server
```

Network flow:

```text
CI Runner
    |
    | TCP 22
    v
Linux Server
```

---

# 28. CI/CD Deployment Over SSH

A simple deployment might look like:

```text
CI Runner
    |
    | SSH
    v
Application Server
    |
    v
Deploy Application
```

Security considerations:

* Use dedicated deployment keys
* Restrict source access
* Use least privilege
* Protect private keys
* Avoid exposing SSH unnecessarily

---

# 29. Artifact Networking

Build artifacts can include:

* `.jar`
* `.war`
* `.zip`
* Binary files
* Reports
* Packages

Flow:

```text
CI Runner
    |
    | HTTPS
    v
Artifact Repository
    |
    v
Deployment
```

---

# 30. Load Balancer and CI/CD

After deployment, application traffic may flow through a Load Balancer.

Example:

```text
Users
  |
  v
Load Balancer
  |
  +---- Application 1
  |
  +---- Application 2
  |
  +---- Application 3
```

CI/CD deploys new application versions behind the Load Balancer.

---

# 31. Blue-Green Deployment Networking

Two environments exist:

```text
             Load Balancer
                  |
          +-------+-------+
          |               |
        BLUE             GREEN
       v1.0               v2.0
```

Traffic can initially go to BLUE.

After validating GREEN:

```text
Load Balancer
      |
      v
    GREEN
     v2.0
```

Networking is important when switching traffic between environments.

---

# 32. Canary Deployment Networking

Canary deployment sends a small percentage of traffic to the new version.

Example:

```text
              Load Balancer
                    |
          +---------+---------+
          |                   |
        90%                 10%
          |                   |
       Version 1           Version 2
```

If the new version is healthy:

```text
10%
 ↓
25%
 ↓
50%
 ↓
100%
```

Traffic routing can be implemented using load balancers, ingress controllers, service meshes, or other deployment mechanisms.

---

# 33. Reverse Proxy in CI/CD

A reverse proxy sits in front of a service.

Example:

```text
Internet
   |
   v
Reverse Proxy
   |
   v
CI/CD Server
```

It can provide:

* TLS termination
* Routing
* Authentication integration
* Access control
* Logging

---

# 34. TLS in CI/CD

TLS protects network communication.

Examples:

```text
Runner → Git
Runner → Registry
Runner → Kubernetes API
User → Application
```

Usually:

```text
HTTPS = HTTP + TLS
```

TLS provides:

* Encryption
* Integrity
* Server authentication

---

# 35. Network Latency in CI/CD

Latency is the time required for data to travel between systems.

Example:

```text
Runner
   |
   | 200 ms
   v
Registry
```

High latency can slow:

* Git clone
* Docker pull
* Docker push
* Dependency downloads
* Deployment API calls

---

# 36. Bandwidth in CI/CD

Bandwidth determines how much data can be transferred over time.

Large Docker images can consume significant bandwidth.

Example:

```text
CI Runner
    |
    | 2 GB image
    v
Registry
```

Optimize by:

* Using smaller images
* Multi-stage builds
* Caching dependencies
* Avoiding unnecessary layers

---

# 37. Network Timeout

A timeout occurs when a connection or request does not receive an expected response within the configured period.

Possible causes:

```text
DNS
 ↓
Routing
 ↓
Firewall
 ↓
Security Group
 ↓
NACL
 ↓
Proxy
 ↓
Destination
```

Useful command:

```bash
curl -v https://example.com
```

---

# 38. Connection Refused

A connection refused response usually means the network path reached the destination host, but no service accepted the connection on that port or the host actively rejected it.

Example:

```text
CI Runner
   |
   v
Server
   |
   X
Port 8080
```

Check:

```bash
ss -lntp
```

---

# 39. DNS Failure vs Network Failure

### DNS Failure

The hostname cannot be resolved.

```text
registry.example.com
        |
        X
       DNS
```

Test:

```bash
dig registry.example.com
```

### Network Failure

The name resolves but the destination cannot be reached.

```text
DNS
 ↓
IP
 ↓
 X
Network
```

Test:

```bash
curl -v https://registry.example.com
```

---

# 40. CI/CD Troubleshooting Method

Always identify:

```text
SOURCE
DESTINATION
PROTOCOL
PORT
NETWORK PATH
SECURITY CONTROLS
```

Example:

```text
SOURCE:
CI Runner

DESTINATION:
Kubernetes API

PROTOCOL:
HTTPS

PORT:
6443

SECURITY:
Firewall + Security Group + RBAC

APPLICATION:
Kubernetes API
```

---

# 41. Layer-by-Layer Troubleshooting

Use this order:

```text
1. DNS
     ↓
2. IP
     ↓
3. Route
     ↓
4. Gateway
     ↓
5. Firewall
     ↓
6. Security Group
     ↓
7. NACL
     ↓
8. Proxy
     ↓
9. Port
     ↓
10. Authentication
     ↓
11. Application
```

This prevents random troubleshooting.

---

# 42. Useful Commands

## DNS

```bash
dig example.com
```

```bash
nslookup example.com
```

---

## IP

```bash
ip addr
```

---

## Routes

```bash
ip route
```

---

## Listening Ports

```bash
ss -lntp
```

---

## TCP Test

```bash
nc -vz example.com 443
```

---

## HTTP/HTTPS

```bash
curl -v https://example.com
```

---

## Trace Route

```bash
traceroute example.com
```

or:

```bash
tracepath example.com
```

---

## Packet Capture

```bash
sudo tcpdump -i any port 443
```

---

# 43. CI/CD Network Security

Important principles:

## Least Privilege

Give only the permissions required.

## Network Segmentation

Separate:

```text
Public
Private Application
Database
CI/CD
Management
```

## Encryption

Use:

```text
HTTPS
TLS
SSH
VPN
```

where appropriate.

## Secrets Management

Never store secrets in:

```text
Git
Dockerfile
Source Code
README
```

---

# 44. Example Secure CI/CD Architecture

```text
                       Internet
                           |
                           v
                    Git Repository
                           |
                           | HTTPS
                           v
                    CI/CD Platform
                           |
                           v
                 Self-Hosted Runner
                    Private Subnet
                           |
             +-------------+-------------+
             |                           |
             v                           v
       Container Registry           AWS APIs
             |                           |
             |                           |
             +-------------+-------------+
                           |
                           v
                    Kubernetes API
                           |
                           v
                        EKS
                           |
                     +-----+-----+
                     |           |
                     v           v
                  Frontend    Backend
                                |
                                v
                             Database
```

---

# 45. Important Ports

| Port | Purpose                         |
| ---: | ------------------------------- |
|   22 | SSH                             |
|   53 | DNS                             |
|   80 | HTTP                            |
|  443 | HTTPS                           |
| 6443 | Kubernetes API                  |
| 2376 | Docker API with TLS             |
| 8080 | Common application port         |
| 9090 | Prometheus                      |
| 3000 | Common application/Grafana port |

Remember:

> Port numbers are conventions and can be changed by configuration.

---

# 46. CI/CD Networking with GitHub Actions

Typical flow:

```text
GitHub Repository
       |
       v
Workflow Trigger
       |
       v
GitHub Runner
       |
       +--- Checkout Code
       |
       +--- Build
       |
       +--- Test
       |
       +--- Docker Build
       |
       +--- Docker Push
       |
       +--- AWS Authentication
       |
       +--- Kubernetes Deployment
```

Each external communication may require network connectivity.

---

# 47. CI/CD Networking with Jenkins

Typical architecture:

```text
Developer
    |
    v
Git Repository
    |
    v
Jenkins Controller
    |
    v
Jenkins Agent
    |
    +--- Build
    +--- Test
    +--- Docker
    +--- Registry
    +--- Kubernetes
```

The controller and agents also require appropriate network connectivity.

---

# 48. CI/CD + Docker + Kubernetes

Complete DevOps flow:

```text
Developer
    |
    v
Git
    |
    v
CI/CD
    |
    v
Docker Build
    |
    v
Container Registry
    |
    v
Kubernetes
    |
    v
Service
    |
    v
Ingress / Load Balancer
    |
    v
User
```

Networking exists at every major stage.

---

# 49. CI/CD Networking Checklist

Before deploying, verify:

### Git

* [ ] Git repository reachable
* [ ] DNS works
* [ ] Authentication works

### Runner

* [ ] Runner online
* [ ] Internet/private connectivity works
* [ ] Required tools installed

### Registry

* [ ] Registry reachable
* [ ] Authentication works
* [ ] Push permission works

### Cloud

* [ ] Cloud API reachable
* [ ] IAM permissions correct
* [ ] VPC connectivity correct

### Kubernetes

* [ ] API server reachable
* [ ] Authentication works
* [ ] RBAC permissions correct
* [ ] NetworkPolicy allows application traffic

### Application

* [ ] Service exists
* [ ] Pods are healthy
* [ ] Load Balancer/Ingress works
* [ ] DNS works
* [ ] Application port is listening

---

# 50. Final Mental Model

Remember CI/CD networking as:

```text
                    CI/CD
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
      Git          Registry         Cloud
       |              |              |
       +--------------+--------------+
                      |
                      v
                 Kubernetes
                      |
                      v
                  Application
                      |
                      v
                    User
```

And troubleshoot every connection using:

```text
WHO?
  ↓
WHERE?
  ↓
DNS?
  ↓
IP?
  ↓
ROUTE?
  ↓
PORT?
  ↓
FIREWALL?
  ↓
AUTHENTICATION?
  ↓
APPLICATION?
```

---

# 🎯 Key Takeaways

1. CI/CD depends heavily on networking.
2. Runners need connectivity to required services.
3. HTTPS is the most common protocol for modern CI/CD communication.
4. DNS must work before hostname-based connections can work.
5. Container registries require network connectivity for image push/pull.
6. Kubernetes API communication commonly uses HTTPS on port 6443.
7. Self-hosted runners can access private infrastructure but require careful security.
8. Proxies can affect pipeline connectivity.
9. VPNs can connect CI/CD infrastructure to private networks.
10. AWS Security Groups and NACLs can affect deployment connectivity.
11. Kubernetes NetworkPolicies can affect application communication.
12. TLS protects network communication.
13. Least privilege should be applied to both network and identity permissions.
14. Network troubleshooting should follow a systematic path.
15. Understanding networking makes DevOps troubleshooting much faster.

---

# 🧠 Interview Definition

> **CI/CD networking is the connectivity, routing, DNS, security, protocols, and network controls that allow CI/CD components to communicate with source repositories, runners, registries, cloud services, Kubernetes clusters, and deployed applications.**

---

# 🚀 Golden Rule

When a CI/CD pipeline fails, don't immediately ask:

> "What's wrong with my code?"

Ask:

```text
Who is connecting?
        ↓
Where are they connecting?
        ↓
Can DNS resolve it?
        ↓
Can the network reach it?
        ↓
Is the port open?
        ↓
Is traffic allowed?
        ↓
Is authentication valid?
        ↓
Is the application working?
```

**This is the CI/CD networking mindset of a DevOps engineer.**
