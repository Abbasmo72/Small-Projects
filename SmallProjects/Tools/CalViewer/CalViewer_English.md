## Displaying the Calendar of the Entered Month and Year
This Python code uses the calendar module to display the calendar of a specific month and year entered by the user. Specifically, it uses the TextCalendar class to display the calendar in a text format, based on the month and year input by the user. Here are the details of each part of the code:
1. Importing the calendar module:
   - The calendar module in Python is used for working with calendars and dates, providing various functions to work with months, years, and weekdays.
2. Defining the display_calendar function:
   - The display_calendar function is responsible for prompting the user to enter the year and month, and then displaying the corresponding calendar.
3. Getting user input:
   - First, the user is prompted to enter the year (year = int(input("Enter year: "))).
   - Then, the user is prompted to enter the month, which must be a number between 1 and 12 (month = int(input("Enter month (1-12): "))).
4. Creating an object of the TextCalendar class:
   - The object cal is created from the TextCalendar class, with calendar.SUNDAY to set Sunday as the first day of the week.
5. Getting the month's calendar:
   - The formatmonth(year, month) method is used to get the text-based calendar of the entered month and year. The resulting calendar is in the form of a string, displaying the days of the week and the days of the month in a tabular format.
6. Displaying the calendar:
   - The calendar for the entered month is then printed to the screen.

## Features of the Code
1. User input for year and month: This code allows the user to input the year and month, and then view the corresponding calendar.
2. Using the TextCalendar class: The calendar is displayed in text format, with weeks starting on Sunday by default.
3. Displaying the specific month's calendar: After entering the year and month, the calendar for that month is displayed in text format.

This code is useful for displaying the calendar of any given month and year and can be used in various applications that require calendar functionality.

## Python Code
```python
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

```
