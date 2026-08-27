
# Chapter 21 — SSH (Secure Shell)

## 1. What is SSH?

SSH stands for **Secure Shell**.

SSH is a network protocol used to securely connect to and manage a remote computer over a network.

It provides an encrypted connection between a client and a server.

### Simple example

```text
My Laptop
   |
   | SSH
   | Encrypted connection
   ↓
Remote Linux Server
````

Example:

```bash
ssh username@192.168.1.100
```

This means:

* `ssh` → SSH client command
* `username` → user account on the remote machine
* `192.168.1.100` → remote server IP address

---

# 2. Why SSH is Important for DevOps

SSH is one of the most important tools for a DevOps engineer.

DevOps engineers use SSH to:

* Access Linux servers remotely
* Manage cloud servers
* Deploy applications
* Check logs
* Restart services
* Troubleshoot production systems
* Transfer files
* Execute commands remotely
* Configure servers
* Manage AWS EC2 instances
* Perform server maintenance

### Real-world example

A production server is running in AWS.

Instead of physically accessing the server, a DevOps engineer can connect remotely:

```bash
ssh ubuntu@<server-ip>
```

After connecting:

```bash
sudo systemctl status nginx
```

The engineer can investigate the server remotely.

---

# 3. SSH Architecture

SSH follows a client-server architecture.

```text
SSH Client
    |
    | Encrypted SSH Connection
    |
    ↓
SSH Server
```

### SSH Client

The client is the machine from which we connect.

Example:

```bash
ssh
```

Our Ubuntu laptop can act as an SSH client.

### SSH Server

The server accepts SSH connections.

The SSH server is usually provided by:

```text
OpenSSH Server
```

The service is commonly called:

```text
sshd
```

---

# 4. SSH Default Port

SSH normally uses:

```text
TCP Port 22
```

Example:

```text
Client
   |
   | TCP 22
   ↓
SSH Server
```

Check whether port 22 is listening:

```bash
ss -ltnp | grep :22
```

Example output:

```text
LISTEN 0 4096 0.0.0.0:22 0.0.0.0:*
```

This means the SSH server is listening on port 22.

---

# 5. SSH Protocol

SSH works at the application layer of the TCP/IP model.

SSH uses:

```text
TCP
```

The default SSH port is:

```text
22
```

### Important

SSH provides:

* Encryption
* Authentication
* Integrity
* Secure remote access

---

# 6. SSH Encryption

SSH encrypts communication between the client and server.

Without encryption, sensitive information could potentially be exposed.

SSH protects:

* Commands
* Passwords
* Data
* File transfers
* Session information

Example:

```text
Client
   |
   | Encrypted data
   ↓
SSH Server
```

---

# 7. SSH Authentication

SSH needs to verify the identity of the user.

Common authentication methods include:

1. Password authentication
2. Public-key authentication

Public-key authentication is commonly preferred for servers.

---

# 8. Password Authentication

With password authentication:

```bash
ssh username@server-ip
```

The server asks for the user's password.

Example:

```text
ssh ubuntu@192.168.1.100
```

Then:

```text
ubuntu@192.168.1.100's password:
```

---

# 9. SSH Key Authentication

SSH keys provide a more secure and convenient way to authenticate.

An SSH key pair contains:

```text
Private Key
Public Key
```

Example:

```text
Private Key → ~/.ssh/id_ed25519
Public Key  → ~/.ssh/id_ed25519.pub
```

### Important rule

**Never share your private key.**

The public key can be placed on the server.

The private key stays on your machine.

---

# 10. Public Key vs Private Key

| Key         | Location        | Purpose                       |
| ----------- | --------------- | ----------------------------- |
| Public Key  | Server          | Used to verify authentication |
| Private Key | Client          | Proves your identity          |
| `.pub`      | Public key file | Safe to copy to server        |
| Private key | Secret          | Never share                   |

Example:

```text
Laptop
 ├── Private Key
 └── Public Key
          |
          ↓
       Server
```

The server stores the public key.

---

# 11. Generate an SSH Key Pair

Use:

```bash
ssh-keygen
```

Modern systems commonly use:

```bash
ssh-keygen -t ed25519
```

Example:

```bash
ssh-keygen -t ed25519 -C "devops@example.com"
```

This creates:

```text
id_ed25519
id_ed25519.pub
```

---

# 12. SSH Key Directory

SSH configuration and keys are commonly stored in:

```text
~/.ssh/
```

Check it:

```bash
ls -la ~/.ssh/
```

Common files include:

```text
id_ed25519
id_ed25519.pub
known_hosts
authorized_keys
config
```

---

# 13. authorized_keys

The SSH server stores authorized public keys in:

```text
~/.ssh/authorized_keys
```

Example:

```text
/home/ubuntu/.ssh/authorized_keys
```

If your public key is stored there, the server can authenticate you using the corresponding private key.

---

# 14. known_hosts

The SSH client stores information about previously contacted SSH servers in:

```text
~/.ssh/known_hosts
```

When connecting to a new server, SSH may display:

```text
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

