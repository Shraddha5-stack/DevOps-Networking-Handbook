# 🔧 Chapter 15 – DNS Commands

## 1. Check `/etc/hosts`

```bash
cat /etc/hosts
```

### Purpose

Shows local hostname-to-IP mappings.

Example:

```text
127.0.0.1       localhost
127.0.1.1       my-machine
```

---

## 2. Check `/etc/resolv.conf`

```bash
cat /etc/resolv.conf
```

### Purpose

Shows resolver configuration used by the system.

You may see:

```text
nameserver 192.168.1.1
```

The exact contents depend on how DNS is managed on the system.

---

## 3. Check DNS Resolver Status

```bash
resolvectl status
```

### Purpose

Displays DNS configuration and resolver information for the system.

Look for:

```text
DNS Servers
DNS Domain
Current DNS Server
```

---

## 4. Resolve a Domain with `resolvectl`

```bash
resolvectl query google.com
```

### Purpose

Tests whether the system resolver can resolve a domain name.

Expected result contains an address such as:

```text
google.com: xxx.xxx.xxx.xxx
```

---

## 5. Use `nslookup`

```bash
nslookup google.com
```

### Purpose

Performs a DNS lookup and displays:

```text
DNS Server
Address
Domain
Resolved IP
```

Example structure:

```text
Server:         192.168.1.1
Address:        192.168.1.1#53

Name:           google.com
Address:        ...
```

---

## 6. Query an A Record

```bash
nslookup -type=A google.com
```

### Purpose

Requests IPv4 address records.

Remember:

```text
A → IPv4
```

---

## 7. Query an AAAA Record

```bash
nslookup -type=AAAA google.com
```

### Purpose

Requests IPv6 address records.

Remember:

```text
AAAA → IPv6
```

---

## 8. Use `dig`

```bash
dig google.com
```

### Purpose

Provides detailed DNS query information.

Important sections include:

```text
QUESTION SECTION
ANSWER SECTION
AUTHORITY SECTION
ADDITIONAL SECTION
```

---

## 9. Short `dig` Output

```bash
dig google.com +short
```

### Purpose

Displays the resolved addresses in a concise format.

This is useful when you only want the answer.

---

## 10. Query A Record with `dig`

```bash
dig google.com A
```

### Purpose

Queries the IPv4 address record.

---

## 11. Query AAAA Record

```bash
dig google.com AAAA
```

### Purpose

Queries the IPv6 address record.

---

## 12. Query MX Record

```bash
dig google.com MX
```

### Purpose

Displays mail exchange records.

Remember:

```text
MX → Mail Servers
```

---

## 13. Query NS Record

```bash
dig google.com NS
```

### Purpose

Displays name server records.

Remember:

```text
NS → Name Servers
```

---

## 14. Query TXT Record

```bash
dig google.com TXT
```

### Purpose

Displays TXT records associated with the domain.

TXT records can be used for:

```text
Domain Verification
Email Security
Service Configuration
```

---

## 15. Reverse DNS Lookup

```bash
dig -x 8.8.8.8
```

### Purpose

Performs a reverse DNS lookup.

Forward:

```text
Domain → IP
```

Reverse:

```text
IP → Domain
```

---

## 16. Reverse Lookup with `nslookup`

```bash
nslookup 8.8.8.8
```

### Purpose

Attempts to resolve the IP address to a hostname.

---

## 17. Use `host`

```bash
host google.com
```

### Purpose

Performs a simple DNS lookup.

Example:

```text
google.com has address ...
```

---

## 18. Query a Specific Record with `host`

```bash
host -t MX google.com
```

Other examples:

```bash
host -t A google.com
```

```bash
host -t AAAA google.com
```

```bash
host -t NS google.com
```

---

## 19. Query a Specific DNS Server

With `dig`:

```bash
dig @8.8.8.8 google.com
```

This asks the specified DNS server to resolve the domain.

Another example:

```bash
dig @1.1.1.1 google.com
```

This is useful for comparing DNS resolvers.

---

## 20. Check DNS Response Time

Use:

```bash
dig google.com
```

Look near the bottom for:

```text
Query time: XX msec
```

This can help when investigating DNS latency.

---

## 21. Trace DNS Delegation

```bash
dig +trace example.com
```

### Purpose

Shows the DNS lookup path from the root servers through the DNS hierarchy.

Conceptually:

```text
Root
 ↓
TLD
 ↓
Authoritative DNS
 ↓
Domain
```

This is useful for understanding how DNS resolution works.

---

# 🧪 Practical DNS Lab

Run the commands below one at a time.

## Step 1 – Check local hosts

```bash
cat /etc/hosts
```

---

## Step 2 – Check resolver configuration

```bash
cat /etc/resolv.conf
```

---

## Step 3 – Check resolver status

```bash
resolvectl status
```

---

## Step 4 – Resolve Google

```bash
resolvectl query google.com
```

---

## Step 5 – Use `nslookup`

```bash
nslookup google.com
```

---

## Step 6 – Use `dig`

```bash
dig google.com
```

---

## Step 7 – Get concise output

```bash
dig google.com +short
```

---

## Step 8 – Check IPv4

```bash
dig google.com A
```

---

## Step 9 – Check IPv6

```bash
dig google.com AAAA
```

---

## Step 10 – Check mail records

```bash
dig google.com MX
```

---

## Step 11 – Check name servers

```bash
dig google.com NS
```

---

## Step 12 – Reverse DNS

```bash
dig -x 8.8.8.8
```

---

# 🛠️ DNS Troubleshooting Commands

If DNS is not working:

### Check connectivity

```bash
ping -c 4 192.168.1.1
```

### Check Internet by IP

```bash
ping -c 4 8.8.8.8
```

### Check DNS resolution

```bash
ping -c 4 google.com
```

### Check resolver

```bash
resolvectl status
```

### Test DNS directly

```bash
nslookup google.com
```

### Detailed test

```bash
dig google.com
```

### Test another resolver

```bash
dig @8.8.8.8 google.com
```

---

# 🧠 Command Cheat Sheet

| Command                       | Purpose                |
| ----------------------------- | ---------------------- |
| `cat /etc/hosts`              | Local hostname mapping |
| `cat /etc/resolv.conf`        | Resolver configuration |
| `resolvectl status`           | DNS resolver status    |
| `resolvectl query google.com` | Resolve domain         |
| `nslookup google.com`         | DNS lookup             |
| `dig google.com`              | Detailed DNS query     |
| `dig google.com +short`       | Short result           |
| `dig google.com A`            | IPv4 record            |
| `dig google.com AAAA`         | IPv6 record            |
| `dig google.com MX`           | Mail records           |
| `dig google.com NS`           | Name server records    |
| `dig google.com TXT`          | TXT records            |
| `dig -x 8.8.8.8`              | Reverse DNS            |
| `host google.com`             | Simple DNS lookup      |
| `dig +trace example.com`      | DNS delegation trace   |

---

# 🎯 DevOps Tip

For everyday troubleshooting, remember these three commands:

```bash
nslookup google.com
```

```bash
dig google.com
```

```bash
resolvectl status
```

For deeper investigation:

```bash
dig +trace example.com
```

The goal is not just to run commands.

The goal is to answer:

```text
Can the system resolve the name?
        ↓
Which DNS server answered?
        ↓
What record was returned?
        ↓
How long did the query take?
        ↓
Where is the failure?
```

> **Learn → Practice → Break → Debug → Document → Explain**
