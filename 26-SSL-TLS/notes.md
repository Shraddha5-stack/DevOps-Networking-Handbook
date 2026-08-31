# 🔐 Chapter 26 — SSL/TLS Notes

## 1. What is SSL?

**SSL** stands for **Secure Sockets Layer**.

SSL was designed to secure communication between a client and server by providing encryption, authentication, and data integrity.

However, SSL is now **deprecated**. Modern systems use TLS instead.

```text
SSL → Old technology
TLS → Modern technology
```

---

# 2. What is TLS?

**TLS** stands for **Transport Layer Security**.

TLS is a cryptographic protocol used to secure communication over a network.

It provides:

* Confidentiality
* Integrity
* Authentication

TLS is commonly used with HTTPS.

```text
HTTP + TLS = HTTPS
```

---

# 3. SSL vs TLS

| SSL             | TLS               |
| --------------- | ----------------- |
| Older protocol  | Modern protocol   |
| Deprecated      | Actively used     |
| SSL 2.0 / 3.0   | TLS 1.2 / TLS 1.3 |
| Not recommended | Recommended       |

### Important

When someone says **"SSL certificate"**, they usually mean a **TLS certificate**.

---

# 4. Why Do We Need TLS?

Without encryption, network traffic may be readable by someone who can observe the communication.

Example:

```text
Without TLS:

Client
  |
  | username: shraddha
  | password: ****
  ↓
Server
```

With TLS:

```text
Client
  |
  | Encrypted data
  ↓
Server
```

TLS protects the communication channel.

---

# 5. What Does TLS Provide?

TLS provides three major security properties.

## 5.1 Confidentiality

Confidentiality means unauthorized people should not be able to read the transmitted data.

```text
Plain Data
    ↓
Encryption
    ↓
Ciphertext
```

---

## 5.2 Integrity

Integrity ensures that data is not modified during transmission without detection.

```text
Client
  ↓
Data
  ↓
Network
  ↓
Server
```

TLS provides mechanisms that allow the receiver to detect tampering.

---

## 5.3 Authentication

Authentication allows the client to verify the identity of the server through certificates and the certificate trust chain.

```text
Client
  ↓
Server Certificate
  ↓
Certificate validation
  ↓
Trusted identity
```

---

# 6. What is a Digital Certificate?

A digital certificate is an electronic document used to associate an identity, such as a domain name, with a public key.

A certificate commonly contains:

* Subject
* Domain names
* Public key
* Issuer
* Validity period
* Signature
* Certificate serial number

Example:

```text
Domain: example.com
Issuer: Certificate Authority
Valid From: ...
Valid Until: ...
Public Key: ...
```

---

# 7. Certificate Authority

A **Certificate Authority (CA)** is an entity that issues and signs digital certificates.

Examples of certificate authorities include:

* Let's Encrypt
* DigiCert
* GlobalSign

The browser or operating system maintains a set of trusted CA certificates.

---

# 8. Certificate Trust Chain

Certificates are commonly organized into a chain.

```text
Root CA
   ↓
Intermediate CA
   ↓
Server Certificate
   ↓
example.com
```

The client validates the chain to determine whether it can trust the server certificate.

---

# 9. Public Key and Private Key

TLS uses asymmetric cryptography as part of establishing secure communication and authentication.

## Public Key

The public key can be shared.

```text
Public Key
    ↓
Certificate
```

## Private Key

The private key must remain secret and should be accessible only to the authorized server/system.

```text
Private Key
    ↓
KEEP SECRET
```

---

# 10. Symmetric Encryption

Symmetric encryption uses the same secret key for encryption and decryption.

```text
Plaintext
   ↓
Secret Key
   ↓
Ciphertext
   ↓
Secret Key
   ↓
Plaintext
```

Symmetric encryption is efficient and is used for bulk data encryption in secure sessions.

---

# 11. Asymmetric Encryption

Asymmetric cryptography uses a key pair:

```text
Public Key
Private Key
```

The two keys are mathematically related.

It is useful for tasks such as:

* Authentication
* Digital signatures
* Key establishment

---

# 12. Symmetric vs Asymmetric Encryption

| Symmetric                   | Asymmetric                                |
| --------------------------- | ----------------------------------------- |
| One shared secret key       | Public/private key pair                   |
| Very fast                   | Generally slower                          |
| Used for bulk data          | Used for authentication/key establishment |
| Requires secure key sharing | Public key can be distributed             |

---

# 13. TLS Handshake

The TLS handshake establishes the security parameters needed for the session.

A simplified TLS flow:

```text
Client
   |
   | ClientHello
   ↓
Server
   |
   | ServerHello
   | Certificate
   ↓
Client
   |
   | Certificate validation
   | Key establishment
   ↓
Both
   |
   | Secure session
   ↓
Encrypted HTTP
```