After accepting the server identity, information is stored in `known_hosts`.

---

# 15. SSH Host Key Verification

SSH uses host keys to help verify that you are connecting to the expected server.

This helps protect against:

```text
Man-in-the-Middle (MITM)
```

attacks.

If the server's host key unexpectedly changes, SSH may display a warning.

Example:

```text
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

Do not blindly ignore this warning.

Investigate why the host key changed.

---

# 16. Basic SSH Connection

Basic syntax:

```bash
ssh username@hostname
```

Example:

```bash
ssh ubuntu@192.168.1.100
```

---

# 17. SSH with a Custom Port

If SSH is running on a port other than 22:

```bash
ssh -p 2222 username@server-ip
```

Example:

```bash
ssh -p 2222 ubuntu@192.168.1.100
```

---

# 18. SSH Using a Specific Private Key

Use:

```bash
ssh -i /path/to/private-key username@server-ip
```

Example:

```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@192.168.1.100
```

This tells SSH which private key to use.

---

# 19. SSH Configuration File

SSH client configuration is commonly stored in:

```text
~/.ssh/config
```

Example:

```text
Host production
    HostName 203.0.113.10
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519
```

Now instead of:

```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@203.0.113.10
```

you can use:

```bash
ssh production
```

This makes frequently used servers easier to manage.

---

# 20. SSH Server Configuration

The SSH server configuration is commonly:

```text
/etc/ssh/sshd_config
```

This file controls SSH server behavior.

Examples of settings include:

```text
Port
PermitRootLogin
PasswordAuthentication
PubkeyAuthentication
AllowUsers
```

Always be careful when modifying SSH configuration on a remote server.

A configuration mistake can lock you out.

---

# 21. Check SSH Service

On Ubuntu:

```bash
systemctl status ssh
```

You may see:

```text
Active: active (running)
```

This means the SSH service is running.

---

# 22. Start SSH Service

```bash
sudo systemctl start ssh
```

---

# 23. Stop SSH Service

```bash
sudo systemctl stop ssh
```

Be extremely careful when stopping SSH on a remote production server because your remote access may be lost.

---

# 24. Restart SSH Service

```bash
sudo systemctl restart ssh
```

Use this after changing SSH server configuration when a restart is required.

---

# 25. Reload SSH Configuration

Instead of completely restarting the service, configuration can often be reloaded:

```bash
sudo systemctl reload ssh
```

Reloading is generally preferable when appropriate because it can minimize disruption to existing connections.

---

# 26. Enable SSH at Boot

```bash
sudo systemctl enable ssh
```

This configures SSH to start automatically during boot.

Check:

```bash
systemctl is-enabled ssh
```

---

# 27. Check Listening SSH Port

Use:

```bash
ss -ltnp | grep :22
```

Or:

```bash
sudo ss -ltnp | grep :22
```

Example:

```text
LISTEN 0 4096 0.0.0.0:22 0.0.0.0:* users:(("sshd",pid=1531,fd=3))
```

This shows:

* SSH is listening
* Port = 22
* Protocol = TCP
* Process = `sshd`

---

# 28. SSH Verbose Mode

For troubleshooting:

```bash
ssh -v username@server-ip
```

More detailed:

```bash
ssh -vv username@server-ip
```

Maximum debugging:

```bash
ssh -vvv username@server-ip
```

`-vvv` is very useful when troubleshooting authentication and connection problems.

---

# 29. Test SSH Port

You can check whether TCP port 22 is reachable:

```bash
nc -zv server-ip 22
```

Example:

```bash
nc -zv 192.168.1.100 22
```

Possible result:

```text
Connection to 192.168.1.100 22 port [tcp/ssh] succeeded!
```

---

# 30. Copy Files Using SCP

SCP stands for:

```text
Secure Copy Protocol
```

Copy a local file to a remote server:

```bash
scp file.txt username@server-ip:/tmp/
```

Example:

```bash
scp app.log ubuntu@192.168.1.100:/tmp/
```

---

# 31. Copy a File from Server

```bash
scp username@server-ip:/path/to/file .
```

Example:

```bash
scp ubuntu@192.168.1.100:/var/log/app.log .
```

---

# 32. Copy Directories Using SCP

Use:

```bash
scp -r directory username@server-ip:/tmp/
```

Example:

```bash
scp -r myapp ubuntu@192.168.1.100:/opt/
```

---

# 33. SFTP

SFTP stands for:

```text
SSH File Transfer Protocol
```

Connect using:

```bash
sftp username@server-ip
```

SFTP provides secure file transfer over SSH.

---

# 34. Execute a Remote Command

SSH does not require an interactive shell.

You can execute a command directly:

```bash
ssh username@server-ip "hostname"
```

Example:

```bash
ssh ubuntu@192.168.1.100 "uptime"
```

Another example:

```bash
ssh ubuntu@192.168.1.100 "df -h"
```

This is very useful for automation.

---

# 35. SSH Agent

SSH Agent can securely hold private keys in memory.

Start the agent:

```bash
eval "$(ssh-agent -s)"
```

Add a key:

```bash
ssh-add ~/.ssh/id_ed25519
```

Check loaded keys:

```bash
ssh-add -l
```

SSH Agent is useful when you need to authenticate to multiple systems without repeatedly entering the key passphrase.

---

# 36. SSH Port Forwarding

SSH can securely forward network traffic.

There are three major types:

1. Local port forwarding
2. Remote port forwarding
3. Dynamic port forwarding

---

# 37. Local Port Forwarding

Syntax:

```bash
ssh -L local-port:destination-host:destination-port user@ssh-server
```

Example:

```bash
ssh -L 8080:localhost:80 ubuntu@server
```

Conceptually:

```text
Your Laptop
   |
   | localhost:8080
   ↓
