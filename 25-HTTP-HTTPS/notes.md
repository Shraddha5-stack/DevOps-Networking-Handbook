# 🌐 Chapter 25 — HTTP & HTTPS

## 1. What is HTTP?

**HTTP (HyperText Transfer Protocol)** is an application-layer protocol used for communication between clients and servers.

It is commonly used to transfer:

* HTML pages
* JSON data
* Images
* CSS
* JavaScript
* API responses
* Files

A basic communication looks like:

```text
Client
  |
  | HTTP Request
  v
Server
  |
  | HTTP Response
  v
Client
```

Example:

```text
Browser → GET /index.html → Web Server
Browser ← 200 OK            ← Web Server
```

---

# 2. HTTP Client and Server

## Client

The client initiates communication.

Examples:

* Web browser
* `curl`
* Mobile application
* API client
* Monitoring system

## Server

The server receives requests and sends responses.

Examples:

* Nginx
* Apache
* Node.js
* Python application
* Java application
* Go application

Example:

```text
Client                         Server

Browser  --------------------> Nginx
         HTTP Request

Browser  <-------------------- Nginx
         HTTP Response
```

---

# 3. HTTP Request

An HTTP request contains information sent from the client to the server.

Example:

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: curl/8.5.0
Accept: */*
```

It contains:

1. Request method
2. URL/path
3. HTTP version
4. Headers
5. Optional body

---

# 4. HTTP Request Structure

General structure:

```text
Request Line
Headers
Blank Line
Body
```

Example:

```http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Shraddha"
}
```

---

# 5. HTTP Response

The server sends an HTTP response to the client.

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 615

<html>
...
</html>
```

A response contains:

1. Status line
2. Headers
3. Optional body

---

# 6. HTTP Response Structure

```text
Status Line
Headers
Blank Line
Body
```

Example:

```text
HTTP/1.1 200 OK
Content-Type: text/html

<html>
<body>
<h1>Hello</h1>
</body>
</html>
```

---

# 7. HTTP URL

A URL can contain:

```text
https://example.com:443/products?id=10
```

Parts:

```text
https     → Protocol
example.com → Host
443       → Port
/products → Path
?id=10    → Query parameter
```

---

# 8. HTTP Methods

HTTP methods tell the server what operation the client wants to perform.

## GET

Used to retrieve data.

```http
GET /users
```

Example:

```bash
curl https://example.com
```

---

## POST

Used to submit data or create a resource.

```http
POST /users
```

Example:

```bash
curl -X POST https://example.com/users
```

---

## PUT

Used to replace an existing resource.

```http
PUT /users/10
```

---

## PATCH

Used to partially modify a resource.

```http
PATCH /users/10
```

---

## DELETE

Used to delete a resource.

```http
DELETE /users/10
```

---

## HEAD

Similar to GET but normally returns headers without the response body.

```bash
curl -I https://example.com
```

Useful for checking:

* Status code
* Server
* Content-Type
* Cache headers
* Redirects

---

## OPTIONS

Used to determine which methods or communication options are supported.

```http
OPTIONS /api/users
```

It is also important in CORS-related requests.

---

# 9. Safe and Idempotent Methods

Some HTTP methods have important properties.

### Safe methods

Methods such as GET are intended not to modify the resource.

### Idempotent methods

An operation is idempotent when repeating the same request has the same intended effect as making it once.

Commonly considered idempotent:

```text
GET
HEAD
PUT
DELETE
OPTIONS
```

POST is generally not idempotent.

---

# 10. HTTP Status Codes

HTTP status codes tell the client what happened.

They are divided into five categories.

```text
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client Error
5xx → Server Error
```

---

# 11. 1xx Informational

Examples:

```text
100 Continue
101 Switching Protocols
```

These indicate that the request is being processed or communication is changing.

---

# 12. 2xx Success

## 200 OK

Request succeeded.

```text
GET /users → 200 OK
```

## 201 Created

A new resource was created.

Common with POST requests.

## 202 Accepted

Request has been accepted for processing but may not have completed yet.

## 204 No Content

Request succeeded but there is no response body.

---

# 13. 3xx Redirection

## 301 Moved Permanently

The resource has permanently moved.

## 302 Found

The resource is temporarily redirected.

## 304 Not Modified

The cached resource can be reused because it has not changed.

Example:

```text
Client → Request
Server → 304 Not Modified
Client → Uses cached copy
```

---

# 14. 4xx Client Errors

## 400 Bad Request

The request is invalid.

Possible causes:

* Invalid JSON
* Missing parameters
* Invalid syntax

## 401 Unauthorized

Authentication is required or credentials are invalid.

## 403 Forbidden

The server understood the request but refuses to allow it.

## 404 Not Found

The requested resource was not found.

## 405 Method Not Allowed

The resource exists but does not support the requested HTTP method.

## 408 Request Timeout

The server timed out waiting for the request.

## 409 Conflict

The request conflicts with the current state of the resource.

## 429 Too Many Requests

The client has sent too many requests in a given period.

Often associated with rate limiting.

---

# 15. 5xx Server Errors

## 500 Internal Server Error

A generic server-side failure.

## 501 Not Implemented

The server does not support the required functionality.

## 502 Bad Gateway

A gateway or proxy received an invalid response from an upstream server.

Example:

```text
Client
  ↓
Nginx
  ↓
Application
  X
```

## 503 Service Unavailable

The service is temporarily unavailable.

Possible causes:

* Application overloaded
* Application stopped
* Maintenance
* No healthy backend

## 504 Gateway Timeout

A gateway or proxy did not receive a timely response from the upstream server.

---

# 16. HTTP Headers

Headers provide additional information about the request or response.

Example:

```http
Content-Type: application/json
Authorization: Bearer TOKEN
User-Agent: curl/8.5.0
```

---

# 17. Important Request Headers

## Host

Identifies the target host.

```http
Host: example.com
```

## User-Agent

Identifies the client.

```http
User-Agent: curl/8.5.0
```

## Accept

Specifies the response formats the client can accept.

```http
Accept: application/json
```

## Authorization

Carries authentication credentials or tokens.

```http
Authorization: Bearer TOKEN
```

## Cookie

Sends cookies to the server.

```http
Cookie: session_id=abc123
```

---

# 18. Important Response Headers

## Content-Type

Specifies the media type.

```http
Content-Type: application/json
```

## Content-Length

Specifies the size of the response body.

## Set-Cookie

Instructs the client to store a cookie.

```http
Set-Cookie: session_id=abc123
```

## Location

Specifies a redirect destination.

```http
Location: https://example.com/login
```

## Cache-Control

Controls caching behavior.

Example:

```http
Cache-Control: no-cache
```

---

# 19. Content-Type

`Content-Type` tells the receiver what type of data is being transmitted.

Examples:

```text
text/html
application/json
text/plain
application/xml
multipart/form-data
application/x-www-form-urlencoded
```

Example:

```http
Content-Type: application/json
```

---

# 20. HTTP Cookies

Cookies are small pieces of data stored by a client and associated with a website.

Example:

```http
Set-Cookie: session_id=abc123
```

The client may later send:

```http
Cookie: session_id=abc123
```

Cookies can be used for:

* Sessions
* Preferences
* Authentication state
* Tracking

---

# 21. Important Cookie Attributes

## Secure

Cookie should only be sent over HTTPS.

## HttpOnly

Helps prevent client-side JavaScript from directly accessing the cookie.

## SameSite

Controls when cookies are sent with cross-site requests.

Example:

```text
SameSite=Strict
```

---

# 22. HTTP Session

HTTP itself is stateless.

This means each request can be handled independently.

Applications use mechanisms such as cookies and session identifiers to maintain state between requests.

Example:

```text
Login
  ↓
Server creates session
  ↓
Session ID sent to client
  ↓
Client sends session ID
  ↓
Server identifies session
```

---

# 23. What is HTTPS?

**HTTPS = HTTP + TLS**

HTTPS protects HTTP communication using TLS.

Instead of:

```text
HTTP
Client ───────── Server
```

HTTPS provides:

```text
HTTPS
Client ════════ Server
       TLS
```

---

# 24. Why HTTPS is Important

HTTPS provides important security properties:

### Confidentiality

Helps prevent unauthorized parties from reading traffic.

### Integrity

Helps detect modification of traffic.

### Authentication

TLS certificates help authenticate the server's identity.

---

# 25. HTTP vs HTTPS

| Feature                  | HTTP              | HTTPS         |
| ------------------------ | ----------------- | ------------- |
| Encryption               | No TLS            | TLS           |
| Typical port             | 80                | 443           |
| Confidentiality          | No                | Yes           |
| Integrity protection     | No TLS protection | Yes           |
| Certificate              | Not required      | Normally used |
| Secure web communication | No                | Yes           |

---

# 26. TLS

**TLS (Transport Layer Security)** is the security protocol used by HTTPS.

TLS helps establish a secure communication channel between client and server.

---

# 27. TLS Certificate

A TLS certificate helps prove the identity of a server.

A certificate can contain:

* Domain name
* Public key
* Certificate issuer
* Validity period
* Signature
* Certificate information

---

# 28. Certificate Authority

A **Certificate Authority (CA)** is a trusted organization that issues or signs certificates.

Examples include publicly trusted CAs and internal organizational CAs.

The client verifies the certificate chain against its trusted CA store.

---

# 29. Public and Private Keys

TLS uses asymmetric cryptography as part of the security process.

Conceptually:

```text
Public Key  → Can be shared
Private Key → Must remain secret
```

A server's private key must be protected.

Never commit production private keys to Git.

---

# 30. Simplified TLS Handshake

A simplified view:

```text
Client                         Server

   | -------- ClientHello ------> |
   |                              |
   | <------- ServerHello ------- |
   | <------- Certificate ------- |
   |                              |
   | ---- Key/Handshake Data ---> |
   |                              |
   | ===== Encrypted Traffic ==== |
```

Modern TLS negotiation is more detailed, but this gives the basic idea.

---

# 31. HTTP/1.1

HTTP/1.1 is widely supported and uses persistent TCP connections.

Example:

```text
Client
  |
TCP Connection
  |
HTTP Requests
  |
Server
```

It introduced mechanisms such as persistent connections and chunked transfer encoding.

---

# 32. HTTP/2

HTTP/2 improves HTTP communication using features such as:

* Binary framing
* Multiplexing
* Header compression
* Stream prioritization mechanisms

Multiple streams can share one TCP connection.

Conceptually:

```text
             TCP Connection
                   |
       +-----------+-----------+
       |           |           |
     Stream      Stream      Stream
       1           2           3
```

---

# 33. HTTP/3

HTTP/3 uses **QUIC**, which runs over UDP.

Conceptually:

```text
HTTP/3
   ↓
 QUIC
   ↓
 UDP
   ↓
 IP
```

HTTP/1.1 and HTTP/2 commonly use TCP, while HTTP/3 uses QUIC over UDP.

---

# 34. HTTP Version Comparison

| Version  | Transport | Major Feature                             |
| -------- | --------- | ----------------------------------------- |
| HTTP/1.1 | TCP       | Persistent connections                    |
| HTTP/2   | TCP       | Multiplexing                              |
| HTTP/3   | QUIC/UDP  | Modern transport with stream multiplexing |

---

# 35. HTTP Keep-Alive

Persistent connections allow multiple requests/responses to use the same TCP connection rather than creating a new connection for every request.

This can reduce connection overhead.

---

# 36. HTTP Caching

Caching stores responses so they can potentially be reused instead of requesting the resource again.

Important headers include:

```http
Cache-Control
ETag
Last-Modified
Expires
```

Example:

```text
Client → GET /image.png
Server → 200 + ETag

Later:

Client → GET /image.png + If-None-Match
Server → 304 Not Modified
```

---

# 37. HTTP Compression

Servers can compress responses to reduce data transfer.

Common compression algorithms include:

* gzip
* Brotli

The client can indicate supported encodings using:

```http
Accept-Encoding: gzip, br
```

---

# 38. HTTP Authentication

HTTP authentication is used to verify the identity of a client.

Common approaches include:

* Basic Authentication
* Bearer tokens
* API keys
* OAuth-based mechanisms
* Session cookies

Example:

```http
Authorization: Bearer <token>
```

Sensitive credentials should be protected and HTTPS should be used for authentication traffic.

---

# 39. CORS

**CORS (Cross-Origin Resource Sharing)** controls whether browsers allow web pages from one origin to access resources from another origin.

Important response headers include:

```http
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
```

---

# 40. Reverse Proxy and HTTP

A reverse proxy receives client requests and forwards them to backend services.

Example:

```text
Client
   |
   | HTTPS
   v
Nginx
   |
   | HTTP/HTTPS
   v
Application
```

A reverse proxy can provide:

* TLS termination
* Load balancing
* Routing
* Caching
* Security controls
* Compression

---

# 41. Load Balancer and HTTP

A load balancer distributes requests among backend servers.

```text
                 Client
                   |
                   v
             Load Balancer
              /     |     \
             v      v      v
          Server  Server  Server
```

This improves scalability and availability.

---

# 42. HTTP in Kubernetes

Kubernetes applications commonly expose HTTP services using:

```text
Pod
 ↓
Service
 ↓
Ingress
 ↓
Load Balancer
 ↓
Client
```

Example:

```text
Internet
   |
   v
Ingress
   |
   v
Service
   |
   v
Pod
```

---

# 43. HTTP in Docker

A container may run an HTTP server on port 80.

Example:

```bash
docker run -d -p 8080:80 nginx
```

Here:

```text
Host Port:      8080
Container Port: 80
```

Test:

```bash
curl http://localhost:8080
```

---

# 44. Useful HTTP Commands

Check response headers:

```bash
curl -I https://example.com
```

Verbose request:

```bash
curl -v https://example.com
```

Follow redirects:

```bash
curl -L http://example.com
```

Send GET request:

```bash
curl https://example.com
```

Send POST request:

```bash
curl -X POST https://example.com/api
```

Send JSON:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha"}' \
  https://example.com/api
```

---

# 45. Checking HTTP Status Code

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Example output:

```text
200
```

This is useful in scripts and monitoring.

---

# 46. Check Redirects

```bash
curl -I http://example.com
```

Look for:

```http
HTTP/1.1 301 Moved Permanently
Location: https://example.com/
```

Follow the redirect:

```bash
curl -IL http://example.com
```

---

# 47. Check TLS Certificate

Use:

```bash
openssl s_client -connect example.com:443
```

Useful information includes:

* Certificate
* TLS version
* Cipher
* Certificate chain
* Handshake information

---

# 48. Check Listening HTTP Ports

Use:

```bash
sudo ss -ltnp
```

Look for ports such as:

```text
:80
:443
:8080
:3000
```

---

# 49. Common HTTP Troubleshooting

## Problem: Connection refused

Possible causes:

* Service is not running
* Nothing is listening on the port
* Incorrect port
* Firewall behavior

Check:

```bash
sudo ss -ltnp
```

---

## Problem: 404

Possible causes:

* Incorrect URL
* Missing resource
* Incorrect application route
* Wrong reverse-proxy configuration

---

## Problem: 502

Possible causes:

* Upstream application unavailable
* Incorrect upstream address
* Backend connection failure
* Reverse proxy configuration issue

---

## Problem: 503

Possible causes:

* Backend unavailable
* No healthy backend
* Service overloaded
* Maintenance

---

## Problem: 504

Possible causes:

* Upstream timeout
* Slow backend
* Network problem
* Incorrect timeout configuration

---

# 50. DevOps Troubleshooting Flow

When an HTTP application is unavailable, troubleshoot from the lower layers upward:

```text
DNS
 ↓
IP Connectivity
 ↓
TCP Port
 ↓
TLS
 ↓
HTTP
 ↓
Reverse Proxy
 ↓
Application
 ↓
Database
```

Useful commands:

```bash
dig example.com
ping example.com
nc -vz example.com 443
curl -v https://example.com
openssl s_client -connect example.com:443
```

---

# 51. Real-World DevOps Architecture

A production web application may look like:

```text
                         Internet
                            |
                            v
                          DNS
                            |
                            v
                     Load Balancer
                            |
                            v
                    Reverse Proxy
                         Nginx
                            |
                     +------+------+
                     |             |
                     v             v
                 App Server    App Server
                     |             |
                     +------+------+
                            |
                            v
                         Database
```

HTTPS can terminate at the load balancer or reverse proxy, depending on the architecture.

---

# 52. Important Security Practices

For production HTTP/HTTPS services:

* Prefer HTTPS
* Protect private keys
* Keep certificates valid
* Use secure authentication
* Avoid exposing internal services unnecessarily
* Configure appropriate security headers
* Apply rate limiting where appropriate
* Monitor HTTP errors
* Keep web servers updated
* Do not expose secrets in URLs or logs unnecessarily

---

# 53. Important HTTP Security Headers

Examples include:

```http
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

These headers can help improve web application security when correctly configured.

---

# 54. HTTP vs TCP

HTTP operates at the application layer.

TCP provides reliable transport for HTTP/1.1 and HTTP/2.

Conceptually:

```text
HTTP
 ↓
TCP
 ↓
IP
 ↓
Ethernet / Wi-Fi
```

For HTTP/3:

```text
HTTP/3
 ↓
QUIC
 ↓
UDP
 ↓
IP
```

---

# 55. Key Things to Remember

```text
HTTP
→ Application-layer protocol

HTTP
→ Usually port 80

HTTPS
→ HTTP over TLS

HTTPS
→ Usually port 443

GET
→ Retrieve

POST
→ Create/submit

PUT
→ Replace

PATCH
→ Partial update

DELETE
→ Delete

2xx
→ Success

3xx
→ Redirect

4xx
→ Client-side/request problem

5xx
→ Server-side problem

HTTP/2
→ Multiplexing over TCP

HTTP/3
→ QUIC over UDP

curl
→ Essential HTTP troubleshooting tool
```

---

# 🎯 Chapter Summary

HTTP and HTTPS are essential technologies for DevOps engineers.

HTTP defines how clients and servers communicate at the application layer. HTTPS adds TLS protection to HTTP communication.

A DevOps engineer should be comfortable with:

```text
HTTP Methods
HTTP Status Codes
Headers
Cookies
Sessions
TLS
Certificates
DNS
TCP
Reverse Proxies
Load Balancers
Kubernetes Ingress
curl
openssl
HTTP Troubleshooting
```

The most important practical skill is understanding the complete request path:

```text
Client
 ↓
DNS
 ↓
Network
 ↓
TCP/QUIC
 ↓
TLS
 ↓
HTTP
 ↓
Load Balancer
 ↓
Reverse Proxy
 ↓
Application
 ↓
Database
```

This foundation is extremely useful when troubleshooting real production systems.