The exact handshake differs between TLS versions.

---

# 14. TLS 1.2

TLS 1.2 is a widely deployed TLS version.

It supports modern cryptographic algorithms and remains common in many environments.

However, where possible, modern systems should prefer TLS 1.3 when compatible.

---

# 15. TLS 1.3

TLS 1.3 is a newer TLS version designed to improve security and reduce handshake latency compared with older versions.

Important characteristics include:

* Reduced handshake latency
* Removal of older insecure cryptographic mechanisms
* Modern cipher suites
* Forward secrecy for normal TLS 1.3 key exchanges

---

# 16. HTTPS and TLS

HTTPS is HTTP transported over TLS.

```text
Application
    ↓
HTTP
    ↓
TLS
    ↓
TCP
    ↓
IP
```

Typical HTTPS traffic uses:

```text
TCP port 443
```

---

# 17. HTTP vs HTTPS

### HTTP

```text
Client
   ↓
HTTP
   ↓
Server
```

### HTTPS

```text
Client
   ↓
TLS
   ↓
Encrypted HTTP
   ↓
Server
```

---

# 18. TLS Certificate Validation

A client generally checks several things when validating a certificate.

### 1. Certificate signature

Is the certificate signed by a trusted issuer?

### 2. Certificate validity

Is the certificate currently within its validity period?

### 3. Hostname

Does the certificate cover the hostname being accessed?

For example:

```text
Requested hostname:
example.com

Certificate:
example.com
```

### 4. Trust chain

Can the certificate chain be traced to a trusted root?

---

# 19. Common TLS Problems

## Expired Certificate

```text
Certificate
     ↓
Expired ❌
```

Result:

```text
TLS certificate validation failure
```

---

## Wrong Hostname

The server may present a certificate for:

```text
api.example.com
```

while the client requests:

```text
www.example.com
```

If the certificate does not cover the requested hostname, validation can fail.

---

## Untrusted Certificate

The client may not trust the certificate issuer.

Possible causes:

* Self-signed certificate
* Missing intermediate certificate
* Unknown CA
* Incorrect trust store

---

## TLS Version Problem

Client and server may not share a compatible TLS version.

---

## Cipher Compatibility Problem

The client and server need compatible cryptographic parameters.

---

# 20. What is SNI?

**SNI** stands for **Server Name Indication**.

SNI allows a TLS client to indicate the hostname it wants during the TLS handshake.

This is important when multiple HTTPS websites share the same IP address.

Example:

```text
             Server
               |
      ┌────────┴────────┐
      ↓                 ↓
example.com       api.example.com
```

SNI helps the server select the appropriate certificate.

---

# 21. What is ALPN?

**ALPN** stands for **Application-Layer Protocol Negotiation**.

It allows the client and server to negotiate the application protocol used over TLS.

Examples:

```text
HTTP/1.1
HTTP/2
```

---

# 22. What is Forward Secrecy?

Forward secrecy means that compromise of a server's long-term private key should not allow an attacker to decrypt previously captured sessions, assuming appropriate ephemeral key exchange was used.

Modern TLS configurations commonly use ephemeral Diffie-Hellman key exchange mechanisms to provide this property.

---

# 23. What is a Self-Signed Certificate?

A self-signed certificate is signed by the same entity that created it rather than by a publicly trusted CA.

```text
Certificate
    ↓
Signed by itself
```

Self-signed certificates can be useful for:

* Development
* Testing
* Internal environments

But they are not automatically trusted by public browsers.

---

# 24. What is Let's Encrypt?

Let's Encrypt is a public Certificate Authority that provides automated TLS certificates.

It supports automated certificate issuance and renewal using the ACME protocol.

A common DevOps pattern is:

```text
Let's Encrypt
      ↓
TLS Certificate
      ↓
Nginx / Ingress
      ↓
HTTPS
```

---

# 25. TLS in Nginx

A typical HTTPS architecture:

```text
Internet
   ↓
Nginx :443
   ↓
TLS termination
   ↓
Application
```

Nginx can terminate TLS and forward HTTP or HTTPS traffic to an upstream application depending on the architecture.

---

# 26. TLS Termination

TLS termination means decrypting TLS traffic at a particular network component.

Example:

```text
Client
   ↓
HTTPS
   ↓
Load Balancer
   ↓
TLS Termination
   ↓
HTTP
   ↓
Backend
```

TLS can also be terminated at:

* Nginx
* Ingress Controller
* Load Balancer
* API Gateway
* Application

---

# 27. TLS Passthrough

In TLS passthrough, the intermediate proxy/load balancer forwards encrypted TLS traffic to the backend instead of terminating TLS there.

