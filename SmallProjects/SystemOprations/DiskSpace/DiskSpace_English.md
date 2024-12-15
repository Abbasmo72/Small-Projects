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
2. Conversion to Gigabytes:
   - Converts the values from bytes to gigabytes by dividing by.
3. Formatted Output:
   - Uses f-strings to print the values with two decimal points for clarity.

## The if __name__ == "__main__": Block
- Ensures that the get_disk_usage() function is executed only when the script is run directly.
- Prevents execution if the script is imported as a module in another project.

## Input/Output (I/O)
- Input: No user input is required.
- Output: Prints the total, used, free space, and usage percentage to the terminal.

## Advantages
1. Simplicity: The script is straightforward and easy to understand.
2. Efficient Use of psutil: Utilizes the library's capabilities to gather system information in a concise manner.
3. Readable Units: Disk space is displayed in gigabytes, making it easier to comprehend for users.

## Suggestions for Improvement
1. Add Path Parameter:
   - Allow users to specify a custom directory or mount point instead of always using /:
```python
def get_disk_usage(path='/'):
    disk_usage = psutil.disk_usage(path)
    ...
```
2. Error Handling:
   - Add error handling to ensure robustness when invalid paths are provided:
```python
try:
    disk_usage = psutil.disk_usage(path)
except FileNotFoundError:
    print("Invalid path. Please check the directory.")
    return
```
3. Save Output to File:
   - Provide an option to save the disk usage details to a file for future reference.
4. Support for Multiple Partitions:
   - Extend functionality to display information for all available partitions:
```python
for partition in psutil.disk_partitions():
    print(f"Partition: {partition.device}")
    get_disk_usage(partition.mountpoint)
```

## Example Output
If the system has a total disk size of 500 GB and 300 GB is used, the output will look like this:
```python
Total Space: 500.00 GB
Used Space: 300.00 GB
Free Space: 200.00 GB
Percent Used: 60%
```

## Python Code
```python
import psutil

def get_disk_usage():
    # Disk usage information
    disk_usage = psutil.disk_usage('/')
    
    total_space = disk_usage.total / (1024 ** 3)  # Convert to GB
    used_space = disk_usage.used / (1024 ** 3)
    free_space = disk_usage.free / (1024 ** 3)
    percent_used = disk_usage.percent
    
    print(f"Total Space: {total_space:.2f} GB")
    print(f"Used Space: {used_space:.2f} GB")
    print(f"Free Space: {free_space:.2f} GB")
    print(f"Percent Used: {percent_used}%")

if __name__ == "__main__":
    get_disk_usage()
```
