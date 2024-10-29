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

- **Python 3.x**: Ensure you have Python installed on your machine. Download from here: https://www.python.org/downloads/
- **Chrome Driver**: Compatible with your version of Chrome. Download from here: https://sites.google.com/chromium.org/driver/downloads?authuser=0
or you can use mine which I'm using.
Chrome: https://drive.google.com/file/d/1NqxJMideomFMnViatO1odq5db6NIHlxt/view?usp=drivesdk
Chrome Driver: https://drive.google.com/file/d/1azFjxzZFwGuV0dqgFxorxyEi42S4XpiX/view?usp=drivesdk
- **Requests Library**: For making HTTP requests.

You can install the required Python packages using pip:

```
pip install selenium requests
```
---
## Installation
1. ChromeDriver Setup

2. Download ChromeDriver, matching your Chrome browser version. (I hve provided link to download on above)

3. Place ChromeDriver in the same directory as the script or specify the path in the code.

4. Clone the repository:
```
git clone https://github.com/ShamimRabby/eth-vanity-crystalsea.git
```

File Preparation

1. Referral Links: Create a file eth_addresses_and_refs.txt with referral links in the format:
```
ETH Address: <address> | Referral Link: https://crystalsea.org/?refer=<code>
```

2. ETH Addresses: If you plan to use existing addresses, add them to ETH_Address.txt.

---
## Usage
1. Navigate to the project directory:
```
cd eth-vanity-crystalsea
```
2. Run the script from your terminal. Choose the desired option when prompted:
```
python eth_submitter.py
```
Option 1: Generate 50 Referrals per Referral Link

This option generates 50 ETH addresses per referral link found in eth_addresses_and_refs.txt.

- Example workflow:

1. The script reads referral links from eth_addresses_and_refs.txt.

2. For each link, it generates 50 ETH addresses and submits them to the specified link.

3. Progress messages display every 50 referrals generated.

Option 2: Generate Referral from ETH Address File

This option uses ETH addresses from ETH_Address.txt to generate referrals. If ETH_Address.txt is empty or not found, a warning will appear.

- Example workflow:

1. The script reads addresses from ETH_Address.txt.

2. Each ETH address is submitted to CrystalSea to generate a referral link.

3. Generated referral links and ETH addresses are saved in eth_addresses_and_refs.txt.

## Configuration
- ETH_Address.txt: Create this file and list your Ethereum addresses, one per line. The script will read from this file to generate referrals.
- eth_addresses_and_refs.txt: This file will be automatically created and updated by the script, storing generated ETH addresses and their corresponding referral links.
---
## Script Details

Key Functions
- setup_driver: Configures ChromeDriver with headless and incognito options.

- check_url_availability: Checks URL connectivity with retry attempts.

- generate_eth_vanity_address: Generates a new ETH address.

- submit_eth_to_crystalsea: Submits ETH addresses to CrystalSea with a given referral link.

- save_eth_and_refer: Saves generated ETH address and referral link to eth_addresses_and_refs.txt.

- Graceful Exit:
To stop the script at any time, press Ctrl+C. This will exit the script smoothly and display the message:

(Process interrupted by user. Exiting gracefully.)

---
## Notes and Troubleshooting

- Headless Mode: The script runs in headless mode by default. To observe actions visually, set headless=False in setup_driver.

- Referral Link Format: Make sure referral links are correctly formatted in eth_addresses_and_refs.txt as https://crystalsea.org/?refer=code.

- SSL and Network Issues: If network issues arise, retry the connection or use the check_url_availability function.
---
## Important Notes
[!CAUTION] This script interacts with web services. Ensure you comply with the terms of service of the websites you're interacting with.

[!WARNING] Use this script responsibly. Excessive automation may lead to IP bans or account restrictions.

---
## Contributing:
Contributions are welcome! If you have suggestions for improvements or encounter issues, please check the issues page or submit a pull request.

---
## License:
This project is licensed under the MIT License.

---
## Acknowledgments:
Thanks to the developers of Selenium for providing the tools necessary for web automation. 
- Special thanks to the community for their contributions and support.
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
