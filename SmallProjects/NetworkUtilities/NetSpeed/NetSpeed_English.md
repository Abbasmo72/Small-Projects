## Network Bandwidth Measurement with psutil
This code uses the psutil library to measure the amount of data sent and received over the network during a specified time interval. The general steps of the code’s operation are as follows:
1. <b>Initial Network Data Collection:</b> The psutil.net_io_counters() function is used to collect information on the amount of data sent (bytes_sent) and received (bytes_recv) over the network.
2. <b>Time Delay:</b> The code waits for a specified duration using the time.sleep() function, allowing time to calculate changes in network data.
3. <b>Bandwidth Calculation:</b> The changes in sent and received data values between two measurement points are calculated and divided by the delay time to compute the bandwidth (in bytes per second).
4. <b>Output:</b> The computed results, including sent and received data, are printed in a readable format.

This code is particularly useful for simple, real-time network bandwidth monitoring and can be employed in network management tools or monitoring scripts.

## Python Code
```python
import psutil
import time

def measure_bandwidth():
    # Get initial network I/O statistics
    old_value = psutil.net_io_counters()
    old_bytes_recv = old_value.bytes_recv
    old_bytes_sent = old_value.bytes_sent

    # Start time for measuring the bandwidth
    start_time = time.time()

    # Sleep for 1 second to measure bandwidth during this time
    time.sleep(1)  # Measure for 1 second

    # Get updated network I/O statistics
    new_value = psutil.net_io_counters()
    new_bytes_recv = new_value.bytes_recv
    new_bytes_sent = new_value.bytes_sent

    # Calculate download and upload speeds
    download_speed = (new_bytes_recv - old_bytes_recv) / 1024  # Convert to kilobytes per second
    upload_speed = (new_bytes_sent - old_bytes_sent) / 1024  # Convert to kilobytes per second

    # End time for measuring the bandwidth
    end_time = time.time()

    # Display the results
    print(f"Download Speed: {download_speed:.2f} KB/s")
    print(f"Upload Speed: {upload_speed:.2f} KB/s")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    measure_bandwidth()
```
