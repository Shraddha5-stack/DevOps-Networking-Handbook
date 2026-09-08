# 🔄 CI/CD Networking — Interview Questions

## Chapter 33 — CI/CD Networking

This chapter contains CI/CD Networking interview questions from **basic → intermediate → advanced → scenario-based** level.

The goal is to understand the networking concepts behind CI/CD pipelines and explain how to troubleshoot real-world failures.

---

# 📚 Table of Contents

1. [Basic Questions](#1-basic-questions)
2. [Intermediate Questions](#2-intermediate-questions)
3. [Advanced Questions](#3-advanced-questions)
4. [Docker CI/CD Networking](#4-docker-cicd-networking)
5. [Kubernetes CI/CD Networking](#5-kubernetes-cicd-networking)
6. [AWS CI/CD Networking](#6-aws-cicd-networking)
7. [Security Questions](#7-security-questions)
8. [Troubleshooting Questions](#8-troubleshooting-questions)
9. [Scenario-Based Questions](#9-scenario-based-questions)
10. [Rapid-Fire Questions](#10-rapid-fire-questions)
11. [Interview Revision Checklist](#11-interview-revision-checklist)

---

# 1. Basic Questions

## Q1. What is CI/CD?

**Answer:**

CI/CD stands for:

* CI — Continuous Integration
* CD — Continuous Delivery or Continuous Deployment

CI/CD automates activities such as:

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
```

---

## Q2. Why is networking important in CI/CD?

**Answer:**

CI/CD pipelines communicate with many external and internal systems.

For example:

```text
Developer
   ↓
Git Repository
   ↓
CI Runner
   ↓
Container Registry
   ↓
Cloud
   ↓
Kubernetes
```

Every connection requires correct networking, DNS, ports, routing, security and authentication.

---

## Q3. What is a CI runner?

**Answer:**

A CI runner is a machine or environment that executes CI/CD jobs.

Examples include:

* GitHub Actions runner
* Jenkins agent
* GitLab Runner

The runner needs network access to the services required by the pipeline.

---

## Q4. What network protocol is commonly used by CI/CD systems?

**Answer:**

HTTPS is one of the most commonly used protocols.

The default HTTPS port is:

```text
443
```

CI/CD systems commonly use HTTPS to communicate with:

* Git repositories
* Container registries
* Cloud APIs
* Package repositories
* External APIs

---

## Q5. What is DNS?

**Answer:**

DNS converts domain names into IP addresses.

Example:

```text
github.com
    ↓
IP Address
```

Without working DNS, a CI runner may not be able to access services using domain names.

---

## Q6. What happens when you run:

```bash
curl https://github.com
```

**Answer:**

At a high level:

```text
DNS Resolution
      ↓
IP Address
      ↓
TCP Connection
      ↓
TLS Handshake
      ↓
HTTP Request
      ↓
HTTP Response
```

---

## Q7. What is a port?

**Answer:**

A port identifies a network service on a host.

Examples:

| Service        | Port |
| -------------- | ---: |
| SSH            |   22 |
| DNS            |   53 |
| HTTP           |   80 |
| HTTPS          |  443 |
| Kubernetes API | 6443 |

---

## Q8. What is a firewall?

**Answer:**

A firewall controls network traffic based on rules.

It can allow or deny traffic based on:

* Source IP
* Destination IP
* Protocol
* Port
* Direction

---

## Q9. What is latency?

**Answer:**

Latency is the time taken for data to travel between two endpoints.

High latency can slow down:

* Git operations
* Image pulls
* Package downloads
* API calls
* Deployment operations

---

## Q10. What is a timeout?

**Answer:**

A timeout occurs when a connection or operation does not receive the expected response within the configured time.

Example:

```text
CI Runner
   |
   | HTTPS
   |
   X
   |
Registry
```

Possible causes include:

* Network failure
* Firewall
* Routing issue
* Proxy problem
* Service unavailable

---

# 2. Intermediate Questions

## Q11. What network access does a CI runner usually need?

**Answer:**

It depends on the pipeline.

A typical runner may need access to:

```text
Git Repository
Container Registry
Package Repository
Cloud APIs
Kubernetes API
Application endpoints
```

The exact ports and destinations should be restricted to what the pipeline requires.

---

## Q12. What is the difference between hosted and self-hosted runners?

**Answer:**

### Hosted Runner

Provided and managed by the CI/CD platform.

### Self-Hosted Runner

Managed by the organization.

A self-hosted runner gives more control over:

* Network placement
* Firewall
* Private resources
* Internal services
* Security policies

---

## Q13. Why would a company place a self-hosted runner in a private subnet?

**Answer:**

For better network isolation and security.

Example:

```text
Internet
   |
   v
Firewall
   |
   v
Private CI Runner
   |
   +----> Registry
   |
   +----> Cloud API
   |
   +----> Kubernetes API
```

The runner does not need to have a public IP.

---

## Q14. How can a private CI runner access the Internet?

**Answer:**

Common options include:

* NAT Gateway
* Proxy
* VPC endpoints where supported
* Controlled egress architecture

Example:

```text
Private Runner
      |
      v
Route Table
      |
      v
NAT Gateway
      |
      v
Internet Gateway
      |
      v
Internet
```

---

## Q15. What is a proxy in CI/CD?

**Answer:**

A proxy acts as an intermediary between the runner and external services.

Example:

```text
CI Runner
    |
    v
Proxy
    |
    v
Internet
```

Environment variables may include:

```bash
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

---

## Q16. What is `NO_PROXY`?

**Answer:**

`NO_PROXY` specifies destinations that should bypass the configured proxy.

Example:

```bash
export NO_PROXY=localhost,127.0.0.1,.internal.example
```

Incorrect proxy configuration can cause CI/CD connectivity problems.

---

## Q17. What is an artifact repository?

**Answer:**

An artifact repository stores build outputs and packages.

Examples:

```text
JAR
WAR
ZIP
DEB
RPM
Container Images
```

The CI pipeline may upload artifacts and later download them during deployment.

---

## Q18. What is a container registry?

**Answer:**

A container registry stores container images.

Example flow:

```text
Source Code
    ↓
Build
    ↓
Docker Image
    ↓
Container Registry
    ↓
Kubernetes
```

---

## Q19. Why is HTTPS important for container registries?

**Answer:**

Registry communication commonly occurs over HTTPS.

This provides:

* Encryption
* Server authentication
* Protection against network interception

---

## Q20. What is a webhook?

**Answer:**

A webhook allows one system to notify another system when an event occurs.

Example:

```text
Developer
   |
   | git push
   v
Git Repository
   |
   | webhook/event
   v
CI System
   |
   v
Pipeline
```

---

# 3. Advanced Questions

## Q21. How would you design secure networking for a CI/CD pipeline?

**Answer:**

I would use:

* Private runners where appropriate
* Least-privilege network access
* Restricted egress
* TLS encryption
* Network segmentation
* Security groups/firewalls
* Kubernetes NetworkPolicies
* Secure secrets management
* Private endpoints where appropriate
* Monitoring and logging

Example:

```text
Developer
    |
    v
Git Repository
    |
    v
CI Platform
    |
    v
Private Runner
    |
    +----> Registry
    |
    +----> Cloud APIs
    |
    +----> Kubernetes API
             |
             v
          Cluster
```

---

## Q22. What is network segmentation?

**Answer:**

Network segmentation divides infrastructure into separate network zones.

For example:

```text
Public Network
      |
      v
Load Balancer
      |
      v
Application Network
      |
      v
Private Database Network
```

This reduces unnecessary network access.

---

## Q23. What is egress traffic?

**Answer:**

Egress traffic is traffic leaving a network or environment.

Example:

```text
CI Runner
    |
    | HTTPS
    v
External Registry
```

The runner is generating egress traffic.

---

## Q24. What is ingress traffic?

**Answer:**

Ingress traffic is traffic entering a network or environment.

Example:

```text
Internet
   |
   v
Load Balancer
```

The traffic entering the environment is ingress traffic.

---

## Q25. What is the difference between a security group and a NACL in AWS?

**Answer:**

At a high level:

| Security Group                | NACL                 |
| ----------------------------- | -------------------- |
| Resource-level control        | Subnet-level control |
| Stateful                      | Stateless            |
| Primarily allow rules         | Allow and deny rules |
| Applied to network interfaces | Applied to subnets   |

---

## Q26. Why might a CI runner successfully resolve a hostname but still fail to connect?

**Answer:**

DNS only proves that the hostname can be resolved.

The actual connection can still fail because of:

* Routing
* Firewall
* Security Group
* NACL
* Proxy
* Port
* Service availability
* TLS problems

Troubleshooting should continue beyond DNS.

---

## Q27. How would you troubleshoot a TCP connection timeout?

**Answer:**

I would check:

```text
DNS
 ↓
IP
 ↓
Route
 ↓
Gateway
 ↓
Firewall
 ↓
Security Group
 ↓
NACL
 ↓
Proxy
 ↓
Destination Port
 ↓
Service
```

Useful commands:

```bash
dig example.com
ip route
nc -vz example.com 443
curl -v https://example.com
```

---

## Q28. How would you troubleshoot "Connection refused"?

**Answer:**

"Connection refused" often indicates that the destination is reachable but the target port is not accepting the connection.

I would check:

```bash
ss -lntp
```

On the destination server.

Then verify:

* Application is running
* Correct port
* Firewall
* Service configuration
* Container port
* Kubernetes Service

---

## Q29. What is the difference between timeout and connection refused?

**Answer:**

### Timeout

The connection attempt does not receive a response within the expected time.

Possible causes:

```text
Firewall
Routing
Network failure
Dropped packets
```

### Connection Refused

The destination is reachable but the connection is actively rejected.

Possible cause:

```text
Nothing listening on the target port
```

---

## Q30. How can packet capture help troubleshoot CI/CD networking?

**Answer:**

Packet capture allows us to observe network traffic.

Example:

```bash
sudo tcpdump -i any port 443
```

It can help determine whether packets are:

* Leaving the runner
* Returning from the destination
* Being retransmitted
* Reaching a specific port

---

# 4. Docker CI/CD Networking

## Q31. Why is Docker networking important in CI/CD?

**Answer:**

CI pipelines frequently build and test applications using containers.

Containers may need to communicate with:

* Databases
* APIs
* Test services
* Other containers
* Registries

---

## Q32. How do containers communicate on a Docker user-defined network?

**Answer:**

Containers attached to the same user-defined network can communicate using container/service names.

Example:

```text
app
 |
 | HTTP
 v
database
```

Docker provides internal DNS for user-defined networks.

---

## Q33. How do you inspect Docker networking?

```bash
docker network ls
docker network inspect <network>
docker inspect <container>
```

---

## Q34. What is port publishing in Docker?

**Answer:**

Port publishing maps a host port to a container port.

Example:

```bash
docker run -p 8080:80 nginx
```

Meaning:

```text
Host:8080
   ↓
Container:80
```

---

## Q35. Why might a CI container not be able to access another container?

**Answer:**

Possible causes:

* Containers are on different networks
* Incorrect hostname
* Incorrect port
* Application not listening
* Firewall
* Container stopped
* Incorrect Docker network configuration

---

# 5. Kubernetes CI/CD Networking

## Q36. What network access does a CI system need to deploy to Kubernetes?

**Answer:**

The CI system needs access to the Kubernetes API server.

Typical Kubernetes API port:

```text
6443
```

The CI system also needs proper authentication and authorization.

---

## Q37. What happens when CI runs `kubectl apply`?

**Answer:**

At a high level:

```text
CI Runner
    |
    | HTTPS
    v
Kubernetes API Server
    |
    v
Kubernetes Control Plane
    |
    v
Cluster Resources
```

---

## Q38. How would you troubleshoot Kubernetes DNS?

Run:

```bash
kubectl get pods -n kube-system
```

Check CoreDNS.

Then create a DNS test Pod:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --restart=Never \
  --rm -it \
  -- nslookup kubernetes.default
```

---

## Q39. What is a Kubernetes Service?

**Answer:**

A Service provides a stable network endpoint for accessing Pods.

Example:

```text
Client
  |
  v
Service
  |
  +----> Pod
  |
  +----> Pod
  |
  +----> Pod
```

---

## Q40. What is a Kubernetes NetworkPolicy?

**Answer:**

A NetworkPolicy controls which network traffic is allowed between Pods and other network endpoints, depending on the CNI implementation.

Example:

```text
Frontend
   |
   | allowed
   v
Backend
   |
   X
   |
Database
```

---

## Q41. How do you troubleshoot a Kubernetes Service with no traffic?

**Answer:**

I would check:

```bash
kubectl get svc
kubectl get endpoints
kubectl get endpointslices
kubectl get pods --show-labels
```

Then compare the Service selector with the Pod labels.

Also check:

```bash
kubectl describe svc <service>
kubectl describe pod <pod>
```

---

## Q42. Why can a Kubernetes Pod be Running but the application still be unreachable?

**Answer:**

`Running` only indicates that the Pod is running.

The application may still have:

* Wrong container port
* Wrong Service port
* Wrong targetPort
* Incorrect Service selector
* NetworkPolicy restriction
* Application not listening
* Readiness failure

---

# 6. AWS CI/CD Networking

## Q43. How can a CI runner access AWS?

**Answer:**

The runner communicates with AWS service APIs over the network, commonly using HTTPS.

Authentication can use appropriate AWS identity mechanisms.

Example:

```bash
aws sts get-caller-identity
```

---

## Q44. What happens when a private CI runner accesses an AWS API?

**Answer:**

Depending on the architecture, traffic may use:

```text
Private Runner
     |
     +----> NAT Gateway ----> Internet/AWS endpoint
```

or:

```text
Private Runner
     |
     v
VPC Endpoint
     |
     v
AWS Service
```

---

## Q45. Why are VPC endpoints useful for CI/CD?

**Answer:**

They can provide private connectivity to supported AWS services without requiring traffic to traverse the public Internet.

They can improve:

* Security
* Network control
* Architecture simplicity
* Egress management

---

## Q46. What should you check if an EC2-based CI runner cannot access the Internet?

**Answer:**

Check:

```text
Subnet
 ↓
Route Table
 ↓
Default Route
 ↓
NAT/Internet Gateway
 ↓
Security Group
 ↓
NACL
 ↓
DNS
```

Useful commands:

```bash
ip route
curl -I https://example.com
dig example.com
```

---

# 7. Security Questions

## Q47. Why should CI/CD network access follow least privilege?

**Answer:**

A compromised CI runner can be dangerous.

Giving unrestricted network access increases the potential impact of a compromise.

Therefore, access should be limited to required:

* Destinations
* Ports
* Protocols
* Resources

---

## Q48. Why should CI/CD traffic use TLS?

**Answer:**

TLS protects data in transit and helps provide secure communication.

Examples:

```text
HTTPS
TLS-protected APIs
Secure registry communication
```

---

## Q49. Why should secrets not be passed through insecure network channels?

**Answer:**

Secrets such as:

* API tokens
* Cloud credentials
* Registry credentials
* SSH keys

must be protected from exposure.

Use secure secret-management mechanisms and encrypted connections.

---

## Q50. What is network isolation?

**Answer:**

Network isolation limits communication between environments or workloads.

Example:

```text
CI Network
     X
     |
Application Network
     |
     X
     |
Database Network
```

Only explicitly required connections should be allowed.

---

# 8. Troubleshooting Questions

## Q51. A CI runner cannot clone a Git repository. What do you check?

**Answer:**

I would check:

### 1. DNS

```bash
dig github.com
```

### 2. Connectivity

```bash
nc -vz github.com 443
```

### 3. HTTPS

```bash
curl -v https://github.com
```

### 4. Git

```bash
git ls-remote <repository>
```

### 5. Proxy

```bash
echo $HTTPS_PROXY
echo $NO_PROXY
```

### 6. Authentication

Check the configured Git credentials or SSH key.

---

## Q52. Docker image pull fails in CI. What do you check?

**Answer:**

I would check:

```text
DNS
 ↓
Registry connectivity
 ↓
HTTPS 443
 ↓
Proxy
 ↓
Registry authentication
 ↓
Image name
 ↓
Image tag
```

Useful command:

```bash
curl -I https://registry-1.docker.io
```

---

## Q53. Kubernetes deployment fails from CI. What do you check?

**Answer:**

I would check:

```bash
kubectl cluster-info
kubectl get nodes
kubectl get deployment
kubectl get pods
kubectl describe pod <pod>
```

Then investigate:

* Kubernetes API connectivity
* Authentication
* RBAC
* Image pull
* Registry access
* Service configuration
* NetworkPolicy

---

## Q54. CI runner can reach the Internet but cannot reach an internal application. Why?

**Answer:**

Possible reasons include:

* Missing route
* VPN requirement
* Firewall
* Security Group
* NACL
* Network segmentation
* Internal DNS
* Proxy configuration
* Application firewall

---

## Q55. DNS works but curl fails. What does that tell you?

**Answer:**

It tells me that hostname resolution is working, but it does not prove that the network/application connection is working.

I would next check:

```bash
nc -vz <host> <port>
curl -v https://<host>
```

Then investigate firewall, routing, proxy, TLS and service availability.

---

# 9. Scenario-Based Questions

## Scenario 1 — Git Clone Timeout

### Problem

A CI pipeline reports:

```text
fatal: unable to access repository
Connection timed out
```

### How would you troubleshoot?

```text
1. DNS
2. Route
3. TCP 443
4. Proxy
5. Firewall
6. Git authentication
```

Commands:

```bash
dig github.com
ip route
nc -vz github.com 443
curl -v https://github.com
```

---

# Scenario 2 — Registry Connection Failure

### Problem

Docker reports:

```text
failed to pull image
```

### Troubleshooting

```bash
dig registry-1.docker.io
nc -vz registry-1.docker.io 443
curl -I https://registry-1.docker.io
```

Then check:

* Credentials
* Proxy
* Image name
* Image tag
* Registry availability

---

# Scenario 3 — Kubernetes API Timeout

### Problem

CI reports:

```text
Unable to connect to the server
```

### Troubleshooting

Check:

```bash
kubectl cluster-info
kubectl config current-context
```

Then investigate:

```text
DNS
 ↓
Route
 ↓
Port 6443
 ↓
Firewall
 ↓
VPN/private connectivity
 ↓
Authentication
```

---

# Scenario 4 — Pod Cannot Pull Image

### Problem

Pod status:

```text
ImagePullBackOff
```

### Troubleshooting

Run:

```bash
kubectl describe pod <pod-name>
```

Check:

* Registry connectivity
* DNS
* Image name
* Image tag
* Registry authentication
* ImagePullSecrets
* NetworkPolicy if relevant

---

# Scenario 5 — Service Has No Endpoints

### Problem

```bash
kubectl get svc
```

shows the Service, but:

```bash
kubectl get endpoints
```

shows no endpoints.

### Troubleshooting

Check:

```bash
kubectl get pods --show-labels
kubectl describe svc <service>
```

Compare:

```text
Service Selector
       ↓
Pod Labels
```

If they don't match, the Service may not select the Pods.

---

# Scenario 6 — Private Runner Has No Internet

### Problem

A self-hosted runner is in a private subnet.

It cannot download dependencies.

### Troubleshooting

Check:

```text
Subnet
 ↓
Route Table
 ↓
NAT Gateway
 ↓
Security Group
 ↓
NACL
 ↓
DNS
 ↓
Proxy
```

The solution may involve NAT, a proxy, or private service endpoints depending on requirements.

---

# Scenario 7 — Application Port Is Not Reachable

### Problem

The application is running, but:

```bash
curl http://server:8080
```

fails.

### Troubleshooting

Check:

```bash
ss -lntp
```

Then verify:

```text
Application listening port
 ↓
Container port
 ↓
Docker published port / Kubernetes Service
 ↓
Firewall
 ↓
Security Group
 ↓
NetworkPolicy
```

---

# Scenario 8 — CI Pipeline Is Very Slow

### Possible Causes

* High network latency
* Slow DNS
* Large container images
* Slow registry
* Slow artifact repository
* Proxy bottleneck
* Limited bandwidth
* Cross-region traffic
* Repeated downloads

### Improvements

* Cache dependencies
* Use nearby registries
* Optimize image size
* Use build caching
* Reduce unnecessary downloads
* Monitor network latency

---

# Scenario 9 — Works Locally but Fails in CI

### Problem

Developer says:

> "It works on my laptop."

But CI fails.

### Possible causes

```text
Different DNS
Different proxy
Different network
Different firewall
Different credentials
Different environment variables
Different routes
Different container network
```

Compare:

```bash
env
ip addr
ip route
cat /etc/resolv.conf
```

Do not expose secrets when collecting environment information.

---

# Scenario 10 — Deployment Works but Users Cannot Access Application

Architecture:

```text
User
  |
  X
  |
Load Balancer
  |
Application
```

### Troubleshooting

Check:

```text
DNS
 ↓
Load Balancer
 ↓
Listener
 ↓
Target Group
 ↓
Health Check
 ↓
Security Group
 ↓
Application Port
 ↓
Application
```

---

# 10. Rapid-Fire Questions

## Q56. Default HTTP port?

```text
80
```

## Q57. Default HTTPS port?

```text
443
```

## Q58. Default SSH port?

```text
22
```

## Q59. Common Kubernetes API port?

```text
6443
```

## Q60. Command to check IP?

```bash
ip addr
```

## Q61. Command to check routes?

```bash
ip route
```

## Q62. Command to check listening ports?

```bash
ss -lntp
```

## Q63. Command to test TCP connectivity?

```bash
nc -vz host port
```

## Q64. Command to troubleshoot HTTPS?

```bash
curl -v https://example.com
```

## Q65. Command to troubleshoot DNS?

```bash
dig example.com
```

## Q66. Command to inspect Docker networks?

```bash
docker network ls
docker network inspect <network>
```

## Q67. Command to check Kubernetes Pods?

```bash
kubectl get pods -o wide
```

## Q68. Command to check Kubernetes Services?

```bash
kubectl get svc
```

## Q69. Command to check Kubernetes endpoints?

```bash
kubectl get endpoints
```

## Q70. Command to check AWS identity?

```bash
aws sts get-caller-identity
```

---

# 11. Interview Revision Checklist

Before an interview, make sure you can explain:

## Networking Fundamentals

* [ ] IP address
* [ ] DNS
* [ ] TCP
* [ ] UDP
* [ ] Ports
* [ ] Routing
* [ ] Gateway
* [ ] Firewall
* [ ] Proxy
* [ ] TLS

## CI/CD

* [ ] CI
* [ ] CD
* [ ] CI runner
* [ ] Hosted runner
* [ ] Self-hosted runner
* [ ] Webhooks
* [ ] Artifacts
* [ ] Container registry

## Docker

* [ ] Docker bridge network
* [ ] User-defined network
* [ ] Container DNS
* [ ] Port publishing
* [ ] Container-to-container communication

## Kubernetes

* [ ] Kubernetes API
* [ ] Service
* [ ] Endpoints
* [ ] DNS
* [ ] CoreDNS
* [ ] NetworkPolicy
* [ ] Pod networking

## AWS

* [ ] VPC
* [ ] Subnet
* [ ] Route table
* [ ] Internet Gateway
* [ ] NAT Gateway
* [ ] Security Group
* [ ] NACL
* [ ] VPC Endpoint

## Troubleshooting

* [ ] DNS troubleshooting
* [ ] TCP troubleshooting
* [ ] Port troubleshooting
* [ ] Routing troubleshooting
* [ ] Firewall troubleshooting
* [ ] Proxy troubleshooting
* [ ] TLS troubleshooting
* [ ] Kubernetes troubleshooting
* [ ] Docker troubleshooting
* [ ] AWS troubleshooting

---

# ⭐ Golden Interview Answer

If the interviewer asks:

> **"How do you troubleshoot a CI/CD networking issue?"**

Use this structure:

```text
First, I identify the source and destination.

Then I verify DNS resolution.

Next, I check the IP address and routing.

After that, I test TCP connectivity to the required port.

Then I check firewalls, security groups, NACLs and proxy configuration.

If the connection is established, I check TLS and authentication.

Finally, I verify the application or service itself.

I troubleshoot layer by layer instead of randomly changing configurations.
```

The key mental model is:

```text
SOURCE
  ↓
DNS
  ↓
IP
  ↓
ROUTE
  ↓
GATEWAY
  ↓
FIREWALL
  ↓
PORT
  ↓
TLS
  ↓
AUTHENTICATION
  ↓
APPLICATION
```

---

# 🧠 Final Takeaway

CI/CD networking is not a separate isolated concept.

It combines:

```text
Linux Networking
       +
DNS
       +
TCP/IP
       +
HTTP/HTTPS
       +
Git
       +
Docker
       +
Kubernetes
       +
AWS
       +
Security
       +
Troubleshooting
```

A strong DevOps engineer should be able to answer:

> **Who is connecting to whom, using which protocol, on which port, through which network path, and what security controls are involved?**

That mindset is more valuable than memorizing individual commands.
