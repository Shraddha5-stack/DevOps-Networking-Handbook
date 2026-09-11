# Chapter 36 — Troubleshooting — Notes

## 1. What Is Troubleshooting?

Troubleshooting is the systematic process of identifying, analyzing, and resolving a problem.

In DevOps, troubleshooting can involve:

* Linux
* Networking
* Applications
* Databases
* Docker
* Kubernetes
* AWS
* CI/CD
* Security
* Monitoring

The goal is not simply to make the system work again.

The goal is to understand:

```text
What happened?
     ↓
Why did it happen?
     ↓
How was it fixed?
     ↓
How can we prevent it?
```

---

# 2. Troubleshooting Mindset

The most important troubleshooting rule is:

> **Do not guess. Collect evidence.**

Bad approach:

```text
Application is slow
        ↓
Restart everything
```

Better approach:

```text
Application is slow
        ↓
Check metrics
        ↓
Check logs
        ↓
Check recent changes
        ↓
Check network
        ↓
Check dependencies
        ↓
Identify root cause
        ↓
Fix
        ↓
Verify
```

---

# 3. Troubleshooting Lifecycle

A practical troubleshooting lifecycle is:

```text
Identify
   ↓
Define
   ↓
Collect Evidence
   ↓
Reproduce
   ↓
Isolate
   ↓
Analyze
   ↓
Mitigate
   ↓
Fix
   ↓
Verify
   ↓
Monitor
   ↓
Document
   ↓
Prevent
```

---

# 4. Identify the Problem

First determine exactly what is failing.

Ask:

* What is not working?
* Which service is affected?
* Who is affected?
* When did it start?
* Is the problem constant?
* Is it intermittent?
* Is one endpoint affected?
* Is the entire application affected?

Example:

```text
Problem:
Users cannot access the website.
```

This is only the symptom.

We still need to determine the cause.

---

# 5. Define the Scope

Scope tells us how large the problem is.

Example:

```text
One user
   ↓
Several users
   ↓
One server
   ↓
Multiple servers
   ↓
One availability zone
   ↓
Entire region
   ↓
Entire application
```

If only one server is affected, the investigation is different from an outage affecting the entire production environment.

---

# 6. Symptoms vs Root Cause

These are not the same.

### Symptom

What users or systems observe.

Example:

```text
Website returns HTTP 503.
```

### Root Cause

The underlying reason.

Example:

```text
All backend instances became unhealthy because
a deployment introduced an invalid configuration.
```

A good troubleshooter separates symptoms from causes.

---

# 7. Evidence

Evidence helps us make technical decisions.

Important evidence includes:

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
Traffic
Errors
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

### Commands

```text
ip
ss
ping
dig
curl
nc
tcpdump
ps
top
df
free
systemctl
journalctl
```

---

# 8. Recent Changes

One of the most important questions during troubleshooting is:

> **What changed recently?**

Check:

* Application deployment
* Infrastructure changes
* DNS changes
* Firewall changes
* Security Group changes
* NetworkPolicy changes
* Configuration changes
* Certificate changes
* Dependency changes
* Database changes

Example:

```text
Application worked at 10:00
        ↓
Deployment at 10:15
        ↓
Application failed at 10:16
```

The deployment becomes an important investigation point.

---

# 9. Troubleshooting from the Outside In

For a web application, a useful approach is:

```text
User
 ↓
DNS
 ↓
Internet / Network
 ↓
Load Balancer
 ↓
Firewall / Security
 ↓
Server
 ↓
Process
 ↓
Application
 ↓
Database / Dependency
```

Test each layer.

---

# 10. DNS Troubleshooting

DNS converts names into IP addresses.

Example:

```text
example.com
     ↓
93.184.x.x
```

Test:

```bash
dig example.com
```

Short output:

```bash
dig +short example.com
```

Check DNS response time:

```bash
dig example.com | grep "Query time"
```

Test a specific DNS server:

```bash
dig @8.8.8.8 example.com
```

