import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://example.com'  # Replace with your website URL

# Sending request to the website
response = requests.get(url)

# Checking the response status
if response.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting data from HTML (Example: extracting all <h1> tags)
    headers = soup.find_all('h1')

    # Displaying the extracted data
    for header in headers:
        print(header.text)
else:
    print(f"Failed to retrieve the webpage: {response.status_code}")
