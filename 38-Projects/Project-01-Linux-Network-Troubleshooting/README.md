# Project 01 — Linux Network Troubleshooting Lab

## 📌 Overview

This project is a practical Linux network troubleshooting lab designed to simulate real-world DevOps troubleshooting.

The goal is to understand how to identify and troubleshoot:

- Network interfaces
- IP addresses
- Default gateway
- Routing
- DNS resolution
- Network connectivity
- Listening ports
- Running services
- HTTP/HTTPS connectivity
- Packet capture
- Network neighbors
- Service failures

---

## 🎯 Objectives

By completing this project, I practiced:

1. Inspecting Linux network interfaces
2. Identifying the system IP address
3. Finding the default gateway
4. Checking routing tables
5. Testing Internet connectivity
6. Troubleshooting DNS
7. Checking listening ports
8. Troubleshooting Apache
9. Capturing packets using tcpdump
10. Understanding a real Linux network troubleshooting workflow

---

## 🖥️ Environment

| Component | Details |
|---|---|
| OS | Ubuntu Linux |
| Hostname | shraddha-HP-Laptop-15s-fr4xxx |
| Main Interface | wlo1 |
| IPv4 Address | 192.168.1.5/24 |
| Default Gateway | 192.168.1.1 |
| DNS Server | 192.168.1.1 |
| Apache | Port 80 |
| SSH | Port 22 |
| Jenkins | Port 8080 |
| Docker Registry | Port 5000 |
| HTTP Service | Port 8081 |
| MariaDB | 127.0.0.1:3306 |

---

## 🏗️ Network Overview

```text
                    Internet
                       |
                192.168.1.1
                Default Gateway
                       |
                    wlo1
                192.168.1.5
                       |
              Ubuntu Linux Host
                       |
        +--------------+--------------+
        |              |              |
      Apache         Jenkins        Docker
       :80            :8080         :5000
                                      |
