# Chapter 36 — Troubleshooting

## Introduction

Troubleshooting is the process of identifying, analyzing, and resolving problems in a system or network.

For a DevOps Engineer, troubleshooting is one of the most important skills because production systems can fail at any time.

A DevOps Engineer should not randomly change configurations.

Instead, the engineer should:

```text
Observe
   ↓
Collect Evidence
   ↓
Identify the Problem
   ↓
Find the Root Cause
   ↓
Apply a Fix
   ↓
Verify
   ↓
Document
   ↓
Prevent Recurrence
```

---

# Learning Objectives

After completing this chapter, you should understand:

* What troubleshooting is
* Troubleshooting methodology
* Incident identification
* Evidence collection
* Logs
* Metrics
* Events
* Network troubleshooting
* DNS troubleshooting
* TCP troubleshooting
* HTTP/HTTPS troubleshooting
* Linux troubleshooting
* Process troubleshooting
* Service troubleshooting
* Disk troubleshooting
* Memory troubleshooting
* CPU troubleshooting
* Docker troubleshooting
* Kubernetes troubleshooting
* AWS troubleshooting
* DNS failures
* Connection refused
* Connection timeout
* Packet loss
* High latency
* Port problems
* Firewall problems
* Routing problems
* Application failures
* Container failures
* Kubernetes Service problems
* Monitoring failures
* Root Cause Analysis
* Incident response
* Postmortems
* Preventive actions

---

# 1. What Is Troubleshooting?

Troubleshooting is a systematic process of finding the cause of a problem and restoring normal operation.

Example:

```text
Application is not reachable
        ↓
Check DNS
        ↓
Check IP connectivity
        ↓
Check routing
        ↓
Check port
        ↓
Check firewall
        ↓
Check service
        ↓
Check application logs
        ↓
Find root cause
```

---

# 2. Why Troubleshooting Is Important in DevOps

DevOps engineers work with:

* Linux
* Networking
* Cloud
* Containers
* Kubernetes
* CI/CD
* Databases
* Monitoring
* Security
* Infrastructure

A problem in one layer can affect many other layers.

For example:

```text
DNS problem
     ↓
Application cannot resolve database
     ↓
Application fails
     ↓
Users receive errors
```

Therefore, troubleshooting requires understanding how different components interact.

---

# 3. Troubleshooting Mindset

A good troubleshooting mindset is:

> **Do not guess. Collect evidence.**

Avoid:

```text
"It looks like the server is down."
```

Instead investigate:

```text
Is the server reachable?
Is the service running?
Is the port listening?
Are packets reaching the server?
Are there errors in logs?
What changed recently?
```

---

# 4. Troubleshooting Methodology

A practical troubleshooting process:

```text
1. Identify
2. Define
3. Collect evidence
4. Reproduce
5. Isolate
6. Analyze
7. Fix
8. Verify
9. Monitor
10. Document
```

---

# 5. Step 1 — Identify the Problem

First understand what is actually failing.

Ask:

* What is not working?
* Who is affected?
* When did it start?
* Is the issue intermittent or constant?
* Is the entire application affected?
* Is only one endpoint affected?
* Was there a recent change?

---

# 6. Step 2 — Define the Scope

Determine the scope of the incident.

For example:

```text
One user
   ↓
One server
   ↓
One availability zone
   ↓
One service
   ↓
Entire application
   ↓
Entire infrastructure
```

Scope helps narrow down the problem.

---

# 7. Step 3 — Collect Evidence

Useful evidence includes:

### Logs

```text
Application logs
System logs
Web server logs
Container logs
Kubernetes logs
Cloud logs
```

### Metrics

```text
CPU
Memory
Disk
Network
Latency
Errors
Traffic
Connections
```

### Events

```text
Deployment
Restart
Scaling
Configuration change
Infrastructure change
```

---

# 8. Step 4 — Reproduce the Problem

If possible, reproduce the issue.

For example:

```bash
curl -v https://example.com
```

or:

```bash
nc -vz <host> <port>
```

