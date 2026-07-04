# phishing-awareness
A Python-based phishing detection and triage project inspired by DecodeLabs Cyber Security Project 3. Includes red-flag detection for suspicious domains, urgent bypass requests, malicious attachments, and phishing vectors (email, SMS, voice, QR codes).
# 🛡️ Phishing Awareness Toolkit
A Python-based phishing detection and triage project inspired by **DecodeLabs Cyber Security Project 3**.  
This toolkit helps identify suspicious emails and messages by scanning for **red flags** such as spoofed domains, urgent bypass requests, malicious attachments, and phishing vectors (email, SMS, voice, QR codes). 
## 📌 Features
- Detect **suspicious sender domains** and display name spoofing  
- Flag **urgency triggers** (e.g., "IMMEDIATE ACTION REQUIRED")  
- Identify **lookalike domains** (typosquatting, combosquatting, homoglyph attacks)  
- Scan for **dangerous attachments** (.iso, .js, .scr, .exe)  
- Provide **triage outcomes**:
  - ✅ Safe → Close  
  - ⚠️ Suspicious → Warn User  
  - 🚨 Malicious → Block & Escalate  
## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- Git installed
### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/phishing-awareness-toolkit.git
# Navigate into the project folder
cd phishing-awareness-toolkit
Usage
Run the phishing detector script:
bash

python phishing_detector.py

Example output:
Code

Phishing suspected ⚠️
Red Flags: ['Suspicious sender domain',
            'Urgency trigger detected',
            'Suspicious link detected: http://secure-login.company-update.com',
            'Malicious attachment: transfer_instructions.iso']


📂 Project Structure
Code

phishing-awareness-toolkit/
│
├── phishing_detector.py   # Core detection logic
├── README.md              # Documentation
└── examples/              # Sample phishing emails/messages


🎯 Project Goals
Strengthen the Human Firewall by training users to spot phishing attempts
Provide a simulation toolkit for realistic phishing scenarios
Build a portfolio-ready cybersecurity project showcasing threat-hunting - hunting skills 
