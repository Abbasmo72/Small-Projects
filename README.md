<div align="center">

# Small Project
<img alt="Gif" src="https://media3.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" height="250px" width="500px">
</div>

<hr>

[Click to see the descriptions in Persian language](Persian.md)<br>
<b>Notice:</b> <b>Each section has a README file in English and Farsi in its respective file. By clicking on the links of each section, you can learn more in-depth information about the code and its function.

<hr>

# File Operations

1. <b>Cerate PDF :</b>
This code creates a graphical application using the Tkinter library in Python, allowing users to generate PDF files. Users can input their desired text into a text box, and by clicking a button, the program generates a PDF file. The ReportLab library is utilized to create the PDF, with support for Persian fonts. The entered text is retrieved from the text box and written line by line into the PDF, managing page positions dynamically. This program is suitable for creating simple textual documents with Persian language support.
To view the file <b>[English README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_English.md)</b> and <b>[Persian README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/FileOperations/CeratePDF/PDF_English.py)</b>.

2. <b>Chek Code Python :</b>
This program creates a graphical interface using the Tkinter library, allowing users to check the syntax validity of Python code. It utilizes the ast module to parse the code and identify syntax errors, reporting any issues along with the line number to the user. Line numbers are displayed in a separate, non-editable text box and are automatically updated whenever the code text changes. Two text boxes are arranged side by side: one for line numbers and the other for the user to input code. Using the "Check Syntax" button, users can validate their code and view the results.<br>
To view the file <b>[English README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_English.md)</b> and <b>[Persian README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/FileOperations/ChekCodePython/CodeCheker_English.py)</b>.

<hr>

# Network Utilities
1. <b>Get IP :</b> This Python code is designed to fetch and display the user's public IP address. It uses the urllib.request library to send a request to the ipify API service, retrieving the user's IP in text format. If the request is successful, the public IP is printed to the console. In case of any error, an appropriate error message is displayed. The script is executable as a standalone program, controlled through the if __name__ == "__main__": block.<br>
To view the file <b>[English README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_English.md)</b> and <b>[Persian README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/NetworkUtilities/GetIP/GetIP_English.py)</b>.

2. <b>SSL Shield :</b>The above code defines a function named is_secure_website that checks whether a website is secure using HTTPS. The function sends an HTTP request to the provided URL using the requests library and validates the certificate with the help of the certifi library. If the request is successful and the URL starts with https, the website is considered secure. In case of any errors, such as an invalid URL or connection issues, the website is deemed insecure. Finally, the user can input a website URL and see the result printed on the console.<br>
To view the file <b>[English README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_ٍEnglish.md)</b> and <b>[Persian README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/NetworkUtilities/SSLShield/SSLShield_ٍEnglish.py)</b>.
<hr>

# System Oprations
1. <b>Alarm Battrey :</b>The program uses the psutil and pygame libraries to monitor the battery status and power connection, playing an alert if necessary. The pygame.mixer.init initializes the sound playback setup. In an infinite loop, the program checks the battery and power connection status; if the power is disconnected, it continuously plays the sg.mp3 sound file. When the power is reconnected, the alarm playback stops. The status is checked every second.<br>
To view the file <b>[English README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍEnglish.md)</b> and <b>[Persian README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍPersian.md)</b> And the complete code <b>[Python Code](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍEnglish.py)</b>.

3. <b>Battery Monitor :</b>The code first retrieves battery information using the psutil.sensors_battery() function and checks if the information is available. If battery data exists, it prints the battery percentage and whether the device is plugged into power. A function named convertTime is defined to convert the remaining battery time from seconds to the format hours:minutes:seconds. The remaining battery time is then displayed using this function. If no battery information is available, it prints "No battery information available."<br>
To view the file <b>[English README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_English.md)</b> and <b>[Persian README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_English.py)</b>.
<hr>

