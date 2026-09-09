# 🔐 Network Security — Commands

## Chapter 34 — DevOps Networking Handbook

This file is a practical command reference for checking, troubleshooting, and analyzing network security on Linux, Docker, Kubernetes, and AWS.

> ⚠️ Use security and scanning commands only on systems and networks you own or are explicitly authorized to test.

---

# 📚 Table of Contents

1. [System Information](#1-system-information)
2. [Network Interfaces](#2-network-interfaces)
3. [Routing](#3-routing)
4. [DNS Security Checks](#4-dns-security-checks)
5. [Ports and Connections](#5-ports-and-connections)
6. [Connectivity Testing](#6-connectivity-testing)
7. [HTTP and HTTPS](#7-http-and-https)
8. [SSH Security](#8-ssh-security)
9. [Firewall — UFW](#9-firewall--ufw)
10. [nftables](#10-nftables)
11. [iptables](#11-iptables)
12. [Packet Capture](#12-packet-capture)
13. [Network Logs](#13-network-logs)
14. [Docker Network Security](#14-docker-network-security)
15. [Kubernetes Network Security](#15-kubernetes-network-security)
16. [AWS Network Security](#16-aws-network-security)
17. [Proxy Checks](#17-proxy-checks)
18. [Security Troubleshooting](#18-security-troubleshooting)
19. [Quick Cheat Sheet](#19-quick-cheat-sheet)

---

# 1. System Information

## Check Current User

```bash
whoami
```

---

## Check Hostname

```bash
hostname
```

---

## Check Operating System

```bash
cat /etc/os-release
```

---

## Check Kernel

```bash
uname -r
```

---

# 2. Network Interfaces

## Show IP Addresses

```bash
ip addr
```

Short form:

```bash
ip a
```

---

## Show Network Interfaces

```bash
ip link
```

---

## Show One Interface

```bash
ip addr show eth0
```

Replace `eth0` with your actual interface.

---

## Show Interface Statistics

```bash
ip -s link
```

Useful for detecting:

* RX errors
* TX errors
* Dropped packets
* Packet counts

---

## Show MAC Address

```bash
ip link
```

Look for:

```text
link/ether
```

---

# 3. Routing

## Show Routing Table

```bash
ip route
```

---

## Show Default Route

```bash
ip route | grep default
```

---

## Check Route to a Destination

```bash
ip route get 8.8.8.8
```

---

## Security Relevance

Incorrect routing can cause:

* Connection timeout
* Unreachable network
* Incorrect traffic path
* Security policy bypasses or failures

---

# 4. DNS Security Checks

## Resolve Domain

```bash
dig example.com
```

---

## Show Only IP Address

```bash
dig +short example.com
```

---

## Query a Specific DNS Server

```bash
dig @8.8.8.8 example.com
```

---

## Check DNS Resolver

```bash
cat /etc/resolv.conf
```

---

## Resolve Using System Configuration

```bash
getent hosts example.com
```

---

## Check DNS Records

```bash
dig example.com A
```

IPv6:

```bash
dig example.com AAAA
```

Mail records:

```bash
dig example.com MX
```

Name servers:

```bash
dig example.com NS
```

---

## Security Checks

Look for:

* Unexpected DNS servers
* Unexpected domains
* Failed resolution
* Suspicious DNS patterns

---

# 5. Ports and Connections

## Show Listening TCP Ports

```bash
ss -lnt
```

---

## Show Listening TCP Ports With Processes

```bash
sudo ss -lntp
```

---

## Show UDP Ports

```bash
ss -lnu
```

---

## Show All TCP Connections

```bash
ss -ant
```

---

## Show All Listening Sockets

```bash
sudo ss -lntup
```

---

## Find a Specific Port

Example:

```bash
sudo ss -lntp | grep ':22'
```

HTTPS:

```bash
sudo ss -lntp | grep ':443'
```

Application port:

```bash
sudo ss -lntp | grep ':8080'
```

---

## Why This Matters

Unexpected listening ports increase the attack surface.

Check:

```text
What is listening?
        ↓
Which process?
        ↓
Which port?
        ↓
Does it need to be exposed?
```

---

# 6. Connectivity Testing

## Ping

```bash
ping -c 4 example.com
```

Note:

> Ping uses ICMP and may be blocked even when TCP/HTTPS connectivity works.

---

## Test TCP Port With Netcat

```bash
nc -vz example.com 443
```

SSH:

```bash
nc -vz example.com 22
```

---

## Test Local Port

```bash
nc -vz 127.0.0.1 8080
```

---

## Trace Network Path

```bash
traceroute example.com
```

If `traceroute` is unavailable:

```bash
tracepath example.com
```

---

# 7. HTTP and HTTPS

## Check HTTP Headers

```bash
curl -I https://example.com
```

---

## Verbose HTTPS

```bash
curl -v https://example.com
```

Useful for seeing:

* DNS
* TCP connection
* TLS
* HTTP response

---

## Test TLS

```bash
curl -Iv https://example.com
```

---

## Follow Redirects

```bash
curl -IL https://example.com
```

---

## Download Headers and Body

```bash
curl -i https://example.com
```

---

## Check HTTP Status

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

---

# 8. SSH Security

## Check SSH Service

```bash
systemctl status ssh
```

On some distributions the service name may be:

```bash
systemctl status sshd
```

---

## Check SSH Port

```bash
sudo ss -lntp | grep ':22'
```

---

## Test SSH Connectivity

```bash
nc -vz <server-ip> 22
```

---

## Connect Using SSH

```bash
ssh user@server
```

---

## Verbose SSH

```bash
ssh -v user@server
```

More detailed:

```bash
ssh -vvv user@server
```

Useful for troubleshooting:

* Authentication
* Key exchange
* Connection
* Configuration

---

## Use a Specific Key

```bash
ssh -i ~/.ssh/id_ed25519 user@server
```

---

## Check SSH Configuration

```bash
sudo sshd -T
```

This can help inspect the effective SSH server configuration.

---

## Check SSH Configuration File

```bash
sudo less /etc/ssh/sshd_config
```

Important settings to review include:

```text
PermitRootLogin
PasswordAuthentication
PubkeyAuthentication
```

Do not change remote SSH settings without ensuring you will not lock yourself out.

---

# 9. Firewall — UFW

## Check Status

```bash
sudo ufw status
```

Detailed:

```bash
sudo ufw status verbose
```

---

## Enable UFW

```bash
sudo ufw enable
```

⚠️ If connected remotely over SSH, ensure SSH access is allowed before enabling the firewall.

---

## Allow SSH

```bash
sudo ufw allow 22/tcp
```

---

## Allow HTTPS

```bash
sudo ufw allow 443/tcp
```

---

## Allow HTTP

```bash
sudo ufw allow 80/tcp
```

---

## Allow a Specific Port

```bash
sudo ufw allow 8080/tcp
```

---

## Allow From a Specific IP

```bash
sudo ufw allow from 192.168.1.100
```

---

## Allow SSH From a Specific Network

```bash
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp
```

---

## Deny a Port

```bash
sudo ufw deny 23/tcp
```

---

## Delete a Rule

First list numbered rules:

```bash
sudo ufw status numbered
```

Then:

```bash
sudo ufw delete <rule-number>
```

---

## Reset UFW

```bash
sudo ufw reset
```

⚠️ This removes UFW rules. Use carefully.

---

# 10. nftables

Modern Linux systems commonly use nftables as a firewall framework.

---

## Check nftables

```bash
sudo nft list ruleset
```

---

## List Tables

```bash
sudo nft list tables
```

---

## List Chains

```bash
sudo nft list chains
```

---

## List Rules

```bash
sudo nft list ruleset
```

---

## Check nftables Service

```bash
systemctl status nftables
```

---

## Important

Do not blindly copy firewall rules from the Internet.

A wrong firewall rule can:

* Block SSH
* Block application traffic
* Break Docker networking
* Break Kubernetes networking
* Disconnect a remote server

Always understand the existing firewall architecture first.

---

# 11. iptables

iptables is still present on many systems and may be provided through compatibility layers.

## List Rules

```bash
sudo iptables -L -n -v
```

---

## List NAT Rules

```bash
sudo iptables -t nat -L -n -v
```

---

## Check Forwarding Rules

```bash
sudo iptables -L FORWARD -n -v
```

---

## Check a Specific Chain

```bash
sudo iptables -L INPUT -n -v
```

---

## Important

Do not assume iptables is the active configuration interface on every modern Linux system.

Check whether the host primarily uses:

```text
nftables
UFW
firewalld
iptables compatibility
```

---

# 12. Packet Capture

## Capture All Interfaces

```bash
sudo tcpdump -i any
```

---

## Capture HTTPS Traffic

```bash
sudo tcpdump -i any port 443
```

---

## Capture HTTP Traffic

```bash
sudo tcpdump -i any port 80
```

---

## Capture SSH Traffic

```bash
sudo tcpdump -i any port 22
```

---

## Capture Traffic From a Host

```bash
sudo tcpdump -i any host 192.168.1.10
```

---

## Capture Specific Interface

```bash
sudo tcpdump -i eth0
```

---

## Save Capture to File

```bash
sudo tcpdump -i any -w network.pcap
```

---

## Read Capture

```bash
sudo tcpdump -r network.pcap
```

---

## Capture Only TCP

```bash
sudo tcpdump -i any tcp
```

---

## Security Uses

Packet capture can help identify:

* Unexpected connections
* Connection attempts
* Retransmissions
* DNS traffic
* Suspicious destinations
* Application communication

---

# 13. Network Logs

## View System Logs

```bash
journalctl
```

---

## Follow Logs

```bash
journalctl -f
```

---

## SSH Logs

```bash
journalctl -u ssh
```

or:

```bash
journalctl -u sshd
```

---

## Firewall Logs

Depending on the firewall and Linux distribution:

```bash
journalctl | grep -i firewall
```

---

## Kernel Network Messages

```bash
dmesg | grep -i network
```

---

# 14. Docker Network Security

## List Networks

```bash
docker network ls
```

---

## Inspect Network

```bash
docker network inspect <network>
```

---

## List Containers

```bash
docker ps
```

---

## Inspect Container

```bash
docker inspect <container>
```

---

## Find Container IP

```bash
docker inspect -f \
'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
<container>
```

---

## Create Isolated Network

```bash
docker network create secure-network
```

---

## Run Container on Network

```bash
docker run -d \
  --name app \
  --network secure-network \
  nginx
```

---

## Test Container Network

Use a diagnostic container when the application image lacks networking tools.

Example:

```bash
docker run --rm \
  --network secure-network \
  curlimages/curl \
  http://app
```

---

## Inspect Published Ports

```bash
docker ps
```

Look for:

```text
0.0.0.0:8080->80/tcp
```

Be careful with:

```text
0.0.0.0:<port>
```

because it can expose the service on all host interfaces.

---

## Bind to Localhost Only

Example:

```bash
docker run -d \
  --name local-app \
  -p 127.0.0.1:8080:80 \
  nginx
```

This limits host exposure to localhost rather than all host interfaces.

---

# 15. Kubernetes Network Security

## Check Pods

```bash
kubectl get pods -A -o wide
```

---

## Check Services

```bash
kubectl get svc -A
```

---

## Check Endpoints

```bash
kubectl get endpoints -A
```

---

## Check EndpointSlices

```bash
kubectl get endpointslices -A
```

---

## Check NetworkPolicies

```bash
kubectl get networkpolicy -A
```

---

## Describe NetworkPolicy

```bash
kubectl describe networkpolicy <policy-name>
```

---

## Check Pod Labels

```bash
kubectl get pods --show-labels
```

---

## Check Service Selector

```bash
kubectl describe svc <service-name>
```

Compare:

```text
Service Selector
       ↓
Pod Labels
```

---

## Check Kubernetes DNS

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --restart=Never \
  --rm -it \
  -- nslookup kubernetes.default
```

---

## Test Service Connectivity

Using a temporary curl container:

```bash
kubectl run curl-test \
  --image=curlimages/curl \
  --rm -it \
  -- sh
```

Then:

```bash
curl http://<service-name>
```

---

## Check Kubernetes API

```bash
kubectl cluster-info
```

---

## Check Current Context

```bash
kubectl config current-context
```

---

## Check Nodes

```bash
kubectl get nodes -o wide
```

---

## Check Kubernetes Events

```bash
kubectl get events -A \
  --sort-by=.lastTimestamp
```

---

# 16. AWS Network Security

## Check AWS CLI

```bash
aws --version
```

---

## Check Identity

```bash
aws sts get-caller-identity
```

---

## Check Configuration

```bash
aws configure list
```

---

## List VPCs

```bash
aws ec2 describe-vpcs
```

---

## List Subnets

```bash
aws ec2 describe-subnets
```

---

## List Route Tables

```bash
aws ec2 describe-route-tables
```

---

## List Security Groups

```bash
aws ec2 describe-security-groups
```

---

## Inspect Security Group Rules

```bash
aws ec2 describe-security-group-rules
```

---

## List Network ACLs

```bash
aws ec2 describe-network-acls
```

---

## List Network Interfaces

```bash
aws ec2 describe-network-interfaces
```

---

## List Internet Gateways

```bash
aws ec2 describe-internet-gateways
```

---

## List NAT Gateways

```bash
aws ec2 describe-nat-gateways
```

---

## List VPC Endpoints

```bash
aws ec2 describe-vpc-endpoints
```

---

## Check EC2 Instances

```bash
aws ec2 describe-instances
```

---

# 17. Proxy Checks

## Check HTTP Proxy

```bash
echo $HTTP_PROXY
```

---

## Check HTTPS Proxy

```bash
echo $HTTPS_PROXY
```

---

## Check NO_PROXY

```bash
echo $NO_PROXY
```

---

## Check Lowercase Variables

```bash
echo $http_proxy
echo $https_proxy
echo $no_proxy
```

---

## Check All Proxy Variables

```bash
env | grep -i proxy
```

---

## Test Without Proxy

For a single command:

```bash
curl --noproxy '*' -v https://example.com
```

This can help determine whether a proxy is causing the problem.

---

# 18. Security Troubleshooting

# Scenario 1 — Unexpected Open Port

Run:

```bash
sudo ss -lntp
```

Identify:

```text
Port
 ↓
Process
 ↓
Application
```

Then ask:

> Does this service need to be exposed?

---

# Scenario 2 — SSH Is Not Working

Check:

```bash
systemctl status ssh
```

Then:

```bash
sudo ss -lntp | grep ':22'
```

Then from the client:

```bash
nc -vz <server-ip> 22
```

Then:

```bash
ssh -vvv user@<server-ip>
```

Check:

```text
Route
Firewall
Port
SSH service
Authentication
```

---

# Scenario 3 — HTTPS Is Not Working

Run:

```bash
dig example.com
```

Then:

```bash
nc -vz example.com 443
```

Then:

```bash
curl -v https://example.com
```

Check:

```text
DNS
 ↓
TCP 443
 ↓
TLS
 ↓
HTTP
```

---

# Scenario 4 — Firewall Blocking Traffic

Check:

```bash
sudo ufw status verbose
```

If nftables is being used:

```bash
sudo nft list ruleset
```

If iptables compatibility is relevant:

```bash
sudo iptables -L -n -v
```

---

# Scenario 5 — Kubernetes NetworkPolicy Problem

Check:

```bash
kubectl get networkpolicy -A
```

Then:

```bash
kubectl describe networkpolicy <policy-name>
```

Check:

```text
Pod labels
Namespace
Ingress rules
Egress rules
Ports
Sources
Destinations
```

---

# Scenario 6 — Docker Container Cannot Communicate

Check:

```bash
docker network ls
```

Then:

```bash
docker network inspect <network>
```

Check whether both containers are attached to the same network.

Then test using a diagnostic container.

---

# Scenario 7 — AWS Instance Cannot Reach Internet

Check:

```text
Subnet
 ↓
Route Table
 ↓
Default Route
 ↓
Internet/NAT Gateway
 ↓
Security Group
 ↓
NACL
 ↓
DNS
```

From the instance:

```bash
ip route
```

Then:

```bash
dig example.com
```

Then:

```bash
curl -I https://example.com
```

---

# Scenario 8 — CI Runner Cannot Access Registry

Check:

```bash
dig <registry>
```

Then:

```bash
nc -vz <registry> 443
```

Then:

```bash
curl -v https://<registry>
```

Then check:

* Proxy
* Firewall
* Credentials
* Registry availability
* Image name
* Image tag

---

# Scenario 9 — Detect Unexpected Outbound Connection

Check current connections:

```bash
ss -antp
```

Then identify the process.

You can inspect network traffic:

```bash
sudo tcpdump -i any
```

Investigate unknown destinations according to your organization's security procedures.

---

# 19. Quick Cheat Sheet

| Task                   | Command                            |
| ---------------------- | ---------------------------------- |
| Show IP                | `ip addr`                          |
| Show interfaces        | `ip link`                          |
| Show routes            | `ip route`                         |
| Resolve DNS            | `dig example.com`                  |
| Show DNS IP            | `dig +short example.com`           |
| Listening ports        | `ss -lntp`                         |
| All connections        | `ss -ant`                          |
| Test TCP port          | `nc -vz host port`                 |
| Test HTTPS             | `curl -v https://example.com`      |
| SSH debug              | `ssh -vvv user@host`               |
| UFW status             | `sudo ufw status`                  |
| nftables rules         | `sudo nft list ruleset`            |
| iptables rules         | `sudo iptables -L -n -v`           |
| Packet capture         | `sudo tcpdump -i any`              |
| System logs            | `journalctl`                       |
| Docker networks        | `docker network ls`                |
| Docker network details | `docker network inspect <network>` |
| Kubernetes Pods        | `kubectl get pods -A -o wide`      |
| Kubernetes Services    | `kubectl get svc -A`               |
| NetworkPolicies        | `kubectl get networkpolicy -A`     |
| AWS identity           | `aws sts get-caller-identity`      |
| AWS VPCs               | `aws ec2 describe-vpcs`            |
| AWS Security Groups    | `aws ec2 describe-security-groups` |
| Proxy variables        | `env \| grep -i proxy`             |

---

# 🧠 Golden Troubleshooting Flow

When investigating a network security problem:

```text
1. SOURCE
   ↓
2. DESTINATION
   ↓
3. DNS
   ↓
4. IP ADDRESS
   ↓
5. ROUTE
   ↓
6. GATEWAY
   ↓
7. PORT
   ↓
8. FIREWALL
   ↓
9. SECURITY GROUP / NACL
   ↓
10. PROXY
   ↓
11. TLS
   ↓
12. AUTHENTICATION
   ↓
13. AUTHORIZATION
   ↓
14. APPLICATION
```

Do not randomly change security rules.

First identify exactly where the connection is failing.

---

# 🔐 Security Command Mindset

Before running a command that changes security configuration, ask:

```text
What does this command change?
        ↓
Who will be affected?
        ↓
Could it block my access?
        ↓
Could it expose a service?
        ↓
Can I verify the change?
        ↓
Can I roll it back?
```

---

# ⭐ Important DevOps Rule

> **Visibility before modification.**

First inspect:

```bash
ip addr
ip route
ss -lntp
sudo ufw status
sudo nft list ruleset
```

Then troubleshoot.

Only after understanding the problem should you modify firewall, routing, security-group, NetworkPolicy, or other security configuration.

---

# 🎯 Final Mental Model

```text
                NETWORK SECURITY
                       |
        +--------------+--------------+
        |              |              |
      Identity       Network         Data
        |              |              |
     AuthN/AuthZ     Firewall       Encryption
        |           Segmentation       |
        |              |              |
        +--------------+--------------+
                       |
                   Monitoring
                       |
                   Detection
                       |
                    Response
```

The objective is not simply to block traffic.

The objective is to:

```text
ALLOW
  ↓
Only Required Traffic
  ↓
From Trusted/Authorized Sources
  ↓
To Required Destinations
  ↓
Using Required Protocols and Ports
  ↓
With Strong Authentication
  ↓
With Encryption
  ↓
And Continuous Monitoring
```
