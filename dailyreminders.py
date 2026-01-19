import time
from datetime import datetime, time as dtime

# -------- DAILY SCHEDULE --------
# 24-hour format (HH, MM)

SCHEDULE = [
    {
        "start": dtime(12, 0),
        "end": dtime(12, 30),
        "activity": "Go for a walk 🚶"
    },
    {
        "start": dtime(12, 30),
        "end": dtime(13, 0),
        "activity": "Meditate for 10 minutes 🧘"
    },
    {
        "start": dtime(14, 0),
        "end": dtime(15, 0),
        "activity": "Study 📚"
    }
]
# --------------------------------

def is_within_time_block(now, start, end):
    return start <= now < end

def main():
    print("\n⏰ Daily Schedule Reminder Started")
    print("Press CTRL+C to stop\n")

    triggered_today = set()
    current_date = datetime.now().date()

    try:
        while True:
            now = datetime.now()
            now_time = now.time()

            # Reset reminders at midnight
            if now.date() != current_date:
                triggered_today.clear()
                current_date = now.date()

            for block in SCHEDULE:
                block_id = (block["start"], block["end"], block["activity"])

                if (
                    is_within_time_block(now_time, block["start"], block["end"])
                    and block_id not in triggered_today
                ):
                    print(
                        f"\n🔔 Reminder ({block['start'].strftime('%H:%M')} - "
                        f"{block['end'].strftime('%H:%M')}):"
                    )
                    print(f"👉 {block['activity']}\n")
                    triggered_today.add(block_id)

            time.sleep(30)

    except KeyboardInterrupt:
        print("\n🛑 Reminder service stopped")

if __name__ == "__main__":
    main()