---

# 11. DNS Failure Symptoms

Common symptoms:

```text
Could not resolve hostname
Temporary failure in name resolution
Name or service not known
NXDOMAIN
```

Possible causes:

* DNS server unavailable
* Incorrect resolver configuration
* Domain does not exist
* DNS record is incorrect
* Network cannot reach DNS
* Local DNS cache issue

Check:

```bash
cat /etc/resolv.conf
```

Depending on the system:

```bash
resolvectl status
```

---

# 12. IP Troubleshooting

Check interfaces:

```bash
ip addr
```

Short format:

```bash
ip -brief addr
```

Check interface state:

```bash
ip link
```

Questions:

```text
Does the interface exist?
Is it UP?
Does it have an IP?
Is the IP correct?
```

---

# 13. Routing Troubleshooting

Check routes:

```bash
ip route
```

Look for the default route:

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

Questions:

* Is the default route present?
* Is the gateway correct?
* Is the destination reachable?
* Is traffic going through the expected interface?

---

# 14. Ping Troubleshooting

Test connectivity:

```bash
ping -c 4 8.8.8.8
```

Ping can help determine:

* Reachability
* Round-trip latency
* Packet loss

However:

> **Ping failure does not always mean the application is down.**

ICMP may be blocked.

---

# 15. Connection Refused

Example:

```text
connect: Connection refused
```

This usually means the destination was reachable but the connection was rejected.

Common causes:

* No service listening
* Wrong port
* Service stopped
* Application crashed
* Firewall rejection

Check listening ports:

```bash
sudo ss -lntup
```

Check a specific port:

```bash
sudo ss -lntp | grep ':8080'
```

---

# 16. Connection Timeout

A timeout means the expected response was not received within the configured time.

Possible causes:

```text
Firewall
Security Group
Network ACL
Routing
Server unavailable
Packet filtering
Network failure
```

Test:

```bash
nc -vz <host> <port>
```

Also:

```bash
traceroute <host>
```

---

# 17. Refused vs Timeout

| Connection Refused              | Connection Timeout                   |
| ------------------------------- | ------------------------------------ |
| Destination generally responded | No response received in time         |
| Often no listener               | Often filtering/routing/connectivity |
| Service may be stopped          | Firewall may be involved             |
| Fast failure                    | Can take longer                      |
| Check listening ports           | Check network path/firewall          |

Mental model:

```text
REFUSED
→ "I reached something, but it rejected me."

TIMEOUT
→ "I didn't get the expected response."
```

---

# 18. Port Troubleshooting

Check local listening ports:

```bash
sudo ss -lntup
```

Test remote TCP port:

```bash
nc -vz <host> <port>
```

Example:

```bash
nc -vz example.com 443
```

Questions:

```text
Is the service listening?
Is it listening on the correct IP?
Is the correct port being used?
Is a firewall blocking it?
```

---

# 19. Bind Address

A common problem is an application listening only on localhost.

Example:

```text
127.0.0.1:8080
```

This means the service is accessible from the local machine through that address but is not directly listening on the machine's other network interfaces.

Check:

```bash
ss -lntp
```

Compare:

```text
127.0.0.1:8080
```

with:

```text
0.0.0.0:8080
```

or an appropriate specific interface address.

---

# 20. HTTP Troubleshooting

Basic test:

```bash
curl -I https://example.com
```

Detailed test:

```bash
curl -v https://example.com
```

Check status:

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://example.com
```

---

# 21. Important HTTP Status Codes

| Code | Meaning               |
| ---: | --------------------- |
|  200 | OK                    |
|  201 | Created               |
|  301 | Permanent redirect    |
|  302 | Temporary redirect    |
|  400 | Bad Request           |
|  401 | Unauthorized          |
|  403 | Forbidden             |
|  404 | Not Found             |
|  500 | Internal Server Error |
|  502 | Bad Gateway           |
|  503 | Service Unavailable   |
|  504 | Gateway Timeout       |

---

# 22. HTTP 502 Bad Gateway

A 502 often indicates that a proxy or load balancer received an invalid or unsuccessful response from an upstream server.

Possible areas:

```text
Load Balancer
     ↓
