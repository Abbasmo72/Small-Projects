## QR Code Generator for Website Links Using Python
This program is a simple tool for generating QR codes for a website URL. Here's an explanation of its functionality:
1. User Input: The program prompts the user to enter the website URL. The user only needs to provide the main part of the URL without http or https.
2. Constructing the Full URL: The program prepends https:// to the user input to create a complete and valid website URL.
3. Generating the QR Code: Using the qrcode library, a QR code is generated that contains the website URL information.
4. Displaying the QR Code: The generated QR code is displayed as an image for the user to view.
5. Saving the QR Code: The QR code is saved as a PNG image file named qrcode.png in the same directory where the program is run.
6. Success Notification: The program notifies the user that the QR code has been successfully saved.

## Use Case:
This program is designed for quickly generating QR codes that embed website URLs. These QR codes can be used for marketing, sharing links, or providing quick access to websites. Additionally, it serves as a great learning example for working with Python libraries to create QR codes.

## Python Code
```python
import qrcode  # Import the qrcode module to generate QR codes

# Get website URL input from the user
website = input("Enter the website URL without http or https: ")

# Add https:// at the beginning of the website URL to make it a valid URL
full_url = f"https://{website}"

# Generate the QR Code for the provided URL
qr = qrcode.make(full_url)

# Display the generated QR Code
qr.show()

# Save the QR Code as an image file (PNG format)
qr.save("qrcode.png")
print("QR Code has been successfully saved.")  # Notify the user that the QR code was saved successfully

```
