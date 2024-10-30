import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome_driver_path = "C:\\Users\\Test\\Desktop\\Red_Packet\\chromedriver-win64\\chromedriver.exe"

def setup_driver(headless=True, incognito=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    if incognito:
        chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors=yes")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

def check_url_availability(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            print(f"Attempt {attempt + 1} failed: Unable to connect to {url}")
            time.sleep(2)
    return False

def generate_eth_vanity_address(driver):
    print("Generating ETH Address...")
    driver.get("https://vanity-eth.tk/")
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-panel > form > div:nth-child(6) > div:nth-child(1) > input.button-large.hide-prerender"))
    ).click()
    eth_address = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div:nth-child(4) > div > div > div > div.col > div:nth-child(1) > span"))
    ).text
    print(f"Generated ETH Address: {eth_address}")
    return eth_address

def submit_eth_to_crystalsea(eth_address, refer_link, save_refer=True, driver=None):
    print(f"Submitting ETH Address to CrystalSea with refer link {refer_link}...")
    incognito_driver = setup_driver(headless=True, incognito=True) if driver is None else driver
    try:
        if check_url_availability(refer_link):
            incognito_driver.get(refer_link)
        else:
            print(f"Skipping {refer_link}: Connection refused after multiple attempts.")
            return

        WebDriverWait(incognito_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#username"))
        ).send_keys(eth_address)
        
        submit_button = WebDriverWait(incognito_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitAirdrop"))
        )
        
        incognito_driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(1)
        incognito_driver.execute_script("arguments[0].click();", submit_button)
        
        refer_generated = WebDriverWait(incognito_driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#airdrop-block > div.text-break > span.text-primary.copy"))
        ).text
        print(f"Received Generated Referral Link: {refer_generated}")

        if save_refer:
            save_eth_and_refer(eth_address, refer_generated)
        
    finally:
        if driver is None:
            incognito_driver.quit()

def save_eth_and_refer(eth_address, refer_generated):
    with open("eth_addresses_and_refs.txt", "a") as file:
        file.write(f"ETH Address: {eth_address} | Referral Link: {refer_generated}\n")
    print(f"Saved: ETH Address: {eth_address} | Referral Link: {refer_generated}")

def check_referral_count(driver):
    driver.refresh()
    referral_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#airdrop-block > div.row.mt-4.text-center.justify-content-between > div:nth-child(2) > div.heading-h5.text-primary"))
    ).text
    return int(referral_count)

def main():
    try:
        while True:
            try:
                print("\nChoose an option:")
                print("1) Generate 50 Referrals per link from eth_addresses_and_refs.txt")
                print("2) Generate Referral from ETH Address File and save ETH and refer link")
                
                choice = input("Enter your choice (1 or 2): ")
            
            except KeyboardInterrupt:
                print("\nProcess interrupted by user during option selection. Exiting gracefully.")
                break  # Exit the main loop

            if choice == "1":
                try:
                    with open("eth_addresses_and_refs.txt", "r") as file:
                        referral_links = [line.split("| Referral Link: ")[1].strip() for line in file.readlines() if "| Referral Link: " in line]
                    
                    if not referral_links:
                        print("No referral links found in eth_addresses_and_refs.txt.")
                        continue

                    vanity_eth_driver = setup_driver(headless=True)
                    crystalsea_driver = setup_driver(headless=True, incognito=True)

                    for refer_link in referral_links:
                        print(f"\nProcessing referral link: {refer_link}")
                        for i in range(1, 51):
                            eth_vanity_address = generate_eth_vanity_address(vanity_eth_driver)
                            submit_eth_to_crystalsea(eth_vanity_address, refer_link, save_refer=False, driver=crystalsea_driver)
                            time.sleep(1)
                            if i % 5 == 0:
                                referrals_done = check_referral_count(crystalsea_driver)
                                print(f"Referrals completed: {referrals_done}")
                                if referrals_done >= 50:
                                    print("50 referrals generated.")
                                    break
                        else:
                            continue
                        break
                
                except FileNotFoundError:
                    print("eth_addresses_and_refs.txt file not found.")
                
                finally:
                    vanity_eth_driver.quit()
                    crystalsea_driver.quit()
            
            elif choice == "2":
                if not os.path.exists("ETH_Address.txt") or os.path.getsize("ETH_Address.txt") == 0:
                    print("No ETH address found in ETH_Address.txt.")
                    continue
                
                referral_link = input("Please enter your CrystalSea referral link (e.g., https://crystalsea.org/?refer=your-code): ").strip()
                
                try:
                    with open("ETH_Address.txt", "r") as file:
                        eth_addresses = file.readlines()
                    
                    address_count = len(eth_addresses)
                    if address_count == 50:
                        print("Found 50 ETH Addresses.")
                    else:
                        print(f"Found {address_count} ETH Addresses.")

                    for eth_address in eth_addresses:
                        eth_address = eth_address.strip()
                        if eth_address:
                            print(f"Using ETH Address from file: {eth_address}")
                            submit_eth_to_crystalsea(eth_address, referral_link, save_refer=True)
                            time.sleep(1)
                
                except FileNotFoundError:
                    print("ETH_Address.txt file not found. Please make sure it exists.")
            
            else:
                print("Invalid choice. Please select either 1 or 2.")
    
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting gracefully.")

if __name__ == "__main__":
    main()
