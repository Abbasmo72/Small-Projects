import psutil
import time

class CpuMonitor:
    def __init__(self, max_usage=80, check_interval=1):
        self.max_usage = max_usage  # Maximum CPU usage threshold
        self.check_interval = check_interval  # Time interval between checks

    def check_cpu_usage(self):
        """Check the current CPU usage"""
        usage = psutil.cpu_percent(interval=self.check_interval)
        print(f"CPU Usage: {usage}%")
        return usage

    def monitor_cpu(self):
        """Continuously monitor CPU usage and alert if it exceeds the threshold"""
        while True:
            usage = self.check_cpu_usage()
            if usage > self.max_usage:
                print(f"Warning: CPU usage exceeded {self.max_usage}%!")
                self.take_action()
            time.sleep(self.check_interval)

    def take_action(self):
        """Take action if CPU usage exceeds the threshold"""
        print("Taking actions to reduce CPU usage...")
        # Example: You can stop high CPU-consuming processes
        # Using psutil, we can identify and terminate processes consuming a lot of CPU
        processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])
        high_cpu_processes = [p for p in processes if p.info['cpu_percent'] > 20]

        if high_cpu_processes:
            print("High CPU consuming processes:")
            for proc in high_cpu_processes:
                print(f"PID: {proc.info['pid']} - Name: {proc.info['name']} - CPU Usage: {proc.info['cpu_percent']}%")
                # Optionally, terminate these processes:
                # proc.terminate()  # Uncomment this line to terminate the process
        else:
            print("No high CPU consuming processes found.")

if __name__ == "__main__":
    cpu_monitor = CpuMonitor(max_usage=80, check_interval=1)  # 80% max usage, 1 second interval
    cpu_monitor.monitor_cpu()