Reverse Proxy
     ↓
Application
     ↓
Backend
```

Investigate:

* Backend health
* Backend port
* Application status
* Network connectivity
* Proxy configuration
* Application logs

---

# 23. HTTP 503 Service Unavailable

503 means the service is currently unable to handle the request.

Possible causes:

* Application unavailable
* No healthy backend
* Maintenance
* Overload
* Load balancer health-check failure

Check:

```text
Backend health
Application logs
Load balancer metrics
Server resources
Recent deployments
```

---

# 24. HTTP 504 Gateway Timeout

A 504 commonly means a gateway/proxy did not receive a timely response from an upstream service.

Possible causes:

```text
Slow backend
Network problem
Database latency
Application overload
Incorrect timeout configuration
```

---

# 25. HTTPS Troubleshooting

HTTPS involves several stages:

```text
DNS
 ↓
TCP connection
 ↓
TLS handshake
 ↓
HTTP request
 ↓
Application response
```

If HTTPS fails, determine which stage is failing.

Use:

```bash
curl -v https://example.com
```

---

# 26. TLS Troubleshooting

Important things to check:

* Certificate validity
* Certificate expiration
* Hostname
* Certificate chain
* TLS configuration
* Supported protocol versions
* Load balancer configuration

A TLS problem can occur even when TCP connectivity works.

---

# 27. High Latency

Symptoms:

* Slow website
* Slow API
* Slow SSH
* Slow database connection

Investigate:

```text
DNS
 ↓
Network
 ↓
Routing
 ↓
TCP
 ↓
TLS
 ↓
Application
 ↓
Database
```

Measure HTTP timing:

```bash
curl -o /dev/null -s -w \
'DNS=%{time_namelookup} CONNECT=%{time_connect} TLS=%{time_appconnect} START=%{time_starttransfer} TOTAL=%{time_total}\n' \
https://example.com
```

---

# 28. Packet Loss

Test:

```bash
ping -c 20 <host>
```

Check interface errors:

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

Packet loss can result from:

* Congestion
* Faulty links
* Interface problems
* Network devices
* Routing issues
* Packet filtering

---

# 29. Network Traffic Troubleshooting

Check interface statistics:

```bash
ip -s link
```

Use:

```bash
sar -n DEV
```

Check connections:

```bash
ss -s
```

Packet-level analysis:

```bash
sudo tcpdump -i any
```

---

# 30. CPU Troubleshooting

Check:

```bash
top
```

or:

```bash
uptime
```

Find high-CPU processes:

```bash
ps aux --sort=-%cpu | head
```

Investigate:

* CPU utilization
* Load average
* Processes
* Recent deployments
* Traffic increase
* Application behavior

---

# 31. Load Average

Check:

```bash
uptime
```

Example:

```text
load average: 1.20, 0.80, 0.50
```

These values represent load over different time windows.

Load average should be interpreted together with CPU count and workload characteristics.

---

# 32. Memory Troubleshooting

Check:

```bash
free -h
```

Find high-memory processes:

```bash
ps aux --sort=-%mem | head
```

Investigate:

* Available memory
* Swap
* OOM events
* Memory leaks
* Container limits

---

# 33. Disk Troubleshooting

Check disk usage:

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

Important:

> A filesystem can have free disk space but still run out of inodes.

---

# 34. Process Troubleshooting

List processes:

```bash
ps aux
```

Search:

```bash
ps aux | grep <process>
```

Monitor:

```bash
top
```

Questions:

```text
Is the process running?
Is it consuming too much CPU?
Is it consuming too much memory?
Is it repeatedly restarting?
```

---

# 35. Service Troubleshooting

Check:

```bash
systemctl status <service>
```

Check recent logs:

```bash
journalctl -u <service> --since "30 minutes ago"
```

Validate configuration where supported:

```bash
sudo <service> -t
```

Restart only after understanding the impact:

```bash
sudo systemctl restart <service>
```

---

# 36. Log Analysis

Search errors:

```bash
grep -i "error" <logfile>
```

Search multiple failure patterns:

```bash
grep -Ei "error|failed|timeout|refused" <logfile>
```

Follow logs:

```bash
tail -f <logfile>
```

For systemd services:

```bash
journalctl -u <service> -f
```

---

# 37. Five Whys

The Five Whys technique helps move from symptom to root cause.

Example:

```text
Why did users receive errors?
→ Application failed.

