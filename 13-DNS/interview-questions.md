# 💼 Chapter 13 – DNS Interview Questions

## 📑 Table of Contents

1. Basic DNS Questions
2. DNS Resolution Questions
3. DNS Records
4. DNS Troubleshooting
5. DevOps DNS Questions
6. AWS DNS Questions
7. Kubernetes DNS Questions
8. Scenario-Based Questions
9. Quick Interview Revision

---

# 🟢 1. Basic DNS Questions

## 1. What is DNS?

**DNS (Domain Name System)** is a distributed naming system that translates domain names into IP addresses and provides other information about domains.

Example:

```text
google.com
     ↓
IP Address
```

---

## 2. Why do we need DNS?

Humans prefer names such as:

```text
google.com
github.com
```

while computers communicate using IP addresses.

DNS provides the mapping between names and network addresses.

---

## 3. What happens when you type google.com in a browser?

A simplified flow is:

```text
Browser Cache
     ↓
OS Resolver/Cache
     ↓
Recursive DNS Resolver
     ↓
Root DNS
     ↓
TLD DNS
     ↓
Authoritative DNS
     ↓
IP Address
     ↓
Web Server
```

If the answer is already cached, the lookup can finish much earlier.

---

## 4. What is a DNS resolver?

A DNS resolver receives DNS queries from clients and obtains answers on their behalf.

It may query:

```text
Root
 ↓
TLD
 ↓
Authoritative DNS
```

and return the result to the client.

---

## 5. What is a recursive DNS resolver?

A recursive resolver performs the DNS lookup process for the client and returns the final answer.

Example:

```text
Laptop
  ↓
Recursive Resolver
  ↓
DNS hierarchy
  ↓
IP address
```

---

## 6. What is an authoritative DNS server?

An authoritative DNS server contains the authoritative DNS records for a domain or DNS zone.

It provides the final authoritative answer for records in that zone.

---

## 7. What is the DNS hierarchy?

DNS is organized hierarchically:

```text
Root
 ↓
TLD
 ↓
Domain
 ↓
Subdomain/Host
```

Example:

```text
.
└── com
    └── example
        └── www
```

---

## 8. What is a TLD?

TLD means **Top-Level Domain**.

Examples:

```text
.com
.org
.net
.in
.edu
```

---

## 9. What are root DNS servers?

Root DNS infrastructure is at the top of the DNS hierarchy.

Root servers help resolvers find the appropriate TLD name servers.

They do not normally provide the final IP address for a website.

---

# 🟡 2. DNS Resolution Questions

## 10. What is DNS resolution?

DNS resolution is the process of finding DNS information for a domain name.

For an A record:

```text
Domain Name
     ↓
IPv4 Address
```

---

## 11. What is a recursive query?

A recursive query asks the DNS resolver to find the final answer on behalf of the client.

Conceptually:

```text
Client
  ↓
Resolver
  ↓
Final Answer
```

---

## 12. What is an iterative query?

In an iterative query, the DNS server responds with the best information it has, such as a referral to another DNS server.

Example:

```text
Resolver → Root
Root → TLD servers

Resolver → TLD
TLD → Authoritative server

Resolver → Authoritative
Authoritative → Answer
```

---

## 13. What is DNS caching?

DNS caching stores DNS answers temporarily.

Benefits:

- Faster lookups
- Lower DNS traffic
- Reduced load on DNS infrastructure

---

## 14. What is DNS TTL?

TTL means **Time To Live**.

It controls how long a DNS answer may remain cached.

Example:

```text
TTL = 300 seconds
```

means the cached answer can generally be reused for about five minutes.

---

## 15. Where can DNS information be cached?

DNS information may be cached in several places, including:

- Browser
- Operating system
- Local DNS resolver
- Intermediate DNS infrastructure

---

# 🟠 3. DNS Records

## 16. What is an A record?

An A record maps a hostname to an IPv4 address.

Example:

```text
example.com → 192.0.2.10
```

---

## 17. What is an AAAA record?

An AAAA record maps a hostname to an IPv6 address.

Example:

```text
example.com → 2001:db8::10
```

---

## 18. What is a CNAME record?

CNAME means **Canonical Name**.

It creates an alias from one hostname to another hostname.

Example:

```text
www.example.com
       ↓
example.com
```

---

## 19. What is an MX record?

MX means **Mail Exchange**.

It identifies mail servers responsible for receiving email for a domain.

Example:

```text
example.com
     ↓
mail.example.com
```

MX records contain preference values.

---

## 20. What is an NS record?

