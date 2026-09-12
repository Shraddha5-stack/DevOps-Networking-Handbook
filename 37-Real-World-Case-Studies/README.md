# Chapter 37 — Real-World Case Studies

Real-world DevOps engineers do not troubleshoot isolated commands or individual tools.

In production, problems usually involve multiple layers:

```text
User
  ↓
DNS
  ↓
Internet
  ↓
Load Balancer
  ↓
Firewall / Security Group
  ↓
Web Server
  ↓
Application
  ↓
Database / Cache / External Services
```

A DevOps engineer must identify **where the failure is happening, why it is happening, how to fix it safely, and how to prevent it from happening again.**

This chapter connects the networking concepts learned throughout this handbook with realistic DevOps incidents.

---

# 1. Learning Objectives

By completing this chapter, you will learn how to:

* Analyze real-world network incidents
* Troubleshoot production-style failures
* Identify symptoms and probable causes
* Follow a structured troubleshooting process
* Understand DNS failures
* Troubleshoot connection refused errors
* Troubleshoot connection timeout errors
* Diagnose HTTP 502, 503, and 504 errors
* Troubleshoot high latency
* Investigate packet loss
* Troubleshoot SSH connectivity
* Troubleshoot EC2 Internet connectivity
* Understand Security Group and NACL problems
* Troubleshoot Kubernetes Services
* Troubleshoot Kubernetes Pods
* Troubleshoot Kubernetes DNS
* Understand Kubernetes NetworkPolicy failures
* Troubleshoot Docker networking
* Troubleshoot CI/CD connectivity
* Troubleshoot TLS/HTTPS problems
* Troubleshoot database connectivity
* Understand load balancer health-check failures
* Perform root cause analysis
* Create incident timelines
* Write postmortems
* Prevent repeated incidents
* Explain incidents during DevOps interviews

---

# 2. Real-World Troubleshooting Mindset

A production incident should not be approached by randomly running commands.

Use a structured process:

```text
Define the problem
       ↓
Understand the impact
       ↓
Check recent changes
       ↓
Reproduce the problem
       ↓
Collect evidence
       ↓
Identify the failing layer
       ↓
Find root cause
       ↓
Apply safe fix
       ↓
Verify
       ↓
Prevent recurrence
       ↓
Document
```

---

# 3. Standard Case Study Format

Every case study in this chapter follows the same structure.

## 3.1 Problem

What is the user or system experiencing?

Example:

```text
Users cannot access the website.
```

---

## 3.2 Impact

Who or what is affected?

Example:

```text
All production users are unable to access the application.
```

Impact can include:

* Users affected
* Services affected
* Geographic scope
* Business impact
* Duration
* Data impact

---

## 3.3 Symptoms

What evidence is visible?

Examples:

```text
DNS resolution fails.
```

```text
Connection timed out.
```

```text
HTTP 502 Bad Gateway.
```

```text
Pods are Running but application is unreachable.
```

---

## 3.4 Architecture

Understand the traffic path.

Example:

```text
User
  |
  v
DNS
  |
  v
Load Balancer
  |
  v
Web Server
  |
  v
Application
  |
  v
Database
```

---

## 3.5 Investigation

Collect evidence instead of guessing.

Typical investigation areas:

```text
DNS
Connectivity
Routing
TCP
Ports
Firewall
Load Balancer
Application
Database
Logs
Metrics
Containers
Kubernetes
Cloud
```

---

## 3.6 Root Cause

Identify the actual reason.

Example:

```text
The application was listening only on 127.0.0.1 instead of
the network interface required by the load balancer.
```

---

## 3.7 Fix

Apply the smallest safe change that resolves the issue.

---

## 3.8 Verification

Confirm that the system works again.

Verification can include:

* DNS resolution
* TCP connection
* HTTP response
* Application health
* Pod health
* Load balancer health
* Database connectivity
* Logs
* Metrics
* User validation

---

## 3.9 Prevention

Ask:

> How can we prevent this incident from happening again?

Examples:

* Monitoring
* Alerts
* Health checks
* Automated testing
* CI/CD validation
* Infrastructure as Code
* Configuration validation
* Documentation
* Runbooks
* Capacity planning
* Security controls

---

# 4. Case Study 1 — Website Is Down Because of DNS

## Problem

Users report:

```text
The website is not opening.
```

## Possible symptoms

```text
DNS resolution fails
```

or:

```text
NXDOMAIN
```

## Investigation

Check:

```text
Domain
  ↓
DNS record
  ↓
DNS response
  ↓
Server IP
  ↓
TCP connection
  ↓
HTTP response
```

## Possible root cause

The DNS record was deleted or incorrectly configured.

## Lesson

A website can have a healthy server and still appear completely down if DNS is broken.

---

# 5. Case Study 2 — Connection Refused

## Problem

An application cannot connect to a server.

The client receives:

```text
Connection refused
```

## Meaning

The destination is reachable, but the TCP connection was rejected.

Possible causes:

