# 🌐 Chapter 15 – DNS Notes

## 1. What is DNS?

DNS stands for **Domain Name System**.

DNS translates human-readable domain names into IP addresses that computers use to communicate.

For example:

```text
google.com
     ↓
DNS
     ↓
142.250.x.x
```

Instead of remembering an IP address, users can use a domain name such as:

```text
google.com
```

---

# 2. Why Do We Need DNS?

Computers communicate using IP addresses.

For example:

```text
142.250.x.x
```

But remembering IP addresses for every website would be difficult.

DNS provides a name-to-IP mapping:

```text
Domain Name
     ↓
DNS
     ↓
IP Address
```

Example:

```text
google.com
     ↓
142.250.x.x
```

### Simple analogy

Think of DNS like the **contacts application on your phone**.

You remember:

```text
Mom
```

instead of remembering:

```text
+91-XXXXXXXXXX
```

Similarly, DNS allows you to remember:

```text
google.com
```

instead of:

```text
IP address
```

---

# 3. Domain Name

A domain name is a human-readable name used to identify a service or website.

Examples:

```text
google.com
github.com
amazon.com
example.org
```

A domain can have multiple levels.

Example:

```text
www.example.com
```

Breaking it down:

```text
www     → Host / subdomain
example → Domain
com     → Top-Level Domain
```

---

# 4. IP Address

An IP address identifies a network interface or endpoint on an IP network.

Examples:

### IPv4

```text
192.168.1.5
```

### IPv6

```text
2001:db8::1
```

DNS can map domain names to IPv4 and IPv6 addresses.

---

# 5. DNS Name Resolution

Name resolution is the process of finding the IP address associated with a domain name.

Example:

```text
User
 ↓
google.com
 ↓
DNS Resolver
 ↓
IP Address
 ↓
Web Server
```

The application can then connect to the destination IP address.

---

# 6. DNS Hierarchy

DNS uses a hierarchical structure.

A simplified hierarchy is:

```text
                    Root
                     |
          +----------+----------+
          |          |          |
         .com       .org       .net
          |
       example
          |
        www
```

The hierarchy allows DNS to scale globally.

---

# 7. Root DNS Servers

At the top of the DNS hierarchy are the **root DNS servers**.

They do not normally provide the final IP address for every domain.

Instead, they help direct queries toward the appropriate Top-Level Domain (TLD) servers.

Example:

```text
Client
  ↓
Resolver
  ↓
Root
  ↓
.com TLD
```

---

# 8. TLD Servers

TLD means **Top-Level Domain**.

Examples:

```text
.com
.org
.net
.in
.edu
```

A TLD server helps direct the resolver toward the authoritative name servers for a domain.

Example:

```text
example.com
     ↓
.com TLD
     ↓
Authoritative DNS
```

---

# 9. Authoritative DNS Server

An authoritative DNS server stores the authoritative DNS records for a domain.

For example:

```text
example.com
     ↓
Authoritative DNS
     ↓
DNS Records
```

It can provide records such as:

```text
A
AAAA
CNAME
MX
TXT
NS
```

---

# 10. Recursive DNS Resolver

A recursive resolver performs DNS queries on behalf of clients.

For example:

```text
Laptop
   ↓
Recursive Resolver
   ↓
Root
   ↓
TLD
   ↓
Authoritative Server
```

The resolver obtains the answer and returns it to the client.

The resolver may also cache the result.

---

# 11. DNS Resolution Process

Suppose a user enters:

```text
www.example.com
```

A simplified resolution process can be:

```text
1. Client
      ↓
2. Recursive Resolver
      ↓
3. Root Server
      ↓
4. .com TLD Server
      ↓
5. Authoritative DNS Server
      ↓
6. IP Address
      ↓
7. Client
```

The resolver may cache the answer, so future requests can be answered without repeating the entire process.

---

# 12. DNS Caching

DNS responses can be cached.

Example:

```text
First Request
Client
  ↓
Resolver
  ↓
DNS Hierarchy
  ↓
Answer
```

Later:

```text
Second Request
Client
  ↓
Resolver Cache
  ↓
Answer
```

Caching improves:

```text
Performance
Response Time
DNS Efficiency
```

---

# 13. TTL

TTL stands for **Time To Live**.