Reproduction gives us additional evidence.

---

# 9. Step 5 — Isolate the Layer

A useful troubleshooting model is:

```text
User
 ↓
DNS
 ↓
Network
 ↓
Routing
 ↓
Firewall
 ↓
Load Balancer
 ↓
Server
 ↓
Process
 ↓
Application
 ↓
Database
```

Test one layer at a time.

---

# 10. Layer-by-Layer Troubleshooting

## Layer 1 — DNS

Check:

```bash
dig example.com
```

Questions:

* Does DNS resolve?
* Is the correct IP returned?
* Is the DNS server reachable?

---

## Layer 2 — Network

Check:

```bash
ping <destination>
```

Then:

```bash
ip addr
ip route
```

---

## Layer 3 — TCP

Check the port:

```bash
nc -vz <host> <port>
```

---

## Layer 4 — Application

Check HTTP:

```bash
curl -v https://example.com
```

---

## Layer 5 — Service

Check:

```bash
systemctl status <service>
```

---

## Layer 6 — Logs

Check:

```bash
journalctl -u <service>
```

---

# 11. Connection Refused

Example:

```text
Connection refused
```

Common causes:

* Service is stopped
* Nothing is listening
* Wrong port
* Application crashed
* Local firewall rejected the connection

Check:

```bash
sudo ss -lntp
```

Then:

```bash
systemctl status <service>
```

---

# 12. Connection Timeout

A timeout usually means that a response was not received within the expected time.

Possible causes:

* Firewall
* Security Group
* Network ACL
* Routing problem
* Server unavailable
* Packet filtering
* Incorrect network configuration

Useful commands:

```bash
ping <host>
nc -vz <host> <port>
traceroute <host>
```

---

# 13. DNS Failure

Symptoms:

```text
Could not resolve hostname
DNS_PROBE_FINISHED_NXDOMAIN
Temporary failure in name resolution
```

Check:

```bash
dig example.com
```

and:

```bash
cat /etc/resolv.conf
```

Depending on the Linux distribution, also inspect:

```bash
resolvectl status
```

---

# 14. High Latency

Symptoms:

```text
Application is slow
API response is slow
SSH is slow
Database requests are slow
```

Investigate:

```text
DNS latency
 ↓
Network latency
 ↓
Packet loss
 ↓
Routing
 ↓
Server resources
 ↓
Application
 ↓
Database
```

Commands:

```bash
ping <host>
traceroute <host>
curl -w '%{time_total}\n' <url>
```

---

# 15. Packet Loss

Check:

```bash
ping -c 20 <host>
```

Then inspect interface statistics:

```bash
ip -s link
```

Look for:

```text
RX errors
TX errors
RX drops
TX drops
```

---

# 16. High Network Traffic

Check:

```bash
ip -s link
```

and:

```bash
sar -n DEV
```

You can also inspect active connections:

```bash
ss -s
```

For packet-level investigation:

```bash
sudo tcpdump -i any
```

---

# 17. Linux Troubleshooting

Important Linux areas:

```text
CPU
Memory
Disk
Processes
Services
Network
Logs
File systems
Permissions
```

Useful commands:

```bash
top
free -h
df -h
du -sh
ps aux
ss -lntup
ip addr
ip route
journalctl
```

---

# 18. CPU Troubleshooting

Check:

```bash
top
```

or:

```bash
uptime
```

Look for:

* High CPU utilization
* Load average
* CPU-consuming processes
* Recent deployments

Find processes:

```bash
ps aux --sort=-%cpu | head
```

---

# 19. Memory Troubleshooting

Check:

```bash
free -h
```

Find memory-heavy processes:

```bash
ps aux --sort=-%mem | head
```

Also investigate:

* Swap usage
* Out-of-memory events
* Application memory leaks
* Container limits

---

# 20. Disk Troubleshooting

Check filesystem usage:

```bash
df -h
```

Find large directories:

```bash
du -sh /* 2>/dev/null
```

Check inode usage:

```bash
df -i
```

A server can have free disk space but still run out of inodes.

