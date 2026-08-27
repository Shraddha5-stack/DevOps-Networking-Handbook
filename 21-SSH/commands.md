
# 🔐 Chapter 21 — SSH Commands

## 1. Check SSH Client Version

```bash
ssh -V
````

### Purpose

Checks the installed OpenSSH client version.

### Example

```text
OpenSSH_9.x
```

### DevOps Use

Useful for checking whether SSH is installed and which version is being used.

---

## 2. Connect to a Remote Server

```bash
ssh username@server-ip
```

### Example

```bash
ssh ubuntu@192.168.1.100
```

### Purpose

Connects to a remote Linux server securely using SSH.

---

## 3. Connect Using a Specific Port

```bash
ssh -p 2222 username@server-ip
```

### Example

```bash
ssh -p 2222 ubuntu@192.168.1.100
```

### Purpose

Connects to an SSH server running on a non-default port.

### Default SSH Port

```text
22
```

---

## 4. Connect Using an SSH Private Key

```bash
ssh -i ~/.ssh/id_ed25519 username@server-ip
```

### Example

```bash
ssh -i ~/.ssh/my-server-key ubuntu@192.168.1.100
```

### Purpose

Uses a specific private key for authentication.

### DevOps Use

Commonly used when connecting to cloud servers such as AWS EC2.

---

## 5. Generate an SSH Key Pair

```bash
ssh-keygen -t ed25519
```

### Purpose

Creates an SSH public/private key pair.

### Files

Private key:

```text
~/.ssh/id_ed25519
```

Public key:

```text
~/.ssh/id_ed25519.pub
```

### Important

Never share your private key.

---

## 6. List SSH Keys

```bash
ls -la ~/.ssh
```

### Purpose

Shows SSH configuration files, keys, and known hosts.

---

## 7. Display Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

### Purpose

Displays the public SSH key.

### DevOps Use

The public key can be added to a remote server's:

```text
~/.ssh/authorized_keys
```

---

## 8. Copy Public Key to a Remote Server

```bash
ssh-copy-id username@server-ip
```

### Example

```bash
ssh-copy-id ubuntu@192.168.1.100
```

### Purpose

Copies your public key to the remote server.

### Benefit

After setup, you can usually connect without entering the account password.

---

## 9. Test SSH Connection

```bash
ssh username@server-ip
```

### Purpose

Tests whether you can establish an SSH connection.

---

## 10. SSH Verbose Mode

```bash
ssh -v username@server-ip
```

### Purpose

Shows detailed SSH connection information.

### Useful for

Troubleshooting:

* Authentication problems
* Connection problems
* Key problems
* SSH configuration problems

---

## 11. SSH Very Verbose Mode

```bash
ssh -vvv username@server-ip
```

### Purpose

Displays extremely detailed SSH debugging information.

### DevOps Use

Useful when normal SSH debugging does not provide enough information.

---

## 12. Check Remote SSH Port

```bash
nc -zv server-ip 22
```

### Example

```bash
nc -zv 192.168.1.100 22
```

### Purpose

Checks whether TCP port 22 is reachable.

---

## 13. Check SSH Server Status

Run this on the Linux server:

```bash
sudo systemctl status ssh
```

Some distributions use:

```bash
sudo systemctl status sshd
```

### Purpose

Checks whether the SSH server is running.

---

## 14. Start SSH Server

```bash
sudo systemctl start ssh
```

or:

```bash
sudo systemctl start sshd
```

---

## 15. Stop SSH Server

```bash
sudo systemctl stop ssh
```

or:

```bash
sudo systemctl stop sshd
```

---

## 16. Restart SSH Server

```bash
sudo systemctl restart ssh
```

or:

```bash
sudo systemctl restart sshd
```

### DevOps Use

Useful after modifying SSH server configuration.

---

## 17. Enable SSH at Boot

```bash
sudo systemctl enable ssh
```

### Purpose

Starts the SSH service automatically when the server boots.

---

## 18. Check SSH Listening Port

```bash
sudo ss -ltnp | grep :22
```

### Example Output

```text
LISTEN 0 4096 0.0.0.0:22 0.0.0.0:* users:(("sshd",...))
```

### Purpose

Checks whether SSH is listening on TCP port 22.

---

## 19. View SSH Server Configuration

```bash
sudo cat /etc/ssh/sshd_config
```

### Purpose

Displays the SSH server configuration.

### Common settings

```text
Port 22
PermitRootLogin
PasswordAuthentication
PubkeyAuthentication
```

---

## 20. Check SSH Configuration

```bash
sudo sshd -t
```

### Purpose

Tests the SSH server configuration for syntax errors.

### Important

Run this before restarting SSH after configuration changes.

---

## 21. Copy Files to a Remote Server

```bash
scp file.txt username@server-ip:/path/
```

### Example

```bash
scp app.conf ubuntu@192.168.1.100:/tmp/
```

### Purpose

Securely copies files over SSH.

---

## 22. Copy a Directory to a Remote Server

```bash
scp -r directory/ username@server-ip:/path/
```

### Example

```bash
scp -r project/ ubuntu@192.168.1.100:/opt/
```

---

## 23. Copy a Remote File to Local Machine

```bash
scp username@server-ip:/path/file.txt .
```

### Example

```bash
scp ubuntu@192.168.1.100:/var/log/app.log .
```

---

## 24. SSH Config File

```bash
nano ~/.ssh/config
```

### Purpose

Creates or edits the SSH client configuration.

### Example

```text
Host myserver
    HostName 192.168.1.100
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

