# 🔓 Huawei Bootloader Breaker

A brute-force script designed to unlock Huawei device bootloaders via fastboot — one code at a time.

This tool attempts to find the correct OEM unlock code by automatically sending sequential fastboot commands using a starting point (default or custom).  
It's useful for older Huawei devices where official bootloader unlock codes are no longer available.

---

## ✨ Features

- ✅ Works via `fastboot oem unlock <code>`
- 🔁 Starts from a default code (`1000000000000000`) or a custom one via CLI argument
- 🗂️ No file creation, no bloat — just pure brute-force
- 💬 Clean loop with real-time output

---

## 🧪 Usage

**💻 On Linux / macOS:**
```
python3 Bootloader-Breaker.py
```

**🪟 On Windows (if Python is installed):**
```
python Bootloader-Breaker.py
```

🛑 You can interrupt the script at any time using `Ctrl + C`.  
💡 The script does not save the last tried code — this is by design for simplicity.

---

## ⚠️ Disclaimer

This tool is intended for **educational and personal use only**.

Using brute-force to unlock a bootloader may:

- ❌ Void your warranty
- ⚠️ Permanently brick your device
- 🚫 Violate terms of service

**Use at your own risk.**
