Ethereum Vanity Address Generator and CrystalSea Submitter

This Python script automates generating Ethereum vanity addresses using Vanity-ETH and submitting them to CrystalSea for potential rewards.

Features

Automated Address Generation: Uses Vanity-ETH to create Ethereum addresses in the background.

Incognito Submission Mode: Opens CrystalSea in incognito mode, ensuring separate sessions for each submission.

Continuous Loop: The script continuously generates and submits addresses, making it easy to gather points over time.



---

Prerequisites

1. Python 3.7+

Ensure you have Python installed. link https://www.python.org/downloads/


2. Selenium

Install Selenium for browser automation by running:
```
pip install selenium
```

3. Google Chrome & ChromeDriver

Google Chrome: Download the latest version from here https://www.google.com/chrome/ or use mine https://drive.google.com/file/d/1NqxJMideomFMnViatO1odq5db6NIHlxt/view?usp=drivesdk

ChromeDriver: Ensure your ChromeDriver version matches your Chrome version. Download ChromeDriver from this link https://sites.google.com/chromium.org/driver/ or you use mine https://drive.google.com/file/d/1azFjxzZFwGuV0dqgFxorxyEi42S4XpiX/view?usp=drivesdk
Place chromedriver.exe in a known location and note the path.



---

Installation & Setup

1. Clone the Repository:
```
git clone https://github.com/ShamimRabby/eth-vanity-crystalsea.git
cd eth-vanity-crystalsea
```

2. Configure ChromeDriver Path:

Open eth_submitter.py in a text editor.

Update chrome_driver_path to the location of your ChromeDriver:

chrome_driver_path = "C:\\Path\\To\\Your\\chromedriver.exe"



3. Update Referral Link:

Replace the referral link in eth_submitter.py with your own.

Example:

incognito_driver.get("https://crystalsea.org/?refer=yourReferralCode")

Note: If you do not replace the referral link, any points earned will be credited to the default referral account in this script.





---

Usage

1. Run the Script:

Open a terminal and navigate to the script's folder:
```
cd path/to/eth-vanity-crystalsea
```
Start the script:
```
python eth_submitter.py
```


2. Stop the Script:

To stop the loop, press Ctrl + C in the terminal.





---

Script Workflow

1. Ethereum Address Generation:

Opens the Vanity-ETH website in headless mode, generates an ETH address, and retrieves the address.



2. Submit ETH Address to CrystalSea:

Launches CrystalSea in an incognito Chrome session, submits the ETH address, and repeats the loop.



3. Loop and Delay:

Waits for 10 seconds (configurable) before generating and submitting the next address.





---

Troubleshooting

WebDriverException: ChromeDriver Not Found:

Ensure chrome_driver_path is correct and points to the location of your ChromeDriver.


Update Selenium:

Run
```
pip install --upgrade selenium
```
to make sure you’re using the latest version.




---

Disclaimer

This script is provided for educational purposes. Use at your own discretion.


---

License

This project is licensed under the MIT License.


---

With this setup, you should be ready to automate the Ethereum address generation and submission to CrystalSea. Enjoy, and remember to customize the referral link!

