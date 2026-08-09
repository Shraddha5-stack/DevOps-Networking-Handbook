# 🧪 Chapter 13 – DNS Practical Lab

## 📑 Table of Contents

1. Lab Objectives
2. Check DNS Configuration
3. Basic DNS Lookup
4. Use dig
5. Query A Record
6. Query AAAA Record
7. Query MX Record
8. Query NS Record
9. Query TXT Record
10. Reverse DNS Lookup
11. Query a Specific DNS Server
12. Trace DNS Delegation
13. Check DNS with ping
14. Check DNS with curl
15. Compare DNS Resolvers
16. DNS Troubleshooting Scenario
17. DevOps DNS Investigation
18. Lab Summary

---

# 🎯 1. Lab Objectives

In this practical lab, we will learn how to:

- Inspect DNS configuration
- Resolve domain names
- Query DNS records
- Perform reverse DNS lookups
- Query specific DNS servers
- Trace DNS delegation
- Troubleshoot DNS failures
- Verify DNS before testing applications

---

# ⚙️ 2. Check DNS Configuration

First, inspect the system DNS configuration.

```bash
cat /etc/resolv.conf
```

Look for:

```text
nameserver <DNS-SERVER>
```

Example:

```text
nameserver 192.168.1.1
```

This tells us which DNS resolver the system is configured to use.

### What We Learn

We identify:

- Configured DNS server
- DNS search configuration
- Resolver settings

---

# 🔍 3. Basic DNS Lookup with nslookup

Run:

```bash
nslookup google.com
```

Example:

```text
Server:     192.168.1.1
Address:    192.168.1.1#53

Non-authoritative answer:
Name:       google.com
Address:    142.x.x.x
```

### What We Learn

The command shows:

```text
DNS Server
     ↓
DNS Query
     ↓
Resolved IP
```

---

# 🔬 4. DNS Lookup with dig

Run:

```bash
dig google.com
```

Look at:

```text
QUESTION SECTION
ANSWER SECTION
```

The answer section contains the returned DNS record.

---

## Short Output

For a simpler result:

```bash
dig +short google.com
```

Example:

```text
142.x.x.x
```

This is useful in scripts and quick troubleshooting.

---

# 🔢 5. Query an A Record

An A record maps a hostname to an IPv4 address.

Run:

```bash
dig google.com A
```

Or:

```bash
dig +short google.com A
```

Expected result:

```text
IPv4 address
```

### Concept

```text
google.com
     ↓
A Record
     ↓
IPv4 Address
```

---

# 🌐 6. Query an AAAA Record

AAAA records contain IPv6 addresses.

Run:

```bash
dig google.com AAAA
```

Or:

```bash
dig +short google.com AAAA
```

Concept:

```text
google.com
     ↓
AAAA Record
     ↓
IPv6 Address
```

---

# 📧 7. Query MX Records

MX records identify mail servers.

Run:

```bash
dig google.com MX
```

Short version:

```bash
dig +short google.com MX
```

Example:

```text
10 mail.example.com.
```

The preference number determines mail-server priority.

---

# 🏷️ 8. Query NS Records

NS records identify authoritative name servers.

Run:

```bash
dig google.com NS
```

Short version:

```bash
dig +short google.com NS
```

Concept:

```text
Domain
  ↓
NS Records
  ↓
Authoritative Name Servers
```

---

# 📝 9. Query TXT Records

TXT records can contain verification and email-security information.

Run:

```bash
dig google.com TXT
```

Short version:

```bash
dig +short google.com TXT
```

Common uses:

- Domain verification
- SPF
- Service configuration

---

# 🔄 10. Reverse DNS Lookup

Reverse DNS maps:

```text
IP Address
     ↓
Hostname
```

Run:

```bash
dig -x 8.8.8.8
```

Short version:

```bash
dig +short -x 8.8.8.8
```

Alternative:

```bash
host 8.8.8.8
```

### Concept

Forward DNS:

```text
google.com → IP
```

Reverse DNS:

```text
IP → hostname
```

---

# 🎯 11. Query a Specific DNS Server

Instead of using the system's default resolver, query a specific DNS server.

Example:

```bash
dig @8.8.8.8 google.com
```

Here:

```text
@8.8.8.8
```

means:

> Send the DNS query directly to 8.8.8.8.

Try another resolver:

```bash
dig @1.1.1.1 google.com
```

This is useful when comparing DNS resolvers.

---

# 🧭 12. Trace DNS Delegation

Run:

```bash
dig +trace example.com
```

This shows the DNS delegation process.

Conceptually:

```text
Root
  ↓
.com TLD
  ↓
Authoritative DNS
  ↓
example.com
  ↓
Final Answer
```

