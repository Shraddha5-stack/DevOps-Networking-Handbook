# 🧪 Chapter 23 – Proxy and Reverse Proxy Practical Lab

## 🎯 Objective

In this lab, we will build a simple **Nginx reverse proxy** that receives requests on port `8080` and forwards them to a backend application running on port `3000`.

### Architecture

```text
Client
   |
   | http://localhost:8080
   v
Nginx Reverse Proxy
   |
   | http://127.0.0.1:3000
   v
Backend Application
```

---

# Lab 1 — Check Current Proxy Configuration

## Step 1: Check proxy environment variables

Run:

```bash
env | grep -i proxy
```

Also check:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

### Observation

If nothing is displayed, those proxy variables are not configured in the current shell.

---

# Lab 2 — Test Internet Connectivity

Run:

```bash
curl -I https://example.com
```

Expected:

```text
HTTP/2 200
```

Now run:

```bash
curl -v https://example.com
```

### Observe

Look for:

```text
Host resolved
TCP connection
TLS handshake
HTTP request
HTTP response
```

This helps understand the complete request flow.

---

# Lab 3 — Check Listening Ports

Run:

```bash
sudo ss -ltnp
```

Look for applications listening on ports such as:

```text
80
443
8080
3000
```

You can filter the output:

```bash
sudo ss -ltnp | grep -E ':80|:443|:8080|:3000'
```

---

# Lab 4 — Create a Backend Server

For this lab, we can use Python's built-in HTTP server.

Create a directory:

```bash
mkdir -p ~/proxy-lab/backend
```

Enter the directory:

```bash
cd ~/proxy-lab/backend
```

Create a simple HTML page:

```bash
cat > index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Backend Server</title>
</head>
<body>
    <h1>Hello from Backend Server!</h1>
    <p>This response came from the backend application.</p>
</body>
</html>
EOF
```

---

# Lab 5 — Start the Backend

From the backend directory, run:

```bash
python3 -m http.server 3000
```

You should see something similar to:

```text
Serving HTTP on 0.0.0.0 port 3000
```

Keep this terminal running.

---

# Lab 6 — Test the Backend Directly

Open another terminal.

Run:

```bash
curl http://127.0.0.1:3000
```

You should see:

```html
<h1>Hello from Backend Server!</h1>
```

### Important

At this point:

```text
Client
   |
   v
Backend :3000
```

There is no reverse proxy yet.

---

# Lab 7 — Install Nginx

Check whether Nginx is installed:

```bash
nginx -v
```

If it is not installed:

```bash
sudo apt update
sudo apt install nginx -y
```

Check the service:

```bash
sudo systemctl status nginx
```

---

# Lab 8 — Create Reverse Proxy Configuration

Create a configuration file:

```bash
sudo nano /etc/nginx/sites-available/proxy-lab
```

Add:

```nginx
server {
    listen 8080;

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Save the file.

---

# Lab 9 — Enable the Configuration

Create a symbolic link:

```bash
sudo ln -s /etc/nginx/sites-available/proxy-lab /etc/nginx/sites-enabled/proxy-lab
```

Test the configuration:

```bash
sudo nginx -t
```

Expected:

```text
syntax is ok
test is successful
```

---

# Lab 10 — Reload Nginx

Run:

```bash
sudo systemctl reload nginx
```

Check that Nginx is listening:

```bash
sudo ss -ltnp | grep ':8080'
```

Expected:

```text
LISTEN ... :8080
```

---

# Lab 11 — Test the Reverse Proxy

Run:

```bash
curl http://127.0.0.1:8080
```

You should receive the backend page:

```html
<h1>Hello from Backend Server!</h1>
```

### What happened?

The request went through:

```text
curl
  |
  | :8080
  v
Nginx
  |
  | :3000
  v
Python Backend
```

This confirms that Nginx is functioning as a reverse proxy.

---

# Lab 12 — Compare Direct vs Proxy Access

Test the backend directly:

```bash
curl http://127.0.0.1:3000
```

Then test through Nginx:

```bash
curl http://127.0.0.1:8080
```

Both should return the same application content.

### Difference

Direct:

```text
Client → Backend
```

Reverse proxy:

```text
Client → Nginx → Backend
```

---

# Lab 13 — Test with Verbose curl

Run:

```bash
curl -v http://127.0.0.1:8080
```

Observe:

```text
> GET / HTTP/1.1
> Host: 127.0.0.1:8080
```

and the response:

```text
< HTTP/1.1 200 OK
```

This confirms that the request successfully passed through the reverse proxy.

---

# Lab 14 — Check Nginx Access Logs

Run:

```bash
sudo tail -f /var/log/nginx/access.log
```

In another terminal:

```bash
curl http://127.0.0.1:8080
```

You should see a new request in the access log.

Stop log monitoring:

```text
Ctrl + C
```

---

# Lab 15 — Check Nginx Error Logs

Run:

```bash
sudo tail -f /var/log/nginx/error.log
```

If there are no errors, the reverse proxy is operating normally.

---

# Lab 16 — Test Backend Failure

This is an important troubleshooting exercise.

Stop the Python backend with:

```text
Ctrl + C
```

Now test:

```bash
curl -v http://127.0.0.1:8080
```

You may receive:

```text
502 Bad Gateway
```

### Why?

Nginx is running, but the backend on port `3000` is unavailable.

```text
Client
   |
   v
