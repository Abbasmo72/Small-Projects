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
