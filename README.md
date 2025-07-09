# 🧠 GitHub Daily Quote Commit

This repository commits a daily inspirational quote to `quotes.txt`.

The quote is fetched from a public API and pushed via cron using the `auto_commit.py` script.

## 🔧 Setup Instructions

1. Clone this repository.
2. Make sure you have Python 3 and `requests` installed.
3. Set up Git credentials (`git config user.name` and `user.email`).
4. Run manually or add to crontab:

### Example Crontab:
```
0 8 * * * /usr/bin/python3 /path/to/github-auto-commit-quotes/auto_commit.py
```

## 📌 Dependencies
- Python 3.x
- requests (`pip install requests`)
