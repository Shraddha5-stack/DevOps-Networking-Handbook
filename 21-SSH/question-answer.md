
# 🔐 Chapter 21 — SSH Interview Questions

## 1. What is SSH?

SSH stands for Secure Shell.

It is a network protocol used to securely connect to and manage remote systems over an encrypted connection.

Default SSH port:

```text
22/TCP
````

---

## 2. Why is SSH important in DevOps?

SSH is important because DevOps engineers frequently need to:

* Access Linux servers
* Deploy applications
* Troubleshoot servers
* Check logs
* Restart services
* Transfer files
* Execute commands remotely
* Manage cloud servers

Example:

```bash
ssh ubuntu@192.168.1.100
```

---

## 3. What is the default SSH port?

The default SSH port is:

```text
22
```

SSH uses TCP.

---

## 4. What is the difference between SSH client and SSH server?

### SSH Client

The client initiates the connection.

Example:

```bash
ssh ubuntu@192.168.1.100
```

### SSH Server

The server accepts SSH connections.

The SSH server process is usually:

```text
sshd
```

---

## 5. What is `sshd`?

`sshd` stands for SSH daemon.

It runs on the remote server and listens for incoming SSH connections.

Check it with:

```bash
sudo systemctl status ssh
```

or:

```bash
ps aux | grep sshd
```

---

## 6. How do you check whether SSH is listening?

```bash
sudo ss -ltnp | grep :22
```

Example:

```text
LISTEN 0 4096 0.0.0.0:22
```

This indicates that SSH is listening on port 22.

---

## 7. How do you connect to a remote server?

```bash
ssh username@server-ip
```

Example:

```bash
ssh ubuntu@192.168.1.100
```

---

## 8. How do you connect using a private key?

```bash
ssh -i ~/.ssh/id_ed25519 username@server-ip
```

Example:

```bash
ssh -i ~/.ssh/aws-key.pem ubuntu@SERVER_IP
```

This is commonly used with cloud servers.

---

## 9. What is SSH key-based authentication?

SSH key-based authentication uses a pair of cryptographic keys:

```text
Private Key → Client
Public Key  → Server
```

The private key remains on the client.

The public key is stored on the server.

---

## 10. Where is the public key stored on the server?

Usually:

```text
~/.ssh/authorized_keys
```

The server checks this file when authenticating a user using public-key authentication.

---

## 11. Where is the private key stored?

A common location is:

```text
~/.ssh/id_ed25519
```

Other keys may have different names.

For example:

```text
~/.ssh/aws-key.pem
```

---

## 12. Why should you never share your private key?

The private key is secret.

Someone who obtains the private key may be able to authenticate as you, depending on the server configuration and protections.

Therefore:

```text
Private Key = Secret
Public Key  = Can be shared
```

---

## 13. How do you generate an SSH key?

Recommended modern option:

```bash
ssh-keygen -t ed25519
```

This creates:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

---

## 14. What is `ssh-keygen`?

`ssh-keygen` is used to generate and manage SSH keys.

Example:

```bash
ssh-keygen -t ed25519
```

---

## 15. What is `ssh-copy-id`?

`ssh-copy-id` copies your public key to a remote server.

Example:

```bash
ssh-copy-id ubuntu@192.168.1.100
```

The public key is normally added to:

```text
~/.ssh/authorized_keys
```

---

## 16. What is `scp`?

`scp` stands for Secure Copy Protocol.

It is used to securely transfer files between systems over SSH.

Example:

```bash
scp app.conf ubuntu@192.168.1.100:/tmp/
```

---

## 17. How do you copy a directory using SCP?

Use:

```bash
scp -r project/ ubuntu@192.168.1.100:/opt/
```

The `-r` option means recursive.

---

## 18. How do you execute a command on a remote server without opening an interactive shell?

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

## 19. How do you troubleshoot SSH connection problems?

Use verbose mode:

```bash
ssh -v username@server-ip
```

For more detailed debugging:

```bash
ssh -vvv username@server-ip
```

Also check:

```bash
ping SERVER_IP
ip route get SERVER_IP
nc -zv SERVER_IP 22
sudo systemctl status ssh
sudo ss -ltnp | grep :22
```

---

## 20. What does `ssh -vvv` do?

It enables very detailed SSH debugging output.

It can help identify:

* Network problems
* Authentication problems
* Key problems
* Configuration problems
* Connection failures

Example:

```bash
ssh -vvv ubuntu@SERVER_IP
```

---

## 21. What does "Connection refused" mean?

Usually, the destination is reachable but nothing is accepting the connection on that port, or a firewall/security control is actively rejecting it.

Check:

```bash
sudo systemctl status ssh
```

and:

```bash
sudo ss -ltnp | grep :22
```

---

## 22. What does "Connection timed out" mean?

It generally means the connection attempt did not receive a response within the expected time.

Possible causes include:

* Firewall blocking traffic
* Security group rules
* Incorrect IP address
* Network routing problems
* Server unavailable

Check:

```bash
ping SERVER_IP
ip route get SERVER_IP
nc -zv SERVER_IP 22
```

---

## 23. What does "Permission denied (publickey)" mean?

It generally means the server did not accept the SSH key authentication attempt.

Possible causes:

* Wrong private key
* Public key missing from `authorized_keys`
* Incorrect username
* Incorrect file permissions
* SSH server configuration problem

Debug with:

```bash
ssh -vvv -i ~/.ssh/id_ed25519 username@server-ip
```

---

## 24. What permissions should a private SSH key have?

A common secure permission is:

```bash
chmod 600 ~/.ssh/id_ed25519
```

The `.ssh` directory commonly uses:

```bash
chmod 700 ~/.ssh
```

---

## 25. What is `known_hosts`?

The file:

```text
~/.ssh/known_hosts
```

stores host keys for SSH servers you have connected to.

It helps SSH recognize previously contacted servers and detect unexpected host-key changes.

---

## 26. What happens when SSH says "REMOTE HOST IDENTIFICATION HAS CHANGED"?

It means the host key presented by the server differs from the key previously stored for that host.

Possible reasons include:

* Server was rebuilt
* Host keys were changed
* IP address now points to another machine
* Possible security attack

Do not blindly ignore this warning.

If you have verified that the server was legitimately rebuilt, you can remove its old entry:

```bash
ssh-keygen -R SERVER_IP
```

Then reconnect and verify the new fingerprint.

---

## 27. What is the SSH configuration file?

The SSH server configuration is usually:

```text
/etc/ssh/sshd_config
```

The SSH client configuration can be:

```text
~/.ssh/config
```

---

## 28. How do you validate SSH server configuration?

Use:

```bash
sudo sshd -t
```

If there is no output, the configuration syntax is generally valid.

Always validate configuration before restarting SSH after making changes.

---

## 29. How do you restart SSH?

On Ubuntu/Debian:

```bash
sudo systemctl restart ssh
```

---

## 30. How do you check SSH logs?

```bash
sudo journalctl -u ssh
```

For recent logs:

```bash
sudo journalctl -u ssh --since "10 minutes ago"
```

To follow logs:

```bash
sudo journalctl -u ssh -f
```

---

## 31. What is SSH Agent?

`ssh-agent` is a program that can hold private keys in memory and provide them to SSH when authentication is required.

Start it with:

```bash
eval "$(ssh-agent -s)"
```

Add a key:

```bash
ssh-add ~/.ssh/id_ed25519
```

List loaded keys:

```bash
ssh-add -l
```

---

## 32. What is the difference between `ssh` and `scp`?

| Command | Purpose                        |
| ------- | ------------------------------ |
| `ssh`   | Remote login/command execution |
| `scp`   | Secure file transfer           |

Example:

```bash
ssh ubuntu@SERVER_IP
```

```bash
scp app.conf ubuntu@SERVER_IP:/tmp/
```

---

## 33. What is the difference between password authentication and key authentication?

### Password Authentication

The user provides a password.

### Key Authentication

The client proves possession of a private key corresponding to a public key trusted by the server.

Key-based authentication is commonly preferred for automated and production environments.

---

## 34. How would you disable password authentication?

Edit:

```bash
sudo nano /etc/ssh/sshd_config
```

Set:

```text
PasswordAuthentication no
```

Then validate:

```bash
sudo sshd -t
```

Then restart:

```bash
sudo systemctl restart ssh
```

### Important

Before disabling password authentication, make sure working key-based access has been tested. Otherwise, you can lock yourself out.

---

## 35. How would you improve SSH security?

Common practices include:

* Use SSH keys
* Protect private keys
* Disable unnecessary password authentication
* Avoid direct root login where appropriate
* Keep OpenSSH updated
* Use firewall rules
* Restrict SSH access to trusted networks where possible
* Monitor authentication logs
* Use least privilege
* Use MFA or additional access controls where supported

---

# 🚀 DevOps Scenario-Based Questions

## 36. A server is reachable by ping but SSH is not working. What do you check?

I would check:

```bash
nc -zv SERVER_IP 22
```

Then:

```bash
sudo systemctl status ssh
```

Then:

```bash
sudo ss -ltnp | grep :22
```

Then check:

* Firewall
* Cloud security group
* SSH configuration
* Correct username
* SSH key
* SSH logs

Finally:

```bash
ssh -vvv user@SERVER_IP
```

---

## 37. SSH worked yesterday but stopped working today. How would you troubleshoot?

I would check:

1. Is the server running?
2. Is the IP address correct?
3. Is the network reachable?
4. Is port 22 reachable?
5. Is SSH service running?
6. Did the firewall change?
7. Did the SSH configuration change?
8. Did the SSH key or user permissions change?
9. Check SSH logs.

Commands:

```bash
ping SERVER_IP
nc -zv SERVER_IP 22
sudo systemctl status ssh
sudo ss -ltnp | grep :22
sudo sshd -t
sudo journalctl -u ssh
ssh -vvv user@SERVER_IP
```

---

## 38. Your SSH private key is rejected. What would you check?

I would check:

```bash
ls -l ~/.ssh/
```

Then:

```bash
chmod 600 ~/.ssh/id_ed25519
```

I would verify:

* Correct username
* Correct private key
* Public key exists on server
* `authorized_keys` is correct
* Server permissions
* SSH server configuration

Then use:

```bash
ssh -vvv -i ~/.ssh/id_ed25519 user@SERVER_IP
```

---

## 39. How would you check whether port 22 is reachable?

```bash
nc -zv SERVER_IP 22
```

Or:

```bash
telnet SERVER_IP 22
```

`nc` is generally the more convenient modern choice when available.

---

## 40. How would you execute the same command on multiple servers?

A simple shell loop can be used:

```bash
for server in server1 server2 server3
do
    ssh "$server" "hostname"