* Service is not running
* Nothing is listening on the port
* Service is listening on another port
* Service is bound to the wrong address
* Local firewall is rejecting traffic

## Troubleshooting model

```text
Client
  ↓
Network reachable?
  ↓
Server reachable?
  ↓
Port reachable?
  ↓
Service listening?
  ↓
Application healthy?
```

## Lesson

`Connection refused` and `connection timeout` are different problems.

---

# 6. Case Study 3 — Connection Timeout

## Problem

A client tries to connect but waits until the connection times out.

## Possible causes

* Security Group
* NACL
* Firewall
* Routing problem
* Network path problem
* Incorrect IP
* Server unreachable
* Dropped packets

## Lesson

A timeout often indicates that traffic is being dropped or the destination cannot be reached.

---

# 7. Case Study 4 — HTTP 502 Bad Gateway

## Architecture

```text
User
  ↓
Load Balancer / Reverse Proxy
  ↓
Backend Application
```

## Problem

User receives:

```text
502 Bad Gateway
```

## Investigation

Check:

* Load balancer health
* Backend port
* Application process
* Application logs
* Backend IP
* Network connectivity
* Reverse proxy configuration

## Possible root cause

The reverse proxy cannot successfully communicate with the backend.

## Lesson

A 502 often points to a problem between a gateway/proxy and its upstream service.

---

# 8. Case Study 5 — HTTP 503 Service Unavailable

## Problem

Users receive:

```text
503 Service Unavailable
```

## Possible causes

* No healthy backend
* Application unavailable
* Server overloaded
* Kubernetes Pods unavailable
* Load balancer health checks failing
* Maintenance mode

## Lesson

Always identify which layer generated the 503.

---

# 9. Case Study 6 — HTTP 504 Gateway Timeout

## Architecture

```text
Client
  ↓
Load Balancer
  ↓
Application
  ↓
Database
```

## Problem

Users receive:

```text
504 Gateway Timeout
```

## Possible causes

The gateway waited too long for the upstream service.

Investigate:

```text
Load Balancer
      ↓
Application
      ↓
Database
      ↓
External API
```

Potential problems:

* Slow application
* Slow database query
* Database connection pool exhaustion
* External API delay
* Network latency
* Incorrect timeout configuration

## Lesson

A 504 often requires tracing the entire request path.

---

# 10. Case Study 7 — High Network Latency

## Problem

The application is working, but users report:

```text
The application is very slow.
```

## Possible causes

* Network latency
* Packet loss
* High server CPU
* High memory usage
* Slow database
* Network congestion
* Cross-region traffic
* Slow external dependency

## Investigation

Measure:

```text
Latency
Packet Loss
CPU
Memory
Disk
Network Throughput
Application Response Time
Database Response Time
```

## Lesson

Do not automatically assume that "slow application" means "network problem."

---

# 11. Case Study 8 — Packet Loss

## Problem

Users experience intermittent connectivity.

Symptoms:

```text
Some requests work.
Some requests fail.
```

## Possible causes

* Network congestion
* Faulty network interface
* Wireless instability
* Routing problems
* Infrastructure problems
* Dropped packets
* Overloaded devices

## Lesson

Intermittent failures require measurements over time rather than one successful test.

---

# 12. Case Study 9 — SSH Is Not Working

## Problem

An engineer cannot SSH into a server.

Possible layers:

```text
Client
  ↓
Internet
  ↓
Route
  ↓
Security Group
  ↓
NACL
  ↓
Server Firewall
  ↓
sshd
  ↓
Authentication
```

## Possible causes

* Incorrect IP
* Incorrect route
* Security Group
* NACL
* Firewall
* SSH service stopped
* Port changed
* Wrong username
* Key problem
* Server resource exhaustion

## Lesson

SSH troubleshooting is a multi-layer problem.

---

# 13. Case Study 10 — EC2 Has No Internet Access

## Problem

An EC2 instance cannot reach the Internet.

## Architecture

```text
EC2
 ↓
Subnet Route Table
 ↓
Internet Gateway
 ↓
Internet
```

For a private subnet:

```text
EC2
 ↓
Private Subnet
 ↓
Route Table
 ↓
NAT Gateway
 ↓
Internet Gateway
 ↓
Internet
```

## Investigate

Check:

* Subnet
* Route table
* Internet Gateway
* NAT Gateway
* Security Group
* NACL
* Public IP
* DNS configuration

## Lesson

Internet connectivity depends on the complete network path.

---

# 14. Case Study 11 — Kubernetes Service Has No Endpoints

## Problem

The Service exists, but traffic does not reach Pods.

Architecture:

```text
Client
  ↓
Service
  ↓
Pod
```

## Possible root cause

The Service selector does not match the Pod labels.

Example:

```text
Service selector:
app=backend
```

Pod:

```text
app=frontend
```

No matching Pod is selected.

## Lesson

When a Kubernetes Service does not work, always inspect:

```text
Service
 ↓
Selector
 ↓
Pod Labels
 ↓
Endpoints / EndpointSlices
```

---

# 15. Case Study 12 — Kubernetes Pod Is Running but Application Is Unreachable

A Pod may show:

```text
Running
```

but the application can still be unreachable.

Investigate:

* Container port
* Service port
* TargetPort
* Pod labels
* Service selector
* Endpoints
* NetworkPolicy
* Application listening address
* Application process

## Lesson

`Pod Running` does not automatically mean `application reachable`.

---

# 16. Case Study 13 — Kubernetes CrashLoopBackOff

## Problem

A Pod repeatedly starts and stops.

Possible causes:

* Application crash
* Incorrect configuration
* Missing environment variable
* Missing Secret
* Missing ConfigMap
* Dependency unavailable
* Incorrect command
* Resource limits
* Health-check failure

## Investigation model

```text
Pod
 ↓
Container
 ↓
Application
 ↓
Configuration
 ↓
Dependencies
```

## Lesson

Always inspect application logs and Pod events.

---

# 17. Case Study 14 — Kubernetes ImagePullBackOff

## Problem

Kubernetes cannot start a container because the image cannot be pulled.

Possible causes:

* Incorrect image name
* Incorrect image tag
* Private registry authentication problem
* Registry unavailable
* Network connectivity problem
* Image does not exist

## Lesson

Separate:

```text
Image exists?
        ↓
Registry reachable?
        ↓
Authentication works?
        ↓
Image can be pulled?
```

---

# 18. Case Study 15 — Kubernetes DNS Failure

## Problem

A Pod cannot resolve another Service by name.

Example:

```text
backend.default.svc.cluster.local
```

cannot be resolved.

Investigate:

* CoreDNS
* Pod DNS configuration
* Service name
* Namespace
* NetworkPolicy
* Cluster networking
* CoreDNS logs

## Lesson

Kubernetes application connectivity often depends on both Service networking and cluster DNS.

---

# 19. Case Study 16 — NetworkPolicy Blocks Application Traffic

## Problem

Two Pods cannot communicate after a NetworkPolicy is introduced.

Architecture:

```text
Frontend Pod
     |
     X
     |
Backend Pod
```

## Possible root cause

A default-deny policy blocks traffic.

The required traffic must be explicitly allowed.

## Lesson

NetworkPolicy troubleshooting requires checking:

```text
Source Pod labels
Target Pod labels
Namespace
Ingress rules
Egress rules
Ports
CNI support
```

---

# 20. Case Study 17 — Docker Application Cannot Reach Another Container

## Problem

Container A cannot communicate with Container B.

Possible causes:

* Containers are on different networks
* Wrong container name
* Wrong port
* Application bound to localhost
* Network configuration issue
* Container stopped

## Architecture

```text
Container A
    |
Docker Network
    |
Container B
```

## Lesson

Container-to-container traffic and host-to-container traffic are different paths.

---

# 21. Case Study 18 — CI/CD Pipeline Cannot Access Container Registry

## Problem

A deployment pipeline fails while pulling or pushing an image.

Possible causes:

* Registry authentication
* DNS
* Internet connectivity
* Firewall
* Proxy
* Credentials
* Token expiration
* Registry outage

## Troubleshooting model

```text
CI Runner
   ↓
DNS
   ↓
Network
   ↓
Registry
   ↓
Authentication
   ↓
Image
```

## Lesson

CI/CD infrastructure is also part of the production network.

---

# 22. Case Study 19 — TLS/HTTPS Failure

## Problem

The website is reachable over HTTP but HTTPS fails.

Possible causes:

* Expired certificate
* Wrong certificate
* Certificate hostname mismatch
* Incorrect TLS configuration
* Missing intermediate certificate
* Load balancer configuration
* Reverse proxy configuration

## Architecture

```text
Client
  ↓
TLS Handshake
  ↓
Certificate Validation
  ↓
HTTPS
  ↓
Application
```

## Lesson

HTTPS problems can occur before the application receives the request.

---

# 23. Case Study 20 — Database Connectivity Failure

## Problem

Application cannot connect to the database.

Architecture:

```text
Application
     ↓
Network
     ↓
Firewall / Security Group
     ↓
Database
```

Investigate:

* Database hostname
* DNS
* Route
* Port
* Security Group
* NACL
* Database listener
* Credentials
* Database health
* Connection limits

## Lesson

Separate network connectivity from database authentication.

---

# 24. Case Study 21 — Load Balancer Health Check Failure

## Problem

The application server is running, but the load balancer marks it unhealthy.

Possible causes:

* Wrong health-check path
* Wrong port
* Application not listening
* Security Group blocking health-check traffic
* Application returning unexpected HTTP status
* Incorrect target configuration

## Lesson

A healthy server process does not necessarily mean a healthy load-balancer target.

---

# 25. Case Study 22 — Deployment Causes Production Outage

## Problem

A deployment completes successfully, but users start receiving errors.

Possible causes:

* Bad application version
* Inc