# Web Scripts
1. <b>Find Table :</b> This code is a simple web scraping tool that uses Python libraries like requests, BeautifulSoup, and pandas to extract table data from a website. First, it fetches the HTML content of a webpage using requests.get. Then, it parses the content with BeautifulSoup to identify tables with the class wikitable. Each extracted table is converted into a DataFrame using pandas.read_html. Finally, these tables can be saved as CSV files for further analysis. This code is highly useful for collecting structured data from web pages.<br>
To view the file <b>[English README.md](SmallProjects/WebScripts/FindTable/FindTable_English.md)</b> and <b>[Persian README.md](SmallProjects/WebScripts/FindTable/FindTable_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/WebScripts/FindTable/FindTable_English.py)</b>.
<hr>

# Tools
1. <b>Cal Viewer :</b> This code prompts the user to enter the desired year and month, then creates an object of the TextCalendar class with the week starting on Sunday. Using the formatmonth method, it generates a textual calendar for the specified month. Finally, the generated calendar is printed for the user to view. The display_calendar function is called to execute the entire process.<br>
To view the file <b>[English README.md](SmallProjects/Tools/CalViewer/CalViewer_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/CalViewer/CalViewer_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/CalViewer/CalViewer_English.py)</b>.

2. <b>Country Info Finder :</b>This code uses the countryinfo library to provide detailed information about a country. It first takes the country name as input from the user and then retrieves various details, including the capital, population, area, geographical region, languages, currency, and neighboring countries, displaying the information in a readable format.<br>
To view the file <b>[English README.md](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_English.py)</b>.

3. <b>Daily Tasker :</b>This program is a simple task manager that stores tasks in a JSON file and allows adding new tasks with a name, due date, and completion status. Users can view all tasks, update their completion status, and delete tasks if needed. Changes are automatically saved to the file, and the program is managed through a main menu offering various options for task operations.<br>
To view the file <b>[English README.md](SmallProjects/Tools/DailyTasker/DailyTasker_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/DailyTasker/DailyTasker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/DailyTasker/DailyTasker_English.py)</b>.
4. <b>Data Faker :</b>This code uses the Faker library to generate and print random fake data such as name, address, text, email, country, geographic coordinates, and URL. It's useful for testing and simulation in software projects.</br>
To view the file <b>[English README.md](SmallProjects/Tools/DataFaker/DataFaker_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/DataFaker/DataFaker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/DataFaker/DataFaker_English.py)</b>.
5. <b>Easy Pad :</b>This program is a simple note-taking application that uses the notes.txt file to store and manage notes. Users can add new notes, view existing ones, or delete specific notes. The notes are managed interactively through a menu loop, and changes are saved to the file. If the notes file does not exist, the program creates it automatically. Available options include adding, viewing, deleting notes, and exiting the program.<br>
To view the file <b>[English README.md](SmallProjects/Tools/EasyPad/EasyPad_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/EasyPad/EasyPad_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/EasyPad/EasyPad_English.py)</b>.
6. <b>Planet Tracker :</b>This code calculates and displays the position of a planet relative to the Greenwich Observatory's location at the current time using Astropy modules. By receiving the planet's name from the user, it provides the planet's position in terms of Right Ascension (RA) and Declination (Dec).<br>
To view the file <b>[English README.md](SmallProjects/Tools/PlanetTracker/PlanetTracker_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/PlanetTracker/PlanetTracker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/PlanetTracker/PlanetTracker_English.py)</b>.
7. <b>QR code :</b>This Python script generates a QR code for a given website URL. It prompts the user to input the website address (without the http or https prefix). The script then automatically prepends https:// to the input to create a valid URL. Using the qrcode module, a QR code is generated for the URL and displayed to the user. Additionally, the QR code is saved as a PNG image file in the current directory, and a success message is printed to inform the user that the QR code has been saved successfully.<br>
To view the file <b>[English README.md](SmallProjects/Tools/QRcode/QRcode_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/QRcode/QRcode_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/QRcode/QRcode_English.py)</b>.
8. <b>Time Code :</b>This code measures the execution time of a specific code block using the time module. It records the start and end times, calculates the elapsed time, and displays it.<br>
To view the file <b>[English README.md](SmallProjects/Tools/TimeCode/TimeCode_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/TimeCode/TimeCode_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/TimeCode/TimeCode_English.md)</b>.
   
<hr>
