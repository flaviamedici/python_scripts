# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#setup Chrome webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open https://www.google.com in Chrome
driver.get("https://www.google.com")

# Keep the browser open until the user presses Enter
input("Press Enter to close the browser...")
driver.quit()