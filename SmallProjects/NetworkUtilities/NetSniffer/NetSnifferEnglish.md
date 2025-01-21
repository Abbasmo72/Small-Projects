## Net Sniffer
This code is a script for monitoring network traffic using the scapy library. It captures and logs network packets to a JSON file, helping in detecting unauthorized access by inspecting packet details.
<hr>

## Code Breakdown:
### 1. Importing Libraries:
- <b>scapy.all:</b> For network-related functions like sniff (to capture packets), get_if_list (to get a list of network interfaces), and conf (for network configuration settings).
- <b>datetime:</b> To get the current date and time.
- <b>threading.Thread:</b> To run network monitoring in a separate thread (for concurrent execution).
- <b>json:</b> To write packet details to a JSON file.
- <b>time:</b> For measuring the execution time of the script.
### 2. detect_unauthorized_access(packet) Function:
- This function logs packet details (timestamp and packet summary) into a JSON file called network_logs.json.
- The timestamp is formatted as YYYY-MM-DD HH:MM:SS, and the packet summary is extracted using the summary() method from scapy.
- If there is an error while writing to the file, it prints the error message.
### 3. monitor_network(interface=None, duration=60, packet_filter=None) Function:
- This function monitors network traffic on a specified interface for a given duration.
- It uses the sniff function to capture packets:
     - iface: The network interface to monitor.
     - prn: The function to call for each captured packet. In this case, it calls detect_unauthorized_access.
     - store=False: Prevents storing packets in memory.
     - timeout=duration: The duration for monitoring.
     - filter: An optional packet filter (e.g., tcp or udp).
### 4. monitor_in_thread(interface, duration, packet_filter=None) Function:
- This function runs the network monitoring in a separate thread.
- It creates a new thread to execute the monitor_network function.
- The thread is started using thread.start() and waits for completion with thread.join().
### 5. Main Block (if __name__ == "__main__":):
- Displays the available network interfaces on the system.
- Prompts the user to enter the network interface (optional), monitoring duration (in seconds), and a packet filter (optional).
- Starts network monitoring in a separate thread and measures the execution time.
- After the monitoring is complete, it prints the total time taken and the location of the saved logs (network_logs.json).
<hr>

## Python Code
```python
from scapy.all import sniff, get_if_list, conf
from datetime import datetime
from threading import Thread
import json
import time

def detect_unauthorized_access(packet):
    """Log packet details to a JSON file."""
    # Get the current timestamp in the format YYYY-MM-DD HH:MM:SS
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create a log entry containing the timestamp and the packet summary
    log_entry = {"timestamp": timestamp, "packet_summary": packet.summary()}
    try:
        # Open 'network_logs.json' file in append mode
        with open("network_logs.json", "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")  # Write the log entry to the file
    except IOError as e:
        # Print an error message if there is an issue with writing to the file
        print(f"Error writing to log file: {e}")

def monitor_network(interface=None, duration=60, packet_filter=None):
    """Monitor network traffic on a specific interface."""
    # If no interface is provided, use the system's default interface
    if interface is None:
        interface = conf.iface  # Use the default system interface

    print(f"Monitoring network on interface: {interface} for {duration} seconds")

    try:
        # Start sniffing the network using the scapy sniff function
        sniff(
            iface=interface,  # The network interface
            prn=detect_unauthorized_access,  # The function to call for each packet
            store=False,  # Do not store packets in memory
            timeout=duration,  # Duration of the monitoring
            filter=packet_filter,  # Optional packet filter (e.g., 'tcp or udp')
        )
    except Exception as e:
        # Print an error message if an exception occurs during monitoring
        print(f"Error occurred while monitoring: {e}")

def monitor_in_thread(interface, duration, packet_filter=None):
    """Run network monitoring in a separate thread."""
    # Create a new thread to run the network monitoring
    thread = Thread(target=monitor_network, args=(interface, duration, packet_filter))
    thread.start()  # Start the thread
    thread.join()  # Wait for the thread to finish

if __name__ == "__main__":
    # Display the available network interfaces
    print("Available interfaces:", get_if_list())

    # Get user input for network interface and monitoring duration
    interface = input("Enter the network interface (default: system default): ") or conf.iface
    try:
        # Get the monitoring duration from the user
        duration = int(input("Enter the monitoring duration in seconds (default: 60): ") or 60)
    except ValueError:
        # If the input is invalid, use the default value of 60 seconds
        print("Invalid duration. Using default value of 60 seconds.")
        duration = 60

    # Get an optional packet filter (e.g., 'tcp or udp')
    packet_filter = input("Enter a packet filter (e.g., 'tcp or udp', default: None): ") or None

    # Start network monitoring
    start_time = time.time()
    monitor_in_thread(interface, duration, packet_filter)
    end_time = time.time()

    # Print the duration of the monitoring and the location of the logs
    print(f"Monitoring completed. Duration: {end_time - start_time:.2f} seconds")
    print("Logs saved in 'network_logs.json'")
```