Why did application fail?
→ Database connection failed.

Why did database connection fail?
→ Database hostname could not be resolved.

Why couldn't it be resolved?
→ DNS configuration was incorrect.

Why was DNS configuration incorrect?
→ Deployment contained an incorrect configuration.
```

Root cause:

```text
Incorrect deployment configuration.
```

---

# 38. Root Cause Analysis

RCA means **Root Cause Analysis**.

A good RCA should answer:

```text
What happened?
When?
Who was affected?
What was the impact?
Why did it happen?
How was it detected?
How was it mitigated?
What was the root cause?
How will we prevent recurrence?
```

---

# 39. Mitigation

Mitigation reduces the immediate impact.

Examples:

```text
Rollback deployment
Scale service
Fail over
Remove unhealthy instance
Disable problematic feature
```

Mitigation may restore service before the complete root cause is understood.

---

# 40. Permanent Fix

A permanent fix addresses the underlying problem.

Example:

```text
Immediate:
Rollback deployment.

Permanent:
Fix invalid configuration,
add validation,
and improve deployment checks.
```

---

# 41. Verification

Never assume that the problem is fixed.

After a change:

```text
Test
 ↓
Check metrics
 ↓
Check logs
 ↓
Check user-facing behavior
 ↓
Monitor
```

Example:

```bash
curl -I https://example.com
```

Then check monitoring dashboards.

---

# 42. Documentation

Document important troubleshooting work.

Record:

* Symptoms
* Commands
* Evidence
* Findings
* Changes
* Root cause
* Fix
* Verification
* Preventive action

This helps future engineers solve similar incidents faster.

---

# 43. Docker Troubleshooting

Start with:

```bash
docker ps
```

Check stopped containers:

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

Inspect:

```bash
docker inspect <container>
```

Monitor resources:

```bash
docker stats
```

---

# 44. Docker Network Troubleshooting

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

Investigate:

```text
Container
 ↓
Network
 ↓
DNS
 ↓
Destination
 ↓
Port
```

---

# 45. Kubernetes Troubleshooting

Start with cluster state:

```bash
kubectl get nodes
```

Check Pods:

```bash
kubectl get pods -A
```

Check Services:

```bash
kubectl get svc -A
```

Check recent events:

```bash
kubectl events -A
```

Depending on Kubernetes version and environment, you can also inspect events with:

```bash
kubectl get events -A --sort-by='.lastTimestamp'
```

---

# 46. Kubernetes Pod Troubleshooting

Check:

```bash
kubectl get pods -o wide
```

Describe:

```bash
kubectl describe pod <pod>
```

Logs:

```bash
kubectl logs <pod>
```

Previous container logs:

```bash
kubectl logs <pod> --previous
```

Look for:

```text
CrashLoopBackOff
ImagePullBackOff
Pending
Failed
OOMKilled
Restart count
```

---

# 47. Kubernetes Service Troubleshooting

A Service depends on matching endpoints.

Mental model:

```text
Service
   ↓
Selector
   ↓
Pod Labels
   ↓
Endpoints
   ↓
