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
