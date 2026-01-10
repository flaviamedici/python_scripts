import csv
import random
from datetime import datetime
from pathlib import Path

# -------- CONFIG --------
DATA_FILE = Path("daily_journal_log.csv")

JOURNAL_PROMPTS = [
    "What was the highlight of your day?",
    "What challenged you today and how did you handle it?",
    "What did you learn today?",
    "What made you smile today?",
    "What is something you want to improve tomorrow?",
    "How did you take care of yourself today?",
    "What are you proud of today?"
]
# ------------------------

def get_today():
    return datetime.now().strftime("%Y-%m-%d")

def get_journal_prompt():
    return random.choice(JOURNAL_PROMPTS)

def ask_gratitude():
    print("\n🙏 Gratitude Time (3 things):")
    gratitude = []
    for i in range(1, 4):
        item = input(f"  {i}. ")
        gratitude.append(item)
    return " | ".join(gratitude)

def ask_mood():
    while True:
        try:
            mood = int(input("\n😊 Mood today (1 = awful, 5 = great): "))
            if 1 <= mood <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a number.")
    note = input("Mood note (optional): ")
    return mood, note

def save_entry(date, prompt, journal, gratitude, mood, mood_note):
    file_exists = DATA_FILE.exists()

    with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "date",
                "journal_prompt",
                "journal_entry",
                "gratitude",
                "mood_score",
                "mood_note"
            ])
        writer.writerow([
            date,
            prompt,
            journal,
            gratitude,
            mood,
            mood_note
        ])

def main():
    print("\n📝 Daily Journal Automation\n" + "-" * 30)
    today = get_today()

    prompt = get_journal_prompt()
    print(f"\n📌 Journal Prompt:\n{prompt}")
    journal_entry = input("\nYour response:\n")

    gratitude = ask_gratitude()
    mood, mood_note = ask_mood()

    save_entry(
        today,
        prompt,
        journal_entry,
        gratitude,
        mood,
        mood_note
    )

    print("\n✅ Entry saved successfully!")
    print(f"📂 File: {DATA_FILE.resolve()}")

if __name__ == "__main__":
    main()