Pod
```

Check:

```bash
kubectl get svc
kubectl describe svc <service>
kubectl get endpoints <service>
kubectl get endpointslices
kubectl get pods --show-labels
```

A selector mismatch can result in a Service with no usable endpoints.

---

# 48. Kubernetes DNS Troubleshooting

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Test DNS:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --rm -it \
  --restart=Never \
  -- nslookup kubernetes.default
```

If needed, inspect CoreDNS logs:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

---

# 49. Kubernetes NetworkPolicy Troubleshooting

Check policies:

```bash
kubectl get networkpolicy -A
```

Describe:

```bash
kubectl describe networkpolicy <policy>
```

If connectivity is blocked, verify:

```text
Pod labels
Namespace
Ingress rules
Egress rules
Ports
Selectors
CNI support
```

Remember:

> NetworkPolicy enforcement depends on the Kubernetes networking implementation/CNI.

---

# 50. AWS Troubleshooting

Important AWS networking components:

```text
VPC
 ↓
Subnet
 ↓
Route Table
 ↓
Internet Gateway / NAT Gateway
 ↓
Security Group
 ↓
Network ACL
 ↓
ENI
 ↓
Application
```

Investigate each relevant layer.

---

# 51. AWS Security Group Troubleshooting

Check:

* Source
* Destination
* Protocol
* Port
* Security Group rules
* Instance/network interface association

Remember:

> Security Groups are stateful.

---

# 52. AWS Network ACL Troubleshooting

Check:

* Inbound rules
* Outbound rules
* Rule numbers
* Allow/deny rules

Remember:

> Network ACLs are stateless.

Therefore, both directions may need appropriate rules.

---

# 53. AWS Route Troubleshooting

Check the subnet route table.

Ask:

```text
Is the destination route present?
Is the next hop correct?
Is the subnet public or private?
Is an Internet Gateway required?
Is a NAT Gateway required?
```

---

# 54. VPC Flow Logs

VPC Flow Logs can help investigate network traffic flows.

They can provide information about:

* Source
* Destination
* Ports
* Protocol
* Traffic direction
* Accepted/rejected traffic
* Flow behavior

Important:

> VPC Flow Logs are flow telemetry, not full packet captures.

---

# 55. Troubleshooting with Monitoring

Monitoring should provide evidence before and during incidents.

Useful metrics:

```text
Latency
Traffic
Errors
Saturation
CPU
Memory
Network utilization
Packet loss
Connections
```

Monitoring helps answer:

```text
When did the problem start?
What changed?
Which component was affected?
Is the problem getting better or worse?
```

---

# 56. Baseline

A baseline represents normal system behavior.

Example:

```text
Normal HTTP latency:
50–100 ms

Current:
700 ms
```

The deviation indicates an abnormal condition.

Baseline data can include:

* CPU
* Memory
* Network traffic
* Latency
* Errors
* Connections
* Request rate

---

# 57. Incident Response

A practical incident lifecycle:

```text
Detect
 ↓
Acknowledge
 ↓
Assess
 ↓
Communicate
 ↓
Mitigate
 ↓
Investigate
 ↓
Resolve
 ↓
Verify
 ↓
Monitor
 ↓
Document
```

---

# 58. Communication During Incidents

During production incidents, communication is important.

Communicate:

* What is affected
* Current impact
* What is being investigated
* Current mitigation
* Expected next update
* Resolution status

Avoid unsupported statements.

Instead of:

```text
"The network is definitely broken."
```

say:

```text
"We are seeing increased connection timeouts
from the application tier and are investigating
network and backend connectivity."
```

---

# 59. Change One Thing at a Time

When possible, avoid making many unrelated changes simultaneously.

Bad:

```text
Change firewall
Restart server
Change DNS
Restart application
```

You may not know which change fixed or caused the problem.

Better:

```text
Change
 ↓
Test
 ↓
Observe
 ↓
Next change if required
```

---

# 60. Common Failure Patterns

## Pattern 1

```text
DNS fails
→ Application cannot resolve dependency
```

## Pattern 2

```text
Port closed
→ Connection refused
```

## Pattern 3

