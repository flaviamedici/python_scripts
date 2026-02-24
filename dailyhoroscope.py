import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

SIGN = "gemini"  # change to your zodiac sign

URL = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={SIGN}"

def get_horoscope():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    horoscope_text = soup.find("div", class_="main-horoscope").p.text
    return horoscope_text.strip()

def show_popup(text):
    root = tk.Tk()
    root.withdraw()  # hide main window

    today = datetime.now().strftime("%A, %B %d")
    messagebox.showinfo(f"Your Horoscope – {today}", text)

if __name__ == "__main__":
    try:
        horoscope = get_horoscope()
        show_popup(horoscope)
    except Exception as e:
        show_popup("Could not load horoscope today 🌙\n\n" + str(e))