---

# 21. Process Troubleshooting

List processes:

```bash
ps aux
```

Find a specific process:

```bash
ps aux | grep <process>
```

Check process resource usage:

```bash
top
```

---

# 22. Service Troubleshooting

Check service status:

```bash
systemctl status <service>
```

Restart only when appropriate:

```bash
sudo systemctl restart <service>
```

Check logs:

```bash
journalctl -u <service>
```

Recent logs:

```bash
journalctl -u <service> --since "30 minutes ago"
```

---

# 23. Log Troubleshooting

Logs are one of the most important sources of evidence.

Useful commands:

```bash
journalctl
```

```bash
tail -f /var/log/<file>
```

Search:

```bash
grep -i "error" <logfile>
```

Search multiple terms:

```bash
grep -Ei "error|failed|timeout|refused" <logfile>
```

---

# 24. Docker Troubleshooting

Check containers:

```bash
docker ps
```

Check all containers:

```bash
docker ps -a
```

Check logs:

```bash
docker logs <container>
```

Follow logs:

```bash
docker logs -f <container>
```

Inspect container:

```bash
docker inspect <container>
```

Check resources:

```bash
docker stats
```

---

# 25. Docker Network Troubleshooting

List networks:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect <network>
```

Check published ports:

```bash
docker ps
```

Test connectivity from a container where appropriate.

---

# 26. Kubernetes Troubleshooting

Start with:

```bash
kubectl get nodes
```

Then:

```bash
kubectl get pods -A
```

Check Services:

```bash
kubectl get svc -A
```

Check endpoints:

```bash
kubectl get endpoints -A
```

Inspect resources:

```bash
kubectl describe pod <pod>
```

Check logs:

```bash
kubectl logs <pod>
```

---

# 27. Kubernetes Pod Troubleshooting

Check:

```bash
kubectl get pods -o wide
```

Then:

```bash
kubectl describe pod <pod>
```

Look for:

* CrashLoopBackOff
* ImagePullBackOff
* Pending
* Failed
* Restart count
* Events

---

# 28. Kubernetes Service Troubleshooting

If a Service is not reachable:

```text
Service
  ↓
Selector
  ↓
Endpoints
  ↓
Pod
  ↓
Container port
```

Check:

```bash
kubectl get svc
kubectl describe svc <service>
kubectl get endpoints <service>
kubectl get endpointslices
kubectl get pods --show-labels
```

A common problem is a selector that does not match Pod labels.

---

# 29. Kubernetes DNS Troubleshooting

Test DNS from a Pod:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --rm -it \
  --restart=Never \
  -- nslookup kubernetes.default
```

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Check logs when appropriate:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

---

# 30. Kubernetes NetworkPolicy Troubleshooting

If communication suddenly stops, check:

```bash
kubectl get networkpolicy -A
```

Inspect:

```bash
kubectl describe networkpolicy <policy>
```

Remember:

> NetworkPolicy behavior depends on the Kubernetes networking implementation/CNI.

---

# 31. AWS Troubleshooting

Important AWS networking components include:

```text
VPC
Subnets
Route Tables
Internet Gateway
NAT Gateway
Security Groups
Network ACLs
Load Balancers
ENIs
VPC Flow Logs
```

---

# 32. AWS Security Group Troubleshooting

Check whether traffic is allowed.

Consider:

```text
Source
Destination
Protocol
Port
Security Group rules
```

Remember:

> Security Groups are stateful.

---

# 33. AWS Network ACL Troubleshooting

Check:

* Inbound rules
* Outbound rules
* Rule numbers
* Allow/deny behavior

Remember:

> Network ACLs are stateless.

---

# 34. AWS Routing Troubleshooting

Check the route table.

Questions:

```text
Does the subnet have the correct route?
Is there an Internet Gateway?
Is there a NAT Gateway?
Is the destination reachable?
```

---

# 35. HTTP Troubleshooting

Check:

```bash
curl -v https://example.com
```

