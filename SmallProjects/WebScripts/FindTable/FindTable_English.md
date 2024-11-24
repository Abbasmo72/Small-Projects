## Extracting and Saving Tabular Data from Websites to CSV Files Using Python
This program is designed to extract tabular data from websites and uses the Pandas, Requests, and BeautifulSoup libraries. Here’s how it works:
1. Fetching Website Content: The program takes a website URL from the user and sends a GET request using the requests library to retrieve the HTML content of the webpage.
2. Parsing HTML Content: The retrieved HTML content is parsed using BeautifulSoup, a powerful library for navigating and extracting specific elements within an HTML structure.
3. Identifying Tables: The program identifies all tables on the webpage that have a CSS class named wikitable. This class is commonly used for tables on wiki-style or similar websites.
4. Converting Tables to DataFrames: Each identified table is converted into a Pandas DataFrame, which provides a convenient structure for managing and processing tabular data.
5. Saving Tables as CSV Files: The extracted tables are saved as CSV files. This makes the data easily accessible and ready for further analysis or use in other applications.

## Use Case:
This program is particularly useful for data analysts and researchers who need to extract structured data from websites. It automates the process of scraping and formatting table data, saving time and effort, especially when manual extraction is not feasible.

## Python Code
```python
import pandas as pd  # Import the pandas library to handle data frames and CSV operations
import requests  # Import the requests library to fetch web content
from bs4 import BeautifulSoup  # Import BeautifulSoup from the bs4 library for parsing HTML

# Fetch HTML page from the website
url = "Enter the website name"  # Enter the URL of the website you want to scrape
response = requests.get(url)  # Make a GET request to the website
soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML content of the response

# Find all tables with the class 'wikitable'
tables = soup.find_all('table', {'class': 'wikitable'})  # Locate all tables with the specified class

# Convert the found tables to CSV files
for i, table in enumerate(tables):  # Loop through each table found
    df = pd.read_html(str(table))[0]  # Convert
```
