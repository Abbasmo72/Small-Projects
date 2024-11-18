import subprocess
import time
import datetime

def ping_ip(ip_address, log_file):
    while True:
        # Get the current time
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Use subprocess to ping the IP address
        try:
            # For Windows, use "ping -n 1"
            # For Linux/Mac, use "ping -c 1"
            response = subprocess.run(
                ["ping", "-c", "1", ip_address],  # Change to ["ping", "-n", "1", ip_address] for Windows
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # Check if the ping was successful
            if response.returncode == 0:
                status = "reachable"
            else:
                status = "not reachable"

        except Exception as e:
            status = f"error: {str(e)}"

        # Log the result to the file
        with open(log_file, 'a') as file:
            file.write(f"{timestamp} - {ip_address} is {status}\n")

        # Wait for 5 seconds before the next ping
        time.sleep(5)

def main():
    ip_address = input("Enter the IP address to ping: ")
    log_file = "ping_results.log"
    
    print(f"Pinging {ip_address} continuously. Press Ctrl+C to stop.")

    ping_ip(ip_address, log_file)

if __name__ == "__main__":
    main()
