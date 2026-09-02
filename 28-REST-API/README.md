# 🌐 Chapter 28 — REST API

## 📚 Overview

REST API (Representational State Transfer Application Programming Interface) is an architectural style for building web services that communicate over HTTP.

REST APIs allow clients and servers to exchange data using standard HTTP methods such as:

* GET
* POST
* PUT
* PATCH
* DELETE

REST APIs are widely used in web applications, microservices, cloud platforms, DevOps tools, and automation.

---

## 🎯 Objectives

In this chapter, I will learn:

* What REST API is
* What an API is
* REST principles
* Client-server architecture
* HTTP methods
* HTTP status codes
* Resources and endpoints
* Request and response
* Headers
* Query parameters
* Path parameters
* JSON
* Authentication and authorization
* CRUD operations
* REST API testing
* `curl`
* REST APIs in DevOps
* REST APIs with Docker and Kubernetes
* API troubleshooting

---

## 🔄 Basic REST API Architecture

```text
Client
   │
   │ HTTP Request
   ▼
REST API
   │
   │
   ▼
Application
   │
   ▼
Database
```

The client sends a request to the API, and the server processes the request and returns a response.

---

## 🌍 Example

A client may request:

```text
GET /users/101
```

The server could return:

```json
{
  "id": 101,
  "name": "Shraddha"
}
```

---

## 🧩 Common HTTP Methods

| Method | Purpose                     |
| ------ | --------------------------- |
| GET    | Retrieve data               |
| POST   | Create a resource           |
| PUT    | Replace a resource          |
| PATCH  | Partially update a resource |
| DELETE | Delete a resource           |

---

## 📦 REST Resources

REST APIs represent data as resources.

Examples:

```text
/users
/products
/orders
/books
/servers
```

A specific resource can be identified using an ID:

```text
/users/101
/products/500
/orders/2001
```

---

## 🏗️ CRUD Operations

REST APIs commonly implement CRUD:

```text
Create → POST
Read   → GET
Update → PUT / PATCH
Delete → DELETE
```

Example:

```text
POST   /users
GET    /users
GET    /users/101
PUT    /users/101
PATCH  /users/101
DELETE /users/101
```

---

## 📤 HTTP Request

A request can contain:

```text
Method
URL
Headers
Body
```

Example:

```http
POST /users HTTP/1.1
Content-Type: application/json

{
  "name": "Shraddha"
}
```

---

## 📥 HTTP Response

A response commonly contains:

```text
Status Code
Headers
Body
```

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 101,
  "name": "Shraddha"
}
```

---

## 🔢 Important Status Codes

### 2xx — Success

```text
200 OK
201 Created
202 Accepted
204 No Content
```

### 4xx — Client Error

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
429 Too Many Requests
```

### 5xx — Server Error

```text
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

---

## 🔍 Query Parameters

Query parameters are commonly used for filtering, searching, or pagination.

Example:

```text
/users?city=pune
```

Multiple parameters:

```text
/users?city=pune&limit=10
```

---

## 🎯 Path Parameters

A path parameter identifies a specific resource.

Example:

```text
/users/101
```

Here:

```text
101
```

identifies the user.

---

## 🧾 JSON

JSON is commonly used for REST API request and response bodies.

Example:

```json
{
  "name": "Shraddha",
  "role": "DevOps Engineer",
  "skills": [
    "Linux",
    "Docker",
    "Kubernetes",
    "AWS"
  ]
}
```

---

## 🔐 API Authentication

REST APIs may use authentication mechanisms such as:

* API keys
* Basic authentication
* Bearer tokens
* OAuth
* JWT

Example:

```http
Authorization: Bearer <token>
```

Authentication verifies identity.

Authorization determines what the authenticated user is allowed to do.

---

## 🔒 HTTPS

REST APIs should normally use HTTPS in production.

```text
HTTP
 ↓
TCP
```

Secure API communication:

```text
HTTPS
 ↓
TLS
 ↓
TCP
```

---

## 🧪 API Testing

REST APIs can be tested using:

```text
curl
Postman
Browser
Python
JavaScript
CI/CD pipelines
```

Example:

```bash
curl https://api.example.com/users
```

---

## 🛠️ REST API and DevOps

REST APIs are extremely important in DevOps.

DevOps engineers interact with APIs to automate:

* Cloud resources
* Kubernetes
* CI/CD systems
* Monitoring systems
* Infrastructure
* Deployment platforms
* Configuration management
* Ticketing systems

---

## ☁️ Cloud APIs

Cloud platforms expose APIs for managing infrastructure.

Conceptually:

```text
DevOps Engineer
       │
       ▼
   API Request
       │
       ▼
Cloud Platform
       │
       ▼
Infrastructure
```

---

## ☸️ Kubernetes API

Kubernetes itself exposes an API.

A simplified architecture:

```text
kubectl
   │
   │ API Request
   ▼
Kubernetes API Server
   │
   ├── Scheduler
   ├── Controllers
   └── etcd
```

For example:

```bash
kubectl get pods
```

ultimately interacts with the Kubernetes control plane through its API.

---

## 🐳 Docker API

Docker also provides an API that tools can use to communicate with the Docker daemon.

Conceptually:

```text
Client
  │
  ▼
Docker API
  │
  ▼
Docker Daemon
  │
  ▼
Containers
```

---

## 🔄 REST API in CI/CD

CI/CD systems can use REST APIs to:

```text
Trigger builds
Create deployments
Check build status
Retrieve artifacts
Manage pipelines
```

Example:

```text
Git Push
   ↓
CI/CD API
   ↓
Pipeline
   ↓
Build
   ↓
Test
   ↓
Deploy
```

---

## 📊 REST API Monitoring

Important API metrics include:

* Request count
* Response time
* Error rate
* Status code distribution
* Throughput
* CPU usage
* Memory usage
* Availability

---

## 🚨 REST API Troubleshooting

A systematic approach:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP Request
 ↓
Authentication
 ↓
Authorization
 ↓
Application
 ↓
Database
```

Useful commands:

```bash
curl -v https://example.com
```

```bash
curl -I https://example.com
```

```bash
dig example.com
```

```bash
nc -vz example.com 443
```

---

## 🧠 REST Principles

Important REST concepts include:

### Client-Server

Client and server have separate responsibilities.

### Statelessness

Each request should contain the information necessary for the server to process it. The server does not rely on stored client session state as a requirement for understanding the request.

### Cacheability

Responses may be cacheable when appropriate.

### Uniform Interface

Resources and operations follow consistent conventions.

### Layered System

A client does not necessarily know whether it is communicating directly with the final server or through intermediary layers.

---

## 🏗️ REST API Example

```text
Client
  │
  │ GET /users/101
  ▼
Load Balancer
  │
  ▼
API Server
  │
  ▼
Application
  │
  ▼
Database
  │
  ▼
JSON Response
```

---

## 📂 Chapter Contents

```text
28-REST-API/
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

---

## 🎓 Expected Outcome

After completing this chapter, I should be able to:

* Explain REST APIs
* Explain REST principles
* Understand HTTP methods
* Understand CRUD
* Understand API endpoints
* Understand requests and responses
* Read JSON
* Understand HTTP status codes
* Test APIs using `curl`
* Understand authentication
* Understand REST APIs in DevOps
* Understand Kubernetes APIs
* Troubleshoot API connectivity

---

## 🏆 Goal

> Understand how REST APIs enable clients, applications, cloud platforms, and DevOps tools to communicate using standard HTTP-based interfaces.
