import certifi
import requests

def is_secure_website(url):
    try:
        # Send a GET request to the provided URL with certificate validation using certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.url.startswith('https://')  # Check if the URL starts with 'https'
    except requests.exceptions.RequestException:
        # Return False if any request exception occurs (e.g., connection error, invalid URL)
        return False

if __name__ == "__main__":
    # Prompt the user to enter a website URL
    website_url = input("Enter the website URL: ")

    # Check if the website is secure and print the result
    if is_secure_website(website_url):
        print(f"{website_url} is a secure website.")
    else:
        print(f"{website_url} is not a secure website.")
