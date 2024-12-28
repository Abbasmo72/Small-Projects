## Net Monitor
This code is a simple network traffic monitoring tool that calculates and displays the number of bytes sent and received every second. It is useful for monitoring network activity, diagnosing issues, and observing internet usage.

### Code Components
1. Imported Modules
   - psutil: Provides system information, including network activity, processes, and hardware stats. In this code, psutil.net_io_counters is used to access the number of bytes sent and received over the network.
   - time: Used to implement delays between updates and to display the current time in the output.
2. The monitor_network Function
   - Print the Table Header:
        - A table with columns for time, bytes sent, bytes received, and total traffic is displayed.
   - Retrieve Initial Network State:
        - Using psutil.net_io_counters, the baseline network stats are captured to calculate changes over time.
   - Infinite Loop:
        - Inside a while True loop, the function performs the following steps:
           - Pause for the Interval: time.sleep(interval) pauses the execution for the specified duration (default is 1 second).
           - Get Updated Network Stats: Fetches the current bytes sent and received.
           - Calculate Traffic Changes: Computes the difference in bytes sent and received since the last interval.
           - Display Results: Prints the results in a formatted table.
           - Update Previous Stats: Updates the baseline stats for the next iteration.

### Python Code
```python
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

```
