# 🛠️ Troubleshooting – OSI Model

The OSI Model provides a structured approach to diagnosing and resolving networking issues. Instead of guessing, engineers troubleshoot one layer at a time until they find the root cause.

---

# 📋 OSI Layer Troubleshooting Flow

```
Application
      ▲
Presentation
      ▲
Session
      ▲
Transport
      ▲
Network
      ▲
Data Link
      ▲
Physical
```

Always start from the lowest layer and move upward, or start from the symptom and work downward.

---

# 1️⃣ Physical Layer Problems (Layer 1)

## Common Issues

- Ethernet cable unplugged
- Damaged cable
- Faulty network adapter
- Wi-Fi disabled
- Switch or router powered off

### Commands

```bash
ip link show
```

### Checks

- Is the interface **UP**?
- Is the cable connected?
- Is Wi-Fi enabled?

### Solution

- Reconnect the cable.
- Enable the interface.
- Restart the switch or router.
- Replace faulty hardware if needed.

---

# 2️⃣ Data Link Layer Problems (Layer 2)

## Common Issues

- Incorrect MAC address learning
- Duplicate MAC addresses
- VLAN misconfiguration
- Switch port disabled

### Commands

```bash
ip neigh
ip link show
```

### Checks

- Is the MAC address resolved?
- Is the switch port active?

### Solution

- Verify switch configuration.
- Check VLAN assignments.
- Clear stale ARP entries if necessary.

---

# 3️⃣ Network Layer Problems (Layer 3)

## Common Issues

- Wrong IP address
- Incorrect subnet mask
- Missing default gateway
- Routing issues

### Commands

```bash
ip addr show
ip route
ping google.com
```

### Checks

- Is the IP address correct?
- Is the default gateway configured?
- Can you reach another host?

### Solution

- Assign the correct IP address.
- Configure the correct gateway.
- Update routing if needed.

---

# 4️⃣ Transport Layer Problems (Layer 4)

## Common Issues

- Closed ports
- Firewall blocking traffic
- Service not listening
- TCP connection timeout

### Commands

```bash
ss -tuln
```

### Checks

- Is the required port listening?
- Is the firewall allowing traffic?

### Solution

- Start the service.
- Open the required port.
- Update firewall rules.

---

# 5️⃣ Session Layer Problems (Layer 5)

## Common Issues

- Session timeout
- Authentication failure
- Unexpected session termination

### Checks

- Verify session settings.
- Check authentication logs.

### Solution

- Re-establish the session.
- Review timeout configuration.

---

# 6️⃣ Presentation Layer Problems (Layer 6)

## Common Issues

- SSL/TLS certificate expired
- Encryption mismatch
- Unsupported data format

### Commands

```bash
curl -I https://example.com
```

### Checks

- Is the SSL certificate valid?
- Is encryption configured correctly?

### Solution

- Renew the certificate.
- Correct TLS configuration.
- Verify supported protocols.

---

# 7️⃣ Application Layer Problems (Layer 7)

## Common Issues

- Website not loading
- DNS resolution failure
- Web server stopped
- Application crash

### Commands

```bash
curl -I https://google.com
nslookup google.com
```

### Checks

- Is DNS working?
- Is the application running?
- Is the web server responding?

### Solution

- Restart the application.
- Fix DNS configuration.
- Review application logs.

---

# 🧰 Quick Troubleshooting Checklist

| Problem | Check |
|----------|-------|
| No network connection | `ip link show` |
| Cannot reach another device | `ping` |
| Wrong IP address | `ip addr show` |
| Routing issue | `ip route` |
| MAC address issue | `ip neigh` |
| Port not responding | `ss -tuln` |
| Website not loading | `curl -I` |
| DNS problem | `nslookup` / `dig` |

---

# ☁️ DevOps Troubleshooting Example

### Problem

A web application hosted on an EC2 instance is unreachable.

### Investigation

1. Check the EC2 network interface.
2. Verify the instance has the correct IP address.
3. Confirm the route table and Internet Gateway.
4. Verify that ports **80** and **443** are open.
5. Check that Nginx or Apache is running.
6. Test the application using `curl`.

This method follows the OSI Model from lower layers to higher layers.

---

# 💡 Best Practices

- Troubleshoot one layer at a time.
- Verify the simplest issues first.
- Use Linux networking commands to confirm observations.
- Don't assume the problem is at the application layer.
- Record findings and the solution for future reference.

---

# ✅ Summary

The OSI Model is one of the most effective frameworks for troubleshooting network problems.

By understanding the responsibility of each layer, engineers can quickly isolate faults, reduce downtime, and resolve issues more efficiently.

This structured approach is widely used in Linux administration, cloud computing, networking, cybersecurity, and DevOps.
