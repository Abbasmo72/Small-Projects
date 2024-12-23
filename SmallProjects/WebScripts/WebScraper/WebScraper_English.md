## Extracting Headings from a Website Using Python
This code is designed to send a request to a website and extract specific data from it. Its functionality is explained below:
1. Importing Libraries
   - requests is used to send HTTP requests.
   - BeautifulSoup is used to parse and work with HTML content.
2. Specifying the Target URL
   - The url variable holds the target website's address from which data will be extracted.
3. Sending a Request to the Website
   - A GET request is sent to the server using requests.get(url), and the response is stored in the response variable.
4. Checking the Response Status
   - If the request is successful (HTTP status code 200), the code proceeds. Otherwise, it prints an error message.
5. Parsing the HTML Content
   - The HTML content of the response is parsed using BeautifulSoup, allowing easy interaction with HTML elements.
6. Extracting Data
   - All (h1) tags from the HTML content are extracted and stored in a list called headers.
7. Displaying the Extracted Data
   - The text of each (h1) tag is retrieved from the list and printed.

## Summary of Functionality
This code fetches a webpage, checks the response, and if successful, extracts and prints all <h1> headings from the page.

## Python Code
```python
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

```
