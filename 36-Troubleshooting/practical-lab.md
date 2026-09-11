# Chapter 36 — Troubleshooting — Practical Lab

This practical lab teaches troubleshooting through real failure scenarios.

The goal is not just to run commands.

The goal is to:

```text
Observe
   ↓
Collect evidence
   ↓
Identify the layer
   ↓
Form a hypothesis
   ↓
Test
   ↓
Fix
   ↓
Verify
   ↓
Document
```

---

# Lab 1 — System Baseline

Before troubleshooting, collect basic information.

Run:

```bash
hostname
whoami
date
uname -a
cat /etc/os-release
```

### Task

Record:

* Hostname
* Username
* Linux distribution
* Kernel version
* Date/time

---

# Lab 2 — Network Interface Investigation

Run:

```bash
ip addr
```

Then:

```bash
ip -brief addr
```

Then:

```bash
ip link
```

### Questions

1. What is your active network interface?
2. What is its IP address?
3. Is the interface UP?
4. Is loopback available?

Check:

```bash
ip link show lo
```

---

# Lab 3 — Network Statistics

Run:

```bash
ip -s link
```

Identify:

```text
RX packets
RX errors
RX dropped
TX packets
TX errors
TX dropped
```

### Task

Write down the current RX/TX statistics.

Then run:

```bash
watch -n 2 'ip -s link'
```

Generate some traffic in another terminal:

```bash
ping -c 20 8.8.8.8
```

Observe whether the statistics change.

Stop `watch` with:

```text
Ctrl+C
```

---

# Lab 4 — Routing Investigation

Run:

```bash
ip route
```

Find:

```text
Default gateway
Network interface
Local network
```

Then:

```bash
ip route | grep default
```

Finally:

```bash
ip route get 8.8.8.8
```

### Questions

1. What is your default gateway?
2. Which interface will be used for `8.8.8.8`?
3. What source IP will Linux use?

---

# Lab 5 — DNS Investigation

Check DNS resolution:

```bash
dig example.com
```

Then:

```bash
dig +short example.com
```

Check another DNS server:

```bash
dig @8.8.8.8 example.com
```

And:

```bash
dig @1.1.1.1 example.com
```

### Questions

1. Does DNS resolve?
2. What IP address is returned?
3. How long did the DNS query take?
4. Do the DNS servers return the same result?

---

# Lab 6 — DNS Failure Simulation

Try resolving a deliberately invalid domain:

```bash
dig this-domain-does-not-exist-12345.example
```

Observe the response.

Look for:

```text
status
ANSWER
AUTHORITY
```

### Task

Explain why this is a DNS problem rather than a TCP problem.

---

# Lab 7 — Connectivity Test

Test your local gateway:

```bash
ip route | grep default
```

Then ping the gateway IP.

Example:

```bash
ping -c 4 <gateway-ip>
```

Test Internet connectivity:

```bash
ping -c 4 8.8.8.8
```

Test DNS + connectivity:

```bash
ping -c 4 google.com
```

### Compare

```text
Gateway
   ↓
8.8.8.8
   ↓
google.com
```

If `8.8.8.8` works but `google.com` does not, what layer should you investigate?

---

# Lab 8 — Routing Path

Run:

```bash
traceroute 8.8.8.8
```

If unavailable:

```bash
tracepath 8.8.8.8
```

### Task

Observe:

* Number of hops
* Latency
* Where responses stop
* Whether some hops do not respond

### Important

A `*` at a hop does not automatically mean that the network is broken. Some routers intentionally do not respond to traceroute probes.

---

# Lab 9 — Listening Port Investigation

Run:

```bash
sudo ss -lntup
```

Find:

```text
Local Address
Port
Process
```

Search for SSH:

```bash
sudo ss -lntp | grep ':22'
```

### Questions

1. Is SSH listening?
2. Which address is it bound to?
3. Which process owns the port?

---

# Lab 10 — Connection Refused

Start a test:

```bash
nc -vz 127.0.0.1 9999
```

You will normally receive something similar to:

```text
Connection refused
```

### Why?

There is probably no service listening on port `9999`.

Verify:

```bash
sudo ss -lnt | grep ':9999'
```

No output indicates that nothing is listening on that port.

### Mental model

```text
Client
  |
  | TCP connection
  ↓
Port 9999
  |
  X
No listener
```

---

# Lab 11 — Create a Test TCP Service

Start a temporary listener:

```bash
nc -lv 9999
```

Open another terminal.

Test:

```bash
nc -vz 127.0.0.1 9999
```

Then:

```bash
sudo ss -lntp | grep ':9999'
```

### Task

Observe how the result changes when a process starts listening.

Stop the listener:

```text
Ctrl+C
```

Test again:

```bash
nc -vz 127.0.0.1 9999
```

Compare both results.

---

# Lab 12 — Connection Refused vs Timeout

Test an unused local port:

```bash
nc -vz 127.0.0.1 9999
```

You will usually see:

```text
Connection refused
```

Now test a deliberately unreachable/private destination only if you understand that it may take time:

```bash
nc -vz -w 3 192.0.2.1 9999
```

`192.0.2.0/24` is reserved for documentation/testing.

### Compare

| Result             | Likely area                                                          |
| ------------------ | -------------------------------------------------------------------- |
| Connection refused | Host reachable, no listener or active rejection                      |
| Timeout            | Filtering, routing, unreachable destination, or service path problem |
| Success            | TCP connection established                                           |

Never conclude the root cause from the symptom alone. Collect more evidence.

---

# Lab 13 — HTTP Server

Create a lab directory:

```bash
mkdir -p ~/network-troubleshooting-lab/http
cd ~/network-troubleshooting-lab/
```
