import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from windows_toasts import Toast, WindowsToaster

JOB_URL = "https://hiring.amazon.com/app#/jobSearch"
TARGET_TITLE = "Locker+ Retail Associate"
TIMEOUT = 30  # seconds

toaster = WindowsToaster("Amazon Job Checker")


def notify_job_found():
    toast = Toast()
    toast.text_fields = [
        "Amazon job found",
        f"'{TARGET_TITLE}' is available."
    ]
    toaster.show_toast(toast)


from selenium.webdriver.common.keys import Keys

def check_job():
    options = Options()
    # While debugging, keep this commented so you can see the browser:
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(JOB_URL)
        wait = WebDriverWait(driver, TIMEOUT)

        # 1) Click the "I consent" button
        try:
            consent_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[data-test-id='consentBtn']")
                )
            )
            consent_button.click()
            print("Clicked 'I consent' button.")
            time.sleep(1)
        except Exception:
            print("Could not click 'I consent' (not found or already accepted).")

        # 2) Click the close (X) button on the consent card popup
        try:
            close_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[aria-label='Close cookie consent card popup']")
                )
            )
            close_button.click()
            print("Clicked close cookie consent popup.")
            time.sleep(1)
        except Exception:
            print("Could not click close cookie consent popup (not found).")

        # 3) Wait for search input to be present
        search_input = wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "input[data-test-component='StencilSearchFieldInput'][placeholder='Search jobs']",
                )
            )
        )

        # 4) Type the job title and press Enter
        search_input.clear()
        search_input.send_keys(TARGET_TITLE)
        search_input.send_keys(Keys.ENTER)
        print("Typed job title into search and pressed Enter.")
        time.sleep(5)  # wait for results to update

        # 5) Look for the job title text anywhere on the page
        found = False
        elements = driver.find_elements(
            By.XPATH,
            "//*[contains(normalize-space(text()), 'Locker+ Retail Associate')]",
        )

        print(f"Found {len(elements)} elements containing the text snippet.")

        for el in elements:
            txt = el.text.strip()
            print("Candidate element text:", repr(txt))
            if "Locker+ Retail Associate" in txt:
                found = True
                break

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
