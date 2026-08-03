# 🛠️ TCP vs UDP Troubleshooting Guide

## 📖 Introduction

Network connectivity issues are common in Linux, cloud, and DevOps environments. Understanding how to troubleshoot TCP and UDP communication helps identify problems related to services, ports, firewalls, DNS, routing, and applications.

This guide covers common issues, possible causes, and practical troubleshooting commands.

---

# 🚨 Issue 1: Application Is Not Accessible

## Symptoms

- Website is not loading.
- API requests fail.
- SSH connection is refused.

## Possible Causes

- Service is stopped.
- Wrong port configured.
- Firewall is blocking the port.
- Application crashed.

## Troubleshooting Commands

```bash
ss -tuln
```

```bash
systemctl status <service-name>
```

```bash
sudo ufw status
```

---

# 🚨 Issue 2: Port Is Closed

## Symptoms

- Connection refused.
- Timeout while connecting.

## Troubleshooting Commands

```bash
nc -zv localhost 80
```

```bash
nc -zv google.com 443
```

```bash
netstat -tuln
```

---

# 🚨 Issue 3: DNS Resolution Fails

## Symptoms

- Unable to access websites using domain names.
- IP address works, but hostname does not.

## Troubleshooting Commands

```bash
nslookup google.com
```

```bash
dig google.com
```

```bash
ping google.com
```

---

# 🚨 Issue 4: High Network Latency

## Symptoms

- Slow website loading.
- Delayed SSH sessions.
- Poor application performance.

## Troubleshooting Commands

```bash
ping google.com
```

```bash
traceroute google.com
```

---

# 🚨 Issue 5: HTTP/HTTPS Service Not Responding

## Symptoms

- Browser displays 404, 500, or timeout errors.

## Troubleshooting Commands

```bash
curl -I https://google.com
```

```bash
curl http://localhost
```

---

# 🚨 Issue 6: Firewall Blocking Traffic

## Symptoms

- Service is running but cannot be accessed.

## Troubleshooting Commands

```bash
sudo ufw status
```

```bash
sudo iptables -L
```

---

# 🚨 Issue 7: SSH Connection Refused

## Symptoms

```text
ssh: connect to host <ip> port 22: Connection refused
```

## Troubleshooting Commands

```bash
sudo systemctl status ssh
```

```bash
ss -tuln
```

```bash
sudo ufw status
```

---

# 📋 Useful Troubleshooting Commands

| Command | Purpose |
|---------|---------|
| `ss -tuln` | Show listening TCP/UDP ports |
| `ss -tan` | Show TCP connections |
| `ss -uan` | Show UDP sockets |
| `netstat -tuln` | Display listening ports |
| `nc -zv host port` | Test port connectivity |
| `curl -I URL` | Retrieve HTTP response headers |
| `ping host` | Test connectivity |
| `traceroute host` | Trace packet path |
| `nslookup domain` | Resolve DNS |
| `dig domain` | Detailed DNS lookup |
| `systemctl status service` | Check service status |
| `sudo ufw status` | Check firewall rules |

---

# ☁️ DevOps Troubleshooting Scenario

### Problem

A web application deployed on a Linux server is not accessible.

### Troubleshooting Steps

1. Verify the application is running.

```bash
systemctl status nginx
```

2. Check if port 80 or 443 is listening.

```bash
ss -tuln
```

3. Verify firewall rules.

```bash
sudo ufw status
```

4. Test the application locally.

```bash
curl http://localhost
```

5. Test connectivity from another machine.

```bash
nc -zv <server-ip> 80
```

6. Check DNS resolution.

```bash
nslookup example.com
```

---

# 💡 Best Practices

- Verify the service is running before troubleshooting the network.
- Confirm the correct port is open and listening.
- Test connectivity locally before testing remotely.
- Check firewall and security group rules.
- Use `ss` instead of `netstat` on modern Linux systems.
- Verify DNS before assuming the application is down.
- Monitor logs for application-specific errors.

---

# 📝 Summary

Troubleshooting TCP and UDP issues requires a systematic approach. By checking services, ports, DNS, routing, and firewall settings, engineers can quickly identify and resolve most network connectivity problems. Mastering these commands and techniques is an essential skill for Linux Administrators, DevOps Engineers, Cloud Engineers, and SREs.