Now connect using:

```bash
ssh myserver
```

### Benefit

You don't need to repeatedly type the full connection command.

---

## 25. Set Correct Private Key Permissions

```bash
chmod 600 ~/.ssh/id_ed25519
```

### Purpose

Restricts access to the private key.

### Why?

SSH may reject a private key if its permissions are too open.

---

## 26. Set SSH Directory Permissions

```bash
chmod 700 ~/.ssh
```

### Purpose

Restricts access to the `.ssh` directory.

---

## 27. View Known Hosts

```bash
cat ~/.ssh/known_hosts
```

### Purpose

Shows host keys saved from previously connected SSH servers.

---

## 28. Remove a Host From known_hosts

```bash
ssh-keygen -R server-ip
```

### Example

```bash
ssh-keygen -R 192.168.1.100
```

### Purpose

Removes the saved host key for a server.

### DevOps Use

Useful when a server is rebuilt and its SSH host key changes.

---

## 29. Run a Command on a Remote Server

```bash
ssh username@server-ip "command"
```

### Example

```bash
ssh ubuntu@192.168.1.100 "uptime"
```

### Another Example

```bash
ssh ubuntu@192.168.1.100 "df -h"
```

### DevOps Use

Very useful for remote automation.

---

## 30. Run Multiple Commands Remotely

```bash
ssh username@server-ip "whoami && hostname && uptime"
```

### Purpose

Runs multiple commands on a remote server.

---

## 31. SSH Agent Status

```bash
ssh-add -l
```

### Purpose

Lists keys currently loaded into the SSH agent.

---

## 32. Start SSH Agent

```bash
eval "$(ssh-agent -s)"
```

### Purpose

Starts an SSH authentication agent for the current shell.

---

## 33. Add a Private Key to SSH Agent

```bash
ssh-add ~/.ssh/id_ed25519
```

### Purpose

Adds the private key to the SSH agent.

---

## 34. List Loaded SSH Keys

```bash
ssh-add -l
```

### Purpose

Shows fingerprints of keys loaded in the SSH agent.

---

## 35. Remove All Keys From SSH Agent

```bash
ssh-add -D
```

### Purpose

Removes all identities from the SSH agent.

---

# 🔥 DevOps SSH Troubleshooting Commands

## 36. Check SSH Port

```bash
nc -zv server-ip 22
```

---

## 37. Test Network Connectivity

```bash
ping server-ip
```

### Important

Ping tests ICMP connectivity.

A failed ping does NOT always mean SSH is unavailable because ICMP may be blocked.

---

## 38. Check Route to Server

```bash
ip route get server-ip
```

### Example

```bash
ip route get 192.168.1.100
```

### Purpose

Shows which route/interface Linux will use to reach the server.

---

## 39. Debug SSH Authentication

```bash
ssh -vvv username@server-ip
```

Look for messages related to:

```text
Authentications that can continue
Offering public key
Permission denied
Connection refused
Connection timed out
```

---

## 40. Check SSH Logs

On Ubuntu/Debian:

```bash
sudo journalctl -u ssh
```

or:

```bash
sudo journalctl -u ssh --since "10 minutes ago"
```

### Purpose

Checks SSH server logs.

---

## 41. Follow SSH Logs in Real Time

```bash
sudo journalctl -u ssh -f
```

### Purpose

Continuously displays new SSH log messages.