done
```

For larger environments, DevOps engineers commonly use configuration-management or automation tools instead of manually looping over SSH commands.

---

# ☁️ Cloud / DevOps Examples

## 41. How do you connect to an AWS EC2 Linux server?

A typical example is:

```bash
ssh -i my-key.pem ubuntu@PUBLIC_IP
```

The exact username depends on the operating system image.

---

## 42. How do you copy an application to a remote server?

```bash
scp -r ./app ubuntu@SERVER_IP:/opt/app/
```

Then connect:

```bash
ssh ubuntu@SERVER_IP
```

---

## 43. How do you restart Nginx remotely?

```bash
ssh ubuntu@SERVER_IP "sudo systemctl restart nginx"
```

---

## 44. How do you check disk usage remotely?

```bash
ssh ubuntu@SERVER_IP "df -h"
```

---

## 45. How do you check memory remotely?

```bash
ssh ubuntu@SERVER_IP "free -h"
```

---

# 🧠 Quick Interview Revision

Remember these:

```text
SSH
│
├── Secure remote access
├── Default port: 22/TCP
├── Client → ssh
├── Server → sshd
├── Key generation → ssh-keygen
├── Public key → authorized_keys
├── Server fingerprints → known_hosts
├── File transfer → scp
├── Key management → ssh-agent / ssh-add
├── Debugging → ssh -vvv
├── SSH service → systemctl
└── Logs → journalctl
```

## 🔑 Key Authentication

```text
Client
  │
  │ Private Key
  ▼
