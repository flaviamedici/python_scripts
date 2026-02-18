# pip install selenium webdriver-manager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def open_page(url, search_box_id, search_term, click_submit):
    #setup Chrome webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open url in Chrome
    driver.get(url)

    #Find the search input field and fill it with the search term
    search_box = driver.find_element(By.ID, search_box_id)
    search_box.send_keys(search_term)
    time.sleep(2)

    #CLick submit or press Enter 
    if click_submit:
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
    else:
        search_box.send_keys(Keys.RETURN)
    return driver

def main():
    #define page url
    site_url = "https://www.wikipedia.org/"
    #The ID of the text box to fill 
    search_box_id = "searchInput"
    search_term = "lent"
    click_submit = True #Set to True if you want to click Submit at the end, otherwise set to False

    #Open the page and perform the search
    try:
        driver = open_page(site_url, search_box_id, search_term, click_submit)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nScript completed: browser remains open.")
        input("Press Enter or ^C to exit the script and close the browser\n")
        driver.quit()

    if __name__ == "__main__":
        main()
