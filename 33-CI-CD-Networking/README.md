# 🔄 CI/CD Networking

## Chapter 33 — CI/CD Networking

CI/CD networking is the networking knowledge required to build, run, secure, and troubleshoot **Continuous Integration and Continuous Delivery/Deployment pipelines**.

In a DevOps environment, CI/CD systems communicate with:

* Git repositories
* CI/CD runners
* Container registries
* Cloud platforms
* Kubernetes clusters
* Application servers
* Databases
* APIs
* Monitoring systems
* Deployment tools

Understanding networking helps a DevOps engineer troubleshoot pipeline failures and securely connect all these components.

---

# 📚 Table of Contents

1. [What is CI/CD Networking?](#-what-is-cicd-networking)
2. [Why Networking is Important in CI/CD](#-why-networking-is-important-in-cicd)
3. [CI/CD Network Architecture](#-cicd-network-architecture)
4. [CI/CD Components](#-cicd-components)
5. [Network Communication in CI/CD](#-network-communication-in-cicd)
6. [Git and Networking](#-git-and-networking)
7. [CI Runners](#-ci-runners)
8. [Container Registry Networking](#-container-registry-networking)
9. [Docker Networking in CI/CD](#-docker-networking-in-cicd)
10. [Kubernetes Networking in CI/CD](#-kubernetes-networking-in-cicd)
11. [AWS Networking and CI/CD](#-aws-networking-and-cicd)
12. [Ports and Protocols](#-ports-and-protocols)
13. [Webhooks](#-webhooks)
14. [Secrets and Network Security](#-secrets-and-network-security)
15. [Self-Hosted Runners](#-self-hosted-runners)
16. [Proxy in CI/CD](#-proxy-in-cicd)
17. [VPN and Private Connectivity](#-vpn-and-private-connectivity)
18. [CI/CD Network Troubleshooting](#-cicd-network-troubleshooting)
19. [Real-World Architecture](#-real-world-architecture)
20. [DevOps Skills Checklist](#-devops-skills-checklist)

---

# 🔹 What is CI/CD Networking?

CI/CD networking refers to the network communication required between different components of a CI/CD pipeline.

A typical pipeline may communicate like this:

```text
Developer
    |
    | HTTPS / SSH
    v
Git Repository
    |
    | Webhook / Polling
    v
CI/CD Runner
    |
    +--------------------+
    |                    |
    v                    v
Container Registry     Cloud API
    |                    |
    v                    v
Docker Image           AWS / Azure
                         |
                         v
                    Kubernetes
                         |
                         v
                    Application
```

Every connection depends on networking.

---

# 🔹 Why Networking is Important in CI/CD

A CI/CD pipeline can fail even when the code is correct.

For example:

```text
Pipeline
   |
   v
git clone
   |
   X
Network timeout
```

Possible causes:

* DNS failure
* Internet connectivity problem
* Firewall
* Security Group
* NACL
* Proxy
* Incorrect port
* Authentication problem
* Routing problem
* Kubernetes NetworkPolicy
* Private subnet configuration

Therefore:

> A DevOps engineer must understand both CI/CD and networking.

---

# 🔹 CI/CD Network Architecture

A basic CI/CD architecture:

```text
                 Developer
                     |
                     | HTTPS
                     v
              Git Repository
                     |
                     | Webhook
                     v
                CI/CD Server
                     |
             +-------+-------+
             |               |
             v               v
          Build            Test
             |               |
             +-------+-------+
                     |
                     v
              Docker Build
                     |
                     v
             Container Registry
                     |
                     | Pull
                     v
               Deployment
                     |
          +----------+----------+
          |                     |
          v                     v
       Kubernetes              VM
          |                     |
          +----------+----------+
                     |
                     v
                Application
```

---

# 🔹 CI/CD Components

Important components include:

| Component           | Purpose                         |
| ------------------- | ------------------------------- |
| Git Repository      | Stores source code              |
| CI Server           | Runs automation                 |
| Runner              | Executes pipeline jobs          |
| Artifact Repository | Stores build artifacts          |
| Container Registry  | Stores Docker images            |
| Cloud API           | Provides cloud automation       |
| Kubernetes API      | Controls Kubernetes             |
| Load Balancer       | Distributes application traffic |
| DNS                 | Resolves names                  |
| Firewall            | Controls traffic                |

---

# 🔹 Network Communication in CI/CD

A CI/CD pipeline may use many protocols.

```text
Git
 |
 +-- HTTPS : 443
 |
 +-- SSH : 22

Container Registry
 |
 +-- HTTPS : 443

Kubernetes API
 |
 +-- HTTPS : 6443

HTTP Application
 |
 +-- HTTP : 80
 |
 +-- HTTPS : 443
```

The exact ports depend on the platform and configuration.

---

# 🔹 Git and Networking

Git communicates with remote repositories using protocols such as:

### HTTPS

```text
git clone https://github.com/user/repository.git
```

Common port:

```text
443
```

### SSH

```text
git clone git@github.com:user/repository.git
```

Common port:

```text
22
```

---

# 🔹 CI/CD Runner

A runner is the machine or execution environment that executes pipeline jobs.

Examples:

```text
GitHub Actions Runner
GitLab Runner
Jenkins Agent
```

The runner may need network access to:

* Git repository
* Package repositories
* Container registry
* Cloud APIs
* Kubernetes API
* Deployment targets

---

# 🔹 Hosted vs Self-Hosted Runner

## Hosted Runner

The CI/CD provider manages the runner.

Example:

```text
GitHub
   |
   v
Managed Runner
```

Advantages:

* Easy setup
* Provider manages infrastructure
* No server maintenance

---

## Self-Hosted Runner

You manage the runner.

Example:

```text
GitHub
   |
   | HTTPS
   v
Private Runner
   |
   +------ Private AWS resources
   |
   +------ Kubernetes
   |
   +------ Internal applications
```

Advantages:

* Access to private networks
* Custom software
* Internal resources
* More control

But it requires security and maintenance.

---

# 🔹 Container Registry Networking

CI/CD commonly builds a Docker image and pushes it to a container registry.

Example:

```text
Developer
    |
    v
Git
    |
    v
CI Runner
    |
    | docker build
    v
Docker Image
    |
    | docker push
    v
Container Registry
```

During deployment:

```text
Kubernetes
     |
     | docker pull
     v
Container Registry
```

The registry must be reachable from the environment performing the push or pull.

---

# 🔹 Docker Networking in CI/CD

CI/CD pipelines frequently run Docker commands.

Example:

```bash
docker build -t myapp:1.0 .
docker run -p 8080:8080 myapp:1.0
docker push myapp:1.0
```

Networking is involved when:

* Containers communicate
* Images are pulled
* Images are pushed
* Ports are published
* Applications access external APIs

---

# 🔹 Kubernetes Networking in CI/CD

A CI/CD pipeline may deploy applications into Kubernetes.

Typical flow:

```text
CI/CD Runner
      |
      | HTTPS
      v
Kubernetes API
      |
      v
Deployment
      |
      v
Pods
      |
      v
Service
      |
      v
Ingress / Load Balancer
      |
      v
Users
```

The CI/CD runner needs appropriate connectivity and authentication to the Kubernetes API.

---

# 🔹 AWS Networking and CI/CD

A common AWS architecture:

```text
Internet
   |
   v
GitHub
   |
   v
CI/CD Runner
   |
   v
AWS
   |
   +----------------+
   |                |
   v                v
ECR              EKS
   |                |
   |                v
   |              Pods
   |                |
   +---------> Application
```

AWS networking components may include:

* VPC
* Subnets
* Route Tables
* Internet Gateway
* NAT Gateway
* Security Groups
* NACLs
* Load Balancers
* Route 53
* VPC Endpoints

---

# 🔹 Ports and Protocols

Important ports for DevOps:

| Port | Protocol | Common Use                                      |
| ---: | -------- | ----------------------------------------------- |
|   22 | SSH      | Remote administration                           |
|   53 | DNS      | Name resolution                                 |
|   80 | HTTP     | Web traffic                                     |
|  443 | HTTPS    | Secure web traffic                              |
| 6443 | HTTPS    | Kubernetes API                                  |
| 2375 | TCP      | Docker API without TLS; avoid exposing publicly |
| 2376 | TCP      | Docker API with TLS                             |
| 3000 | TCP      | Common application/dev port                     |
| 8080 | TCP      | Common web/application port                     |
| 9090 | TCP      | Prometheus                                      |
| 3000 | TCP      | Common Grafana/default web port                 |

> Ports are conventions, not universal requirements. Applications can be configured to use different ports.

---

# 🔹 Webhooks

A webhook allows one system to notify another system when an event occurs.

Example:

```text
Developer
    |
    v
Git Push
    |
    v
GitHub
    |
    | Webhook
    v
CI/CD System
    |
    v
Pipeline
```

Example events:

* Push
* Pull Request
* Tag
* Release

Webhooks commonly use HTTP/HTTPS.

---

# 🔹 Webhook Network Flow

```text
Git Provider
     |
     | HTTPS
     v
Webhook Endpoint
     |
     v
CI/CD Server
     |
     v
Pipeline
```

If the webhook doesn't arrive, check:

```text
DNS
 ↓
Network route
 ↓
Firewall
 ↓
Port 443
 ↓
Load Balancer
 ↓
Webhook endpoint
 ↓
CI/CD server
```

---

# 🔹 Secrets and Network Security

CI/CD pipelines commonly use secrets such as:

* Cloud credentials
* API tokens
* SSH keys
* Registry credentials
* Kubernetes credentials

Secrets should:

* Never be hardcoded
* Never be committed to Git
* Be stored in secret-management systems
* Have minimum required permissions
* Be rotated regularly

Example:

```text
CI/CD
   |
   v
Secret Manager
   |
   v
Temporary Credential
   |
   v
AWS / Kubernetes
```

---

# 🔹 Self-Hosted Runner in a Private Network

Example:

```text
                 Internet
                    |
                    v
              Git Provider
                    |
                  HTTPS
                    |
                    v
            Self-Hosted Runner
             Private Subnet
                    |
          +---------+---------+
          |                   |
          v                   v
       ECR/EKS             Internal API
```

The runner may need:

* DNS
* HTTPS
* NAT Gateway or VPC endpoints
* Security Group access
* Kubernetes API access

---

# 🔹 Proxy in CI/CD

Some organizations require all outbound traffic to pass through a proxy.

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

Environment variables may be configured:

```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
export NO_PROXY=localhost,127.0.0.1
```

The exact configuration depends on the environment.

---

# 🔹 VPN and Private Connectivity

A CI/CD system may need access to private infrastructure.

Example:

```text
CI/CD
  |
  | VPN / Private Connection
  v
Corporate Network
  |
  +---- Internal Servers
  |
  +---- Private Kubernetes
  |
  +---- Internal APIs
```

AWS environments may use services such as:

* Site-to-Site VPN
* Direct Connect
* Transit Gateway

depending on the architecture.

---

# 🔹 CI/CD Network Troubleshooting

When a pipeline fails, do not immediately assume the code is wrong.

Follow this process:

```text
1. Identify SOURCE
        ↓
2. Identify DESTINATION
        ↓
3. Check DNS
        ↓
4. Check IP
        ↓
5. Check Route
        ↓
6. Check Firewall
        ↓
7. Check Security Group/NACL
        ↓
8. Check Port
        ↓
9. Check Authentication
        ↓
10. Check Application/API
```

---

# 🔹 Useful Linux Commands

### Check IP

```bash
ip addr
```

### Check routes

```bash
ip route
```

### Check listening ports

```bash
ss -lntp
```

### Test DNS

```bash
dig example.com
```

### Test HTTP

```bash
curl -v https://example.com
```

### Test TCP port

```bash
nc -vz example.com 443
```

### Trace network path

```bash
traceroute example.com
```

or:

```bash
tracepath example.com
```

### Capture traffic

```bash
sudo tcpdump -i any port 443
```

---

# 🔹 Common CI/CD Networking Problems

## Problem 1 — Git clone fails

Possible causes:

```text
DNS
 ↓
Internet
 ↓
Proxy
 ↓
Firewall
 ↓
Authentication
```

Test:

```bash
git ls-remote https://github.com/user/repository.git
```

---

## Problem 2 — Docker image push fails

Check:

```text
Registry DNS
 ↓
HTTPS connectivity
 ↓
Registry authentication
 ↓
Image tag
 ↓
Registry permissions
```

---

## Problem 3 — Kubernetes deployment fails

Check:

```text
CI Runner
    |
    v
Kubernetes API
    |
    v
Authentication
    |
    v
RBAC
    |
    v
Deployment
```

Test API connectivity:

```bash
curl -k https://<kubernetes-api>:6443
```

Use authenticated Kubernetes tooling rather than relying on a raw curl request for actual cluster operations.

---

## Problem 4 — Private runner cannot access Internet

Check:

```text
Private Subnet
      |
Route Table
      |
NAT Gateway
      |
Internet Gateway
      |
Internet
```

Also check:

* Security Group
* NACL
* DNS
* NAT Gateway status

---

# 🔹 Real-World Architecture

A production-style CI/CD architecture may look like:

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
                    CI/CD Platform
                            |
                            v
                    Build/Test Runner
                            |
                +-----------+-----------+
                |                       |
                v                       v
           Artifact Store         Container Registry
                                        |
                                        |
                                        v
                                   AWS / Cloud
                                        |
                              +---------+---------+
                              |                   |
                              v                   v
                             EKS                 EC2
                              |
                              v
                             Pods
                              |
                              v
                         Load Balancer
                              |
                              v
                            Users
```

---

# 🔹 Secure CI/CD Architecture

A stronger architecture separates public and private components:

```text
                    Internet
                       |
                       v
                Public Load Balancer
                       |
                       v
                Private Application
                       |
                       v
                Private Database


CI/CD
  |
  v
Private Runner
  |
  +---- Container Registry
  |
  +---- Kubernetes API
  |
  +---- Cloud APIs
```

Security controls:

```text
IAM
Security Groups
NACLs
Network Policies
Secrets Management
TLS
Private Networking
Least Privilege
Logging
Monitoring
```

---

# 🔹 CI/CD Networking Mindset

When troubleshooting a CI/CD pipeline, ask:

### WHO?

Who is making the request?

```text
Developer
Runner
Pod
Server
```

### WHERE?

Where is the destination?

```text
GitHub
Registry
AWS
Kubernetes
API
```

### HOW?

How is it connecting?

```text
HTTPS
SSH
DNS
TCP
API
Webhook
```

### WHICH PORT?

```text
22
53
80
443
6443
```

### WHAT SECURITY CONTROL?

```text
Firewall
Security Group
NACL
NetworkPolicy
Proxy
IAM
```

---

# 🔹 CI/CD Networking + DevOps

CI/CD networking connects many DevOps technologies:

```text
Linux
  |
Networking
  |
Git
  |
GitHub
  |
CI/CD
  |
Docker
  |
Container Registry
  |
Kubernetes
  |
AWS
  |
Monitoring
```

This is why networking is one of the most important foundations for a DevOps engineer.

---

# 🎯 What You Should Know After This Chapter

After completing Chapter 33, you should understand:

* [ ] CI/CD networking fundamentals
* [ ] CI/CD architecture
* [ ] Git networking
* [ ] CI/CD runners
* [ ] Hosted vs self-hosted runners
* [ ] Container registry connectivity
* [ ] Docker networking
* [ ] Kubernetes API networking
* [ ] AWS networking for CI/CD
* [ ] Webhooks
* [ ] Ports and protocols
* [ ] Proxy
* [ ] VPN
* [ ] Private networking
* [ ] Secrets and network security
* [ ] CI/CD troubleshooting
* [ ] Network debugging commands
* [ ] Production CI/CD architecture

---

# 🧠 One-Line Interview Definition

> **CI/CD networking is the network connectivity, routing, security, and communication required for CI/CD components to interact with source repositories, runners, registries, cloud services, Kubernetes clusters, and deployed applications.**

---

# 🚀 Final Mental Model

Remember:

```text
                 SOURCE CODE
                     |
                     v
                GIT REPOSITORY
                     |
                  WEBHOOK
                     |
                     v
                CI/CD RUNNER
                     |
              +------+------+
              |             |
              v             v
           BUILD          TEST
              |
              v
           DOCKER
              |
              v
      CONTAINER REGISTRY
              |
              v
          KUBERNETES
              |
              v
          APPLICATION
              |
              v
             USER
```

And underneath everything:

```text
DNS
 ↓
IP
 ↓
ROUTING
 ↓
PORT
 ↓
FIREWALL
 ↓
AUTHENTICATION
 ↓
APPLICATION
```

> **Master the network path, and CI/CD troubleshooting becomes much easier.**

---

# ✅ Chapter 33 Complete Structure

```text
33-CI-CD-Networking/
│
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

**Next:** `notes.md` — detailed CI/CD Networking theory.
