from datetime import datetime, time as dtime
import time
import sys
import tkinter as tk
from tkinter import messagebox

REMINDER_TIMES = [
    dtime(8, 55),
    dtime(9, 55),
    dtime(10, 55),
    dtime(11, 55),
    dtime(12, 55),
    dtime(13, 55),
    dtime(14, 55),
    dtime(15, 55),
]

MESSAGE = "Get up and stretch! It's time for your daily standup reminder."

def should_remind(now):
    return now.time().replace(second=0, microsecond=0) in REMINDER_TIMES

def remind():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Reminder", MESSAGE)
    root.destroy()

def main():
    last_shown = None
    while True:
        now = datetime.now()
        key = now.strftime("%Y-%m-%d %H:%M")
        if should_remind(now) and key != last_shown:
            remind()
            last_shown = key
        time.sleep(20)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)