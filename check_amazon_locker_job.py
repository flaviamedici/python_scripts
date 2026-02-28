# file: check_amazon_locker_job.py

import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from windows_toasts import Toast, WindowsToaster # <- Windows-Toasts library [web:27]

JOB_URL = "https://hiring.amazon.com/app#/jobSearch"
TARGET_TITLE = "Locker+ Retail Associate"
TIMEOUT = 30  # seconds

# Create toaster once
toaster = WindowsToaster("Amazon Job Checker")  # app name shown in notification [web:27]

def notify_job_found():
    """Show a Windows toast when the job is found."""
    title = "Amazon job found"
    message = f"'{TARGET_TITLE}' is available."
    toast = ToastText2(title, message)
    toaster.show_toast(toast)  # simple, blocking toast [web:27]

def check_job():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(JOB_URL)

        wait = WebDriverWait(driver, TIMEOUT)
        job_cards = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[data-testid='job-card'], .job-card, [class*='JobCard']")
            )
        )

        found = False
        for card in job_cards:
            try:
                title_el = card.find_element(By.CSS_SELECTOR, "h2, h3, [data-testid='job-title']")
                title_text = title_el.text.strip()
                if title_text == TARGET_TITLE:
                    found = True
                    break
            except Exception:
                continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if found:
            print(f"[{timestamp}] Job FOUND: {TARGET_TITLE}")
            notify_job_found()
        else:
            print(f"[{timestamp}] Job NOT found: {TARGET_TITLE}")

    finally:
        driver.quit()

if __name__ == "__main__":
    check_job()
