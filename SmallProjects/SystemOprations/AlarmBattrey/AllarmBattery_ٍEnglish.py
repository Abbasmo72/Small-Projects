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
