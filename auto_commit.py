#!/usr/bin/env python3
import requests
import datetime
import os
import subprocess

def fetch_quote():
    try:
        res = requests.get("https://api.quotable.io/random", timeout=10)
        data = res.json()
        return f'"{data["content"]}" — {data["author"]}'
    except Exception as e:
        return f"Quote fetch failed: {e}"

def update_and_commit():
    quote = fetch_quote()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("quotes.txt", "a") as f:
        f.write(f"{timestamp} - {quote}\n")
    subprocess.run(["git", "add", "quotes.txt"])
    subprocess.run(["git", "commit", "-m", f"Daily quote update: {timestamp}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    update_and_commit()
