# -Advanced-Keylogger
An advanced keylogger with encrypted logging, stealth mode, screenshot capture, and Telegram exfiltration. Designed as a cybersecurity research tool for ethical security analysis and keylogging detection studies.
Advanced Keylogger

Overview

This is an advanced keylogger designed for educational and security research purposes. It captures keystrokes, records active windows, takes screenshots, and exfiltrates data via Telegram while implementing encryption and stealth features. This project is intended to help security professionals understand keylogger techniques and develop defenses against them.

Features

Efficient Key Capture – Logs keystrokes with timestamps and application context.

Advanced Formatting – Organizes logs into readable JSON format.

Screenshot Capture – Periodically captures and encrypts screenshots.

Data Encryption – Uses AES encryption for secure log storage and transmission.

Telegram Exfiltration – Sends encrypted logs and screenshots to a configured Telegram bot.

Stealth Mode – Runs in the background with minimal footprint.

Anti-Detection Techniques – Avoids basic detection methods and process monitoring.

Installation & Setup

Prerequisites

Ensure you have Python 3 installed along with the required dependencies:

pip install requests pycryptodome pyautogui psutil pynput pywin32

Configuration

Set up a Telegram bot

Create a Telegram bot via BotFather and obtain the bot token.

Get your Telegram chat ID by messaging your bot and using the API call:

https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates

Edit config variables in the script:

Replace BOT_TOKEN with your Telegram bot token.

Replace CHAT_ID with your Telegram chat ID.

Set a SECRET_KEY for encryption (16, 24, or 32 bytes).

Usage

Run the keylogger script:

python keylogger.py

The script will:

Capture and log keystrokes with active window details.

Take encrypted screenshots at defined intervals.

Periodically send logs and screenshots to the configured Telegram bot.

Security & Ethical Considerations

This tool is intended for educational and security research purposes only.

Unauthorized use of this software to log or steal data without consent is illegal.

Use it responsibly to test and improve your security defenses.

Technologies Used

Python – Main programming language.

Pycryptodome – Encryption library.

Pyautogui – For capturing screenshots.

Psutil – Process monitoring.

Pynput – Keyboard event tracking.

Requests – Telegram API communication.

Defenses Against Keyloggers

To protect against keyloggers like this:

Use antivirus software and behavior-based malware detection.

Enable two-factor authentication (2FA) for sensitive accounts.

Regularly check for unknown processes running on your system.

Use a virtual keyboard for sensitive inputs.

Monitor network traffic for suspicious outgoing connections.

Disclaimer

This project is strictly for research and ethical hacking purposes. Any unauthorized use is at your own risk and may result in legal consequences.

Contributions

Contributions are welcome for improving detection evasion techniques, enhancing encryption, or adding new security-related features.