```text
Client
   ↓
HTTPS
   ↓
Proxy
   ↓
Encrypted TLS
   ↓
Backend
```

The backend performs TLS termination.

---

# 28. TLS Termination vs Passthrough

| TLS Termination              | TLS Passthrough                             |
| ---------------------------- | ------------------------------------------- |
| Proxy decrypts traffic       | Proxy keeps traffic encrypted               |
| Proxy can inspect HTTP       | Proxy cannot inspect encrypted HTTP content |
| Certificate usually at proxy | Certificate usually at backend              |
| Common with reverse proxies  | Useful when backend must handle TLS         |

---

# 29. OpenSSL

**OpenSSL** is a widely used open-source cryptographic toolkit.

It can be used to:

* Inspect certificates
* Test TLS connections
* Generate keys
* Generate CSRs
* Generate certificates for testing
* Troubleshoot TLS

---

# 30. Inspect a TLS Connection

```bash
openssl s_client -connect example.com:443
```

This can show information about:

* TLS version
* Certificate
* Certificate chain
* Cipher
* Handshake
* Connection details

---

# 31. Check Certificate Dates

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

Example:

```text
notBefore=...
notAfter=...
```

`notAfter` indicates when the certificate expires.

---

# 32. Check Certificate Issuer

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -issuer
```

---

# 33. Check Certificate Subject

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -subject
```

---

# 34. Check Certificate SAN

SAN means **Subject Alternative Name**.

Run:

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"
```

SANs specify the hostnames covered by the certificate.

---

# 35. Test HTTPS with curl

```bash
curl -v https://example.com
```

This helps inspect:

```text
DNS
TCP
TLS
HTTP
```

---

# 36. Verify TLS Version with curl

You can force a specific TLS version.

TLS 1.2:

```bash
curl --tlsv1.2 -I https://example.com
```

TLS 1.3:

```bash
curl --tlsv1.3 -I https://example.com
```

This can help troubleshoot TLS compatibility.

---

# 37. DevOps TLS Troubleshooting

When HTTPS fails, troubleshoot in layers.

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
7. Backend
```

Useful commands:

```bash
dig example.com
```

```bash
nc -vz example.com 443
```

```bash
openssl s_client -connect example.com:443
```

```bash
curl -v https://example.com
```

---

# 38. Kubernetes and TLS

TLS is commonly used with Kubernetes Ingress.

Example architecture:

```text
Internet
   ↓
HTTPS :443
   ↓
Ingress Controller
   ↓
TLS Termination
   ↓
Service
   ↓
Pod
```

A Kubernetes TLS Secret can store certificate material used by an Ingress.

Example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: tls-secret
type: kubernetes.io/tls
```

---

# 39. DevOps Real-World Example

Suppose a website is not opening:

```text
https://app.example.com
```

Start with DNS:

```bash
dig app.example.com
```

Then test TCP:

```bash
nc -vz app.example.com 443
```

Then TLS:

```bash
openssl s_client -connect app.example.com:443
```

Then HTTPS:

```bash
curl -v https://app.example.com
```

Then check the proxy/load balancer and backend.

---

# 40. Key Takeaways

Remember:

```text
SSL → Deprecated
TLS → Modern security protocol
HTTPS → HTTP over TLS
443 → Common HTTPS port
CA → Certificate Authority
Certificate → Identity + Public Key
Private Key → Must remain secret
TLS → Encryption + Integrity + Authentication
SNI → Hostname indication during TLS
ALPN → Application protocol negotiation
OpenSSL → TLS/certificate troubleshooting tool
```

---

# 🧠 Quick Revision

### What is TLS?

A protocol for securing network communication.

### What does TLS provide?

```text
Confidentiality
Integrity
Authentication
```

### What is HTTPS?

```text
HTTP + TLS
```

### What is a certificate?

A signed digital document that associates an identity such as a hostname with a public key.

### What is a CA?

An entity trusted to issue/sign certificates.

### What is TLS termination?

Decrypting TLS traffic at a network component such as a load balancer, reverse proxy, or ingress controller.

### Most important troubleshooting command?

```bash
openssl s_client -connect example.com:443
```

---

# 🎯 DevOps Mental Model

```text
                 HTTPS
                   │
                   ▼
              TCP :443
                   │
                   ▼
              TLS Handshake
                   │
          ┌────────┴────────┐
          │                 │
     Certificate       Key Establishment
          │                 │
          └────────┬────────┘
                   ▼
           Encrypted Session
                   │
                   ▼
             HTTP Request
                   │
                   ▼
          Proxy / Load Balancer
                   │
                   ▼
              Application
```

**Core idea:**

> TLS creates a secure channel; HTTPS uses that secure channel to carry HTTP traffic.
