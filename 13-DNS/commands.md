# 💻 DNS Commands

## 📑 Table of Contents

1. Introduction
2. Check DNS Configuration
3. nslookup
4. dig
5. host
6. resolvectl
7. DNS Lookup for A Record
8. DNS Lookup for AAAA Record
9. DNS Lookup for MX Record
10. DNS Lookup for NS Record
11. DNS Lookup for TXT Record
12. Reverse DNS Lookup
13. Check DNS Server
14. Query a Specific DNS Server
15. Check DNS Resolution with ping
16. Check DNS Resolution with curl
17. DNS Troubleshooting Commands
18. Command Comparison
19. DevOps DNS Workflow
20. Key Takeaways

---

# 📖 1. Introduction

Linux provides several commands for investigating DNS.

The most useful commands are:

```text
nslookup
dig
host
resolvectl
ping
curl
```

These commands help us investigate:

- Domain resolution
- DNS records
- DNS servers
- DNS configuration
- Reverse DNS
- DNS failures
- DNS response time

---

# ⚙️ 2. Check DNS Configuration

## Check `/etc/resolv.conf`

```bash
cat /etc/resolv.conf
```

This file contains DNS resolver configuration used by the system.

Example:

```text
nameserver 192.168.1.1
```

The `nameserver` entry identifies a DNS server that can be queried.

---

# 🔍 3. nslookup

`nslookup` is a simple DNS query tool.

## Basic Lookup

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

This tells us:

- Which DNS server answered
- The resolved IP address

---

## Query a Specific Record

### A Record

```bash
nslookup -type=A google.com
```

### AAAA Record

```bash
nslookup -type=AAAA google.com
```

### MX Record

```bash
nslookup -type=MX google.com
```

### NS Record

```bash
nslookup -type=NS google.com
```

### TXT Record

```bash
nslookup -type=TXT google.com
```

---

# 🧪 4. dig

`dig` stands for **Domain Information Groper**.

It is one of the most useful DNS troubleshooting tools for engineers.

## Basic Query

```bash
dig google.com
```

---

## Short Answer

```bash
dig +short google.com
```

This displays a concise answer.

Example:

```text
142.x.x.x
```

---

# 🔢 5. Query Specific DNS Records with dig

## A Record

```bash
dig google.com A
```

## AAAA Record

```bash
dig google.com AAAA
```

## MX Record

```bash
dig google.com MX
```

## NS Record

```bash
dig google.com NS
```

## TXT Record

```bash
dig google.com TXT
```

## CNAME Record

```bash
dig www.example.com CNAME
```

---

# 🔄 6. host

`host` is a simple DNS lookup utility.

Basic lookup:

```bash
host google.com
```

Example:

```text
google.com has address 142.x.x.x
```

---

## MX Lookup

```bash
host -t MX google.com
```

## NS Lookup

```bash
host -t NS google.com
```

## TXT Lookup

```bash
host -t TXT google.com
```

---

# 🖥️ 7. resolvectl

`resolvectl` can inspect the DNS configuration and resolver state on systems using `systemd-resolved`.

Check status:

```bash
resolvectl status
```

This can show:

- DNS servers
- DNS domains
- Network interfaces
- Resolver configuration

---

## Query a Domain

```bash
resolvectl query google.com
```

Example:

```text
google.com
    -- link: wlo1
    -- 142.x.x.x
```

---

# 🔢 8. DNS Lookup for A Record

An A record maps:

```text
Hostname → IPv4 address
```

Command:

```bash
dig +short google.com A
```

Example:

```text
142.x.x.x
```

---

# 🌐 9. DNS Lookup for AAAA Record

AAAA records provide IPv6 addresses.

Command:

```bash
dig +short google.com AAAA
```

Example:

```text
2607:f8b0::...
```

---

# 📧 10. DNS Lookup for MX Record

MX records identify mail servers.

Command:

```bash
dig google.com MX
```

Short form:

```bash
dig +short google.com MX
```

Example:

```text
10 mail.example.com.
```

The number represents the mail server preference.

Lower preference values are generally preferred.

---

# 🏷️ 11. DNS Lookup for NS Record

NS records identify authoritative name servers.

Command:

```bash
dig +short google.com NS
```

Example:

```text
ns1.example-dns.com.
ns2.example-dns.com.
```

---

# 📝 12. DNS Lookup for TXT Record

TXT records can contain verification and email-security information.

Command:

```bash
dig +short google.com TXT
```

Useful for investigating:

- Domain verification
- SPF
- Other TXT-based configuration

---

# 🔄 13. Reverse DNS Lookup

Reverse DNS converts:

```text
IP Address
     ↓
Hostname
```

Use:

```bash
dig -x 8.8.8.8
```

Short form:

```bash
dig +short -x 8.8.8.8
```

Another option:

```bash
host 8.8.8.8
```

---

# 🌍 14. Check DNS Server

Use:

```bash
nslookup google.com
```

Look for:

```text
Server:
Address:
```

Or:

```bash
cat /etc/resolv.conf
```

Look for:

```text
nameserver
```

---

# 🎯 15. Query a Specific DNS Server

Sometimes we want to compare DNS resolvers.

With `dig`:

```bash
dig @8.8.8.8 google.com
```

Here:

```text
@8.8.8.8
```

means:

> Ask the DNS server at 8.8.8.8.

Another example:

```bash
dig @1.1.1.1 google.com
```

This is useful when troubleshooting resolver problems.

---

# 📡 16. Check DNS Resolution with ping

```bash
ping -c 4 google.com
```

Before pinging the destination, the system generally needs to resolve:

```text
google.com
     ↓
IP address
```

If the hostname cannot be resolved, investigate DNS.

---

# 🌐 17. Check DNS Resolution with curl

`curl` can also help determine whether a hostname resolves and whether the web service is reachable.

```bash
curl -I https://google.com
```

If DNS resolution fails, `curl` will report a name-resolution error.

Important:

```text
DNS working
      ≠
Website application working
```

DNS only gets us to the destination address. The application still needs to be reachable.

---

# 🛠️ 18. DNS Troubleshooting Commands

## Check IP Configuration

```bash
ip addr show
```

## Check Routing

```bash
ip route
```

## Check DNS Configuration

```bash
cat /etc/resolv.conf
```

## Test DNS Resolution

```bash
nslookup google.com
```

## Detailed DNS Query

```bash
dig google.com
```

## Simple DNS Answer

```bash
dig +short google.com
```

## Query Specific Resolver

```bash
dig @8.8.8.8 google.com
```

## Reverse DNS

```bash
dig -x 8.8.8.8
```

## Check Resolver State

```bash
resolvectl status
```

---

# 🔬 19. Useful dig Output

Run:

```bash
dig google.com
```

The output normally contains sections such as:

```text
QUESTION SECTION
ANSWER SECTION
AUTHORITY SECTION
ADDITIONAL SECTION
```

### QUESTION SECTION

Shows what was requested.

### ANSWER SECTION

Contains the DNS answer.

### AUTHORITY SECTION

Can provide authoritative information or delegation-related information.

### ADDITIONAL SECTION

Can provide additional records related to the response.

---

# ⏱️ 20. Check DNS Response Time

`dig` provides query timing information.

Run:

```bash
dig google.com
```

Look near the bottom for:

```text
Query time: ...
```

This can help identify slow DNS responses.

---

# 🔁 21. Compare DNS Resolvers

Test your configured resolver:

```bash
dig google.com
```

Test another resolver:

```bash
dig @8.8.8.8 google.com
```

Test another resolver:

```bash
dig @1.1.1.1 google.com
```

Compare:

- Response
- Query time
- Returned records

This can help isolate resolver-specific problems.

---

# 🧭 22. Trace DNS Delegation

`dig` can trace DNS resolution:

```bash
dig +trace example.com
```

This asks `dig` to follow the DNS delegation chain.

Conceptually:

```text
Root
 ↓
TLD
 ↓
Authoritative DNS
 ↓
Answer
```

This is extremely useful for understanding how DNS resolution works.

---

# 🚀 23. DevOps DNS Workflow

When an application cannot reach:

```text
api.example.com
```

use:

### Step 1

```bash
nslookup api.example.com
```

### Step 2

```bash
dig api.example.com
```

### Step 3

```bash
dig +short api.example.com
```

### Step 4

Check the configured resolver:

```bash
cat /etc/resolv.conf
```

### Step 5

Test another resolver:

```bash
dig @8.8.8.8 api.example.com
```

### Step 6

Test the returned IP:

```bash
ping -c 4 <IP>
```

### Step 7

Test the application:

```bash
curl -I https://api.example.com
```

---

# 📊 24. Command Comparison

| Command | Main Purpose |
|---|---|
| `nslookup` | Basic DNS lookup |
| `dig` | Detailed DNS investigation |
| `dig +short` | Simple DNS answer |
| `dig +trace` | Follow DNS delegation |
| `host` | Simple DNS lookup |
| `resolvectl status` | DNS resolver configuration |
| `resolvectl query` | Query system resolver |
| `cat /etc/resolv.conf` | View resolver configuration |
| `ping hostname` | Test resolution + ICMP reachability |
| `curl URL` | Test DNS + application connectivity |

---

# 🧠 25. Important Difference

Do not confuse:

```bash
ping google.com
```

with:

```bash
dig google.com
```

`dig` specifically investigates DNS.

`ping` performs DNS resolution as part of trying to send ICMP packets.

Therefore:

```text
dig works
ping fails
```

can mean DNS is working while ICMP connectivity is blocked.

---

# 📌 26. Key Takeaways

- `dig` is one of the best DNS troubleshooting tools.
- `nslookup` is useful for simple DNS queries.
- `host` provides quick DNS information.
- `resolvectl` helps inspect the system resolver.
- `/etc/resolv.conf` can show configured nameservers.
- `dig +short` provides concise results.
- `dig +trace` helps understand DNS delegation.
- `dig -x` performs reverse DNS lookup.
- `dig @server` lets you query a specific DNS resolver.
- DNS troubleshooting should be separated from application troubleshooting.

---

# 📝 27. Summary

Linux DNS commands allow engineers to investigate the complete DNS path.

A practical toolkit is:

```bash
nslookup
dig
host
resolvectl
```

combined with:

```bash
ip addr
ip route
ping
curl
```

Together, these commands help DevOps engineers diagnose DNS, networking, and application connectivity problems.
