# 🛠️ Chapter 13 – DNS Troubleshooting

## 📑 Table of Contents

1. Introduction
2. DNS Troubleshooting Method
3. Check Network Connectivity
4. Check DNS Configuration
5. Test DNS Resolution
6. Use dig
7. Test a Specific DNS Server
8. Check DNS Records
9. Check Reverse DNS
10. Check DNS Delegation
11. Check DNS Cache
12. DNS vs Network Failure
13. DNS vs Application Failure
14. Common DNS Problems
15. Troubleshooting Scenarios
16. DevOps Troubleshooting Workflow
17. Troubleshooting Checklist
18. Key Takeaways

---

# 📖 1. Introduction

DNS problems are common in networking, cloud, and DevOps environments.

A DNS failure can make an application appear to be completely unavailable even when the server itself is healthy.

For example:

```text
Server → Running
Network → Working
Application → Running
DNS → Broken
```

Users may still see:

```text
Website unavailable
```

Therefore, DNS should be checked separately from network and application connectivity.

---

# 🔍 2. DNS Troubleshooting Method

Use a structured troubleshooting process:

```text
1. Check network
       ↓
2. Check DNS configuration
       ↓
3. Test DNS resolution
       ↓
4. Inspect DNS records
       ↓
5. Test another resolver
       ↓
6. Test the destination IP
       ↓
7. Test the application
```

Do not immediately assume that every connectivity problem is a DNS problem.

---

# 🌐 3. Check Network Connectivity

Before troubleshooting DNS, make sure the machine has network connectivity.

## Check IP Address

```bash
ip addr show
```

Look for an active interface and an assigned IP address.

---

## Check Routing

```bash
ip route
```

Look for a default route such as:

```text
default via 192.168.1.1
```

---

## Test Internet Connectivity by IP

```bash
ping -c 4 8.8.8.8
```

If this works but DNS names fail, DNS becomes a strong suspect.

---

# ⚙️ 4. Check DNS Configuration

Inspect:

```bash
cat /etc/resolv.conf
```

Look for:

```text
nameserver
```

Example:

```text
nameserver 192.168.1.1
```

This tells you which DNS server the system is configured to use.

---

## Check systemd-resolved

On systems using `systemd-resolved`:

```bash
resolvectl status
```

This can show:

- DNS servers
- Network interfaces
- DNS domains
- Resolver configuration

---

# 🔎 5. Test DNS Resolution

Start with:

```bash
nslookup google.com
```

Then:

```bash
dig google.com
```

For a simple answer:

```bash
dig +short google.com
```

You can also use:

```bash
host google.com
```

---

# 🔬 6. Use dig for Detailed Investigation

Run:

```bash
dig google.com
```

Check:

```text
QUESTION SECTION
ANSWER SECTION
AUTHORITY SECTION
ADDITIONAL SECTION
```

Also check:

```text
Query time:
SERVER:
```

These fields provide useful troubleshooting information.

---

# 🎯 7. Test a Specific DNS Server

If your normal resolver is not working, test another resolver directly.

For example:

```bash
dig @8.8.8.8 google.com
```

Or:

```bash
dig @1.1.1.1 google.com
```

Compare the results with:

```bash
dig google.com
```

---

## Interpretation

### Case 1

```text
dig google.com
      ↓
FAIL

dig @8.8.8.8 google.com
      ↓
WORKS
```

Possible problem:

```text
Configured DNS resolver
```

---

### Case 2

```text
dig google.com
      ↓
WORKS

dig @8.8.8.8 google.com
      ↓
WORKS
```

DNS is probably functioning normally.

Investigate the application or network path.

---

# 📋 8. Check DNS Records

Different problems require checking different record types.

## A Record

```bash
dig example.com A
```

Checks IPv4.

---

## AAAA Record

```bash
dig example.com AAAA
```

Checks IPv6.

---

## CNAME

```bash
dig www.example.com CNAME
```

Checks aliases.

---

## MX

```bash
dig example.com MX
```

Checks mail servers.

---

## NS

```bash
dig example.com NS
```

Checks authoritative name servers.

---

## TXT

```bash
dig example.com TXT
```

Checks TXT information.

---

# 🔄 9. Check Reverse DNS

Reverse DNS maps:

```text
IP
 ↓
Hostname
```

Use:

```bash
dig -x 8.8.8.8
```

or:

```bash
host 8.8.8.8
```

Reverse DNS is particularly useful when investigating:

- Servers
- Mail systems
- Logs
- Network infrastructure

---

# 🧭 10. Check DNS Delegation

Use:

```bash
dig +trace example.com
```

This follows the DNS delegation path.

Conceptually:

```text
Root
 ↓
TLD
 ↓
Authoritative DNS
 ↓
Domain
 ↓
Record
```

If delegation is broken, the trace can help identify where the problem occurs.

---

# 💾 11. Check DNS Cache

DNS responses can be cached.

A cached response may cause a user to receive an older record until its TTL expires.

Check the TTL:

```bash
dig example.com
```

Look in the answer section.

Example:

```text
example.com. 300 IN A 192.0.2.10
```

Here:

```text
300
```

is the TTL in seconds.

---

# 🚨 12. DNS vs Network Failure

Consider:

```bash
ping -c 4 8.8.8.8
```

works.

But:

```bash
ping -c 4 google.com
```

fails because the hostname cannot be resolved.

This strongly suggests:

```text
Network connectivity → Working
DNS resolution      → Failing
```

---

## Another Scenario

Suppose:

```bash
ping -c 4 google.com
```

returns an IP but receives no ICMP replies.

DNS may be working.

Possible issue:

```text
ICMP blocked
```

Therefore:

```text
Ping failure ≠ DNS failure
```

---

# 🌐 13. DNS vs Application Failure

