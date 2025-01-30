# Net Pic
Downloading Images from a Website Using Python<br>
The provided script is a Python program designed to download images from a specified webpage. It utilizes the requests, BeautifulSoup, and os libraries to fetch the webpage, parse its HTML content, and save the images.
## 1. Taking User Input
The script starts by asking the user for two inputs:
- website_url: The URL of the target website
- folder_name: The name of the folder where images will be saved
## 2. Creating the Storage Folder
Before downloading images, the program checks if the specified folder exists. If it doesn’t, it creates the folder using os.makedirs(folder_name).
## 3. Fetching HTML Content and Extracting Images
- The script retrieves the webpage content using requests.get(url).
- It then parses the HTML using BeautifulSoup.
- All <img> tags from the webpage are extracted.
## 4. Filtering and Processing Image URLs
- The src attribute of each image is obtained.
- If src is missing, the script skips that image.
- If the image URL is relative, it is converted into an absolute URL using urljoin(url, img_url).
- Only images with .png and .jpg extensions are considered, while others are ignored.
## 5. Downloading and Saving Images
- The filename is extracted from the image URL, and invalid characters are replaced with _.
- The image content is fetched using requests.get(img_url).content and saved to the specified folder.
- A success message is displayed upon downloading each image.
- If an error occurs during the download, an appropriate error message is sho
## Conclusion
This script is a simple yet effective tool for extracting and saving images from webpages. With some optimizations, it can be enhanced for more advanced and professional use cases.
<hr>

## Python Code
```python
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def download_images(url, folder_name):
    # Check if the folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # Create the folder if it doesn't exist

    # Request the HTML content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <img> tags in the page
    img_tags = soup.find_all('img')

    for img in img_tags:
        # Get the image URL from the <img> tag
        img_url = img.get('src')
        if not img_url:
            continue  # Skip if the image URL is missing
        img_url = urljoin(url, img_url)  # Resolve relative URLs to absolute ones

        # Check if the file extension is .png or .jpg
        if not img_url.endswith(('.png', '.jpg')):
            continue  # Skip if the image format is not valid

        # Extract the file name from the URL
        img_name = os.path.basename(img_url)
        
        # Replace invalid characters in the file name
        img_name = re.sub(r'[<>:"/\\|?*]', '_', img_name)  # Replace invalid characters with '_'

        # Create the full path to save the image
        img_path = os.path.join(folder_name, img_name)

        # Download and save the image
        try:
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as f:
                f.write(img_data)  # Write the image data to the file
            print(f'Downloaded {img_path}')  # Success message
        except requests.exceptions.RequestException as e:
            print(f'Error downloading {img_url}: {e}')  # Error message if download fails

# Get website URL and folder name as input from the user
website_url = input("Enter the website URL: ")  # Website URL
folder_name = input("Enter the folder name to save images: ")  # Folder name to save images

# Call the function to download images
download_images(website_url, folder_name)

```
