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
