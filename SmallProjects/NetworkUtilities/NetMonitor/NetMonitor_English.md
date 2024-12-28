## Net Monitor
This code is a simple network traffic monitoring tool that calculates and displays the number of bytes sent and received every second. It is useful for monitoring network activity, diagnosing issues, and observing internet usage.

### Code Components
1. Imported Modules
   - psutil: Provides system information, including network activity, processes, and hardware stats. In this code, psutil.net_io_counters is used to access the number of bytes sent and received over the network.
   - time: Used to implement delays between updates and to display the current time in the output.