```text
Firewall blocks traffic
→ Timeout
```

## Pattern 4

```text
Service selector mismatch
→ Kubernetes Service has no endpoints
```

## Pattern 5

```text
Container exits
→ Application unavailable
```

## Pattern 6

```text
Disk full
→ Application cannot write logs/data
```

## Pattern 7

```text
Memory exhausted
→ Process killed / OOM
```

## Pattern 8

```text
High CPU
→ Application response becomes slow
```

---

# 61. Troubleshooting Decision Tree

```text
Application unavailable
        |
        ↓
Can DNS resolve?
   /          \
 NO            YES
 |              |
Fix DNS       Can TCP connect?
              /          \
            NO            YES
            |               |
       Check network       HTTP works?
       routing/firewall    /       \
                          NO        YES
                          |          |
                     Check HTTP     Service
                     / TLS / app    healthy
```

---

# 62. Production Troubleshooting Model

Think in layers:

```text
┌─────────────────────────┐
│       Application       │
├─────────────────────────┤
│      Dependencies       │
├─────────────────────────┤
│      Load Balancer      │
├─────────────────────────┤
│      TCP / Ports        │
├─────────────────────────┤
│   Firewall / Security   │
├─────────────────────────┤
│    Routing / Network    │
├─────────────────────────┤
│          DNS            │
├─────────────────────────┤
│     Infrastructure      │
└─────────────────────────┘
```

Troubleshoot from the evidence, not from assumptions.

---

# 63. Important Commands Cheat Sheet

## Network

```bash
ip addr
ip link
ip route
ip -s link
```

## Connections

```bash
ss -lntup
ss -ant
ss -s
```

## Connectivity

```bash
ping -c 4 <host>
traceroute <host>
tracepath <host>
```

## DNS

```bash
dig <domain>
dig +short <domain>
```

## Ports

```bash
nc -vz <host> <port>
```

## HTTP

```bash
curl -I <url>
curl -v <url>
```

## Packets

```bash
sudo tcpdump -i any
```

## Processes

```bash
ps aux
top
```

## Memory

```bash
free -h
```

## Disk

```bash
df -h
df -i
du -sh
```

## Services

```bash
systemctl status <service>
journalctl -u <service>
```

## Docker

```bash
docker ps
docker logs <container>
docker inspect <container>
docker stats
docker network ls
```

## Kubernetes

```bash
kubectl get nodes
kubectl get pods -A
kubectl get svc -A
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get endpoints -A
```

---

# 64. Troubleshooting Best Practices

### 1. Start with the symptom

Understand exactly what users are experiencing.

### 2. Collect evidence

Use logs, metrics, events, and commands.

### 3. Check recent changes

Changes are important clues.

### 4. Isolate the layer

Do not investigate everything simultaneously.

### 5. Make controlled changes

Avoid random configuration changes.

### 6. Verify

Confirm that the fix actually works.

### 7. Monitor

Watch the system after recovery.

### 8. Document

Record the incident and solution.

### 9. Prevent

Improve automation, monitoring, testing, and architecture.

---

# 65. Interview Mental Model

When asked:

> **"How do you troubleshoot a production issue?"**

Think:

```text
WHAT?
 ↓
WHO?
 ↓
WHEN?
 ↓
WHAT CHANGED?
 ↓
EVIDENCE
 ↓
ISOLATE
 ↓
ROOT CAUSE
 ↓
MITIGATE
 ↓
FIX
 ↓
VERIFY
 ↓
PREVENT
```

---

# 66. Final Mental Model

The best troubleshooting mindset is:

```text
Don't Guess
    ↓
Observe
    ↓
Collect Evidence
    ↓
Form Hypothesis
    ↓
Test Hypothesis
    ↓
Find Root Cause
    ↓
Fix
    ↓
Verify
    ↓
Learn
    ↓
Prevent
```

> **Troubleshooting is not about knowing every answer. It is about knowing how to find the answer systematically.**
