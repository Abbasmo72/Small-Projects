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
