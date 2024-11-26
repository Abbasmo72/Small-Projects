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
