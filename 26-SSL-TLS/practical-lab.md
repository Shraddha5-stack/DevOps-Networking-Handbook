# 🧪 Chapter 26 — SSL/TLS Practical Lab

## 🎯 Lab Objective

In this lab, I will practice SSL/TLS troubleshooting using:

* `curl`
* `openssl`
* `dig`
* `nc`
* Certificate inspection
* TLS version testing
* SNI
* Self-signed certificates

---

# Lab 1 — Test HTTPS

## Step 1: Test a Website

Run:

```bash
curl -I https://example.com
```

### Expected Observation

You should receive an HTTP response such as:

```text
HTTP/2 200
```

or another valid HTTP status.

### What I Learned

HTTPS is HTTP communication protected by TLS.

---

# Lab 2 — Verbose HTTPS Test

Run:

```bash
curl -v https://example.com
```

### Observe

Look for:

```text
* Connected to example.com
* TLS handshake
* SSL connection
> GET /
< HTTP/...
```

### What I Learned

`curl -v` helps us see the connection process and TLS negotiation.

---

# Lab 3 — Inspect TLS with OpenSSL

Run:

```bash
openssl s_client -connect example.com:443
```

### Observe

Find:

```text
Protocol
Cipher
Certificate
Verify return code
```

Example:

```text
Protocol  : TLSv1.3
```

### What I Learned

`openssl s_client` is one of the most useful tools for TLS troubleshooting.

Exit:

```text
Ctrl + C
```

---

# Lab 4 — Test SNI

Run:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

### Observation

The `-servername` option sends the hostname using SNI.

### What I Learned

SNI allows a server to select the appropriate certificate when multiple hostnames share an IP address.

---

# Lab 5 — Check Certificate Dates

Run:

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -dates
```

### Expected Output

```text
notBefore=...
notAfter=...
```

### What I Learned

`notAfter` tells me when the certificate expires.

---

# Lab 6 — Check Certificate Issuer

Run:

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -issuer
```

### Observation

Record the certificate issuer:

```text
Issuer:
________________________
```

### What I Learned

The issuer identifies the authority that signed the certificate.

---

# Lab 7 — Check Certificate Subject

Run:

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -subject
```

### Observation

Record:

```text
Subject:
________________________
```

---

# Lab 8 — Check SAN

SAN means **Subject Alternative Name**.

Run:

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -text |
grep -A1 "Subject Alternative Name"
```

### Observation

Find the hostname(s) covered by the certificate.

### What I Learned

The hostname I request should be covered by the certificate's SAN entries.

---

# Lab 9 — Check Certificate Chain

Run:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-showcerts
```

### Observe

Look for:

```text
Certificate chain
```

### What I Learned

A certificate chain can contain:

```text
Root CA
   ↓
Intermediate CA
   ↓
Server Certificate
```

---

# Lab 10 — Test TLS 1.2

Run:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-tls1_2
```

### Observation

Check whether the TLS handshake succeeds.

Record:

```text
TLS 1.2:
[ ] Successful
[ ] Failed
```

---

# Lab 11 — Test TLS 1.3

Run:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-tls1_3
```

### Observation

Record:

```text
TLS 1.3:
[ ] Successful
[ ] Failed
```

### What I Learned

Different clients and servers may support different TLS versions.

---

# Lab 12 — Test TCP Port 443

Run:

```bash
nc -vz example.com 443
```

### Expected Result

A successful TCP connection indicates that port 443 is reachable.

### What I Learned

Before troubleshooting TLS, I should first verify basic TCP connectivity.

---

# Lab 13 — DNS Check

Run:

```bash
dig example.com
```

### Observe

Find:

```text
ANSWER SECTION
```

Record:

```text
Domain:
________________

IP:
________________
```

### What I Learned

DNS must resolve the hostname before a normal HTTPS connection can be established.

---

# Lab 14 — HTTPS Status Code

Run:

```bash
curl -o /dev/null -s \
-w "%{http_code}\n" \
https://example.com
```

### Observation

Example:

```text
200
```

### What I Learned

The command allows me to quickly check the HTTP status returned by the HTTPS endpoint.

---

# Lab 15 — Check TLS with curl

Run:

```bash
curl --tlsv1.2 -I https://example.com
```

Then:

```bash
curl --tlsv1.3 -I https://example.com
```

### Observation

Record:

| TLS Version | Result |
| ----------- | ------ |
| TLS 1.2     |        |
| TLS 1.3     |        |

---

# Lab 16 — Generate an RSA Private Key

This lab uses a local test key.

Run:

```bash
openssl genrsa -out server.key 2048
```

Check:

```bash
ls -lh server.key
```

### Protect the key

```bash
chmod 600 server.key
```

Check:

```bash
ls -l server.key
```

### What I Learned

Private keys must be protected because anyone with the private key may be able to impersonate the associated service depending on the system and certificate.

---

# Lab 17 — Generate a CSR

Run:

```bash
openssl req \
-new \
-key server.key \
-out server.csr
```

Enter the requested information.

Check:

```bash
ls -lh server.csr
```

### What I Learned

A CSR is a Certificate Signing Request that can be submitted to a CA when requesting a certificate.

---

# Lab 18 — Inspect CSR

Run:

```bash
openssl req \
-in server.csr \
-text \
-noout
```

### Observe

Look for:

```text
Subject
Public Key
Signature
```

---

# Lab 19 — Generate Self-Signed Certificate

For local testing:

```bash
openssl req \
-x509 \
-new \
-nodes \
-key server.key \
-sha256 \
-days 365 \
-out server.crt
```

Check:

```bash
ls -lh server.key server.csr server.crt
```

### What I Learned

A self-signed certificate is useful for testing but is not automatically trusted by public browsers.

---

# Lab 20 — Inspect Self-Signed Certificate

Run:

```bash
openssl x509 \
-in server.crt \
-text \
-noout
```

---

# Lab 21 — Check Certificate Expiration

Run:

```bash
openssl x509 \
-in server.crt \
-noout \
-dates
```

Record:

```text
Valid From:
________________