In DNS, TTL determines how long a DNS record can be cached before it should be queried again.

Example:

```text
TTL = 300 seconds
```

This means the cached record can normally be reused for 300 seconds.

After the TTL expires, the resolver may need to obtain a fresh answer.

---

# 14. DNS Record Types

DNS supports different record types.

Important records include:

```text
A
AAAA
CNAME
MX
NS
TXT
PTR
```

Each record has a different purpose.

---

# 15. A Record

An **A record** maps a domain name to an IPv4 address.

Example:

```text
example.com
     ↓
192.0.2.10
```

Conceptually:

```text
A
↓
IPv4
```

---

# 16. AAAA Record

An **AAAA record** maps a domain name to an IPv6 address.

Example:

```text
example.com
     ↓
2001:db8::10
```

Remember:

```text
A    → IPv4
AAAA → IPv6
```

---

# 17. CNAME Record

CNAME stands for **Canonical Name**.

It creates an alias from one domain name to another domain name.

Example:

```text
www.example.com
        ↓
example.com
```

The target is another DNS name, not an IP address.

---

# 18. MX Record

MX stands for **Mail Exchange**.

It identifies mail servers responsible for receiving email for a domain.

Example:

```text
example.com
     ↓
MX
     ↓
mail.example.com
```

MX records also have a priority value.

---

# 19. NS Record

NS stands for **Name Server**.

It identifies the authoritative name servers for a DNS zone or domain.

Example:

```text
example.com
     ↓
NS
     ↓
ns1.example-dns.com
```

---

# 20. TXT Record

TXT records store text information associated with a domain.

They are commonly used for:

```text
Domain Verification
Email Security
SPF
DKIM-related information
DMARC-related information
```

The exact use depends on the service and DNS configuration.

---

# 21. PTR Record

PTR records are commonly used for **reverse DNS**.

Forward DNS:

```text
Domain
  ↓
IP
```

Reverse DNS:

```text
IP
 ↓
Domain
```

PTR records are commonly used in reverse DNS zones.

---

# 22. Forward DNS

Forward DNS resolves a name to an address.

Example:

```text
google.com
     ↓
IP Address
```

Tools:

```bash
dig google.com
```

or:

```bash
nslookup google.com
```

---

# 23. Reverse DNS

Reverse DNS resolves an IP address to a name.

Example:

```text
192.0.2.10
     ↓
example.com
```

A common command is:

```bash
dig -x 192.0.2.10
```

---

# 24. `/etc/hosts`

Linux can perform local hostname mapping using:

```text
/etc/hosts
```

Example:

```text
192.168.1.10    server1
192.168.1.20    database
```

Then:

```text
server1
   ↓
192.168.1.10
```

This mapping is local to the machine.

---

# 25. `/etc/resolv.conf`

Linux systems use resolver configuration to determine how DNS queries should be handled.

Inspect it with:

```bash
cat /etc/resolv.conf
```

It may contain DNS server information such as:

```text
nameserver 192.168.1.1
```

On systems using NetworkManager or `systemd-resolved`, `/etc/resolv.conf` may be generated or managed dynamically.

---

# 26. `nslookup`

`nslookup` is a command-line tool for querying DNS.

Example:

```bash
nslookup google.com
```

It can be useful for quickly checking:

```text
DNS Resolution
DNS Server
Returned Address
```

---

# 27. `dig`

`dig` stands for **Domain Information Groper**.

It provides detailed DNS query information.

Example:

```bash
dig google.com
```

Specific record:

```bash
dig google.com A
```

IPv6:

```bash
dig google.com AAAA
```

Mail records:

```bash
dig google.com MX
```

Name servers:

```bash
dig google.com NS
```

Reverse DNS:

```bash
dig -x 8.8.8.8
```

---

# 28. `host`

The `host` command provides a simple way to perform DNS lookups.

Example:

```bash
host google.com
```

Reverse lookup:

```bash
host 8.8.8.8
```

---

# 29. `resolvectl`

`resolvectl` can be used to inspect and query DNS resolution when `systemd-resolved` is in use.

Check resolver status:

```bash
resolvectl status
```

Query a domain:

```bash
resolvectl query google.com
```

---

# 30. DNS Troubleshooting

Suppose:

```bash
ping 8.8.8.8
```

works, but:

```bash
ping google.com
```

fails.

A likely area to investigate is DNS resolution.

Check:

```bash
cat /etc/resolv.conf
```

Then:

```bash
resolvectl status
```

Test directly:

```bash
nslookup google.com
```

or:

```bash
dig google.com
```

---

# 31. DNS Troubleshooting Flow

Use this approach:

```text
Can I reach the network?
        ↓
Can I reach the gateway?
        ↓
Can I reach an external IP?
        ↓
Can I resolve a domain?
        ↓
Check DNS configuration
        ↓
Check DNS server
        ↓
Check DNS records
```

Example:

```bash
ping -c 4 192.168.1.1
```

Then:

```bash
ping -c 4 8.8.8.8
```

Then:

```bash
ping -c 4 google.com
```

---

# 32. DNS in DevOps

DNS is extremely important in DevOps.

It is used by:

```text
Web Applications
APIs
Load Balancers
Cloud Services
Containers
Kubernetes
CI/CD Systems
Monitoring
Service Discovery
```

For example:

```text
Application
    ↓
api.example.com
    ↓
DNS
    ↓
Load Balancer
    ↓
Backend Servers
```

---

# 33. DNS and Load Balancers

A domain can point users toward a load-balancing service.

Conceptually:

```text
www.example.com
        ↓
       DNS
        ↓
Load Balancer
        ↓
+-------+-------+
|       |       |
App 1  App 2  App 3
```

DNS provides the name-based entry point.

---

# 34. DNS and Kubernetes

Kubernetes provides internal DNS-based service discovery.

Instead of applications needing to know Pod IP addresses directly:

```text
Application
    ↓
Service DNS Name
    ↓
Kubernetes Service
    ↓
Pods
```

This makes service communication easier because Pod IP addresses can change.

---

# 35. DNS and Containers

Containers often communicate using DNS names on container networks.

Example:

```text
app
 ↓
database
 ↓
PostgreSQL
```

Instead of hard-coding a container IP, an application can use a service/container name when supported by the networking setup.

---

# 36. DNS and CI/CD

CI/CD pipelines may need to resolve:

```text
Git repositories
Container registries
Cloud APIs
Package repositories
Deployment endpoints
Internal services
```

A DNS failure can therefore cause:

```text
Build Failure
Dependency Download Failure
Docker Push Failure
Deployment Failure
API Connection Failure
```

---

# 37. Important DNS Commands

```bash
cat /etc/hosts
```

```bash
cat /etc/resolv.conf
```

```bash
nslookup google.com
```

```bash
dig google.com
```

```bash
host google.com
```

```bash
resolvectl status
```

```bash
resolvectl query google.com
```

---

# 38. DNS Mental Model

Remember DNS as:

```text
Name
 ↓
Resolver
 ↓
DNS Hierarchy
 ↓
Authoritative Server
 ↓
Record
 ↓
IP Address
```

And remember:

```text
A     → IPv4
AAAA  → IPv6
CNAME → Alias
MX    → Mail
NS    → Name Server
TXT   → Text / Verification
PTR   → Reverse DNS
```

---

# 🎯 DevOps Interview Summary

A strong interview explanation:

> DNS stands for Domain Name System. It translates human-readable domain names into IP addresses. A client normally sends its DNS query to a recursive resolver. If the answer is not already cached, the resolver can query the DNS hierarchy, including root and TLD servers, and ultimately obtain the authoritative answer. Important DNS records include A, AAAA, CNAME, MX, NS, TXT, and PTR. In DevOps, DNS is critical for applications, APIs, load balancers, cloud services, containers, Kubernetes service discovery, and CI/CD systems.

---

# 🧠 Key Takeaways

```text
DNS
 ↓
Name Resolution
```

```text
Domain Name
 ↓
IP Address
```

```text
A
 ↓
IPv4
```

```text
AAAA
 ↓
IPv6
```

```text
CNAME
 ↓
Alias
```

```text
MX
 ↓
Mail
```

```text
NS
 ↓
Name Server
```

```text
PTR
 ↓
Reverse DNS
```

```text
TTL
 ↓
Caching Duration
```

> **Learn → Practice → Break → Debug → Document → Explain**
