
# Honeypot with Pentbox on Kali Linux

A simple lab project in which I set up a low-interaction honeypot on port 443 using **Pentbox** to detect and log connection attempts.

---

## Project Goal

- Understand how a honeypot works and what it is used for in network security
- Open a port that imitates a real service
- Detect access attempts and record them in a log file

## Tools Used

| Tool | Purpose |
|------|---------|
| Kali Linux | Operating system / lab environment |
| Pentbox 1.8 | Security toolkit with a built-in honeypot |
| Web browser | Simulating a connection attempt |

---

## Procedure

### 1. Start Pentbox

```bash
cd pentbox-1.8
./pentbox.rb
```

### 2. Configure the honeypot

| Input | Meaning |
|-------|---------|
| `2` | Select Network tools |
| `3` | Select Honeypot |
| `2` | Manual Configuration |
| `443` | Open the port (default HTTPS port) |
| `Caught You!!` | Fake message sent to the attacker |
| `y` | Save a log of intrusion attempts |
| `Enter` | Accept the default log file path |
| `n` | Disable the beep sound on intrusion |

The honeypot is now listening on port 443 and waiting for incoming connections.

### 3. Simulate an attack

The IP address of the Kali machine was opened in a browser:

```
https://<IP-ADDRESS>
```

---

## Result

**Browser:** `Secure Connection Failed`

**Terminal (Pentbox):**

```
INTRUSION ATTEMPT DETECTED! from <IP-ADDRESS>:<PORT> (<DATE/TIME>)
```


### Analysis

On port 443 the browser expects a **TLS handshake** (HTTPS). The Pentbox honeypot, however, is just a simple TCP listener without encryption and replies with the plain-text message `Caught You!!`. As a result, the browser aborts the connection with "Secure Connection Failed".

**The key point:** the connection was still established. The honeypot detected the access attempt and logged the source IP, port and timestamp, which is exactly its purpose.

---

## What I Learned

- How a **low-interaction honeypot** works and where its limitations are
- The difference between an open TCP port and a real service (e.g. HTTPS with TLS)
- How access attempts are detected and logged for later analysis
- Why honeypots are useful as an **early warning system** in networks

## Security Notice

This project was carried out exclusively in an **isolated lab environment**. Honeypots should never be run on production systems or on networks without permission.

## Possible Extensions

- [ ] Set up a realistic SSH honeypot with **Cowrie**
- [ ] Simulate multiple services at once with **OpenCanary**
- [ ] Visualize logs with the **ELK stack**
- [ ] Test and analyze port scans against the honeypot with **Nmap**
