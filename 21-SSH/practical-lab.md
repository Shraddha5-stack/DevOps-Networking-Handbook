Absolutely 👍 Let's create the **practical lab** for Chapter 21 – SSH.

From your current directory:

```bash
cd ~/DevOps-Networking-Handbook/21-SSH
code practical-lab.md
```

Paste this complete content:

````markdown
# Chapter 21 – SSH Practical Lab

## 🎯 Objective

In this lab, we will practice SSH fundamentals on a Linux system.

We will learn how to:

- Check the SSH service
- Check the SSH listening port
- Check SSH configuration
- Generate SSH keys
- Understand public and private keys
- Configure key-based authentication
- Test SSH locally
- Use SSH verbose mode
- Copy files using SCP
- Test SFTP
- Understand SSH security
- Troubleshoot common SSH problems

---

# 1. Check SSH Service

Check whether the SSH service is running:

```bash
sudo systemctl status ssh
````

### Expected observation

The service should show:

```text
Active: active (running)
```

If SSH is not running:

```bash
sudo systemctl start ssh
```

Enable it at boot:

```bash
sudo systemctl enable ssh
```

---

# 2. Check SSH Listening Port

Run:

```bash
sudo ss -ltnp | grep :22
```

Example:

```text
LISTEN 0 4096 0.0.0.0:22
LISTEN 0 4096 [::]:22
```

### Observation

SSH is listening on port:

```text
22
```

This means the system is ready to accept SSH connections.

---

# 3. Identify the SSH Process

Run:

```bash
sudo ss -ltnp | grep ssh
```

You may see:

```text
users:(("sshd",pid=...,fd=...))
```

### Observation

`sshd` is the SSH server daemon.

---

# 4. Check SSH Version

Run:

```bash
ssh -V
```

Example:

```text
OpenSSH_9.xp1 Ubuntu-...
```

### Observation

This shows the installed OpenSSH client version.

---

# 5. Check SSH Server Configuration

The main SSH server configuration file is:

```text
/etc/ssh/sshd_config
```

View it:

```bash
sudo less /etc/ssh/sshd_config
```

Search for important settings:

```bash
sudo grep -E '^(Port|PermitRootLogin|PasswordAuthentication)' /etc/ssh/sshd_config
```

---

# 6. Check the Current SSH Configuration

Use:

```bash
sudo sshd -T | grep -E 'port|permitrootlogin|passwordauthentication|pubkeyauthentication'
```

### Observation

This displays the effective SSH server configuration.

This is useful because SSH configuration can include settings from multiple configuration files.

---

# 7. Check Your SSH Directory

Run:

```bash
ls -la ~/.ssh
```

You may see files such as:

```text
authorized_keys
known_hosts
id_ed25519
id_ed25519.pub
config
```

Not every file will necessarily exist.

---

# 8. Generate an SSH Key Pair

Generate an Ed25519 key:

```bash
ssh-keygen -t ed25519
```

Press Enter to accept the default location.

You may be asked for a passphrase.

### Expected files

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

---

# 9. Understand the SSH Key Pair

Check the files:

```bash
ls -l ~/.ssh/id_ed25519*
```

You should have:

```text
id_ed25519
id_ed25519.pub
```

### Important

```text
id_ed25519
```

is the **private key**.

```text
id_ed25519.pub
```

is the **public key**.

### Security rule

Never share:

```text
id_ed25519
```

The public key can be copied to servers.

---

# 10. Display the Public Key

Run:

```bash
cat ~/.ssh/id_ed25519.pub
```

You will see a long line beginning with something similar to:

```text
ssh-ed25519 AAAA...
```

Do not share your private key.

---

# 11. Check SSH Key Permissions

Run:

```bash
ls -ld ~/.ssh
ls -l ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.pub
```

Recommended permissions:

```text
~/.ssh              → 700
private key         → 600
public key          → 644
```

Set them:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

---

# 12. Check Known Hosts

Run:

```bash
ls -l ~/.ssh/known_hosts
```

If the file exists:

```bash
cat ~/.ssh/known_hosts
```

### Purpose

`known_hosts` stores host-key information for servers you have connected to.

It helps SSH detect unexpected server identity changes.

---

# 13. Test Local SSH Connection

Because SSH is running on this machine, test:

```bash
ssh localhost
```

Or:

```bash
ssh $(whoami)@localhost
```

If successful, you will enter a shell on the same machine.

Check:

```bash
hostname
whoami
```

Exit:

```bash
exit
```

---

# 14. Test SSH Using Port 22

Run:

```bash
ssh -p 22 localhost
```

### Observation

This explicitly tells SSH to connect to port `22`.

Exit:

```bash
exit
```

---

# 15. Test SSH with Verbose Mode

Run:

```bash
ssh -v localhost
```

For more debugging:

```bash
ssh -vv localhost
```

Maximum debugging:

```bash
ssh -vvv localhost
```

### Observation

Verbose mode shows details about:

* Configuration
* DNS resolution
* Connection
* Authentication
* Key exchange
* Encryption
* Session establishment

This is extremely useful for troubleshooting.

---

# 16. Test the SSH Port with nc

Check whether port 22 is reachable:

```bash
nc -zv localhost 22
```

Expected result:

```text
Connection to localhost 22 port [tcp/ssh] succeeded!
```

---

# 17. Test SSH with Telnet

If Telnet is installed:

```bash
telnet localhost 22
```

You may see an SSH banner similar to:

```text
SSH-2.0-OpenSSH_...
```

Exit with:

```text
Ctrl + ]
```

Then:

```text
quit
```

---

# 18. Copy a File Using SCP

Create a test file:

```bash
echo "SSH SCP test" > ~/ssh-test.txt
```

Copy it to `/tmp` on the local machine:

```bash
scp ~/ssh-test.txt localhost:/tmp/
```

Verify:

```bash
cat /tmp/ssh-test.txt
```

Expected:

```text
SSH SCP test
```

---

# 19. Copy a Directory Using SCP

Create a directory:

```bash
mkdir -p ~/ssh-lab
echo "DevOps SSH Lab" > ~/ssh-lab/test.txt
```

Copy it:

```bash
scp -r ~/ssh-lab localhost:/tmp/
```

Verify:

```bash
ls -l /tmp/ssh-lab
```

---

# 20. Test SFTP

Connect:

```bash
sftp localhost
```

Inside SFTP:

```bash
pwd
ls
```

Exit:

```bash
exit
```

---

# 21. Run a Remote Command

Instead of opening an interactive SSH session, run:

```bash
ssh localhost "hostname"
```

Run:

```bash
ssh localhost "whoami"
```

Run:

```bash
ssh localhost "df -h"
```

### Observation

SSH can execute commands remotely and return the output.

This is useful for DevOps automation.

---

# 22. SSH Port Forwarding Lab

Create a simple local HTTP server:

```bash
python3 -m http.server 8000
```

Keep this terminal running.

Open another terminal.

Create an SSH tunnel:

```bash
ssh -L 9000:localhost:8000 localhost
```

In another terminal:

```bash
curl http://localhost:9000
```

### Concept

```text
localhost:9000
      |
      | SSH Tunnel
      ↓
