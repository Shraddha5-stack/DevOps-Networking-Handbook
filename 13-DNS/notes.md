# 🌐 Chapter 13 – Domain Name System (DNS)

## 📑 Table of Contents

1. Introduction
2. What is DNS?
3. Why Do We Need DNS?
4. Domain Name vs IP Address
5. How DNS Works
6. DNS Resolution – Step by Step
7. DNS Hierarchy
8. Root DNS Servers
9. TLD DNS Servers
10. Authoritative DNS Servers
11. Recursive DNS Resolver
12. DNS Cache
13. DNS TTL
14. DNS Records
15. A Record
16. AAAA Record
17. CNAME Record
18. MX Record
19. NS Record
20. TXT Record
21. PTR Record
22. Forward DNS
23. Reverse DNS
24. Recursive vs Iterative Queries
25. DNS over UDP and TCP
26. DNS Ports
27. DNS and HTTP/HTTPS
28. DNS Failure Example
29. DNS in DevOps
30. DNS in Cloud
31. DNS in Kubernetes
32. Real-World Example
33. Key Takeaways
34. Summary
35. Interview Tip

---

# 📖 1. Introduction

Every time you type:

```text
https://www.google.com
```

your computer needs to discover the IP address of the server hosting that website.

Computers communicate using IP addresses, but humans prefer memorable names such as:

```text
google.com
github.com
amazon.com
```

**DNS (Domain Name System)** connects these two worlds.

DNS translates human-readable domain names into IP addresses.

For example:

```text
google.com
     ↓
142.250.x.x
```

DNS is one of the fundamental services that makes the Internet usable.

---

# 🌐 2. What is DNS?

**DNS stands for Domain Name System.**

DNS is a distributed naming system that translates domain names into IP addresses and provides other information about domains.

The simplest example is:

```text
Domain Name
     ↓
DNS
     ↓
IP Address
```

Example:

```text
example.com
     ↓
93.184.216.34
```

DNS can also provide information such as:

- Mail servers
- Name servers
- Aliases
- Verification information
- Reverse mappings

---

# ❓ 3. Why Do We Need DNS?

Without DNS, users would need to remember IP addresses.

Instead of:

```text
google.com
```

we would have to remember something like:

```text
142.250.x.x
```

Imagine doing this for hundreds of websites.

DNS provides a human-friendly naming system.

### Without DNS

```text
Browser
   ↓
IP Address
```

### With DNS

```text
Browser
   ↓
Domain Name
   ↓
DNS
   ↓
IP Address
   ↓
Web Server
```

---

# 🔢 4. Domain Name vs IP Address

## Domain Name

A human-readable name:

```text
google.com
```

## IP Address

A numerical network address:

```text
142.250.x.x
```

The domain name is easier for humans to remember.

The IP address is used for network communication.

---

# ⚙️ 5. How DNS Works

Suppose you type:

```text
www.example.com
```

into your browser.

The computer needs the IP address.

The simplified process is:

```text
User
 ↓
Browser
 ↓
DNS Resolver
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

The exact path may be shorter when the answer is already cached.

---

# 🔄 6. DNS Resolution – Step by Step

Let's understand the complete process.

Suppose you request:

```text
www.example.com
```

## Step 1 – Browser Cache

The browser may already know the IP address.

If it does:

```text
Browser Cache
     ↓
IP Address
```

DNS lookup may not need to continue.

---

## Step 2 – Operating System Cache

If the browser does not know the answer, the operating system may have a cached DNS result.

---

## Step 3 – DNS Resolver

If the answer is not cached locally, the request goes to a **recursive DNS resolver**.

Examples include DNS resolvers provided by:

- ISP
- Enterprise network
- Public DNS providers

The resolver performs the lookup on behalf of the client.

---

## Step 4 – Root DNS Server

If the resolver does not have the answer cached, it can query a root DNS server.

The root server does not normally provide the final IP address.

Instead, it tells the resolver where to find the appropriate TLD server.

For:

```text
www.example.com
```

the root points toward the:

```text
.com
```

TLD infrastructure.

---

## Step 5 – TLD Server

The TLD means:

**Top-Level Domain**

Examples:

```text
.com
.org
.net
.in
```

The `.com` TLD infrastructure can direct the resolver toward the authoritative name servers for `example.com`.

---

## Step 6 – Authoritative DNS Server

The authoritative DNS server contains the actual DNS records for the domain.

It can return something such as:

```text
www.example.com
A
93.184.216.34
```

---

## Step 7 – Resolver Returns the Answer

The recursive resolver sends the result back to your computer.

```text
Authoritative DNS
       ↓
Recursive Resolver
       ↓
Your Computer
```

---

## Step 8 – Browser Connects

Now the browser knows the destination IP.

It can establish the appropriate connection, such as HTTPS.

```text
Browser
   ↓
IP Address
   ↓
