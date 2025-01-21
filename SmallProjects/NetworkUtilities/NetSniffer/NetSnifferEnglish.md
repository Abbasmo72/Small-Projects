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


