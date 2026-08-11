# 🧪 Chapter 15 – Ports & Protocols Practical Lab

## Objective

In this lab, we will inspect listening ports, identify processes, test TCP connectivity, and verify HTTP/HTTPS services.

---

## Lab 1 — View Listening Ports

Run:

```bash
ss -tuln
```

### What this shows

* TCP listening sockets
* UDP listening sockets
* Local IP addresses
* Local port numbers

Record the output as **Screenshot 01**.

---

## Lab 2 — Identify Processes Using Ports

Run:

```bash
sudo ss -tulpn
```

This shows the process associated with listening sockets.

Look for services such as:

```text
ssh
systemd
docker-proxy
```

Record the output as **Screenshot 02**.

---

## Lab 3 — Find SSH Port

Run:

```bash
sudo ss -tulpn | grep :22
```

If SSH is running, you may see something similar to:

```text
LISTEN 0 128 0.0.0.0:22
```

Record the output as **Screenshot 03**.

If there is no output, SSH may not currently be listening on port 22.

---

## Lab 4 — Test a Local TCP Port

Test SSH:

```bash
nc -zv localhost 22
```

Possible successful output:

```text
Connection to localhost 22 port [tcp/ssh] succeeded!
```

If port 22 is not available, test another listening TCP port shown by:

```bash
ss -tuln
```

Record the successful test as **Screenshot 04**.

---

## Lab 5 — Test HTTPS Connectivity

Run:

```bash
nc -zv google.com 443
```

A successful result indicates that a TCP connection to Google's HTTPS port could be established.

Record the output as **Screenshot 05**.

---

## Lab 6 — Test HTTPS with curl

Run:

```bash
curl -I https://google.com
```

Look for an HTTP response such as:

```text
HTTP/2 200
```

or a redirect such as:

```text
HTTP/2 301
```

Record the output as **Screenshot 06**.

---

## Lab 7 — Detailed HTTPS Troubleshooting

Run:

```bash
curl -v https://google.com
```

Observe:

```text
DNS resolution
TCP connection
TLS handshake
Certificate information
HTTP request
HTTP response
```

Record the output as **Screenshot 07**.

---

## Lab 8 — Find a Process Using a Port

Run:

```bash
sudo lsof -i :22
```

If SSH is not running on port 22, replace `22` with another listening TCP port.

Example:

```bash
sudo lsof -i :8080
```

Record the output as **Screenshot 08**.

---

## Lab 9 — Check the Routing Path

Run:

```bash
ip route
```

Then:

```bash
ip route get 8.8.8.8
```

This helps identify:

* Default gateway
* Network interface
* Source IP
* Route used to reach the destination

Record the output as **Screenshot 09**.

---

# 🔍 Troubleshooting Exercise

Imagine an application is running on port `8080`, but users cannot access it.

Follow this sequence:

### 1. Is the application running?

```bash
sudo systemctl status <service>
```

### 2. Is port 8080 listening?

```bash
sudo ss -tulpn | grep :8080
```

### 3. Can the local machine connect?

```bash
nc -zv localhost 8080
```

### 4. Can a remote machine connect?

```bash
nc -zv <server-ip> 8080
```

### 5. Is the firewall blocking it?

```bash
sudo ufw status
```

### 6. Is routing correct?

```bash
ip route
```

### 7. Does the application respond?

```bash
curl -v http://localhost:8080
```

---

# 📸 Screenshot Checklist

Capture these **9 screenshots**:

```text
screenshots/
├── 01-ss-tuln.png
├── 02-ss-tulpn.png
├── 03-ssh-port-22.png
├── 04-nc-local-port.png
├── 05-nc-google-443.png
├── 06-curl-google-headers.png
├── 07-curl-google-verbose.png
├── 08-lsof-port.png
└── 09-ip-route.png
```

### Important

Don't worry if your output is different from the examples.

Your actual Ubuntu system output is what we want to document. Different services may be listening on your machine, especially because you use Docker.

---

# 🎯 Expected Learning

After completing this lab, you should be able to:

* Identify listening ports.
* Identify processes using ports.
* Test TCP connectivity.
* Test HTTPS connectivity.
* Understand port 22, 443, and other common ports.
* Use `ss`, `nc`, `curl`, and `lsof`.
* Perform basic port troubleshooting.
* Understand how ports fit into DevOps infrastructure.
