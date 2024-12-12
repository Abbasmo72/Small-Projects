import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Display the time on a single line
        time.sleep(1)  # Wait for one second
        seconds -= 1
    
    print("Time's up!")

# Input the countdown duration (in seconds)
duration = int(input("Enter the countdown duration (in seconds): "))
countdown_timer(duration)
