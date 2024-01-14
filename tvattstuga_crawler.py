import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from get_config import get_config

wait_for_clickable_time = 5

# Get username and password from config
username, password = get_config()

# Setup WebDriver
webdriver_service = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)


# Navigate to the login page
print("Navigating to the login page...")
driver.get("https://hamnkaptenen.baxectotal.se/m5webbokning/")

# Find the username, password, and login button elements
print("Finding login elements...")
username_input = driver.find_element("id", "ctl00_ContentPlaceHolder1_tbUsername")
password_input = driver.find_element("id", "ctl00_ContentPlaceHolder1_tbPassword")
login_button = driver.find_element("id", "ctl00_ContentPlaceHolder1_btOK")

# Input username and password
print("Entering username and password...")
username_input.send_keys(username)
password_input.send_keys(password)

# Wait for 5 seconds (you can adjust this if needed)
print("Waiting for 5 seconds...")
time.sleep(5)

# Click the login button
print("Clicking the login button...")
login_button.click()

# Click the first anchor
print("Clicking the first anchor...")
first_anchor = WebDriverWait(driver, wait_for_clickable_time).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'ctl00$ContentPlaceHolder1$dgTerminaler$ctl03$ctl00')]"))
)
first_anchor.click()

# Click the second anchor
print("Clicking the second anchor...")
second_anchor = WebDriverWait(driver, wait_for_clickable_time).until(
    EC.element_to_be_clickable((By.ID, "ctl00_LinkBooking"))
)
second_anchor.click()

# Click the third anchor
print("Clicking the third anchor...")
third_anchor = WebDriverWait(driver, wait_for_clickable_time).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'ctl00$ContentPlaceHolder1$dgForval$ctl02$ctl00')]"))
)
third_anchor.click()

# Click the first input (16:00-19:00)
print("Clicking the first input (16:00-19:00)...")
first_input = WebDriverWait(driver, wait_for_clickable_time).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_2,4,1,']"))
)
first_input.click()

# Click the second input (Boka)
print("Clicking the second input (Boka)...")
second_input = WebDriverWait(driver, wait_for_clickable_time).until(
    EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btMaskingruppRandom"))
)
second_input.click()

# Check if the element with id "ctl00_ContentPlaceHolder1_lblYouHaveBooked" exists
try:
    print("Checking booking status...")
    booked_element = WebDriverWait(driver, wait_for_clickable_time).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_lblYouHaveBooked"))
    )
    print("Du har bokat tisdag 16-19")
except:
    print("Upptaget tisdag 16-19")

# Close the WebDriver
print("Closing the WebDriver...")
driver.quit()

