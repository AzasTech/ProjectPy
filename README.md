# 💾 Auto Disk Space Checker

A Python script that automatically detects all drives on your system, lets you pick which one(s) to check (if multiple exist), prints disk usage, and always saves the report to `disk_report.txt`.

---

## Features
- Auto-detect available drives
- Interactive menu if multiple drives exist
- Automatic check if only one drive
- Shows total, used, free, and usage %
- Warns if disk usage > 80%
- Always saves output to `disk_report.txt`
- Works on Windows

---

## How to Run
```bash
python disk_checker.py
