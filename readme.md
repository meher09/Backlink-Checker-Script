# Backlink Checker Script
This script reads a CSV file containing a list of backlinks and checks if your domain (mysite) is mentioned in the HTML source code of each URL. It uses asynchronous HTTP requests to improve performance and avoid getting blocked by implementing custom headers like user-agent, referrer, and other necessary options.

The result of the backlink check is saved in the same CSV file, with a new column named with the current date. This column will indicate whether the backlink is "Present", "Absent", "Timeout", or "Unable to Fetch".

## Features
1. **Asynchronous requests**: Uses aiohttp to perform requests concurrently, making the process faster.

2. **Custom headers**: Includes custom headers like User-Agent, Referer, and others to avoid being blocked by websites.

3. **Error handling**: Handles various errors like timeouts, connection issues, etc.

4. **CSV output**: Adds a new column with the current date and backlink status.

## Prerequisites

To run this script, you need to have Python installed on your machine. You can download Python.


## Installation

### Step 1: Install the required dependencies

You need the following Python libraries to run the script:

- **aiohttp**: For making asynchronous HTTP requests.
- **pandas**: For handling CSV files.

Install the required dependencies by running the following command:

```bash
pip install aiohttp pandas requests
```
### Step 2: Prepare your CSV file

Create a CSV file (for example, `mybacklink.csv`) with a column named `backlink_url`, where each row contains a backlink URL to be checked. Example:

```csv
backlink_url
https://example.com
https://anotherexample.com
https://somedomain.com
```

### Step 3: Edit the script

Replace the `mysite` variable in the script with your own domain:

```python
mysite = "your-site-url.com"  
```

### Step 4: Run the Script


## Script Overview

This script performs the following actions:

- Reads a CSV file (`mybacklink.csv`) containing backlinks.
- For each URL in the CSV:
  - Sends an asynchronous request to the URL.
  - Checks if the domain (`mysite`) is present in the HTML content of the page.
  - Handles timeouts and network failures.
- Adds a new column to the CSV file with the current date and fills it with one of the following statuses:
  - **Present**: If the domain is found in the page's source code.
  - **Absent**: If the domain is not found in the page's source code.
  - **Timeout**: If the request takes too long to respond.
  - **Unable to Fetch**: If there is any other error during the request.

## Example Output

After running the script, the CSV file (`mybacklink.csv`) will be updated with a new column for the current date:

```csv
backlink_url,2024-10-04
https://example.com,Present
https://anotherexample.com,Absent
https://somedomain.com,Unable to Fetch
```
## License
This project is licensed under the MIT License. Feel free to use and modify it according to your needs.