Status code:

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://example.com
```

Possible responses:

```text
200 → Success
301/302 → Redirect
400 → Client request problem
401 → Authentication required
403 → Forbidden
404 → Not Found
500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout
```

---

# 36. HTTPS Troubleshooting

Check:

```bash
curl -v https://example.com
```

Investigate:

* DNS
* TCP connection
* TLS handshake
* Certificate
* Expiration
* Hostname
* Load balancer
* Backend service

---

# 37. Recent Changes

One of the most important troubleshooting questions is:

> **What changed?**

Check:

```text
Deployment
Configuration
DNS
Firewall
Security Group
NetworkPolicy
Infrastructure
Application version
Dependencies
Certificates
```

Many production incidents occur immediately after a change.

---

# 38. Five Whys

The Five Whys technique helps find the root cause.

Example:

```text
Why did users get errors?
→ Application failed.

Why did application fail?
→ Database connection failed.

Why did database connection fail?
→ DNS resolution failed.

Why did DNS resolution fail?
→ Resolver configuration changed.

Why did configuration change?
→ Incorrect deployment configuration.
```

Root cause:

```text
Incorrect deployment configuration
```

---

# 39. Root Cause Analysis

RCA means **Root Cause Analysis**.

An RCA should explain:

```text
What happened?
When did it happen?
Who/what was affected?
Why did it happen?
How was it detected?
How was it fixed?
How will we prevent it?
```

---

# 40. Incident Response

A simple incident lifecycle:

```text
Detect
 ↓
Acknowledge
 ↓
Assess
 ↓
Mitigate
 ↓
Investigate
 ↓
Resolve
 ↓
Verify
 ↓
Document
 ↓
Prevent
```

---

# 41. Mitigation vs Root Cause Fix

These are different.

### Mitigation

Reduces the immediate impact.

Example:

```text
Rollback deployment
```

### Root Cause Fix

Fixes the underlying problem.

Example:

```text
Correct deployment configuration
```

A good engineer performs both.

---

# 42. Postmortem

After a significant incident, teams may perform a postmortem.

A useful postmortem contains:

* Incident summary
* Timeline
* Impact
* Root cause
* Detection
* Resolution
* Contributing factors
* Corrective actions
* Preventive actions

The goal should be learning and prevention, not blame.

---

# 43. Troubleshooting Golden Rules

## Rule 1

```text
Do not guess.
Collect evidence.
```

## Rule 2

```text
Change one thing at a time when possible.
```

## Rule 3

```text
Check recent changes.
```

## Rule 4

```text
Start with the simplest explanation.
```

## Rule 5

```text
Troubleshoot layer by layer.
```

## Rule 6

```text
Verify after fixing.
```

## Rule 7

```text
Document important incidents.
```

---

# 44. Production Troubleshooting Flow

Use this mental model:

```text
                INCIDENT
                    |
                    ↓
             What is failing?
                    |
                    ↓
               Who is affected?
                    |
                    ↓
             When did it start?
                    |
                    ↓
             What changed?
                    |
                    ↓
             Collect evidence
                    |
          +---------+---------+
          |         |         |
         Logs     Metrics   Events
          |         |         |
          +---------+---------+
                    |
                    ↓
              Isolate layer
                    |
        +-----------+-----------+
        |           |           |
       DNS        Network     System
        |           |           |
        +-----------+-----------+
                    |
                    ↓
                Application
                    |
                    ↓
                Root Cause
                    |
                    ↓
                 Mitigate
                    |
                    ↓
                   Fix
                    |
                    ↓
                 Verify
                    |
                    ↓
               Monitor
                    |
                    ↓
               Document
