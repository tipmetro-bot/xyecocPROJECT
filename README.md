<div align="center">

# 🟢 xyecocPROJECT

### OSINT TOOL v11.2 — no api • no mercy

[![Python](https://img.shields.io/badge/Python-3.8%2B-00ff9f?style=for-the-badge&logo=python&logoColor=black)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-ff0040?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-00b3ff?style=for-the-badge)]()
[![No API](https://img.shields.io/badge/No%20API-Required-b026ff?style=for-the-badge)]()
[![Stars](https://img.shields.io/github/stars/USERNAME/xyecocPROJECT?style=for-the-badge&color=00ff9f)](https://github.com/USERNAME/xyecocPROJECT/stargazers)

**A modern OSINT tool with a graphical interface.  
No API keys required. Everything local. Everything free.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Team](#-team) • [License](#-license)

</div>

---

## ⚡ Features

| Module | What it does |
|--------|--------------|
| 🖥 **IP INFO** | Country, region, city, ISP, coordinates, timezone by IP |
| 🌐 **DNS** | A, AAAA, MX, NS, TXT, CNAME records |
| 📡 **HTTP** | Full HTTP headers, status code, server info |
| 🗂 **DOMAIN REPORT** | Full domain report → HTML file on your desktop |
| 📱 **PHONE REPORT** | Detects carrier, region, country by number → HTML report |
| 💬 **CHAT SYSTEM** | Local chats, groups, user search, profiles |

### 🎨 Under the Hood

- ✅ **Animated GUI** on Tkinter — particles connected by lines, react to mouse
- ✅ **Register / Login** — email + password (SHA256 + salt), nickname, username
- ✅ **Profile** in the top-left corner — click to edit
- ✅ **User Agreement** — generated as HTML, opens in browser
- ✅ **Chat system** — private chats, groups, search for users and chats, click an author → profile
- ✅ **HTML reports** on your desktop with auto-increment (`XYECOC-создано_1.html`, `_2`, ...)
- ✅ **No API keys** — works purely on open sources
- ✅ **100% local** — data stored in `~/.xyecoc_*.json`, nothing leaves your machine

---

## 📸 Screenshots

> Replace these placeholders with your own screenshots after upload

| Main Window | Chats | Domain Report |
|:---:|:---:|:---:|
| ![main](screenshots/main.png) | ![chats](screenshots/chats.png) | ![report](screenshots/report.png) |

| Register | Profile | Agreement |
|:---:|:---:|:---:|
| ![reg](screenshots/register.png) | ![profile](screenshots/profile.png) | ![eula](screenshots/agreement.png) |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/xyecocPROJECT.git
cd xyecocPROJECT
```

### 2. Install dependencies

```bash
pip install requests python-whois dnspython
```

**Requires Python 3.8+** and `tkinter` (usually bundled with Python).

<details>
<summary>🐧 Linux — installing tkinter</summary>

```bash
sudo apt install python3-tk
```
</details>

<details>
<summary>🍎 macOS — installing tkinter</summary>

```bash
brew install python-tk
```
</details>

### 3. Run

```bash
python xyecoc.py
```

---

## 🎮 Usage

### First launch

1. A **login window** opens — click "No account? Register"
2. Fill in: email, nickname, username, password
3. Check the box **"I accept the agreement"** (you can read it by clicking)
4. Register → auto login

### Modules

**🖥 IP INFO**
```
1. Click IP INFO
2. Enter an IP (e.g. 8.8.8.8)
3. Press Enter → get country, ISP, coordinates
```

**🌐 DOMAIN REPORT**
```
1. Click 🌐 DOMAIN
2. Enter a domain (e.g. google.com)
3. Press Enter → XYECOC-создано_1.html is created on your desktop
4. Opens in your browser automatically
```

**📱 PHONE REPORT**
```
1. Click 📱 PHONE REPORT
2. Enter a phone number (+79001234567 or 89001234567)
3. Press Enter → xyecoc-number-1.html is created on your desktop
4. Contains: carrier, region, country + links for manual lookup
```

**💬 CHATS**
```
1. Click 💬 CHATS
2. Create a chat or a group
3. Search for users by nickname / username
4. Click a message author → profile → send DM
```

---

## 📁 Structure

```
xyecocPROJECT/
├── xyecoc.py              # main script
├── agreement.html         # generated automatically
├── README.md
├── LICENSE
└── screenshots/           # screenshots for README
```

**User files** (created in your home folder):
```
~/.xyecoc_users.json       # user database (SHA256 passwords)
~/.xyecoc_session.json     # current session
~/.xyecoc_chats.json       # all chats and messages
```

**Reports** (created on your desktop):
```
Desktop/XYECOC-создано_1.html
Desktop/XYECOC-создано_2.html
Desktop/xyecoc-number-1.html
Desktop/xyecoc-number-2.html
```

---

## 🛡 Security

- ✅ Passwords are **hashed with SHA256 + salt** (16 bytes)
- ✅ Everything is stored **locally** — no servers, no data transmission
- ✅ No external API keys
- ✅ Open source — you can audit every line

---

## ⚠️ Disclaimer

This project is intended **for educational purposes**.

**FORBIDDEN:**
- ❌ Stalking, harassment, bullying
- ❌ Illegal collection of personal data
- ❌ Sharing other people's data with third parties
- ❌ Hacking, DDoS, fraud

**ALLOWED:**
- ✅ Self-OSINT (looking up information about yourself)
- ✅ Checking the security of your own resources
- ✅ Educational and research tasks
- ✅ Pentest under an official contract

**The authors are not responsible for the actions of third parties.**

---

## 👥 Team

### Creators
- **vobas25**
- **mr iron**
- **окак 67** (also known as **greencat**)
- **sakura.cc** (also known as **sakuradev**) — Roblox scripts, injectors. *Favorite member. Didn't test the project.*

### Lead
- **окак 67** (greencat)

### Admins
- **vobas25**
- **mr iron**
- **dsfsfsdfsdfds**

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork the repository
2. Create a branch (`git checkout -b feature/amazing`)
3. Commit (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing`)
5. Open a Pull Request

---

## 📜 License

MIT License — do whatever you want, just don't change the authorship.

See [LICENSE](LICENSE) for details.

---

## ⭐ Support the project

If you like xyecocPROJECT — drop a **star** ⭐ and tell your friends.

<div align="center">

**no api • no mercy**

© 2026 xyecocPROJECT

</div>
