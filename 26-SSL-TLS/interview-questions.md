# 🎤 Chapter 26 — SSL/TLS Interview Questions

## 🟢 Basic Questions

### 1. What is SSL?

SSL stands for **Secure Sockets Layer**. It is an older protocol designed to secure communication between a client and server.

SSL is deprecated today, and modern systems use TLS.

---

### 2. What is TLS?

TLS stands for **Transport Layer Security**.

It is a cryptographic protocol used to secure network communication by providing:

* Confidentiality
* Integrity
* Authentication

---

### 3. What is the difference between SSL and TLS?

SSL is the older protocol, while TLS is its modern successor.

```text
SSL → Old / Deprecated
TLS → Modern / Recommended
```

---

### 4. What is HTTPS?

HTTPS means **HTTP over TLS**.

```text
HTTP + TLS = HTTPS
```

HTTPS protects HTTP communication from unauthorized observation and tampering.

---

### 5. Which port is commonly used by HTTPS?

HTTPS commonly uses:

```text
TCP 443
```

---

### 6. Why do we need TLS?

TLS protects communication against threats such as:

* Eavesdropping
* Data modification
* Server impersonation

---

### 7. What are the main security properties provided by TLS?

The three major properties are:

```text
Confidentiality
Integrity
Authentication
```

---

## 🟡 Intermediate Questions

### 8. What is a digital certificate?

A digital certificate is a signed document that associates an identity, such as a hostname, with a public key.

It contains information such as:

* Subject
* Public key
* Issuer
* Validity period
* Signature
* SAN

---

### 9. What is a Certificate Authority?

A **Certificate Authority (CA)** is a trusted organization that issues and signs digital certificates.

Examples include:

* Let's Encrypt
* DigiCert
* GlobalSign

---

### 10. What is a certificate chain?

A certificate chain establishes trust between the server certificate and a trusted root CA.

```text
Root CA
   ↓
Intermediate CA
   ↓
Server Certificate
```

---

### 11. What is a public key?

A public key is part of a public/private key pair and can generally be distributed publicly.

It is used for cryptographic operations such as authentication, encryption in applicable schemes, and signature verification.

---

### 12. What is a private key?

A private key is the secret counterpart to a public key.

It must be protected and should not be shared publicly.

---

### 13. What is symmetric encryption?

Symmetric encryption uses the same secret key for encryption and decryption.

It is efficient and commonly used to protect bulk application data in secure sessions.

---

### 14. What is asymmetric cryptography?

Asymmetric cryptography uses a public/private key pair.

It is commonly used for:

* Authentication
* Digital signatures
* Key establishment

---

### 15. Symmetric vs asymmetric encryption?

| Symmetric                      | Asymmetric                       |
| ------------------------------ | -------------------------------- |
| Shared secret key              | Public/private key pair          |
| Fast                           | Generally slower                 |
| Bulk data encryption           | Authentication/key establishment |
| Requires secure secret sharing | Public key can be distributed    |

---

### 16. What is the TLS handshake?

The TLS handshake is the process through which the client and server negotiate security parameters and establish the cryptographic state needed for a secure session.

A simplified flow:

```text
Client
  ↓
ClientHello
  ↓
ServerHello
  ↓
Certificate
  ↓
Key Establishment
  ↓
Secure Session
```

The exact messages differ between TLS versions.

---

### 17. What is SNI?

SNI stands for **Server Name Indication**.

It allows a client to indicate the hostname it wants during the TLS handshake.

This is useful when multiple HTTPS websites share the same IP address.

---

### 18. What is ALPN?

ALPN stands for **Application-Layer Protocol Negotiation**.

It allows the client and server to negotiate the application protocol used over TLS.

Examples:

```text
HTTP/1.1
HTTP/2
```

---

### 19. What is TLS termination?

TLS termination means decrypting TLS traffic at a network component.

Example:

```text
Client
  ↓ HTTPS
Load Balancer
  ↓
TLS Termination
  ↓
Backend
```

TLS can be terminated at:

* Load balancer
* Nginx
* Reverse proxy
* Kubernetes Ingress
* API Gateway
* Application

---

### 20. What is TLS passthrough?

TLS passthrough means an intermediate proxy forwards the encrypted TLS connection without terminating TLS.

```text
Client
  ↓ HTTPS
Proxy
  ↓ HTTPS
Backend
```

The backend performs TLS termination.

---

## 🔴 Advanced Questions

### 21. What is forward secrecy?