localhost:8000
      |
      ↓
Python HTTP Server
```

Exit SSH:

```bash
exit
```

Stop the Python server with:

```text
Ctrl + C
```

---

# 23. Check SSH Agent

Run:

```bash
ssh-add -l
```

If the agent is not running:

```bash
eval "$(ssh-agent -s)"
```

Add your key:

```bash
ssh-add ~/.ssh/id_ed25519
```

Check again:

```bash
ssh-add -l
```

---

# 24. Create an SSH Config Entry

Create:

```bash
code ~/.ssh/config
```

Add:

```text
Host local-lab
    HostName localhost
    User YOUR_USERNAME
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

Replace:

```text
YOUR_USERNAME
```

with your Linux username.

Save the file.

Set permissions:

```bash
chmod 600 ~/.ssh/config
```

Now connect using:

```bash
ssh local-lab
```

---

# 25. Troubleshooting Practice

## Problem 1: Connection Refused

Test:

```bash
ssh localhost
```

If you get:

```text
Connection refused
```

Check:

```bash
sudo systemctl status ssh
sudo ss -ltnp | grep :22
```

---

## Problem 2: Permission Denied

Run:

```bash
ssh -vvv localhost
```

Check:

* Username
* SSH key
* Authentication configuration
* Key permissions
* `authorized_keys`

