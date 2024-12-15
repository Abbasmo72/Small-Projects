## Code Analysis
The provided Python script uses the psutil library to retrieve and display disk usage information. Here's a detailed analysis:

## The psutil Library
  - psutil is a powerful library for system monitoring and resource management.
  - It provides functionalities for retrieving information about CPU, memory, disk, network, and other system resources.
## The get_disk_usage() Function
This function collects and displays disk usage information. The key steps are:
1. psutil.disk_usage('/'):
   - Fetches disk usage statistics for the root directory (/).
   - Returns a named tuple containing:
       - total: Total disk space.
       - used: Space currently in use.
       - free: Available free space.
       - percent: Percentage of space used.