Suppose:

```bash
dig example.com
```

works.

And:

```bash
ping example.com
```

works.

But:

```bash
curl https://example.com
```

fails.

DNS is probably not the primary problem.

Investigate:

- TCP connectivity
- Firewall
- TLS
- HTTP
- Application server
- Load balancer

---

# ❌ 14. Common DNS Problems

## Problem 1 – Incorrect DNS Server

Example:

```text
nameserver 192.168.1.100
```

but that resolver is unavailable.

Check:

```bash
cat /etc/resolv.conf
```

---

## Problem 2 – DNS Server Unreachable

The configured DNS server may be unreachable because of:

- Routing problem
- Firewall
- Network failure
- Server outage

---

## Problem 3 – Incorrect DNS Record

Example:

```text
api.example.com
      ↓
Wrong IP
```

Users may be sent to the wrong server.

Check:

```bash
dig api.example.com
```

---

## Problem 4 – Stale DNS Cache

A resolver may still return an older answer.

Check:

```text
TTL
```

---

## Problem 5 – CNAME Misconfiguration

Example:

```text
www.example.com
       ↓
CNAME
       ↓
Incorrect hostname
```

Check:

```bash
dig www.example.com CNAME
```

---

## Problem 6 – DNS Delegation Problem

The parent zone may delegate a domain to incorrect or unavailable name servers.

Use:

```bash
dig +trace example.com
```

---

## Problem 7 – Split-Horizon DNS

An organization may intentionally provide different DNS answers depending on where the query comes from.

Example:

```text
Internal user
     ↓
10.0.0.20

External user
     ↓
203.0.113.20
```

This is commonly used for internal and external services.

---

# 🧪 15. Troubleshooting Scenarios

## Scenario 1 – Domain Does Not Resolve

Command:

```bash
dig example.com
```

If it fails:

### Step 1

Check configuration:

```bash
cat /etc/resolv.conf
```

### Step 2

Check resolver:

```bash
resolvectl status
```

### Step 3

Test public resolver:

```bash
dig @8.8.8.8 example.com
```

### Step 4

Check network:

```bash
ping -c 4 8.8.8.8
```

---

# Scenario 2 – Domain Resolves to Wrong IP

Run:

```bash
dig example.com A
```

Check:

```text
ANSWER SECTION
```

Compare the returned IP with the expected infrastructure.

If incorrect, investigate:

- DNS record
- DNS zone
- CNAME
- Load balancer
- DNS cache

---

# Scenario 3 – DNS Works on Laptop but Not Server

On the server:

```bash
cat /etc/resolv.conf
```

Then:

```bash
dig example.com
```

Compare with:

```bash
dig @8.8.8.8 example.com
```

If the public resolver works but the default resolver fails, investigate the server's DNS configuration or network policy.

---

# Scenario 4 – DNS Change Not Visible

Suppose you changed:

```text
example.com → new IP
```

but users still receive the old IP.

Check:

```bash
dig example.com
```

Check the TTL.

Possible reason:

```text
DNS caching
```

Different recursive resolvers may update at different times depending on cache state and TTL.

---

# Scenario 5 – Kubernetes DNS Failure

Application:

```text
frontend
   ↓
backend.default.svc.cluster.local
```

fails to resolve.

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Then inspect logs:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

Test DNS from inside a Pod if necessary.

---

# 🚀 16. DevOps Troubleshooting Workflow

When an application reports:

```text
Unable to resolve api.example.com
```

follow this workflow.

### Step 1 – Check IP

```bash
ip addr
```

### Step 2 – Check route

```bash
ip route
```

### Step 3 – Check DNS configuration

```bash
cat /etc/resolv.conf
```

### Step 4 – Test DNS

```bash
dig api.example.com
```

### Step 5 – Test a different resolver

```bash
dig @8.8.8.8 api.example.com
```

### Step 6 – Inspect records

```bash
dig api.example.com A
dig api.example.com AAAA
dig api.example.com CNAME
```

### Step 7 – Test returned IP

```bash
ping -c 4 <IP>
```

### Step 8 – Test application

```bash
curl -I https://api.example.com
```

### Step 9 – Trace DNS if necessary

```bash
dig +trace api.example.com
```

---

# 📋 17. Troubleshooting Checklist

## Network

```bash
ip addr
ip route
ping -c 4 8.8.8.8
```

## DNS Configuration

```bash
cat /etc/resolv.conf
resolvectl status
```

## DNS Resolution

```bash
nslookup example.com
dig example.com
host example.com
```

## Specific Resolver

```bash
dig @8.8.8.8 example.com
```

## Records

```bash
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
```

## Reverse DNS

```bash
dig -x 8.8.8.8
```

## Delegation

```bash
dig +trace example.com
```

## Application

```bash
curl -I https://example.com
```

---

# 🧠 18. Key Takeaways

Remember:

```text
DNS problem
    ↓
Check resolver
    ↓
Check records
    ↓
Check network
    ↓
Check application
```

Important commands:

```bash
dig
nslookup
host
resolvectl
```

Network commands:

```bash
ip addr
ip route
ping
```

Application test:

```bash
curl
```

---

# 🎯 Final Troubleshooting Principle

Never troubleshoot DNS in isolation.

Think in layers:

```text
┌──────────────────────────┐
│ Application              │
├──────────────────────────┤
│ HTTP / HTTPS             │
├──────────────────────────┤
│ TCP / UDP                │
├──────────────────────────┤
│ IP Routing               │
├──────────────────────────┤
│ DNS Resolution           │
├──────────────────────────┤
│ Network Interface        │
└──────────────────────────┘
```

A good DevOps engineer determines **which layer is actually failing** before changing configuration.

DNS is only one part of the complete connectivity path.