SSH Authentication
  │
  │ Public Key trusted by server
  ▼
Server
  │
  └── ~/.ssh/authorized_keys
```

## 🚨 Troubleshooting Flow

```text
SSH Not Working
       │
       ▼
Check IP
       │
       ▼
Check Network
       │
       ▼
Check Port 22
       │
       ▼
Check sshd
       │
       ▼
Check Firewall
       │
       ▼
Check SSH Config
       │
       ▼
Check Key/Auth
       │
       ▼
Check Logs
       │
       ▼
ssh -vvv
```

# ⭐ Top 10 SSH Interview Questions

1. What is SSH?
2. What is the default SSH port?
3. What is the difference between SSH client and server?
4. What is `sshd`?
5. How does SSH key-based authentication work?
6. What is the difference between private and public keys?
7. What is `authorized_keys`?
8. How do you troubleshoot SSH connection problems?
9. What is the difference between `ssh` and `scp`?
10. How would you secure an SSH server?

# 🎯 Interview Answer

### "Explain SSH in simple words."

> SSH is a secure protocol used to remotely access and manage systems over an encrypted connection. It normally uses TCP port 22. A DevOps engineer uses SSH to connect to Linux servers, execute commands, troubleshoot systems, deploy applications, and transfer files. SSH supports authentication using passwords or, preferably in many production setups, public/private key pairs.

````

