import time
import csv
import argparse
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("pomodoro_log.csv")

# ---------------- Logging ----------------

def log_session(session_type, duration):
    file_exists = LOG_FILE.exists()
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "session_type", "duration_minutes"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            session_type,
            duration
        ])

# ---------------- Timer ----------------

def countdown(minutes, label):
    seconds = minutes * 60
    print(f"\n⏱️ {label} — {minutes} min")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"\n✅ {label} finished")

# ---------------- Core Logic ----------------

def run_pomodoro(args):
    focus_count = 0

    print("\n🍅 Pomodoro CLI started")
    print("Press CTRL+C to stop\n")

    try:
        while True:
            # Focus
            countdown(args.focus, "Focus")
            log_session("Focus", args.focus)
            focus_count += 1

            # Break logic
            if focus_count % args.cycles == 0:
                countdown(args.long_break, "Long Break")
                log_session("Long Break", args.long_break)
            else:
                countdown(args.short_break, "Short Break")
                log_session("Short Break", args.short_break)

    except KeyboardInterrupt:
        print("\n🛑 Pomodoro stopped")
        print(f"📂 Sessions saved to {LOG_FILE.resolve()}")

# ---------------- CLI ----------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="🍅 Pomodoro Timer CLI"
    )

    parser.add_argument(
        "--focus",
        type=int,
        default=25,
        help="Focus duration in minutes (default: 25)"
    )
    parser.add_argument(
        "--short-break",
        type=int,
        default=5,
        help="Short break duration in minutes (default: 5)"
    )
    parser.add_argument(
        "--long-break",
        type=int,
        default=15,
        help="Long break duration in minutes (default: 15)"
    )
    parser.add_argument(
        "--cycles",
        type=int,
        default=4,
        help="Number of focus sessions before a long break (default: 4)"
    )

    return parser.parse_args()

# ---------------- Entry ----------------

if __name__ == "__main__":
    args = parse_args()
    run_pomodoro(args)


#Some examples for commands to run in CMD
# # Classic Pomodoro
#python pomodoro.py

# Deep focus mode
#python pomodoro.py --focus 50 --short-break 10

# Custom cycles
#python pomodoro.py --cycles 3
 
#another custom 
#python pomodoro.py --focus 50 --short-break 10 --long-break 20 --cycles 4
