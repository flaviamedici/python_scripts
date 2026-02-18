from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")
    
    search = driver.find_element(By.ID, "searchInput")
    search.send_keys("Seattle")
    search.send_keys(Keys.RETURN)

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
