# Chapter 37 — Real-World Case Studies — Notes

## 1. Introduction

Real-world DevOps problems rarely belong to only one technology.

A production outage can involve:

```text
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
Web Server
 ↓
Application
 ↓
Database
 ↓
External Dependency
```

A DevOps engineer must understand the complete request path.

The most important skill is not memorizing commands.

It is:

> **Observe → Isolate → Investigate → Fix → Verify → Prevent**

---

# 2. Production Troubleshooting Mindset

Never begin with:

> "I think the firewall is the problem."

Instead begin with:

> "What evidence do we have?"

A good troubleshooting process is:

```text
1. Understand the problem
2. Determine the scope
3. Check impact
4. Check recent changes
5. Reproduce the issue
6. Collect evidence
7. Identify the failing layer
8. Find the root cause
9. Apply a safe mitigation
10. Verify recovery
11. Prevent recurrence
12. Document the incident
```

---

# 3. Incident Scope

Before troubleshooting, determine how large the problem is.

Ask:

```text
Is one user affected?
Is one machine affected?
Is one application affected?
Is one availability zone affected?
Is one region affected?
Are all users affected?
```

Example:

```text
One user cannot access website
```

is very different from:

```text
All users cannot access website
```

Scope helps narrow the investigation.

---

# 4. Recent Changes

Always ask:

> What changed before the problem started?

Possible changes:

* Application deployment
* DNS change
* Security Group change
* NACL change
* Firewall change
* Load balancer change
* Route change
* Kubernetes deployment
* NetworkPolicy change
* Certificate renewal
* Database change
* Infrastructure change
* Configuration change

A timeline is extremely useful.

```text
Deployment
    ↓
Latency increases
    ↓
Errors increase
    ↓
Incident starts
```

The deployment becomes an important investigation point.

---

# 5. DNS Failure

DNS translates names into IP addresses.

Example:

```text
example.com
     ↓
DNS
     ↓
203.0.113.10
```

If DNS fails:

```text
User
 ↓
DNS
 X
Server
```

The server itself may be completely healthy.

## Common DNS problems

* Missing DNS record
* Incorrect DNS record
* Wrong IP address
* DNS server unavailable
* Resolver problem
* DNS propagation/cache issue
* CoreDNS problem in Kubernetes
* Incorrect search domain

## Troubleshooting flow

```text
Domain
 ↓
DNS query
 ↓
DNS response
 ↓
Correct IP?
 ↓
Connect to IP
```

Important principle:

> A healthy server can appear down when DNS is broken.

---

# 6. Connection Refused

Connection refused means the connection attempt reached the destination, but the connection was rejected.

Typical causes:

* Service is stopped
* Nothing is listening on the port
* Wrong port
* Application crashed
* Application bound to another address
* Local firewall rejection

Example:

```text
Client
   |
   | TCP connection
   v
Server
   |
   X
Port 8080
```

## Investigation

Check:

```text
Is the server reachable?
Is the port correct?
Is anything listening?
Is the application running?
Is the application bound to the correct address?
Is a firewall rejecting the connection?
```

---

# 7. Connection Timeout

A timeout means the client did not receive the expected connection response within the timeout period.

Possible causes:

* Firewall
* Security Group
* NACL
* Routing problem
* Incorrect destination
* Server unreachable
* Network failure
* Packet dropping

Example:

```text
Client
  |
  | SYN
  |
  X
  |
Server
```

Traffic may be silently dropped.

---

# 8. Refused vs Timeout

This is an important interview topic.

| Connection Refused                 | Connection Timeout                               |
| ---------------------------------- | ------------------------------------------------ |
| Destination is generally reachable | Destination may not be reachable                 |
| Connection rejected                | Connection attempt receives no expected response |
| Service may not be listening       | Firewall/routing/drop is often suspected         |
| Usually fails quickly              | Often waits until timeout                        |
| Check service/port first           | Check network path/firewall first                |

Do not treat both symptoms as identical.

---

# 9. HTTP 502 Bad Gateway

A 502 commonly occurs when a gateway or reverse proxy cannot obtain a valid response from its upstream server.

Architecture:

```text
Client
  ↓
Reverse Proxy
  ↓
Backend
```

Possible causes:

* Backend is down
* Wrong backend port
* Backend connection refused
* Invalid upstream response
* Reverse proxy configuration problem
* Backend crash

Troubleshooting:

```text
Client
 ↓
Proxy
 ↓
Backend IP
 ↓
Backend Port
 ↓
Application
```

Check each layer.

---

# 10. HTTP 503 Service Unavailable

503 means the service is unavailable.

Possible causes:

* No healthy backend
* Application unavailable
* Server overloaded
* Kubernetes Pods unavailable
* Load balancer has no healthy targets
