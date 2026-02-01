import time
import argparse
from datetime import datetime, time as dtime

# -------- DAILY SCHEDULE (EDIT HERE) --------
# 24-hour format

SCHEDULE = [
    {
        "start": "12:00",
        "end": "12:30",
        "activity": "Go for a walk 🚶"
    },
    {
        "start": "12:30",
        "end": "13:00",
        "activity": "Meditate for 10 minutes 🧘"
    },
    {
        "start": "14:00",
        "end": "15:00",
        "activity": "Study 📚"
    }

]
# -------------------------------------------

def parse_time(value):
    hour, minute = map(int, value.split(":"))
    return dtime(hour, minute)

def build_schedule():
    parsed = []
    for block in SCHEDULE:
        parsed.append({
            "start": parse_time(block["start"]),
            "end": parse_time(block["end"]),
            "activity": block["activity"]
        })
    return parsed

def is_within_block(now, start, end):
    return start <= now < end

def run_reminder(interval):
    schedule = build_schedule()

    print("\n⏰ Daily Reminder CLI started")
    print("Press CTRL+C to stop\n")

    triggered_today = set()
    current_date = datetime.now().date()

    try:
        while True:
            now = datetime.now()
            now_time = now.time()

            # Reset at midnight
            if now.date() != current_date:
                triggered_today.clear()
                current_date = now.date()

            for block in schedule:
                block_id = (block["start"], block["end"], block["activity"])

                if (
                    is_within_block(now_time, block["start"], block["end"])
                    and block_id not in triggered_today
                ):
                    print(
                        f"\n🔔 Reminder "
                        f"({block['start'].strftime('%H:%M')} - "
                        f"{block['end'].strftime('%H:%M')})"
                    )
                    print(f"👉 {block['activity']}\n")
                    triggered_today.add(block_id)

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n🛑 Reminder service stopped")

# ---------------- CLI ----------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="⏰ Daily Schedule Reminder CLI"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=30,
        help="Check interval in seconds (default: 30)"
    )

    return parser.parse_args()

# ---------------- Entry ----------------

if __name__ == "__main__":
    args = parse_args()
    run_reminder(args.interval)
