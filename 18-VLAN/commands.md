# VLAN Commands Cheat Sheet

| Command | Purpose |
|---|---|
| `bridge vlan show` | Display VLAN configuration |
| `bridge -d vlan show` | Display detailed VLAN information |
| `bridge link` | Show bridge interfaces and their state |
| `ip -d link show type vlan` | Show VLAN interfaces |
| `ip link show` | Display network interfaces |
| `ip addr show` | Display IP addresses |
| `ip route` | Display routing table |
| `bridge fdb show` | Display forwarding database |
| `sudo ip link add link eth0 name eth0.10 type vlan id 10` | Create VLAN 10 interface |
| `sudo ip link set eth0.10 up` | Bring VLAN interface up |
| `sudo ip link delete eth0.10` | Delete VLAN interface |