### DevOps Use

Useful while troubleshooting login attempts.

---

## 42. Check Failed SSH Login Attempts

On systems using `auth.log`:

```bash
sudo grep "Failed password" /var/log/auth.log
```

### Purpose

Finds failed password authentication attempts.

---

## 43. Check Successful SSH Logins

```bash
sudo grep "Accepted" /var/log/auth.log
```

### Purpose

Finds successful SSH authentication events.

---

# 🔐 SSH Security Commands

## 44. Check Root Login Configuration

```bash
sudo grep -i "^PermitRootLogin" /etc/ssh/sshd_config
```

---

## 45. Check Password Authentication

```bash
sudo grep -i "^PasswordAuthentication" /etc/ssh/sshd_config
```

---

## 46. Check Public Key Authentication

```bash
sudo grep -i "^PubkeyAuthentication" /etc/ssh/sshd_config
```

---

## 47. Check SSH Server Process

```bash
ps aux | grep sshd
```

### Purpose

Checks running SSH server processes.

---

# 🚀 DevOps Real-World SSH Examples

## Example 1 — Connect to a Cloud Server

```bash
ssh -i ~/.ssh/aws-key.pem ubuntu@SERVER_IP
```

---

## Example 2 — Check Disk Space Remotely

```bash
ssh ubuntu@SERVER_IP "df -h"
```

---

## Example 3 — Check Memory Remotely

```bash
ssh ubuntu@SERVER_IP "free -h"
```

---

## Example 4 — Check Running Processes

```bash
ssh ubuntu@SERVER_IP "ps aux"
```

---

## Example 5 — Check Listening Ports

```bash
ssh ubuntu@SERVER_IP "sudo ss -ltnp"
```

---

## Example 6 — Copy Application Files

```bash
scp -r ./app ubuntu@SERVER_IP:/opt/app/
```

---

## Example 7 — Restart an Application

```bash
ssh ubuntu@SERVER_IP "sudo systemctl restart nginx"
```

---

# 🧠 Most Important SSH Commands for DevOps

| Command                 | Purpose                    |
| ----------------------- | -------------------------- |
| `ssh user@host`         | Connect to remote server   |
| `ssh -i key user@host`  | Connect using private key  |
| `ssh -p PORT user@host` | Connect using custom port  |
| `ssh -v user@host`      | Debug SSH connection       |
| `ssh -vvv user@host`    | Detailed SSH debugging     |
| `ssh-keygen`            | Generate SSH keys          |
| `ssh-copy-id`           | Copy public key            |
| `scp`                   | Secure file copy           |
| `ssh-add`               | Manage SSH agent keys      |
| `ssh-keygen -R`         | Remove known host          |
| `ss -ltnp`              | Check listening ports      |
| `systemctl status ssh`  | Check SSH service          |
| `sshd -t`               | Validate SSH configuration |
| `journalctl -u ssh`     | Check SSH logs             |

---

# 🎯 Production Troubleshooting Flow

When SSH is not working, check in this order:

```text
1. Check network connectivity
        ↓
2. Check server IP
        ↓
3. Check route
        ↓
4. Check port 22
        ↓
5. Check SSH service
        ↓
6. Check firewall
        ↓
7. Check SSH configuration
        ↓
8. Check authentication/key
        ↓
9. Check SSH logs
```

Useful commands:

```bash
ping SERVER_IP
ip route get SERVER_IP
nc -zv SERVER_IP 22
sudo systemctl status ssh
sudo ss -ltnp | grep :22
sudo sshd -t
ssh -vvv user@SERVER_IP
sudo journalctl -u ssh
```

---

# 💡 Important SSH Concepts

```text
SSH
├── Client
├── Server
├── Port 22
├── Authentication
│   ├── Password
│   └── Public/Private Key
├── ssh
├── ssh-keygen
├── ssh-copy-id
├── scp
├── ssh-agent
├── known_hosts
└── authorized_keys
```

---

# 🔑 Important Files

| File                     | Purpose                          |
| ------------------------ | -------------------------------- |
| `~/.ssh/id_ed25519`      | Private key                      |
| `~/.ssh/id_ed25519.pub`  | Public key                       |
| `~/.ssh/authorized_keys` | Authorized public keys on server |
| `~/.ssh/known_hosts`     | Known server host keys           |
| `~/.ssh/config`          | SSH client configuration         |
| `/etc/ssh/sshd_config`   | SSH server configuration         |

---

