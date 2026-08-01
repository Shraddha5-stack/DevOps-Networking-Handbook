# 🧪 Practical Lab – OSI Model

## 🎯 Objective

The objective of this lab is to understand how different Linux networking commands relate to the seven layers of the OSI Model and to troubleshoot network connectivity step by step.

---

# 📋 Lab Environment

- Operating System: Ubuntu Linux
- Internet Connection: Active
- User: Regular Linux User
- Required Tools:
  - ip
  - ping
  - ss
  - curl
  - nslookup or dig

---

# ✅ Task 1 – Check Physical Layer

## Command

```bash
ip link show
```

### Objective

Verify that the network interface is available and in the **UP** state.

### Expected Result

- Interface exists
- Interface status is `UP`

---

# ✅ Task 2 – Verify Data Link Layer

## Command

```bash
ip neigh
```

### Objective

View the ARP/Neighbor table.

### Expected Result

Display MAC addresses of nearby devices.

---

# ✅ Task 3 – Verify Network Layer

## Display IP Address

```bash
ip addr show
```

### Display Routing Table

```bash
ip route
```

### Test Connectivity

```bash
ping google.com
```

### Objective

Verify IP configuration, routing, and Internet connectivity.

### Expected Result

- Valid IP address
- Default gateway present
- Successful ping replies

---

# ✅ Task 4 – Verify Transport Layer

## Command

```bash
ss -tuln
```

### Objective

Display listening TCP and UDP ports.

### Expected Result

Ports such as SSH (22) or other active services are displayed.

---

# ✅ Task 5 – Verify Application Layer

## Command

```bash
curl -I https://google.com
```

### Objective

Send an HTTP request and verify that the web server responds.

### Expected Result

Response headers similar to:

```text
HTTP/2 200
```

or

```text
HTTP/1.1 301 Moved Permanently
```

---

# 📝 Observation Table

| Task | Command | Status |
|------|---------|--------|
| Physical Layer | `ip link show` | ✅ |
| Data Link Layer | `ip neigh` | ✅ |
| Network Layer | `ip addr show` | ✅ |
| Routing | `ip route` | ✅ |
| Connectivity | `ping google.com` | ✅ |
| Transport Layer | `ss -tuln` | ✅ |
| Application Layer | `curl -I https://google.com` | ✅ |

---

# 🌍 Real-World Scenario

Suppose a user reports that they cannot access a website.

A DevOps engineer can troubleshoot using the OSI Model:

1. Check the network interface (`ip link show`)
2. Verify MAC resolution (`ip neigh`)
3. Verify IP address (`ip addr show`)
4. Check routing (`ip route`)
5. Test connectivity (`ping`)
6. Verify open ports (`ss -tuln`)
7. Test the web service (`curl -I`)

This structured approach helps identify the exact layer where the issue occurs.

---

# 🎯 Lab Summary

In this lab, we verified multiple OSI layers using Linux networking commands.

We learned how to:

- Check network interfaces
- Verify MAC address resolution
- Inspect IP configuration
- Verify routing
- Test Internet connectivity
- Check listening ports
- Test web server responses

These practical steps are commonly used by Linux Administrators, Network Engineers, and DevOps Engineers to troubleshoot networking problems efficiently.

---

# ✅ Conclusion

The OSI Model provides a systematic way to troubleshoot networking issues.

By checking one layer at a time, engineers can quickly identify the root cause of a problem and resolve it effectively.
