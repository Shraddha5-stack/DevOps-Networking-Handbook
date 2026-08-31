# 🛠️ Chapter 26 — SSL/TLS Commands

## 1. Test HTTPS with curl

```bash
curl https://example.com
```

### Observation

The server returns the HTTPS response.

---

## 2. Check HTTPS Response Headers

```bash
curl -I https://example.com
```

### Observe

```text
HTTP status
Server
Content-Type
Date
```

---

## 3. Verbose HTTPS Debugging

```bash
curl -v https://example.com
```

### Observe

Look for:

```text
DNS resolution
TCP connection
TLS handshake
Certificate
HTTP request
HTTP response
```

---

## 4. Follow HTTPS Redirects

```bash
curl -IL https://example.com
```

### Observation

Check for:

```text
301
302
Location:
```

---

# 🔐 OpenSSL Commands

## 5. Connect to an HTTPS Server

```bash
openssl s_client -connect example.com:443
```

### Observe

Look for:

```text
Protocol
Cipher
Certificate
Verify return code
```

Exit:

```text
Ctrl + C
```

---

## 6. Check TLS Version

```bash
openssl s_client -connect example.com:443
```

Look for:

```text
Protocol
```

Example:

```text
TLSv1.3
```

---

## 7. Force TLS 1.2

```bash
openssl s_client -connect example.com:443 -tls1_2
```

### Observation

Check whether the server successfully establishes a TLS 1.2 connection.

---

## 8. Force TLS 1.3

```bash
openssl s_client -connect example.com:443 -tls1_3
```

### Observation

Check whether TLS 1.3 is supported.

---

# 📜 Certificate Commands

## 9. Display Certificate

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -text
```

This displays detailed certificate information.

---

## 10. Check Certificate Subject

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -subject
```

### Observation

The subject identifies the certificate's subject information.

---

## 11. Check Certificate Issuer

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -issuer
```

### Observation

The issuer shows which CA or certificate authority issued the certificate.

---

## 12. Check Certificate Dates

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

Example:

```text
notBefore=...
notAfter=...
```

`notAfter` indicates the certificate expiration date.

---

## 13. Check Certificate Serial Number

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -serial
```

---

## 14. Check Certificate Fingerprint

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -fingerprint
```

---

## 15. Check Subject Alternative Names

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"
```

### Observation

SAN contains hostnames covered by the certificate.

---

# 🌐 SNI

## 16. Test Using SNI

Use:

```bash
openssl s_client -connect example.com:443 -servername example.com
```

`-servername` specifies the hostname through SNI.

### Why is this useful?

Multiple HTTPS websites can share the same IP address.

```text
             Same IP
                |
       ┌────────┴────────┐
       ↓                 ↓
example.com       api.example.com
```

SNI helps the server select the correct certificate.

---

# 🔎 Certificate Verification

## 17. Verify Certificate

```bash
openssl s_client -connect example.com:443 -verify_return_error
```

### Observation

Check:

```text
Verify return code
```

A successful verification should end with a successful verification status.

---

## 18. Display Certificate Chain

```bash
openssl s_client -connect example.com:443 -showcerts
```

### Observe

Look for:

```text
Certificate chain
```

---

# 🔌 Network Commands

## 19. Check HTTPS Port

```bash
nc -vz example.com 443
```

### Observation

This checks TCP connectivity to port 443.

---

## 20. Check HTTP Port

```bash
nc -vz example.com 80
```

---

## 21. Check Listening HTTPS Ports

```bash
sudo ss -ltnp | grep :443
```

---

## 22. Check Listening HTTP Ports

```bash
sudo ss -ltnp | grep :80
```

---

# 🌍 DNS + TLS Troubleshooting

## 23. Resolve the Domain

```bash
dig example.com
```

or:

```bash
getent hosts example.com
```

### Observation

Record:

```text
Domain:
IP:
```

---

## 24. Test HTTPS by IP

You can test TCP connectivity to an IP:

```bash
nc -vz <IP> 443
```

Be careful when testing HTTPS directly by IP because TLS certificate validation normally depends on the hostname.

---

# 🧪 HTTP/TLS Testing

## 25. Test HTTPS Status Code

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

---

## 26. Measure HTTPS Response Time

```bash
curl -o /dev/null -s \
-w "Status: %{http_code}\nTime: %{time_total}s\n" \
https://example.com
```

---

## 27. Test TLS 1.2 with curl

```bash
curl --tlsv1.2 -I https://example.com
```

---

## 28. Test TLS 1.3 with curl

```bash
curl --tlsv1.3 -I https://example.com
```

---

# 🔑 Generate a Private Key for Lab Use

> Use these commands only for your own testing environment.

## 29. Generate RSA Private Key

```bash
openssl genrsa -out server.key 2048
```

Check:

```bash
ls -l server.key
```

Protect the key:

```bash
chmod 600 server.key
```

---

## 30. Inspect Private Key

```bash
openssl rsa -in server.key -check
```

---

# 📄 Generate a CSR

## 31. Create Certificate Signing Request

```bash
openssl req -new -key server.key -out server.csr
```

The CSR contains information that can be submitted to a certificate authority.

---

## 32. Inspect CSR

```bash
openssl req -in server.csr -text -noout
```

---

# 🧪 Generate a Self-Signed Certificate

For a local lab:

```bash
openssl req -x509 -new -nodes \
-key server.key \
-sha256 \
-days 365 \
-out server.crt
```

Check:

```bash
ls -lh server.key server.csr server.crt
```

---

## 33. Inspect Local Certificate

```bash
openssl x509 -in server.crt -text -noout
```

---

## 34. Check Local Certificate Dates

```bash
openssl x509 -in server.crt -noout -dates
```

---

## 35. Check Local Certificate Subject

```bash
openssl x509 -in server.crt -noout -subject
```

---

## 36. Check Local Certificate Issuer

```bash
openssl x509 -in server.crt -noout -issuer
```

For a self-signed certificate, the subject and issuer are typically the same.

---

# 🧹 Lab Cleanup

Remove the test certificate files when finished:

```bash
rm -f server.key server.csr server.crt
```

Verify:

```bash
ls
```

---

# ☸️ Kubernetes TLS Commands

## 37. Check Kubernetes Secrets

```bash
kubectl get secrets
```

---

## 38. Check TLS Secret

```bash
kubectl get secret tls-secret
```

---

## 39. Inspect Secret Metadata

```bash
kubectl describe secret tls-secret
```

Do not expose secret contents unnecessarily.

---

## 40. Check Ingress

```bash
kubectl get ingress
```

---

## 41. Describe Ingress

```bash
kubectl describe ingress <INGRESS-NAME>
```

Look for:

```text
TLS
Hosts
Rules
Backend
```

---

# 🚨 TLS Troubleshooting Workflow

When HTTPS fails, use this order:

```text
1. DNS
   ↓
2. TCP 443
   ↓
3. TLS handshake
   ↓
4. Certificate
   ↓
5. HTTP
   ↓
6. Reverse Proxy
   ↓
7. Load Balancer
   ↓
8. Backend
```

### Step 1 — DNS

```bash
dig example.com
```

### Step 2 — TCP

```bash
nc -vz example.com 443
```

### Step 3 — TLS

```bash
openssl s_client -connect example.com:443 -servername example.com
```

### Step 4 — Certificate

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

### Step 5 — HTTPS

```bash
curl -v https://example.com
```

---

# 🧠 Command Cheat Sheet

| Purpose                | Command                                                             |
| ---------------------- | ------------------------------------------------------------------- |
| Test HTTPS             | `curl -I https://example.com`                                       |
| Verbose HTTPS          | `curl -v https://example.com`                                       |
| TLS connection         | `openssl s_client -connect example.com:443`                         |
| TLS + SNI              | `openssl s_client -connect example.com:443 -servername example.com` |
| TLS 1.2                | `openssl s_client -connect example.com:443 -tls1_2`                 |
| TLS 1.3                | `openssl s_client -connect example.com:443 -tls1_3`                 |
| Certificate            | `openssl x509 -in cert.crt -text -noout`                            |
| Certificate dates      | `openssl x509 -in cert.crt -noout -dates`                           |
| Certificate issuer     | `openssl x509 -in cert.crt -noout -issuer`                          |
| Certificate subject    | `openssl x509 -in cert.crt -noout -subject`                         |
| SAN                    | `openssl x509 -in cert.crt -text -noout`                            |
| TCP 443                | `nc -vz example.com 443`                                            |
| DNS                    | `dig example.com`                                                   |
| Listening ports        | `ss -ltnp`                                                          |
| Kubernetes TLS secrets | `kubectl get secrets`                                               |
| Kubernetes Ingress     | `kubectl get ingress`                                               |

---

# 📝 My Observations

| Command                       | Result | What I Learned |
| ----------------------------- | ------ | -------------- |
| `curl -v https://example.com` |        |                |
| `openssl s_client ...`        |        |                |
| `openssl x509 ... -dates`     |        |                |
| `openssl x509 ... -issuer`    |        |                |
| `nc -vz ... 443`              |        |                |
| `dig example.com`             |        |                |

---

# 🎯 Practical Goal

After practicing these commands, I should be able to answer:

```text
Is DNS working?
        ↓
Is TCP 443 reachable?
        ↓
Does TLS handshake succeed?
        ↓
Is the certificate valid?
        ↓
Does the hostname match?
        ↓
Is HTTPS returning a valid response?
        ↓
Is the backend healthy?
```

This is the basic troubleshooting workflow I should follow whenever an HTTPS service is not working.
