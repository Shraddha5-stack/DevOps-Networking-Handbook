# 🔐 Chapter 26 — SSL/TLS

## 📚 Overview

SSL/TLS is used to secure communication between clients and servers over a network.

In modern systems, **TLS (Transport Layer Security)** is the standard technology used to protect HTTPS communication. SSL is the older predecessor and is no longer considered secure for modern deployments.

---

## 🎯 Objectives

In this chapter, I will learn:

* What SSL is
* What TLS is
* SSL vs TLS
* Why TLS is required
* TLS handshake
* Encryption
* Authentication
* Digital certificates
* Certificate Authorities
* Public and private keys
* Symmetric and asymmetric encryption
* Certificate chain
* TLS versions
* HTTPS and TLS
* TLS troubleshooting
* OpenSSL commands
* Real-world DevOps use cases

---

## 🏗️ TLS Communication

```text
Client
   │
   │ TLS Handshake
   ▼
Server
   │
   │ Secure encrypted connection
   ▼
HTTPS Application
```

---

## 🔑 Important Concepts

| Concept       | Meaning                          |
| ------------- | -------------------------------- |
| SSL           | Older security protocol          |
| TLS           | Modern successor to SSL          |
| Certificate   | Proves server identity           |
| CA            | Certificate Authority            |
| Public Key    | Can be shared                    |
| Private Key   | Must remain secret               |
| TLS Handshake | Establishes secure communication |
| HTTPS         | HTTP protected by TLS            |
| Encryption    | Protects confidentiality         |

---

## 🌐 HTTPS Flow

```text
Browser
   │
   │ HTTPS Request
   ▼
TCP :443
   │
   ▼
TLS Handshake
   │
   ▼
Certificate Validation
   │
   ▼
Encrypted HTTP
   │
   ▼
Web Server
```

---

## 🛠️ Important Commands

Inspect a TLS connection:

```bash
openssl s_client -connect example.com:443
```

Check certificate dates:

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

Test HTTPS:

```bash
curl -v https://example.com
```

Check port 443:

```bash
nc -vz example.com 443
```

---

## ☁️ DevOps Relevance

SSL/TLS is commonly used with:

* Web servers
* Reverse proxies
* Load balancers
* Kubernetes Ingress
* API gateways
* AWS services
* CI/CD systems
* Monitoring systems
* Internal services
* Service-to-service communication

---

## 🎓 Expected Outcome

After completing this chapter, I should be able to:

* Explain TLS clearly
* Explain the TLS handshake
* Understand certificates
* Explain public/private keys
* Troubleshoot HTTPS
* Inspect certificates using OpenSSL
* Understand certificate chains
* Explain TLS in Kubernetes and cloud environments

---

## 📂 Chapter Contents

```text
26-SSL-TLS/
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

---

## 🔗 Related Chapters

* Chapter 16 — HTTP/HTTPS
* Chapter 25 — HTTP/HTTPS
* Chapter 26 — SSL/TLS
* Chapter 34 — Network Security

---

## 🏆 Goal

> Understand how TLS protects network communication and become confident troubleshooting HTTPS and certificates as a DevOps engineer.
