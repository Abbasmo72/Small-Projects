## Fetching and Displaying Your Public IP Address Using Python
This code is a simple Python program designed to fetch and display the user's public IP address via the internet. Here is a detailed explanation of how it works:
1. Importing the Library:
   - The urllib.request library is imported to send HTTP requests to websites or APIs.
2. Defining the get_public_ip Function:
   - This function is responsible for sending a request to an API to retrieve the public IP address of the user's device.
3. Sending a Request to the API:
   - The function uses urllib.request.urlopen to send a request to the free API ipify at https://api.ipify.org.
   - The response (containing the public IP) is read and decoded to a string using decode('utf8')
4. Displaying the IP Address:
   - The fetched IP address is printed to the console with a user-friendly message.
5. Error Handling:
   - The code is wrapped in a try-except block to handle potential errors, such as internet connectivity issues or problems with the API.
   - If an exception occurs, an error message is printed along with the exception details.
6. Running the Program:
   - The if __name__ == "__main__": block ensures that the get_public_ip function is executed only when the script is run directly, not when imported as a module

## Features of the Code
1. Simplicity:
   - The code is concise, easy to understand, and uses Python's standard library.
2. Using a Free API:
   - The ipify API is a reliable and free service for retrieving public IP addresses.
3. Error Handling:
   - The program gracefully handles errors to prevent abrupt termination and informs the user of the issue.
4. Platform Independence:
   - The program can run on any device connected to the internet, including Windows, Linux, and macOS.
5. Practical Use:
   - It can be used in various network, security, or monitoring projects.
6. Extensibility:
   - The code can be enhanced with additional features like saving the IP address to a file, displaying the date and time of retrieval, or sending the IP address via email.

This code is a simple yet practical example of using Python to interact with APIs and can serve as a beginner-friendly introduction to working with networking and APIs in Python.

## Python Code 
```python
import urllib.request

def get_public_ip():
    try:
        # Send a request to the API to get the public IP
        public_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
        print(f'Your Public IP Address is: {public_ip}')
    except Exception as e:
        print(f'Error occurred: {e}')

if __name__ == "__main__":
    get_public_ip()

```