Nginx :8080
   |
   X
Backend :3000
```

Check the error log:

```bash
sudo tail -n 20 /var/log/nginx/error.log
```

---

# Lab 17 — Start Backend Again

Return to the backend directory:

```bash
cd ~/proxy-lab/backend
```

Start the server:

```bash
python3 -m http.server 3000
```

Test again from another terminal:

```bash
curl http://127.0.0.1:8080
```

The request should work again.

---

# Lab 18 — Check Nginx Process

Run:

```bash
ps aux | grep nginx
```

You should see the Nginx master and worker processes.

---

# Lab 19 — Check Which Process Uses Port 8080

Run:

```bash
sudo ss -ltnp | grep ':8080'
```

Or:

```bash
sudo lsof -i :8080
```

You should see Nginx associated with the port.

---

# Lab 20 — Test Proxy Headers

Run:

```bash
curl -v http://127.0.0.1:8080
```

The Nginx configuration forwards headers such as:

```text
Host
X-Real-IP
X-Forwarded-For
X-Forwarded-Proto
```

These headers are commonly used when applications need information about the original client request.

---

# Lab 21 — Troubleshooting Exercise

If the reverse proxy does not work, follow this sequence.

### Check backend

```bash
curl http://127.0.0.1:3000
```

### Check backend port

```bash
sudo ss -ltnp | grep ':3000'
```

### Check Nginx

```bash
sudo systemctl status nginx
```

### Check Nginx port

```bash
sudo ss -ltnp | grep ':8080'
```

### Validate configuration

```bash
sudo nginx -t
```

### Check errors

```bash
sudo tail -n 30 /var/log/nginx/error.log
```

### Test proxy

```bash
curl -v http://127.0.0.1:8080
```

---

# Lab 22 — Request Flow

After completing the lab, understand this complete flow:

```text
                 HTTP Request
Client
   |
   | localhost:8080
   v
+-------------------+
|       Nginx       |
|  Reverse Proxy    |
+-------------------+
          |
          | proxy_pass
          v
+-------------------+
| Python Backend    |
|      :3000        |
+-------------------+
          |
          v
      HTTP Response
          |
          v
        Client
```

---

# Lab 23 — Important Observations

Record your observations after completing the lab.

### Backend Port

```text
Backend: 3000
```

### Reverse Proxy Port

```text
Nginx: 8080
```

### Direct Request

```text
http://127.0.0.1:3000
```

### Proxy Request

```text
http://127.0.0.1:8080
```

### Successful Status

```text
HTTP 200 OK
```

### Backend Failure

```text
HTTP 502 Bad Gateway
```

---

# Lab 24 — Cleanup

After completing the lab, stop the Python server with:

```text
Ctrl + C
```

Disable the Nginx lab configuration:

```bash
sudo rm /etc/nginx/sites-enabled/proxy-lab
```

Test Nginx:

```bash
sudo nginx -t
```

Reload:

```bash
sudo systemctl reload nginx
```

Optionally remove the configuration:

```bash
sudo rm /etc/nginx/sites-available/proxy-lab
```

Remove the lab directory:

```bash
rm -rf ~/proxy-lab
```

---

# 🎯 Final Lab Summary

We successfully practiced:

* Checking proxy environment variables
* Testing network connectivity with `curl`
* Creating a backend server
* Running a Python HTTP server
* Installing and configuring Nginx
* Creating a reverse proxy
* Forwarding traffic with `proxy_pass`
* Testing proxy responses
* Checking Nginx logs
* Troubleshooting backend failures
* Understanding `502 Bad Gateway`

## Final Architecture

```text
                    Client
                      |
                      | :8080
                      v
               +-------------+
               |    Nginx    |
               |    Proxy    |
               +-------------+
                      |
                      | :3000
                      v
               +-------------+
               |   Backend   |
               |   Python    |
               +-------------+
```

### Key Lesson

A **reverse proxy does not replace the backend application**.

It sits in front of the backend and controls how client requests reach it.

```text
Reverse Proxy
      ↓
Receives request
      ↓
Selects/forwards to backend
      ↓
Receives response
      ↓
Returns response to client
```