SSH Server
   |
   | localhost:80
   ↓
Web Application
```

This is useful when a service is not directly exposed to the network.

---

# 38. Remote Port Forwarding

Syntax:

```bash
ssh -R remote-port:destination-host:destination-port user@server
```

This allows a remote server to access a service through the SSH connection.

---

# 39. Dynamic Port Forwarding

Use:

```bash
ssh -D 1080 username@server
```

This creates a SOCKS proxy.

It can be used for routing application traffic through the SSH server.

---

# 40. SSH in AWS EC2

SSH is commonly used to access Linux EC2 instances.

Typical command:

```bash
ssh -i my-key.pem ubuntu@<EC2-PUBLIC-IP>
```

For Amazon Linux, the username may be:

```text
ec2-user
```

For Ubuntu:

```text
ubuntu
```

Example:

```bash
ssh -i devops-key.pem ubuntu@203.0.113.10
```

The EC2 security group must allow inbound TCP traffic to the SSH port.

For default SSH:

```text
TCP 22
```

---

# 41. SSH Security Best Practices

Important SSH security practices:

### 1. Prefer SSH keys

Use public-key authentication instead of passwords where appropriate.

### 2. Protect private keys

Never share:

```text
id_ed25519
```

or:

```text
*.pem
```

private keys.

### 3. Use correct permissions

Example:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

### 4. Disable direct root login when appropriate

In `/etc/ssh/sshd_config`:

```text
PermitRootLogin no
```

### 5. Use least privilege

Give users only the access they need.

### 6. Keep SSH software updated

Security updates are important for SSH servers.

### 7. Restrict SSH access

Use firewalls, security groups, VPNs, bastion hosts, or other controls where appropriate.

---

# 42. SSH File Permissions

Typical permissions:

```text
~/.ssh                 → 700
private key            → 600
authorized_keys        → 600
public key             → 644
known_hosts            → 644
```

Example:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 600 ~/.ssh/authorized_keys
```

Incorrect permissions can cause SSH authentication failures.

---

# 43. Common SSH Errors

## Connection refused

```text
ssh: connect to host ... port 22: Connection refused
```

Possible causes:

* SSH service is not running
* Wrong port
* Firewall is rejecting the connection
* SSH server is not listening

Check:

```bash
systemctl status ssh
ss -ltnp | grep :22
```

---

# 44. Connection Timed Out

Example:

```text
Connection timed out
```

Possible causes:

* Firewall
* Security group
* Network routing problem
* Server unreachable
* Wrong IP address

Test:

```bash
ping server-ip
```

and:

```bash
nc -zv server-ip 22
```

---

# 45. Permission Denied

Example:

```text
Permission denied (publickey)
```

Possible causes:

* Wrong username
* Wrong private key
* Public key missing from `authorized_keys`
* Incorrect key permissions
* SSH server configuration issue

Use:

```bash
ssh -vvv username@server-ip
```

to troubleshoot.

---

# 46. SSH Troubleshooting Flow

When SSH fails, troubleshoot systematically.

```text
1. Check IP address
       ↓
2. Check network connectivity
       ↓
3. Check port 22
       ↓
4. Check SSH service
       ↓
5. Check firewall/security group
       ↓
6. Check username
       ↓
7. Check SSH key
       ↓
8. Check file permissions
       ↓
9. Use ssh -vvv
       ↓
10. Check server logs
```

---

# 47. SSH Logs

On Ubuntu, SSH authentication logs can commonly be checked with:

```bash
sudo journalctl -u ssh
```

You can also search authentication logs:

```bash
sudo grep ssh /var/log/auth.log
```

Follow logs in real time:

