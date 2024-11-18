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
