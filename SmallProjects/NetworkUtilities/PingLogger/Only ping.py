import subprocess
import platform

def ping_host(host):
    # تشخیص نوع سیستم عامل
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # اجرای دستور پینگ
    command = ['ping', param, '4', host]
    
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError:
        print(f"{host} is unreachable.")

if __name__ == "__main__":
    host = input("Enter the IP address or domain to ping: ")
    ping_host(host)