```bash
sudo journalctl -u ssh -f
```

---

# 48. SSH and Bastion Host

A bastion host is a controlled server used to access private servers.

Example:

```text
Internet
   |
   ↓
Bastion Host
   |
   ↓
Private Server
```

Instead of exposing every production server to the Internet, organizations may allow SSH only through a bastion host.

---

# 49. SSH in DevOps

SSH is used in many DevOps workflows:

```text
Developer
    |
    ↓
GitHub
    |
    ↓
CI/CD Pipeline
    |
    ↓
Deployment Server
    |
    ↓
Production Application
```

SSH may be used to:

* Access deployment servers
* Copy artifacts
* Run deployment commands
* Troubleshoot servers
* Inspect logs
* Restart services
* Configure infrastructure

---

# 50. SSH and Automation

SSH can execute commands remotely:

```bash
ssh user@server "sudo systemctl restart nginx"
```

Multiple servers can also be managed using automation tools such as:

* Ansible
* Terraform provisioners (where appropriate)
* CI/CD systems
* Shell scripts

Example:

```bash
for server in server1 server2 server3
do
    ssh "$server" "hostname"
done
```

---

# 51. SSH vs Telnet

| SSH                         | Telnet                             |
| --------------------------- | ---------------------------------- |
| Encrypted                   | Unencrypted                        |
| Secure                      | Insecure                           |
| Default port 22             | Default port 23                    |
| Used in modern environments | Mostly legacy                      |
| Supports key authentication | No equivalent secure key mechanism |

SSH replaced Telnet for secure remote administration.

---

# 52. Important SSH Files

| File                     | Purpose                    |
| ------------------------ | -------------------------- |
| `~/.ssh/`                | SSH configuration and keys |
| `~/.ssh/id_ed25519`      | Private key                |
| `~/.ssh/id_ed25519.pub`  | Public key                 |
| `~/.ssh/authorized_keys` | Authorized public keys     |
| `~/.ssh/known_hosts`     | Known server identities    |
| `~/.ssh/config`          | Client configuration       |
| `/etc/ssh/sshd_config`   | SSH server configuration   |

---

# 53. Important SSH Commands

```bash
ssh
ssh-keygen
ssh-copy-id
ssh-add
ssh-agent
scp
sftp
ss
systemctl
journalctl
```

Useful examples:

```bash
ssh user@server
```

```bash
ssh -p 2222 user@server
```

```bash
ssh -i ~/.ssh/id_ed25519 user@server
```

```bash
ssh -vvv user@server
```

```bash
ssh-keygen -t ed25519
```

```bash
ssh-copy-id user@server
```

```bash
scp file.txt user@server:/tmp/
```

```bash
sftp user@server
```

---

# 54. Production Checklist

Before connecting to a production server:

* Verify the server IP/hostname
* Verify the username
* Verify the SSH port
* Use the correct SSH key
* Confirm the server environment
* Avoid running destructive commands blindly
* Check current users and processes
* Check disk space before maintenance
* Check service status before restarting
* Keep an audit trail of important changes

Useful commands:

```bash
hostname
whoami
uptime
df -h
free -h
systemctl status <service>
```

---

# 55. Key Takeaways

### SSH means:

**Secure Shell**

### Default port:

```text
TCP 22
```

### SSH server:

```text
sshd
```

### Client command:

```bash
ssh
```

### Generate key:

```bash
ssh-keygen -t ed25519
```

### Copy public key:

```bash
ssh-copy-id user@server
```

### Secure file copy:

```bash
scp
```

### Secure file transfer:

```bash
sftp
```

### Debug connection:

```bash
ssh -vvv user@server
```

### SSH server configuration:

```text
/etc/ssh/sshd_config
```

### SSH client configuration:

```text
~/.ssh/config
```

### Authorized keys:

```text
~/.ssh/authorized_keys
```

### Known servers:

```text
~/.ssh/known_hosts
```

---

# 56. DevOps Interview One-Liner

**What is SSH?**

SSH (Secure Shell) is a secure network protocol used to remotely access and manage systems over an encrypted connection. It normally operates over TCP port 22 and supports password and public-key authentication.

---

# 57. Final Mental Model

Remember SSH like this:

```text
                 SSH
                  |
        ┌─────────┴─────────┐
        ↓                   ↓
     Client              Server
        |                   |
        | TCP 22            |
        └──── Encrypted ────┘
                  |
             Authentication
             /           \
        Password        SSH Key
                           |
                    Public + Private
                           |
                    Secure Access
```

For DevOps:

```text
SSH
 |
 ├── Linux Servers
 ├── AWS EC2
 ├── Production
 ├── Troubleshooting
 ├── File Transfer
 ├── Automation
 ├── CI/CD
 ├── Bastion Hosts
 └── Secure Remote Access
```

**SSH is a fundamental DevOps skill.**

````