This is one of the best commands for understanding how DNS resolution works.

---

# 📡 13. Check DNS with ping

Run:

```bash
ping -c 4 google.com
```

Before sending the ICMP request, your system generally needs to resolve:

```text
google.com
     ↓
IP Address
```

If you receive:

```text
Name or service not known
```

investigate DNS.

However:

```text
ping failure ≠ DNS failure
```

ICMP may simply be blocked.

---

# 🌐 14. Check DNS with curl

Test a website:

```bash
curl -I https://google.com
```

This checks whether:

1. The hostname can be resolved
2. A connection can be established
3. The web server responds

For DNS-specific investigation, prefer:

```bash
dig google.com
```

---

# ⚖️ 15. Compare DNS Resolvers

First test the default resolver:

```bash
dig google.com
```

Then test:

```bash
dig @8.8.8.8 google.com
```

And:

```bash
dig @1.1.1.1 google.com
```

Compare:

- Response
- Query time
- Returned records

Look for:

```text
Query time:
```

in the `dig` output.

---

# 🚨 16. DNS Troubleshooting Scenario

## Problem

You can access:

```bash
ping -c 4 8.8.8.8
```

but:

```bash
ping -c 4 google.com
```

fails with a DNS error.

---

## Step 1 – Check DNS Configuration

```bash
cat /etc/resolv.conf
```

---

## Step 2 – Test DNS Directly

```bash
nslookup google.com
```

---

## Step 3 – Use dig

```bash
dig google.com
```

---

## Step 4 – Query Public Resolver

```bash
dig @8.8.8.8 google.com
```

---

## Step 5 – Compare

If:

```bash
dig @8.8.8.8 google.com
```

works but:

```bash
dig google.com
```

fails, investigate the configured DNS resolver.

---

# 🚀 17. DevOps DNS Investigation

## Scenario

An application cannot reach:

```text
api.example.com
```

Perform the following steps.

### Step 1 – Resolve the hostname

```bash
dig +short api.example.com
```

### Step 2 – Inspect DNS records

```bash
dig api.example.com
```

### Step 3 – Check configured DNS

```bash
cat /etc/resolv.conf
```

### Step 4 – Test another resolver

```bash
dig @8.8.8.8 api.example.com
```

### Step 5 – Test the resolved IP

```bash
ping -c 4 <IP>
```

### Step 6 – Test the application

```bash
curl -I https://api.example.com
```

### Step 7 – Check routing

```bash
ip route
```

---

# 🧠 Important Observation

Suppose:

```text
dig api.example.com
        ↓
      WORKS

ping api.example.com
        ↓
      FAILS

curl https://api.example.com
        ↓
      WORKS
```

This tells us:

```text
DNS       → Working
ICMP      → Blocked/Unavailable
HTTPS     → Working
```

Therefore, do not automatically conclude that the server is down.

---

# 📸 18. Practical Screenshots

Store your DNS command screenshots inside:

```text
screenshots/
```

Recommended names:

```text
01-resolv-conf.png
02-nslookup.png
03-dig-basic.png
04-dig-a-record.png
05-dig-aaaa-record.png
06-dig-mx-record.png
07-dig-ns-record.png
08-dig-txt-record.png
09-reverse-dns.png
10-specific-dns-server.png
11-dig-trace.png
12-dns-troubleshooting.png
```

---

# 📊 Lab Command Summary

| Task | Command |
|---|---|
| Check DNS configuration | `cat /etc/resolv.conf` |
| Basic lookup | `nslookup google.com` |
| Detailed lookup | `dig google.com` |
| Short answer | `dig +short google.com` |
| A record | `dig google.com A` |
| AAAA record | `dig google.com AAAA` |
| MX record | `dig google.com MX` |
| NS record | `dig google.com NS` |
| TXT record | `dig google.com TXT` |
| Reverse DNS | `dig -x 8.8.8.8` |
| Specific resolver | `dig @8.8.8.8 google.com` |
| Trace DNS | `dig +trace example.com` |
| Simple DNS lookup | `host google.com` |
| Resolver status | `resolvectl status` |

---

# 📌 19. Lab Summary

In this practical lab we learned how to:

- Inspect DNS configuration
- Resolve domain names
- Query different DNS record types
- Perform reverse DNS
- Query specific resolvers
- Trace DNS delegation
- Troubleshoot DNS failures
- Separate DNS problems from network and application problems

The most important commands to remember are:

```bash
dig
nslookup
host
resolvectl
```

Combined with:

```bash
ping
curl
ip route
ip addr
```

they form a powerful DNS and network troubleshooting toolkit for DevOps engineers.
