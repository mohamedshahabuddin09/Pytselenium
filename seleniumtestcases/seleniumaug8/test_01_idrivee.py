# Open the Browser
# Navigate to a URL
# Find the Email WebElement and put email id = “abc@gmail.com”
# Find the Password input box and enter the password = 123
# Click on the button - Sign in


# Verify that the Dashboard is loaded - PyTest
# Create a Report to send to QA Lead - HTML --> Allure Report

import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_idrive():
    LOGGER = logging.getLogger(__name__)
    # Selenium API - Create Session
    driver = webdriver.Chrome()
    # driver.implicitly_wait(20)
    # # Tell Webdriver to wait for 20 Seconds to Load - All the elements
    # # What if e1,e2,e3 <  20 waste of time

    driver.maximize_window()

    # Open the Browser
    # Navigate to a URL
    # Command - driver.get ( Navigate command to Existing Session)
    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.NAME, "username")
    username.send_keys("shahabuddin202020@gmail.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("Shabu@786")


    submit_button = driver.find_element(By.CSS_SELECTOR, "#frm-btn")
    submit_button.click()

    time.sleep(50)

    add_button = driver.find_element(By.ID,"add-device-header-btn")
    add_button.click()
    time.sleep(50)
    download_btn = driver.find_element(By.XPATH, "//*[@id='id-card-bdy-backup-agent-win']/button")
    download_btn.click()