Server
```

---

# 🏗️ 7. DNS Hierarchy

DNS is organized hierarchically.

```text
                    .
                 Root
                   |
        -----------------------
        |          |          |
       .com       .org       .in
        |
     example
        |
      www
```

The hierarchy contains:

1. Root
2. TLD
3. Second-level domain
4. Subdomain/host

---

# 🌳 8. Root DNS Servers

The DNS root is represented by:

```text
.
```

The root zone sits at the top of the DNS hierarchy.

Root DNS infrastructure helps resolvers locate the appropriate TLD servers.

Examples:

```text
.com
.org
.net
.in
```

The root does not normally contain the final IP address for every website.

---

# 🌍 9. TLD DNS Servers

TLD means:

**Top-Level Domain**

Examples:

```text
.com
.org
.net
.edu
.in
```

For:

```text
www.example.com
```

the `.com` TLD infrastructure helps the resolver find the authoritative name servers for:

```text
example.com
```

---

# 🏛️ 10. Authoritative DNS Servers

An authoritative DNS server contains the DNS records for a domain or DNS zone.

For example:

```text
example.com
```

may have records such as:

```text
www → IP address
mail → mail server
```

The authoritative server provides the final authoritative answer for the zone.

---

# 🔁 11. Recursive DNS Resolver

A recursive resolver receives DNS requests from clients and finds the answer.

Example:

```text
Laptop
   |
   ↓
Recursive Resolver
   |
   ↓
Root
   |
   ↓
TLD
   |
   ↓
Authoritative DNS
```

The resolver then returns the answer to the client.

---

# 💾 12. DNS Cache

DNS results are often cached.

Caching reduces:

- DNS lookup time
- Network traffic
- Load on DNS servers

Example:

```text
First request
Client → Resolver → DNS hierarchy

Later request
Client → Resolver Cache
```

If the answer is cached, the resolver may return it immediately.

---

# ⏳ 13. DNS TTL

**TTL stands for Time To Live.**

DNS TTL determines how long a DNS answer may remain cached.

Example:

```text
TTL = 300 seconds
```

This means the cached answer can generally be reused for about:

```text
5 minutes
```

After the TTL expires, the resolver may need to obtain a fresh answer.

---

# 📋 14. DNS Records

DNS uses different record types for different purposes.

Common records:

| Record | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Alias |
| MX | Mail server |
| NS | Name server |
| TXT | Text/verification information |
| PTR | Reverse DNS |

---

# 🔢 15. A Record

An **A record** maps a hostname to an IPv4 address.

Example:

```text
example.com → 192.0.2.10
```

Conceptually:

```text
A
example.com
192.0.2.10
```

---

# 🌐 16. AAAA Record

An **AAAA record** maps a hostname to an IPv6 address.

Example:

```text
example.com
    ↓
2001:db8::10
```

---

# 🔗 17. CNAME Record

**CNAME** means Canonical Name.

It creates an alias from one hostname to another hostname.

Example:

```text
www.example.com
       ↓
example.com
```

The CNAME points to another hostname rather than directly storing an IP address.

---

# 📧 18. MX Record

**MX** means Mail Exchange.

It identifies mail servers responsible for receiving email for a domain.

Example:

```text
example.com
    ↓
mail.example.com
```

MX records also have priorities.

---

# 🏷️ 19. NS Record

**NS** means Name Server.

NS records identify the authoritative name servers for a DNS zone.

Example:

```text
example.com
    ↓
ns1.example-dns.com
ns2.example-dns.com
```

---

# 📝 20. TXT Record

TXT records contain text information associated with a domain.

Common uses include:

- Domain verification
- SPF
- Email security
- Service configuration

Example:

```text
example.com
TXT
"verification=value"
```

---

# 🔄 21. PTR Record

PTR records are used for **reverse DNS**.

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

# ➡️ 22. Forward DNS

Forward DNS maps:

```text
Hostname → IP Address
```

Example:

```text
google.com
    ↓
IP address
```

Common records:

```text
A
AAAA
```

---

# ⬅️ 23. Reverse DNS

Reverse DNS maps:

```text
IP Address → Hostname
```

Example:

```text
192.0.2.10
    ↓
server.example.com
```

The PTR record is used for this purpose.

---

# 🔄 24. Recursive vs Iterative Queries

## Recursive Query

The client asks the resolver:

> "Find the answer for me."

The resolver performs the work.

```text
Client
  ↓
Resolver
  ↓
DNS hierarchy
  ↓
Answer
```

---

## Iterative Query

A DNS server responds with the best information it currently has, such as a referral to another DNS server.

Conceptually:

```text
Resolver → Root
Root → Ask TLD

Resolver → TLD
TLD → Ask Authoritative Server

