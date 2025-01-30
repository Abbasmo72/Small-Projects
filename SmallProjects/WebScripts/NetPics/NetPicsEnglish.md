## Net Pic
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
## 