NS means **Name Server**.

It identifies the authoritative name servers for a DNS zone.

Example:

```text
example.com
     ↓
ns1.example.com
ns2.example.com
```

---

## 21. What is a TXT record?

TXT records store text associated with a domain.

Common uses include:

- Domain verification
- SPF
- Email security
- Service configuration

---

## 22. What is a PTR record?

PTR records are used for reverse DNS.

They map:

```text
IP Address
     ↓
Hostname
```

Example:

```text
192.0.2.10
     ↓
server.example.com
```

---

## 23. What is the difference between A and AAAA?

| A | AAAA |
|---|---|
| IPv4 | IPv6 |
| 32-bit address | 128-bit address |

Example:

```text
A     → 192.0.2.10
AAAA  → 2001:db8::10
```

---

# 🔴 4. DNS Troubleshooting Questions

## 24. How do you troubleshoot a DNS problem in Linux?

Start with:

```bash
cat /etc/resolv.conf
```

Then:

```bash
nslookup google.com
```

Then:

```bash
dig google.com
```

Then test another resolver:

```bash
dig @8.8.8.8 google.com
```

Also check:

```bash
ip addr
ip route
```

---

## 25. `ping 8.8.8.8` works but `ping google.com` fails. What could be wrong?

This strongly suggests a DNS resolution problem.

Because:

```text
IP connectivity → Working
DNS resolution  → Possibly failing
```

Check:

```bash
cat /etc/resolv.conf
dig google.com
```

---

## 26. `dig` works but `ping` fails. Is DNS broken?

Not necessarily.

DNS may be working perfectly.

Possible reason:

```text
ICMP blocked
```

Test the application instead:

```bash
curl -I https://example.com
```

---

## 27. How do you query a specific DNS server?

Use:

```bash
dig @8.8.8.8 google.com
```

The `@8.8.8.8` specifies the DNS server.

---

## 28. How do you perform reverse DNS lookup?

Use:

```bash
dig -x 8.8.8.8
```

or:

```bash
host 8.8.8.8
```

---

## 29. How do you see only the resolved IP address?

Use:

```bash
dig +short google.com
```

---

## 30. How do you trace DNS delegation?

Use:

```bash
dig +trace example.com
```

This can show the delegation path from:

```text
Root
 ↓
TLD
 ↓
Authoritative DNS
```

---

## 31. Which Linux commands are useful for DNS troubleshooting?

Important commands:

```bash
dig
nslookup
host
resolvectl
ping
curl
```

Configuration:

```bash
cat /etc/resolv.conf
```

Network checks:

```bash
ip addr
ip route
```

---

# 🔵 5. DevOps DNS Questions

## 32. Why is DNS important in DevOps?

DNS is used for:

- Applications
- APIs
- Load balancers
- Microservices
- Databases
- Cloud services
- Kubernetes service discovery
- CI/CD systems

---

## 33. Why should applications use DNS names instead of hard-coded IP addresses?

IP addresses can change.

DNS provides an abstraction:

```text
Application
     ↓
api.example.com
     ↓
Current IP / Load Balancer
```

Infrastructure can change without requiring applications to hard-code new IP addresses.

---

## 34. What happens if DNS is unavailable?

Applications may be unable to resolve service names.

For example:

```text
api.example.com
      ↓
DNS unavailable
      ↓
IP address cannot be resolved
      ↓
Connection fails
```

Existing connections may continue working, depending on the application and caching, but new lookups can fail.

---

## 35. How does DNS affect application availability?

Incorrect DNS configuration can cause:

- Application unreachable
- API failures
- Email delivery problems
- Service discovery failures
- Traffic sent to the wrong destination

Therefore DNS is part of the application's availability chain.

---

# ☁️ 6. AWS DNS Questions

## 36. What is Amazon Route 53?

Amazon Route 53 is AWS's managed DNS service.

It provides DNS hosting and can also provide traffic-routing and health-check capabilities.

---

## 37. How can DNS be used with an AWS Load Balancer?

Example:

```text
api.example.com
       ↓
DNS
       ↓
AWS Load Balancer
       ↓
Application Servers
```

This lets users access the application using a stable hostname.

---

## 38. What is a hosted zone?

A hosted zone is a container for DNS records for a domain within Route 53.

Example:

```text
example.com
```

can have records such as:

```text
www
api
mail
```

---

## 39. What is the difference between public and private DNS?

### Public DNS

Used for names resolvable on the public Internet.

Example:

```text
www.example.com
```

### Private DNS

