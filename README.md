# CrystalSea Referral Generator

## Description

The **CrystalSea Referral Generator** is a Python script designed to automate the process of generating Ethereum (ETH) addresses and referral links for the CrystalSea platform. By leveraging the power of Selenium WebDriver, this script interacts with web pages to create multiple referrals efficiently. It is particularly useful for users looking to maximize their referral potential on the platform.

## Features

- **Batch Referral Generation**: Generate up to 50 referrals from existing referral links in a single run.
- **ETH Address Creation**: Automatically generate new Ethereum addresses using a vanity address generator.
- **Headless Browser Support**: Operate in headless mode for faster execution without opening a browser window.
- **Error Handling**: Built-in retry mechanisms for network requests to ensure reliability.
- **Data Storage**: Save generated ETH addresses and referral links in a text file for future reference.

## Requirements

To run this script, you will need:

- **Python 3.x**: Ensure you have Python installed on your machine. Link: https://www.python.org/downloads/
- **Selenium WebDriver**: For browser automation.
- **Chrome WebDriver**: Compatible with your version of Chrome.
- **Requests Library**: For making HTTP requests.

You can install the required Python packages using pip:

```
pip install selenium requests
```
Installation
1. Clone the repository:
```bash
git clone https://github.com/ShamimRabby/eth-vanity-crystalsea.git
```
2. Navigate to the project directory:
```bash
cd eth-vanity-crystalsea
```
3. Download and install Chrome WebDriver:

Visit the Chrome WebDriver download page and download the version that matches your Chrome browser.
4. Update the chrome_driver_path:

Open the script and set the chrome_driver_path variable to the location of your downloaded Chrome WebDriver.
Usage
1. Run the script:
```bash
python eth_submitter.py
```
2. Choose an option from the menu:

Option 1: Generate 50 referrals per link from eth_addresses_and_refs.txt.
Option 2: Generate referrals from ETH addresses listed in ETH_Address.txt.

Configuration
ETH_Address.txt: Create this file and list your Ethereum addresses, one per line. The script will read from this file to generate referrals.
eth_addresses_and_refs.txt: This file will be automatically created and updated by the script, storing generated ETH addresses and their corresponding referral links.
Important Notes
[!CAUTION] This script interacts with web services. Ensure you comply with the terms of service of the websites you're interacting with.

[!WARNING] Use this script responsibly. Excessive automation may lead to IP bans or account restrictions.

Contributing
Contributions are welcome! If you have suggestions for improvements or encounter issues, please check the issues page or submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgments
Thanks to the developers of Selenium for providing the tools necessary for web automation.
Special thanks to the community for their contributions and support.
---
### Key Enhancements:
- **Detailed Description**: Expanded the project description to clarify its purpose and functionality.
- **Features Section**: Added more specific features to highlight the capabilities of the script.
- **Installation Instructions**: Provided clearer steps for installation and setup.
- **Usage Instructions**: Clarified how to run the script and what options are available.
- **Configuration Details**: Explained the purpose of the configuration files.
- **Acknowledgments and Contact Information**: Added sections to recognize contributions and provide a way for users to reach out.

Feel free to modify any sections to better fit your project's specifics!
---
For any questions or support, please open an issue or contact the maintainer directly. Happy coding!
