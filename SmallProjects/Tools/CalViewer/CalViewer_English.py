import calendar

def display_calendar():
    # Prompt the user to enter the year
    year = int(input("Enter year: "))
    
    # Prompt the user to enter the month (a number between 1 and 12)
    month = int(input("Enter month (1-12): "))

    # Create an object of the TextCalendar class with Sunday as the start of the week
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # Get the month's calendar in text format for the entered year and month
    month_calendar = cal.formatmonth(year, month)
    
    # Display the calendar of the entered month
    print(month_calendar)

# Call the function to display the calendar
display_calendar()
