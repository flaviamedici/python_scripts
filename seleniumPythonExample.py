from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    # Login
    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password = driver.find_element(By.ID, "password")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    password.send_keys(Keys.RETURN)

    # Add first item to cart
    add_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))
    )
    add_button.click()

    # Click cart
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    # Checkout
    checkout = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout.click()

    # Fill checkout form
    driver.find_element(By.ID, "first-name").send_keys("Flavia")
    driver.find_element(By.ID, "last-name").send_keys("Medici")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    print("Checkout page reached successfully!")

    driver.quit()

if __name__ == "__main__":
    main()
