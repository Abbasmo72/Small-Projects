## Checking Website Security Using HTTPS and SSL Certificates in Python
This Python code checks if a given website is secure by validating whether it uses HTTPS and verifies the server's SSL certificate using the certifi package. Below is a detailed explanation of how it works:
1. Importing Libraries:
- The code imports two libraries:
   - certifi is used to obtain a collection of root certificates for SSL verification.
   - requests is a popular HTTP library used to send HTTP requests and handle responses in Python.
2. Defining the is_secure_website Function:
   - This function accepts a url as a parameter and checks if the website is secure by sending an HTTPS request and validating the SSL certificate.
3. Sending a GET Request:
   - Inside the function, a GET request is made to the provided URL using requests.get(url, verify=certifi.where()).
   - The verify parameter is set to certifi.where(), which points to the path of the CA (Certificate Authority) certificates for SSL verification. This ensures the server's certificate is verified during the request.
4. Error Handling:
   - The response.raise_for_status() method checks if the HTTP response is successful. If the response contains an HTTP error (e.g., 404 or 500), it will raise an exception.
   - Any exceptions during the request (e.g., connection issues, invalid URLs) are caught by the except block, and the function returns False in such cases.
5. Checking if URL Starts with 'https://':
   - The function then checks if the URL begins with https://, which indicates that the website is using a secure connection (SSL/TLS).
   - If the URL is secure, it returns True; otherwise, it returns False.
6. Main Block of Code (if __name__ == "__main__":):
   - This block ensures that the following code only runs when the script is executed directly (not when imported as a module).
   - The program prompts the user to input a website URL using input().
7. Checking Website Security:
   - The is_secure_website function is called with the entered URL to check if it is secure.
   - Based on the result (True or False), the program prints a message indicating whether the website is secure or not.
8. Secure Website Message:
   - If the website is secure (using HTTPS and having a valid certificate), the message "is a secure website" is printed.
   - If the website is not secure (using HTTP or failing the certificate validation), the message "is not a secure website" is printed.

## Features of the Code
1. SSL/TLS Certificate Validation:
   - The use of certifi ensures that the server's SSL certificate is validated, providing additional security in confirming the authenticity of the website.
2. Error Handling:
   - The code handles various exceptions (like connection errors or invalid URLs), ensuring the program doesn’t crash unexpectedly.
3. HTTPS Check:
   - The program checks not only for SSL certificate validation but also ensures that the URL starts with https://, which is an indicator of a secure website.
4. User Input:
   - The program prompts the user to input a website URL, making it interactive and flexible for checking different websites.
5. HTTP/HTTPS Protocol Verification:
   - By checking the protocol (https://), the code can quickly determine if a website is secure or not.
6. Simple and Efficient:
   - The program is concise and efficient, providing an easy-to-use tool for website security checks.

This program is useful for quickly determining the security of websites, especially for ensuring that sensitive data is transmitted securely over the internet using HTTPS and validated SSL certificates.

## Python Code
```python
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

```





