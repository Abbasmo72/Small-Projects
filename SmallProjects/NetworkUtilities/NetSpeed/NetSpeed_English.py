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
