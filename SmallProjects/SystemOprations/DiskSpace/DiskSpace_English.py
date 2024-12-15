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