Forward secrecy means that compromise of a server's long-term private key should not allow an attacker to decrypt previously captured sessions when appropriate ephemeral key exchange was used.

Modern TLS commonly uses ephemeral Diffie-Hellman mechanisms to provide this property.

---

### 22. What is TLS 1.2?

TLS 1.2 is a widely deployed version of TLS that supports modern cryptographic algorithms.

It remains common in many production environments.

---

### 23. What is TLS 1.3?

TLS 1.3 is a newer TLS version designed to improve security and reduce handshake latency.

Important characteristics include:

* Reduced handshake latency
* Modern cryptographic mechanisms
* Removal of older insecure mechanisms
* Forward secrecy with standard ephemeral key exchanges

---

### 24. What happens when a certificate expires?

When a certificate is expired, clients that validate certificates will normally reject the connection or display a certificate warning.

Example:

```text
Certificate
     ↓
Expired
     ↓
TLS validation failure
```

---

### 25. What causes a certificate hostname mismatch?

A hostname mismatch occurs when the hostname requested by the client is not covered by the certificate's identity, typically its SAN entries.

Example:

```text
Requested:
api.example.com

Certificate:
www.example.com
```

If `api.example.com` is not covered by the certificate, validation can fail.

---

### 26. What is SAN?

SAN stands for **Subject Alternative Name**.

It specifies the DNS names and/or other identities covered by a certificate.

Modern hostname validation relies primarily on SAN rather than the old Common Name field.

---

### 27. What is a self-signed certificate?

A self-signed certificate is signed by the same entity that created it instead of a publicly trusted CA.

It is commonly used for:

* Development
* Testing
* Internal labs

It is not automatically trusted by public browsers.

---

### 28. What is Let's Encrypt?

Let's Encrypt is a publicly trusted Certificate Authority that provides automated TLS certificates.

It supports certificate automation through the ACME protocol.

---

### 29. What is OpenSSL?

OpenSSL is an open-source cryptographic toolkit used for:

* TLS testing
* Certificate inspection
* Key generation
* CSR generation
* Certificate generation for labs
* Troubleshooting

---

### 30. How do you inspect an HTTPS connection?

Use:

```bash
openssl s_client -connect example.com:443
```

For SNI:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

---

### 31. How do you check certificate expiration?

Use:

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -dates
```

Look at:

```text
notAfter
```

---

### 32. How do you check the certificate issuer?

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -issuer
```

---

### 33. How do you check the certificate subject?

```bash
echo | openssl s_client \
-connect example.com:443 \
-servername example.com 2>/dev/null |
openssl x509 -noout -subject
```

---

### 34. How do you inspect the certificate chain?

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-showcerts
```

---

### 35. How do you test TLS 1.2?

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-tls1_2
```

---

### 36. How do you test TLS 1.3?

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com \
-tls1_3
```

---

# ☸️ Kubernetes Interview Questions

### 37. How is TLS commonly implemented in Kubernetes?

TLS is commonly configured at an **Ingress Controller** or another edge component.

Typical architecture:

```text
Internet
   ↓
HTTPS :443
   ↓
Ingress
   ↓
TLS Termination
   ↓
Service
   ↓
Pod
```

---

### 38. Where can Kubernetes TLS certificates be stored?

They are commonly stored in a Kubernetes Secret of type:

```text
kubernetes.io/tls
```

Example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: tls-secret
type: kubernetes.io/tls
```

---

### 39. How do you check TLS secrets in Kubernetes?

```bash
kubectl get secrets
```

To inspect metadata:

```bash
kubectl describe secret tls-secret
```

Avoid unnecessarily exposing secret contents.

---

### 40. How do you troubleshoot Kubernetes HTTPS?

Follow the network path:

```text
DNS
 ↓
TCP 443
 ↓
Load Balancer
 ↓
Ingress
 ↓
TLS Certificate
 ↓
Service
 ↓
Pod
```

Useful commands:

```bash
kubectl get ingress
```

```bash
kubectl describe ingress <INGRESS-NAME>
```

```bash
kubectl get secrets
```

---

# 🚨 Scenario-Based Questions

### 41. A website shows "certificate expired." How do you troubleshoot?

I would:

1. Check the certificate expiration date.
2. Identify where TLS is terminated.
3. Check whether the correct certificate is installed.
4. Check certificate renewal.
5. Check the certificate chain.
6. Reload or restart the relevant TLS endpoint if required.

Useful command:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

---

### 42. The certificate is valid, but the browser reports a hostname mismatch. What do you check?

I would check:

1. The hostname being requested.
2. The certificate SAN entries.
3. SNI configuration.
4. Whether the load balancer or reverse proxy is serving the correct certificate.

---

### 43. `curl` cannot connect to HTTPS. What would you check first?

I would troubleshoot layer by layer:

```text
DNS
 ↓
TCP 443
 ↓
TLS handshake
 ↓
Certificate
 ↓
HTTP
```

Commands:

```bash
dig example.com
```

```bash
nc -vz example.com 443
```

```bash
openssl s_client -connect example.com:443 -servername example.com
```

```bash
curl -v https://example.com
```

---

### 44. TLS works, but the application returns HTTP 502. What does that suggest?

If TLS succeeds but the response is `502 Bad Gateway`, the TLS layer may be working while the reverse proxy/load balancer cannot successfully communicate with the upstream backend.

I would then check:

* Backend availability
* Service configuration
* Target port
* Network connectivity
* Application logs
* Reverse proxy logs

---

### 45. Why can `curl https://example.com` work while accessing an IP directly fails certificate validation?

Because TLS hostname validation checks whether the requested hostname is covered by the certificate.

For example:

```text
Certificate:
example.com

Request:
https://192.0.2.10
```

The certificate may not be valid for the IP address.

Also, SNI normally uses the hostname to help the server select the correct certificate.

---

# 🎯 DevOps Interview Answer

### 46. Explain SSL/TLS in an interview.

A strong answer:

> TLS is a cryptographic protocol used to secure communication between clients and servers. It provides confidentiality, integrity, and authentication. HTTPS uses HTTP over TLS, commonly on TCP port 443. During the TLS handshake, the client and server negotiate security parameters, authenticate the server using a certificate, and establish keys for the secure session. In DevOps, TLS is commonly terminated at load balancers, reverse proxies, or Kubernetes Ingress controllers. I use tools such as `curl` and `openssl s_client` to troubleshoot TLS, certificates, and HTTPS connectivity.

---

# 🧠 Rapid-Fire Revision

| Question                 | Short Answer                                                         |
| ------------------------ | -------------------------------------------------------------------- |
| SSL?                     | Deprecated predecessor to TLS                                        |
| TLS?                     | Secure communication protocol                                        |
| HTTPS?                   | HTTP over TLS                                                        |
| HTTPS port?              | TCP 443                                                              |
| CA?                      | Certificate Authority                                                |
| Certificate?             | Identity + public key binding                                        |
| Private key?             | Secret cryptographic key                                             |
| SNI?                     | Sends hostname during TLS handshake                                  |
| ALPN?                    | Negotiates application protocol                                      |
| SAN?                     | Certificate identities/hostnames                                     |
| TLS termination?         | Decrypt TLS at an intermediary                                       |
| TLS passthrough?         | Forward encrypted TLS to backend                                     |
| OpenSSL?                 | TLS/certificate toolkit                                              |
| Self-signed certificate? | Certificate signed by itself                                         |
| TLS 1.3?                 | Modern TLS version with reduced handshake latency                    |
| Forward secrecy?         | Past sessions remain protected if long-term key is later compromised |
| HTTPS port?              | 443                                                                  |
| Kubernetes TLS?          | Commonly configured at Ingress                                       |
| TLS Secret?              | `kubernetes.io/tls`                                                  |

---

# 🏆 Final Interview Checklist

Before moving to the next chapter, I should be able to explain:

```text
[ ] SSL vs TLS
[ ] TLS purpose
[ ] HTTPS
[ ] TLS handshake
[ ] Digital certificates
[ ] Certificate Authority
[ ] Certificate chain
[ ] Public/private keys
[ ] Symmetric/asymmetric cryptography
[ ] TLS 1.2
[ ] TLS 1.3
[ ] SNI
[ ] ALPN
[ ] SAN
[ ] Forward secrecy
[ ] TLS termination
[ ] TLS passthrough
[ ] Self-signed certificates
[ ] OpenSSL
[ ] Certificate troubleshooting
[ ] Kubernetes TLS
```

---

# 🎯 Final Mental Model

```text
                 HTTPS
                   │
                   ▼
                TCP :443
                   │
                   ▼
              TLS Handshake
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
   Certificate           Key Establishment
   Validation
        │                     │
        └──────────┬──────────┘
                   ▼
            Encrypted Session
                   │
                   ▼
          Load Balancer / Proxy
                   │
                   ▼
               Backend
```

> **Interview key point:** TLS is not simply "encryption." It combines encryption, integrity protection, and authentication to establish a secure communication channel.
