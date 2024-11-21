## Battery Status Monitoring and Audio Alert When Power is Disconnected
This Python script is designed to continuously monitor the device's battery status and play an audio alert when the device is running on battery (i.e., not plugged into a power source). The alert will stop when the device is plugged back in. Below is a detailed explanation of the code:
1. Importing Libraries:
   - psutil: This library is used to access system information, including battery status.
   - time: This library is used to introduce delays in the program execution (here, every 1 second).
   - pygame: A library for handling and playing sounds in Python.
2. Configuring pygame for Playing Sound:
   - pygame.mixer.init() initializes the sound-mixing module of pygame.
3. Defining the battery_alert Function:
   - This function continuously checks the battery status of the device.
   - The alert_playing variable keeps track of whether the alert is currently playing. If the alert is already playing, it prevents playing it again.
4. Checking Battery Status:
   - psutil.sensors_battery() retrieves information about the battery, such as its charge percentage and whether the device is plugged in.
   - The plugged variable checks if the device is plugged into a power source.
5. Playing the Alert Sound:
   - If the device is running on battery (i.e., not plugged in) and the alert is not already playing (alert_playing is False), the message "Power is disconnected! Running on battery." is printed to the console, and the sound file sg.mp3 is loaded and played continuously.
   - If the device is plugged in and an alert sound is already playing, the message "Battery is plugged in. Alarm stopped." is printed, and the sound is stopped.
6. Sleep Between Checks:
   - time.sleep(1) ensures that the program checks the battery status every 1 second.
7. Running the battery_alert Function:
   - Finally, the battery_alert function is continuously executed, monitoring the battery status.

## Features of the Code

1. Audio Alert: When the device is unplugged, an audio alert is played using the pygame library.
2. Continuous Monitoring: The battery status is checked every second, and the program reacts automatically to any changes.
3. Using psutil Library: The script uses psutil to retrieve information about the battery and its charging status.
4. Alert Status Control: The alert_playing variable ensures that the sound is not played repeatedly if the device remains unplugged.

This program can be useful as a tool for monitoring battery status and notifying the user when the device needs to be charged.

## Python Code
```python
import psutil
import time
import pygame

# Configure pygame for playing sound
pygame.mixer.init()

def battery_alert():
    alert_playing = False  # Check if the alert is currently playing
    
    while True:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged  # Check if the device is plugged in

        if not plugged and not alert_playing:  # If the device is running on battery and no alert is playing
            print("Power is disconnected! Running on battery.")
            pygame.mixer.music.load("sg.mp3")  # Load the sound file
            pygame.mixer.music.play(-1)  # Play the sound continuously
            alert_playing = True  # Set the alert status to playing

        elif plugged and alert_playing:  # If the device is plugged in and an alert is playing
            print("Battery is plugged in. Alarm stopped.")
            pygame.mixer.music.stop()  # Stop the sound
            alert_playing = False  # Set the alert status to not playing
        
        time.sleep(1)  # Check the status every 1 second

battery_alert()

```