Valid Until:
________________
```

---

# Lab 22 — Check Certificate Issuer

Run:

```bash
openssl x509 \
-in server.crt \
-noout \
-issuer
```

Then:

```bash
openssl x509 \
-in server.crt \
-noout \
-subject
```

### Observation

For a self-signed certificate, the issuer and subject are generally the same.

---

# Lab 23 — TLS Troubleshooting Simulation

Assume:

```text
https://app.example.com
```

is not working.

Follow this order.

## Step 1 — DNS

```bash
dig app.example.com
```

Question:

```text
Does DNS resolve?
[ ] Yes
[ ] No
```

---

## Step 2 — TCP

```bash
nc -vz app.example.com 443
```

Question:

```text
Is TCP port 443 reachable?
[ ] Yes
[ ] No
```

---

## Step 3 — TLS

```bash
openssl s_client \
-connect app.example.com:443 \
-servername app.example.com
```

Question:

```text
Does TLS handshake succeed?
[ ] Yes
[ ] No
```

---

## Step 4 — Certificate

```bash
echo | openssl s_client \
-connect app.example.com:443 \
-servername app.example.com 2>/dev/null |
openssl x509 -noout -dates
```

Check:

```text
Is certificate expired?
[ ] Yes
[ ] No
```

---

## Step 5 — HTTPS

```bash
curl -v https://app.example.com
```

Check the HTTP response.

---

# Lab 24 — Kubernetes TLS Investigation

Check available secrets:

```bash
kubectl get secrets
```

Check Ingress:

```bash
kubectl get ingress
```

Describe the Ingress:

```bash
kubectl describe ingress <INGRESS-NAME>
```

Check TLS-related information:

```bash
kubectl describe secret <TLS-SECRET-NAME>
```

### Observation

Record:

```text
Ingress:
____________________

TLS Secret:
____________________

Host:
____________________
```

---

# Lab 25 — Build a TLS Troubleshooting Checklist

When an HTTPS application fails:

```text
[ ] DNS resolves
        ↓
[ ] TCP 443 reachable
        ↓
[ ] TLS handshake succeeds
        ↓
[ ] Certificate is valid
        ↓
[ ] Certificate hostname matches
        ↓
[ ] Certificate chain is trusted
        ↓
[ ] HTTP response works
        ↓
[ ] Reverse proxy works
        ↓
[ ] Backend works
```

---

# 📊 Lab Results

| Test               | Command                        | Result |
| ------------------ | ------------------------------ | ------ |
| DNS                | `dig example.com`              |        |
| TCP 443            | `nc -vz example.com 443`       |        |
| HTTPS              | `curl -I https://example.com`  |        |
| TLS                | `openssl s_client ...`         |        |
| TLS 1.2            | `openssl s_client ... -tls1_2` |        |
| TLS 1.3            | `openssl s_client ... -tls1_3` |        |
| Certificate        | `openssl x509 ...`             |        |
| Certificate dates  | `openssl x509 ... -dates`      |        |
| Certificate issuer | `openssl x509 ... -issuer`     |        |
| SAN                | `openssl x509 ...`             |        |

---

# 🧹 Cleanup

Remove the local lab files:

```bash
rm -f server.key server.csr server.crt
```

Verify:

```bash
ls -la
```

---

# 🧠 What I Learned

After completing this lab, I can:

* Test HTTPS using `curl`
* Inspect TLS using OpenSSL
* Check certificates
* Check certificate expiration
* Identify certificate issuers
* Understand SNI
* Test TLS 1.2 and TLS 1.3
* Check TCP port 443
* Troubleshoot DNS
* Generate a test private key
* Generate a CSR
* Generate a self-signed certificate
* Understand TLS termination
* Troubleshoot Kubernetes TLS

---

# 🎯 Final DevOps Mental Model

```text
User
 │
 │ https://app.example.com
 ▼
DNS
 │
 ▼
IP Address
 │
 ▼
TCP :443
 │
 ▼
TLS Handshake
 │
 ├── Certificate
 ├── Authentication
 └── Key Establishment
 │
 ▼
Encrypted HTTP
 │
 ▼
Load Balancer / Reverse Proxy
 │
 ▼
Application
```

> **Key lesson:** When HTTPS fails, don't immediately blame the certificate. Troubleshoot systematically from **DNS → TCP → TLS → Certificate → HTTP → Proxy → Backend**.
