from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

chrome_driver_path = "C:\\Users\\Test\\Desktop\\Red_Packet\\chromedriver-win64\\chromedriver.exe"

def setup_vanity_eth_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    return webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

def setup_incognito_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    return webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

def generate_eth_vanity_address(driver):
    driver.get("https://vanity-eth.tk/")
    time.sleep(random.uniform(1, 3))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-panel > form > div:nth-child(6) > div:nth-child(1) > input.button-large.hide-prerender"))
    ).click()
    eth_address = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div:nth-child(4) > div > div > div > div.col > div:nth-child(1) > span"))
    ).text
    return eth_address

def submit_eth_to_crystalsea(eth_address):
    incognito_driver = setup_incognito_driver()
    try:
        incognito_driver.get("https://crystalsea.org/?refer=5c5c99")
        time.sleep(random.uniform(1, 3))
        WebDriverWait(incognito_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#username"))
        ).send_keys(eth_address)
        submit_button = WebDriverWait(incognito_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitAirdrop"))
        )
        submit_button.click()
        time.sleep(2)
    finally:
        incognito_driver.quit()

if __name__ == "__main__":
    vanity_eth_driver = setup_vanity_eth_driver()
    try:
        while True:
            eth_vanity_address = generate_eth_vanity_address(vanity_eth_driver)
            submit_eth_to_crystalsea(eth_vanity_address)
            time.sleep(10)
    finally:
        vanity_eth_driver.quit()