```

---

# 45. Common Troubleshooting Scenarios

## Scenario 1 — Website is down

Check:

```bash
dig example.com
ping <ip>
nc -vz <ip> 443
curl -v https://example.com
```

Then investigate:

```text
DNS
Load Balancer
Firewall
Server
Web server
Application
```

---

## Scenario 2 — SSH is not working

Check:

```bash
ping <server>
nc -vz <server> 22
```

On the server:

```bash
sudo ss -lntp | grep ':22'
systemctl status ssh
```

Then check firewall and cloud security rules.

---

## Scenario 3 — API is slow

Check:

```text
DNS latency
Network latency
HTTP response time
Application CPU
Memory
Database latency
Recent deployments
```

---

## Scenario 4 — Container cannot connect to database

Check:

```text
DNS
Container network
Database hostname
Database port
Firewall
Credentials
Database availability
```

Useful commands:

```bash
docker network ls
docker network inspect <network>
nc -vz <database-host> <port>
```

---

## Scenario 5 — Kubernetes application is unreachable

Check:

```bash
kubectl get pods -o wide
kubectl get svc
kubectl get endpoints
kubectl get endpointslices
```

Then investigate:

```text
Pod
Service
Selector
Endpoints
Port
NetworkPolicy
Ingress/Load Balancer
```

---

# 46. Troubleshooting Toolkit

## Linux

```bash
ip
ss
ping
traceroute
tracepath
dig
curl
nc
tcpdump
ps
top
free
df
du
systemctl
journalctl
```

## Docker

```bash
docker ps
docker logs
docker inspect
docker stats
docker network
```

## Kubernetes

```bash
kubectl get
kubectl describe
kubectl logs
kubectl exec
kubectl top
kubectl events
```

## AWS

```text
CloudWatch
VPC Flow Logs
Route Tables
Security Groups
Network ACLs
Load Balancer metrics
```

---

# 47. Important Troubleshooting Principle

A useful DevOps troubleshooting sequence is:

```text
DNS
 ↓
Connectivity
 ↓
Routing
 ↓
Port
 ↓
Firewall
 ↓
Service
 ↓
Application
 ↓
Dependencies
 ↓
Logs
 ↓
Metrics
 ↓
Root Cause
```

But this is not a rigid rule.

Always adapt the investigation based on the evidence and symptoms.

---

# 48. What Makes a Good DevOps Troubleshooter?

A strong DevOps troubleshooter:

* Thinks systematically
* Remains calm during incidents
* Uses evidence
* Understands Linux
* Understands networking
* Understands cloud
* Understands containers
* Understands Kubernetes
* Reads logs
* Understands metrics
* Knows useful commands
* Avoids unnecessary changes
* Communicates clearly
* Documents incidents
* Looks for root causes
* Prevents recurrence

---

# 49. Final Checklist

Before completing this chapter, make sure you understand:

* [ ] Troubleshooting methodology
* [ ] Evidence collection
* [ ] Logs
* [ ] Metrics
* [ ] Events
* [ ] DNS troubleshooting
* [ ] Network troubleshooting
* [ ] TCP troubleshooting
* [ ] HTTP troubleshooting
* [ ] HTTPS troubleshooting
* [ ] Linux troubleshooting
* [ ] CPU troubleshooting
* [ ] Memory troubleshooting
* [ ] Disk troubleshooting
* [ ] Process troubleshooting
* [ ] Service troubleshooting
* [ ] Docker troubleshooting
* [ ] Kubernetes troubleshooting
* [ ] AWS troubleshooting
* [ ] Firewall troubleshooting
* [ ] Routing troubleshooting
* [ ] Packet loss
* [ ] High latency
* [ ] Connection refused
* [ ] Connection timeout
* [ ] Five Whys
* [ ] Root Cause Analysis
* [ ] Incident response
* [ ] Mitigation
* [ ] Postmortems

---

# 50. Final Mental Model

```text
PROBLEM
   ↓
OBSERVE
   ↓
COLLECT EVIDENCE
   ↓
ISOLATE
   ↓
ANALYZE
   ↓
ROOT CAUSE
   ↓
MITIGATE
   ↓
FIX
   ↓
VERIFY
   ↓
MONITOR
   ↓
DOCUMENT
   ↓
PREVENT
```

## The DevOps Troubleshooting Mindset

> **Don't ask "What should I change?" first.**

Ask:

> **"What evidence can tell me what is actually wrong?"**

That mindset turns troubleshooting from guesswork into engineering.
