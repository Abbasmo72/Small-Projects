import os
import time

def schedule_shutdown():
    try:
        # Get the shutdown delay from the user (in minutes)
        minutes = int(input("Enter the time in minutes until the system shuts down: "))
        # Convert minutes to seconds
        seconds = minutes * 60

        print(f"The system will shut down in {minutes} minutes...")
        time.sleep(seconds)  # Wait for the specified duration

        # Execute the shutdown command based on the operating system
        if os.name == "nt":  # Windows
            os.system("shutdown /s /t 1")
        elif os.name == "posix":  # Linux/Mac
            os.system("shutdown -h now")
        else:
            print("Your operating system is not supported.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    schedule_shutdown()
