import psutil  # Module to interact with system information, including network stats
import time  # Module to handle timing and delays

# Function to monitor network traffic
def monitor_network(interval=1):  
    """
    Monitor network traffic and display bytes sent, bytes received, and total bytes every interval.
    
    Args:
        interval (int): Time interval (in seconds) for updating the stats (default: 1 second)
    """
    
    # Print table header
    print(f"{'Time':<15} {'Bytes Sent':<15} {'Bytes Received':<15} {'Total Bytes':<15}")
    print("=" * 60)  # Separator line for better readability
    
    # Capture initial network stats for comparison
    previous_counters = psutil.net_io_counters()
    
    while True:
        time.sleep(interval)  # Pause for the specified time interval
        
        # Capture current network stats
        current_counters = psutil.net_io_counters()
        
        # Calculate bytes sent and received during the interval
        bytes_sent = current_counters.bytes_sent - previous_counters.bytes_sent
        bytes_received = current_counters.bytes_recv - previous_counters.bytes_recv
        total_bytes = bytes_sent + bytes_received  # Calculate total bytes transferred
        
        # Print the stats in a formatted manner
        print(f"{time.strftime('%H:%M:%S'):<15} {bytes_sent:<15} {bytes_received:<15} {total_bytes:<15}")
        
        # Update previous counters for the next iteration
        previous_counters = current_counters

# Main program execution
if __name__ == "__main__":
    monitor_network()  # Call the network monitoring function
