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