Used within private networks such as a VPC.

Example:

```text
database.internal
```

---

# ☸️ 7. Kubernetes DNS Questions

## 40. Why does Kubernetes need DNS?

Kubernetes DNS provides service discovery.

Instead of applications using changing Pod IP addresses, they can communicate using Service names.

Example:

```text
backend
```

or a fully qualified name such as:

```text
backend.default.svc.cluster.local
```

---

## 41. What is `cluster.local`?

`cluster.local` is commonly used as the default Kubernetes cluster DNS domain.

Example:

```text
service.namespace.svc.cluster.local
```

---

## 42. What is CoreDNS?

CoreDNS is commonly used as the DNS server within Kubernetes clusters.

It resolves internal service names and can also forward external DNS queries.

---

## 43. What happens if Kubernetes DNS fails?

Applications may fail to communicate using service names.

For example:

```text
frontend
   ↓
backend.default.svc.cluster.local
   ↓
DNS failure
   ↓
Service cannot be resolved
```

Troubleshooting may include:

```bash
kubectl get pods -n kube-system
```

and checking CoreDNS logs.

---

# 🟣 8. Scenario-Based Questions

## 44. Scenario: Website doesn't open by domain, but opens by IP. What is likely wrong?

Example:

```text
https://192.0.2.10
       ↓
Works

https://example.com
       ↓
Fails
```

Possible DNS problem.

Check:

```bash
dig example.com
```

and:

```bash
cat /etc/resolv.conf
```

---

## 45. Scenario: DNS works from your laptop but not from a server.

What would you check?

### Check server DNS configuration

```bash
cat /etc/resolv.conf
```

### Test DNS

```bash
dig example.com
```

### Test external resolver

```bash
dig @8.8.8.8 example.com
```

### Check network connectivity

```bash
ip route
ping -c 4 8.8.8.8
```

---

## 46. Scenario: DNS record was changed but users still receive the old IP.

What could cause this?

Most likely:

```text
DNS caching
```

Check the record's:

```text
TTL
```

Resolvers may continue returning the cached value until its TTL expires.

---

## 47. Scenario: Application works using IP but not hostname.

What would you investigate?

```bash
dig hostname
```

Then:

```bash
cat /etc/resolv.conf
```

Then:

```bash
dig @8.8.8.8 hostname
```

Possible causes:

- DNS failure
- Wrong DNS record
- DNS server problem
- Search-domain issue

---

## 48. Scenario: Kubernetes Pods cannot connect using service names.

What would you check?

First:

```bash
kubectl get pods -n kube-system
```

Then investigate CoreDNS.

Check:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

Also test DNS from a Pod.

---

## 49. Scenario: DNS resolution is very slow.

What would you investigate?

Check:

```bash
dig example.com
```

Look for:

```text
Query time:
```

Then compare resolvers:

```bash
dig @8.8.8.8 example.com
```

and:

```bash
dig @1.1.1.1 example.com
```

Also investigate:

- Network latency
- Resolver availability
- DNS server load
- Routing

---

# ⚡ 9. Quick Interview Revision

### DNS

```text
Domain Name → IP Address
```

### A

```text
Hostname → IPv4
```

### AAAA

```text
Hostname → IPv6
```

### CNAME

```text
Alias → Hostname
```

### MX

```text
Domain → Mail Server
```

### NS

```text
Domain → Name Server
```

### TXT

```text
Domain → Text Information
```

### PTR

```text
IP → Hostname
```

### DNS Port

```text
UDP 53
TCP 53
```

### Important Commands

```bash
dig
nslookup
host
resolvectl
```

### DNS Hierarchy

```text
Root
 ↓
TLD
 ↓
Authoritative DNS
 ↓
DNS Record
```

---

# 🎯 Interview Golden Answer

If the interviewer asks:

> **"Explain DNS in simple terms."**

Answer:

> DNS is the Internet's naming system. Humans use domain names such as `google.com`, while network communication uses IP addresses. When a client needs to access a domain, it queries a DNS resolver. If the answer isn't cached, the resolver can follow the DNS hierarchy from the root to the appropriate TLD and then to the authoritative DNS server. The authoritative server returns the required record, such as an A or AAAA record. The resolver returns the answer to the client, which can then connect to the destination.

---

# 📌 Final Takeaways

Remember these five things:

```text
1. DNS translates names into network addresses.
2. DNS is hierarchical and distributed.
3. DNS uses different record types.
4. DNS caching and TTL affect resolution.
5. DNS troubleshooting is essential for DevOps.
```
