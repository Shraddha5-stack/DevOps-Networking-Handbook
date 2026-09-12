# Chapter 37 — Real-World Case Studies — Practical Lab

This practical lab simulates real-world DevOps and networking incidents.

The goal is not simply to run commands.

The goal is to practice:

```text
Problem
  ↓
Scope
  ↓
Evidence
  ↓
Investigation
  ↓
Root Cause
  ↓
Fix
  ↓
Verification
  ↓
Prevention
```

> **Safety:** Perform destructive or configuration-changing exercises only in your local lab, disposable containers, test Kubernetes namespaces, or explicitly authorized environments.

---

# Lab 1 — Build Your Troubleshooting Baseline

## Objective

Before investigating an incident, collect a baseline.

Run:

```bash
hostname
```

```bash
uptime
```

```bash
ip addr
```

```bash
ip route
```

```bash
ss -lntup
```

```bash
free -h
```

```bash
df -h
```

## Record

Create a file:

```bash
mkdir -p ~/chapter37-lab
cd ~/chapter37-lab
touch baseline.txt
```

Record:

* Hostname
* IP address
* Default route
* Listening ports
* Memory
* Disk usage

## Interview Question

Why should we collect a baseline before troubleshooting?

---

# Lab 2 — DNS Investigation

## Objective

Understand how to determine whether a website problem is actually DNS-related.

Run:

```bash
dig example.com
```

Then:

```bash
dig +short example.com
```

Check the resolver:

```bash
cat /etc/resolv.conf
```

If available:

```bash
resolvectl status
```

## Investigation

Answer:

1. Did DNS return an IP?
2. Which DNS server was used?
3. Is the response successful?
4. What would you check if DNS returned `NXDOMAIN`?

## Mental Model

```text
Domain
  ↓
Resolver
  ↓
DNS Server
  ↓
DNS Record
  ↓
IP Address
```

---

# Lab 3 — DNS Failure Simulation

## Objective

Understand the difference between DNS failure and server failure.

Test:

```bash
dig example.com
```

Now intentionally query a domain that should not exist:

```bash
dig this-domain-should-not-exist-123456.example
```

Observe the response.

## Questions

* Is the Internet broken?
* Is the server necessarily down?
* What does `NXDOMAIN` indicate?

## Lesson

A DNS failure can make a healthy server appear unavailable.

---

# Lab 4 — Connection Refused

## Objective

Create a controlled connection-refused scenario.

Check a port that is unlikely to have a listener:

```bash
nc -vz 127.0.0.1 65000
```

You may see something similar to:

```text
Connection refused
```

Now check listening ports:

```bash
ss -lnt
```

## Investigation

Answer:

1. Is localhost reachable?
2. Is port `65000` listening?
3. Why was the connection refused?

## Root Cause

Usually:

```text
Nothing is listening on that port.
```

---

# Lab 5 — Create a TCP Listener

## Objective

Understand what changes when a service begins listening.

Terminal 1:

```bash
nc -lv 127.0.0.1 9090
```

Terminal 2:

```bash
nc -vz 127.0.0.1 9090
```

Then:

```bash
ss -lnt | grep :9090
```

## Observe

Before the listener:

```text
Connection refused
```

After the listener:

```text
TCP connection succeeds
```

## Lesson

The listening service is one of the first things to check when you receive `connection refused`.

---

# Lab 6 — Connection Timeout Concept

## Objective

Understand timeout behavior without changing your firewall.

Try a deliberately unroutable/private test destination appropriate for your lab:

```bash
nc -vz -w 3 192.0.2.1 8080
```

`192.0.2.0/24` is reserved for documentation/examples.

Observe the result.

## Important

Do not conclude that every timeout means a firewall.

A timeout can result from:

* Routing
* Packet dropping
* Firewall
* Security Group
* NACL
* Unreachable destination

---

# Lab 7 — Local HTTP Server

## Objective

Create a simple application.

```bash
mkdir -p ~/chapter37-lab/http-test
cd ~/chapter37-lab/http-test
```

Create content:

```bash
echo "Chapter 37 HTTP Troubleshooting Lab" > index.html
```

Start:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

In another terminal:

```bash
curl http://127.0.0.1:8080
```

Expected:

```text
Chapter 37 HTTP Troubleshooting Lab
```

---

# Lab 8 — Inspect the HTTP Port

Run:

```bash
ss -lnt | grep :8080
```

You should see a listener on:

```text
127.0.0.1:8080
```

Now test:

```bash
curl -I http://127.0.0.1:8080
```

## Questions

* Which address is the server listening on?
* Which port?
* What HTTP status did you receive?

---

# Lab 9 — Bind Address Troubleshooting

Stop the Python server:

```text
Ctrl+C
```

Start it again explicitly on loopback:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

Check:

```bash
ss -lnt | grep :8080
```

The service is available through loopback.

## Lesson

An application listening only on `127.0.0.1` is not equivalent to an application listening on all required interfaces.

This is a common source of:

```text
Application works locally
BUT
Remote client cannot connect
```

---

# Lab 10 — HTTP Status Investigation

Run:

```bash
curl -I http://127.0.0.1:8080
```

Then:

```bash
curl -v http://127.0.0.1:8080
```

Record:

* HTTP version
* Status code
* Server
* Content type
* Connection details

## Mental Model

```text
TCP works
  ↓
HTTP request sent
  ↓
Application responds
```

---

# Lab 11 — Measure HTTP Latency

Run:

```bash
curl -s -o /dev/null \
-w "DNS: %{time_namelookup}\nConnect: %{time_connect}\nStart Transfer: %{time_starttransfer}\nTotal: %{time_total}\n" \
http://127.0.0.1:8080
```

Record the results.

## Questions

Which measurement represents:

* DNS lookup?
* TCP connection?
* First response byte?
* Complete request?

---

# Lab 12 — Service Logs

Check a service available on your system.

Example:

```bash
systemctl status ssh
```

or:

```bash
systemctl status sshd
```

View logs:

```bash
journalctl -u ssh -n 50
```

If the service is named `sshd`:

```bash
journalctl -u sshd -n 50
```

## Lesson

When a service fails, combine:

```text
Service status
+
Logs
+
Listening port
```

---

# Lab 13 — Process-to-Port Investigation

Run:

```bash
sudo ss -lntup
```

Choose one listening port.

Identify:

```text
Port
 ↓
Process
 ↓
Service
```

If `lsof` is installed:

```bash
sudo lsof -i :22
```

or use another listening port.

---

# Lab 14 — Packet Capture

## Objective

Observe real packets.

Find your interface:

``