---

## Problem 3: Wrong Port

Try:

```bash
ssh -p 22 localhost
```

Check listening ports:

```bash
sudo ss -ltnp
```

---

# 26. SSH Security Checks

Check whether root login is enabled:

```bash
sudo sshd -T | grep permitrootlogin
```

Check password authentication:

```bash
sudo sshd -T | grep passwordauthentication
```

Check public-key authentication:

```bash
sudo sshd -T | grep pubkeyauthentication
```

### Production best practices

* Prefer SSH keys over passwords
* Protect private keys
* Use strong passphrases
* Disable unnecessary root login
* Use least privilege
* Restrict SSH access with firewalls/security groups
* Use bastion/jump hosts for private servers
* Monitor SSH authentication logs
* Keep OpenSSH updated

---

# 27. Check SSH Authentication Logs

On Ubuntu/Debian systems:

```bash
sudo journalctl -u ssh
```

You can also check:

```bash
sudo journalctl -u ssh --since "1 hour ago"
```

For failed authentication attempts:

```bash
sudo journalctl -u ssh | grep -i "failed"
```

---

# 28. Production DevOps Scenario

Imagine an AWS EC2 server:

```text
Developer Laptop
       |
       | SSH
       ↓
Bastion Host
       |
       | SSH
       ↓
Private EC2 Server
       |
       ↓
Application
```

A DevOps engineer may use SSH to:

1. Connect to the bastion host.
2. Access the private server.
3. Check application status.
4. Check logs.
5. Check disk usage.
6. Restart services.
7. Troubleshoot networking.

Useful commands:

```bash
ssh user@server
```

```bash
df -h
```

```bash
free -h
```

```bash
ss -ltnp
```

```bash
systemctl status nginx
```

```bash
journalctl -u nginx
```

---

# 29. Final Verification

Run these commands:

```bash
ssh -V
```

```bash
sudo systemctl status ssh
```

```bash
sudo ss -ltnp | grep :22
```

```bash
ls -la ~/.ssh
```

```bash
ssh localhost "hostname"
```

```bash
ssh localhost "whoami"
```

```bash
ssh localhost "df -h"
```

```bash
nc -zv localhost 22
```

```bash
ssh -v localhost
```

---

# 📝 Lab Summary

In this practical lab, I learned:

* SSH provides secure remote access.
* SSH normally uses TCP port 22.
* `sshd` is the SSH server daemon.
* SSH uses public/private key authentication.
* Private keys must be protected.
* `authorized_keys` stores authorized public keys.
* `known_hosts` stores known server host keys.
* `scp` transfers files securely.
* `sftp` provides secure file transfer.
* `ssh -v` helps troubleshoot SSH.
* SSH can execute remote commands.
* SSH supports port forwarding.
* SSH is widely used in DevOps and cloud environments.

---

# 🎯 Interview Connection

Important commands to remember:

```text
ssh user@server
ssh -p PORT user@server
ssh -v user@server
ssh-keygen
ssh-copy-id user@server
scp file user@server:/path
sftp user@server
ssh -L ...
ssh -R ...
ssh -D ...
ssh -J ...
```

## Real-world DevOps usage

```text
SSH
 ↓
Remote Server Access
 ↓
Troubleshooting
 ↓
Deployment
 ↓
Log Investigation
 ↓
Service Management
 ↓
Automation
```

````



