## Displaying Battery Information Including Charge Percentage, Power Status, and Remaining Time
This Python code retrieves and displays battery-related information using the psutil library. It shows the battery percentage, whether the device is plugged into power, and the remaining battery time. If battery information is not available, a message is displayed. Below is the detailed explanation of the code:
1. Importing psutil library:
   - psutil is a library that provides system information, including battery status.
2. Getting Battery Information:
   - psutil.sensors_battery() retrieves battery-related data, such as the battery percentage, charging status, and time remaining before the battery drains.
3. Checking for Battery Information:
 - If battery information is available, the following details are printed:
   - Battery Percentage: The battery charge percentage is displayed using battery.percent.
   - Power Plugged Status: Whether the device is plugged into power is displayed using battery.power_plugged.
4. Defining the convertTime Function:
   - This function converts the remaining battery time from seconds to the format of hours:minutes
   - using the divmod function, which divides the total seconds into minutes and hours.
5. Displaying Remaining Battery Time:
   - Using the convertTime function, the remaining battery time is displayed in a readable format: hours:minutes
6. Handling No Battery Information:
   - If no battery information is available, a message "No battery information available" is printed.

## Features of the Code
1. Battery Information Retrieval: The script automatically retrieves battery details like percentage, power plugged status, and remaining time.
2. Converting Time to Hours:Minutes:Seconds: The convertTime function converts remaining battery time to a human-readable format.
3. Displaying Power Plugged Status: The script shows whether the device is connected to power or not.

This program can be useful for monitoring the battery status of laptops or mobile devices, helping users stay informed about their battery life.

## Python Code
```python
import psutil

# Get battery information
battery = psutil.sensors_battery()

if battery is not None:
    # Print the battery percentage
    print("Battery Percentage:", battery.percent, "%")
    
    # Print whether the power is plugged in
    print("Power plugged in:", battery.power_plugged)

    def convertTime(seconds):
        # Convert seconds to the format of hours:minutes:seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

    # Print the remaining battery time
    print("Battery remaining time:", convertTime(battery.secsleft))
else:
    # Print a message if no battery information is available
    print("No battery information available.")

```