Resolver → Authoritative
Authoritative → Final Answer
```

---

# 📡 25. DNS over UDP and TCP

DNS commonly uses:

```text
UDP port 53
```

UDP is preferred for many standard DNS queries because it has low overhead.

DNS can also use:

```text
TCP port 53
```

TCP may be used when:

- A response does not fit the normal UDP exchange
- Zone transfers are performed
- Reliable transport is required for certain DNS operations

Modern DNS can also be carried over encrypted protocols such as DNS over HTTPS (DoH) and DNS over TLS (DoT).

---

# 🔢 26. DNS Ports

Traditional DNS uses:

```text
UDP 53
TCP 53
```

Important:

DNS does not use:

```text
TCP 80
TCP 443
```

for traditional DNS itself.

HTTP/HTTPS are separate application protocols.

---

# 🌐 27. DNS and HTTP/HTTPS

When you enter:

```text
https://example.com
```

DNS generally happens before the browser connects to the web server.

Simplified:

```text
1. DNS lookup
       ↓
2. Obtain IP address
       ↓
3. Establish network connection
       ↓
4. TLS handshake for HTTPS
       ↓
5. HTTP request
       ↓
6. HTTP response
```

DNS therefore acts as an important first step in accessing many Internet services.

---

# 🚨 28. DNS Failure Example

Suppose:

```bash
ping 8.8.8.8
```

works.

But:

```bash
ping google.com
```

fails with a name-resolution error.

This suggests:

```text
Internet connectivity
        ↓
       WORKING

DNS resolution
        ↓
       FAILING
```

Possible causes:

- DNS server unavailable
- Incorrect DNS configuration
- DNS firewall restrictions
- Resolver problem

Check:

```bash
cat /etc/resolv.conf
```

and:

```bash
nslookup google.com
```

or:

```bash
dig google.com
```

---

# ☁️ 29. DNS in DevOps

DevOps engineers interact with DNS constantly.

Examples:

- Web applications
- APIs
- Microservices
- Databases
- Load balancers
- Cloud infrastructure
- Kubernetes
- Service discovery
- CI/CD systems

A deployment can be healthy while users still experience problems because DNS records are incorrect or not updated as expected.

---

# ☁️ 30. DNS in Cloud

Cloud platforms provide managed DNS services.

DNS can be used to map:

```text
api.example.com
       ↓
Load Balancer
```

or:

```text
app.example.com
       ↓
Cloud service
```

DNS is commonly used with:

- Load balancers
- CDN endpoints
- Application servers
- Kubernetes ingress
- Failover systems

---

# ☸️ 31. DNS in Kubernetes

Kubernetes provides internal DNS-based service discovery.

For example:

```text
my-service
```

can resolve to a Kubernetes Service.

A service may be accessed using a DNS name similar to:

```text
my-service.my-namespace.svc.cluster.local
```

This allows applications to communicate using service names instead of hard-coded IP addresses.

---

# 🌍 32. Real-World Example

Suppose a company has:

```text
www.example.com
api.example.com
db.example.com
```

DNS can map these names to different infrastructure:

```text
www.example.com
       ↓
Load Balancer

api.example.com
       ↓
API Servers

db.example.com
       ↓
Database
```

Applications can use stable names even when the underlying infrastructure changes.

---

# 📌 33. Key Takeaways

- DNS translates names into IP addresses and provides other DNS information.
- DNS is hierarchical and distributed.
- Root servers sit at the top of the hierarchy.
- TLD servers handle domains such as `.com` and `.in`.
- Authoritative DNS servers contain the actual zone records.
- Recursive resolvers find answers on behalf of clients.
- DNS caching improves performance.
- TTL controls how long DNS information can remain cached.
- A records map names to IPv4 addresses.
- AAAA records map names to IPv6 addresses.
- CNAME creates aliases.
- MX records identify mail servers.
- NS records identify name servers.
- TXT records store text-based information.
- PTR records support reverse DNS.
- Traditional DNS commonly uses UDP/TCP port 53.
- DNS is critical for DevOps, cloud, containers, and Kubernetes.

---

# 📝 34. Summary

DNS is the Internet's distributed naming system.

Instead of requiring users and applications to remember IP addresses, DNS allows them to use meaningful names.

The simplified flow is:

```text
Domain Name
     ↓
Recursive Resolver
     ↓
Root
     ↓
TLD
     ↓
Authoritative DNS
     ↓
IP Address
     ↓
Application Connection
```

DNS is not simply a "name-to-IP lookup." It is a distributed, hierarchical system with caching, delegation, multiple record types, and different query mechanisms.

Understanding DNS is essential for anyone working in networking, Linux, cloud computing, DevOps, SRE, or Kubernetes.

---

# 💼 35. Interview Tip

### Question:

**"What happens when you type google.com into a browser?"**

A strong answer:

> First, the browser and operating system check their DNS caches. If the IP address is not cached, the request goes to a recursive DNS resolver. The resolver may query the root DNS infrastructure, the appropriate TLD servers, and finally the authoritative DNS server for the domain. The authoritative server returns the DNS record, the resolver caches the answer according to its TTL, and the browser receives the IP address. The browser can then connect to the server and request the webpage.

This answer demonstrates practical understanding rather than simply saying:

> "DNS converts a domain name into an IP address."
