<div align="center">

# Small Project
<img alt="Gif" src="https://media3.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" height="250px" width="500px">
</div>

<hr>

[Click to see the descriptions in Persian language](Persian.md)<br>
<b>Notice:</b> <b>Each section has a README file in English and Farsi in its respective file. By clicking on the links of each section, you can learn more in-depth information about the code and its function.

<hr>

# File Operations
### 1. <b>Cerate PDF :</b>
This code creates a graphical application using the Tkinter library in Python, allowing users to generate PDF files. Users can input their desired text into a text box, and by clicking a button, the program generates a PDF file. The ReportLab library is utilized to create the PDF, with support for Persian fonts. The entered text is retrieved from the text box and written line by line into the PDF, managing page positions dynamically. This program is suitable for creating simple textual documents with Persian language support.
To view the file <b>[English README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_English.md)</b> and <b>[Persian README.md](SmallProjects/FileOperations/CeratePDF/CeratePDF_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/FileOperations/CeratePDF/PDF_English.py)</b>.
### 2. <b>Chek Code Python :</b>
This program creates a graphical interface using the Tkinter library, allowing users to check the syntax validity of Python code. It utilizes the ast module to parse the code and identify syntax errors, reporting any issues along with the line number to the user. Line numbers are displayed in a separate, non-editable text box and are automatically updated whenever the code text changes. Two text boxes are arranged side by side: one for line numbers and the other for the user to input code. Using the "Check Syntax" button, users can validate their code and view the results.<br>
To view the file <b>[English README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_English.md)</b> and <b>[Persian README.md](SmallProjects/FileOperations/ChekCodePython/CodeCheker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/FileOperations/ChekCodePython/CodeCheker_English.py)</b>.

### 3. CSV Collector:<br>
This program is designed to combine multiple CSV files from a specified folder into a single consolidated CSV file. The process begins by verifying the existence of the input folder and identifying all CSV files within it. Each file is then sequentially read using the pandas library and appended to a unified dataset while ensuring data integrity through proper error handling. Once all files are successfully processed, the program saves the combined data into a new CSV file specified by the user. Additionally, it provides informative messages during each step to keep the user informed of the progress and potential issues, ensuring a seamless and user-friendly experience.<br>
To view the file <b>[English README.md](SmallProjects/FileOperations/CSVCollector/CSVCollectorEnglish.md)</b> and <b>[Persian README.md](SmallProjects/FileOperations/CSVCollector/CSVCollectorPersian.md)</b> And the complete code <b>[Python Code](SmallProjects/FileOperations/CSVCollector/CSVCollectorEnglish.py)</b>.

### 4. PDF Image Saver:<br>
This code is designed to extract images from PDF files using the PyPDF2, PIL, and tkinter libraries. It first creates a folder to store the extracted images if it doesn't already exist. Then, it opens the PDF file and scans its pages to locate images. If a page contains image objects, the image data is extracted and converted to an image using PIL. The images are saved in PNG format in the specified folder. Users can select their desired PDF file through a file selection dialog. A folder named "extracted_images" is created in the same directory as the PDF file, and the images are saved there. If no images are found in the PDF file, an appropriate message is displayed. In case of errors while processing images, the relevant error message is shown. This code provides a simple user interface using tkinter for file selection.<br>
To view the file <b>[English README.md](SmallProjects/FileOperations/PDFImageSaver/PDFImageSaverEnglish.md)</b> and <b>[Persian README.md](SmallProjects/FileOperations/PDFImageSaver/PDFImageSaverPersian.md)</b> And the complete code <b>[Python Code](SmallProjects/FileOperations/PDFImageSaver/PDFImageSaverEnglish.py)</b>.

<hr>

# Network Utilities
### 1. <b>Get IP :</b>
This Python code is designed to fetch and display the user's public IP address. It uses the urllib.request library to send a request to the ipify API service, retrieving the user's IP in text format. If the request is successful, the public IP is printed to the console. In case of any error, an appropriate error message is displayed. The script is executable as a standalone program, controlled through the if __name__ == "__main__": block.<br>
To view the file <b>[English README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_English.md)</b> and <b>[Persian README.md](SmallProjects/NetworkUtilities/GetIP/GetIP_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/NetworkUtilities/GetIP/GetIP_English.py)</b>.
### 2. <b>SSL Shield :</b>
The above code defines a function named is_secure_website that checks whether a website is secure using HTTPS. The function sends an HTTP request to the provided URL using the requests library and validates the certificate with the help of the certifi library. If the request is successful and the URL starts with https, the website is considered secure. In case of any errors, such as an invalid URL or connection issues, the website is deemed insecure. Finally, the user can input a website URL and see the result printed on the console.<br>
To view the file <b>[English README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_ٍEnglish.md)</b> and <b>[Persian README.md](SmallProjects/NetworkUtilities/SSLShield/SSLShield_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/NetworkUtilities/SSLShield/SSLShield_ٍEnglish.py)</b>.
### 3. <b>Net Speed :</b>
This Python script measures the network bandwidth by calculating the download and upload speeds. It uses psutil to get the initial and updated network statistics, then calculates the difference in bytes received and sent over a 1-second interval. The results are printed in kilobytes per second. The script also tracks the time taken to measure the bandwidth for performance insight.<br>
To view the file <b>[English README.md](SmallProjects/NetworkUtilities/NetSpeed/NetSpeed_English.md)</b> and <b>[Persian README.md](SmallProjects/NetworkUtilities/NetSpeed/NetSpeed_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/NetworkUtilities/NetSpeed/NetSpeed_English.py)</b>.
### 4. <b>Net Monitor :<b>
This script monitors network traffic using the psutil library to fetch network statistics and the time library for timing control. It defines a function, monitor_network, which continuously calculates and displays the number of bytes sent, received, and the total bytes transferred at regular intervals (default is 1 second). Initially, the script fetches and stores the current network stats. Inside an infinite loop, it calculates the difference in sent and received bytes compared to the previous stats, prints the data in a formatted table, and updates the previous stats for the next iteration. The program runs continuously until manually stopped.<br>
To view the file <b>[English README.md](SmallProjects/NetworkUtilities/NetMonitor/NetMonitor_English.md)</b> and <b>[Persian README.md](SmallProjects/NetworkUtilities/NetMonitor/NetMonitor_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/NetworkUtilities/NetMonitor/NetMonitor_English.py)</b>.
### 5. <b>Net Sniffer :</b>
This code is designed to monitor network traffic and detect unauthorized access through network packets. It uses the scapy library to capture and analyze packets, logging the details of each packet into a JSON file. The network monitoring runs in a separate thread for a specified duration, so the main program doesn't stop. The user can choose the network interface and packet filter. Finally, the execution time and the location of the logs are displayed.<br>
To view the file <b>[English README.md](SmallProjects/NetworkUtilities/NetSniffer/NetSnifferEnglish.md)</b> and <b>[Persian README.md](SmallProjects/NetworkUtilities/NetSniffer/NetSnifferPersian.md)</b> And the complete code <b>[Python Code](SmallProjects/NetworkUtilities/NetSniffer/NetSnifferEnglish.py)</b>.
<hr>

# System Oprations
### 1. <b>Alarm Battrey :</b>
The program uses the psutil and pygame libraries to monitor the battery status and power connection, playing an alert if necessary. The pygame.mixer.init initializes the sound playback setup. In an infinite loop, the program checks the battery and power connection status; if the power is disconnected, it continuously plays the sg.mp3 sound file. When the power is reconnected, the alarm playback stops. The status is checked every second.<br>
To view the file <b>[English README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍEnglish.md)</b> and <b>[Persian README.md](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍPersian.md)</b> And the complete code <b>[Python Code](SmallProjects/SystemOprations/AlarmBattrey/AllarmBattery_ٍEnglish.py)</b>.
### 2. <b>Battery Monitor :</b>
The code first retrieves battery information using the psutil.sensors_battery() function and checks if the information is available. If battery data exists, it prints the battery percentage and whether the device is plugged into power. A function named convertTime is defined to convert the remaining battery time from seconds to the format hours:minutes:seconds. The remaining battery time is then displayed using this function. If no battery information is available, it prints "No battery information available."<br>
To view the file <b>[English README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_English.md)</b> and <b>[Persian README.md](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/SystemOprations/BatteryMonitor/BatteryMonitor_English.py)</b>.
### 3. <b>Cpu Guardian :</b>
The provided code is a CPU monitoring program that utilizes the psutil library. The CpuMonitor class is designed with two main attributes: max_usage to define the maximum acceptable CPU usage and check_interval to set the interval between checks. The check_cpu_usage method monitors and displays the current CPU usage, while the monitor_cpu method continuously tracks CPU usage and triggers an alert if it exceeds the defined threshold, invoking the take_action method to manage the situation. The take_action method identifies high CPU-consuming processes, displays their details, and optionally terminates them if necessary. In the main program section (__main__), an instance of the class is created with customizable settings, and monitoring begins. This program effectively monitors and optimizes CPU usage in real time.<br>
To view the file <b>[English README.md](SmallProjects/SystemOprations/CpuGuardian/CpuGuardian_English.md)</b> and <b>[Persian README.md](SmallProjects/SystemOprations/CpuGuardian/CpuGuardian_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/SystemOprations/CpuGuardian/CpuGuardian_English.py)</b>.
### 4. <b> Disk Space :</b>
The psutil library is imported to access system information. Then, the get_disk_usage function is defined to retrieve disk information, including total space, used space, free space, and percentage of used space, using the disk_usage method. The total, used, and free spaces are converted from bytes to gigabytes for better readability. The disk information is then printed in a formatted manner, and finally, the function get_disk_usage is executed if the script is run directly by checking the __name__ == "__main__" condition.<br>
To view the file <b>[English README.md](SmallProjects/SystemOprations/DiskSpace/DiskSpace_English.md)</b> and <b>[Persian README.md](SmallProjects/SystemOprations/DiskSpace/DiskSpace_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/SystemOprations/DiskSpace/DiskSpace_English.py)</b>.
### 5. <b> Python FileFinder :</b>
The os and tkinter libraries are imported for file management and GUI creation. The search_files function searches directories for files with a specific extension like .py. In the on_search_button_click function, the file name is retrieved from the input, and a warning is shown if it's empty. Then, .py files are searched, filtered for the search term, and displayed in the Listbox; if no files are found, an information message is shown. Finally, root.mainloop runs the GUI, starting the application.<br>
To view the file <b>[English README.md](SmallProjects/SystemOprations/PythonFileFinder/PythonFileFinder_English.md)</b> and <b>[Persian README.md](SmallProjects/SystemOprations/PythonFileFinder/PythonFileFinder_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/SystemOprations/PythonFileFinder/PythonFileFinder_English.py)</b>.
<hr>

# Web Scripts
### 1. <b>Find Table :</b>
This code is a simple web scraping tool that uses Python libraries like requests, BeautifulSoup, and pandas to extract table data from a website. First, it fetches the HTML content of a webpage using requests.get. Then, it parses the content with BeautifulSoup to identify tables with the class wikitable. Each extracted table is converted into a DataFrame using pandas.read_html. Finally, these tables can be saved as CSV files for further analysis. This code is highly useful for collecting structured data from web pages.<br>
To view the file <b>[English README.md](SmallProjects/WebScripts/FindTable/FindTable_English.md)</b> and <b>[Persian README.md](SmallProjects/WebScripts/FindTable/FindTable_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/WebScripts/FindTable/FindTable_English.py)</b>.
### 2. <b>Web Scraper :</b>
This code uses the requests and BeautifulSoup libraries to send a request to a website and extract HTML data. It first sends an HTTP request to the specified URL and checks the response status. If the response is successful, it parses the HTML content and extracts all (hr) tags. Finally, it prints the text of the extracted tags line by line.<br>
To view the file <b>[English README.md](SmallProjects/WebScripts/WebScraper/WebScraper_English.md)</b> and <b>[Persian README.md](SmallProjects/WebScripts/WebScraper/WebScraper_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/WebScripts/WebScraper/WebScraper_English.py)</b>.
<hr>

# Tools
### 1. <b>Cal Viewer :</b>
This code prompts the user to enter the desired year and month, then creates an object of the TextCalendar class with the week starting on Sunday. Using the formatmonth method, it generates a textual calendar for the specified month. Finally, the generated calendar is printed for the user to view. The display_calendar function is called to execute the entire process.<br>
To view the file <b>[English README.md](SmallProjects/Tools/CalViewer/CalViewer_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/CalViewer/CalViewer_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/CalViewer/CalViewer_English.py)</b>.
### 2. <b>Country Info Finder :</b>
This code uses the countryinfo library to provide detailed information about a country. It first takes the country name as input from the user and then retrieves various details, including the capital, population, area, geographical region, languages, currency, and neighboring countries, displaying the information in a readable format.<br>
To view the file <b>[English README.md](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/CountryInfoFinder/CountryInfoFinder_English.py)</b>.
### 3. <b>Daily Tasker :</b>
This program is a simple task manager that stores tasks in a JSON file and allows adding new tasks with a name, due date, and completion status. Users can view all tasks, update their completion status, and delete tasks if needed. Changes are automatically saved to the file, and the program is managed through a main menu offering various options for task operations.<br>
To view the file <b>[English README.md](SmallProjects/Tools/DailyTasker/DailyTasker_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/DailyTasker/DailyTasker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/DailyTasker/DailyTasker_English.py)</b>.
### 4. <b>Data Faker :</b>
This code uses the Faker library to generate and print random fake data such as name, address, text, email, country, geographic coordinates, and URL. It's useful for testing and simulation in software projects.</br>
To view the file <b>[English README.md](SmallProjects/Tools/DataFaker/DataFaker_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/DataFaker/DataFaker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/DataFaker/DataFaker_English.py)</b>.
### 5. <b>Easy Pad :</b>
This program is a simple note-taking application that uses the notes.txt file to store and manage notes. Users can add new notes, view existing ones, or delete specific notes. The notes are managed interactively through a menu loop, and changes are saved to the file. If the notes file does not exist, the program creates it automatically. Available options include adding, viewing, deleting notes, and exiting the program.<br>
To view the file <b>[English README.md](SmallProjects/Tools/EasyPad/EasyPad_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/EasyPad/EasyPad_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/EasyPad/EasyPad_English.py)</b>.
### 6. <b>Planet Tracker :</b>
This code calculates and displays the position of a planet relative to the Greenwich Observatory's location at the current time using Astropy modules. By receiving the planet's name from the user, it provides the planet's position in terms of Right Ascension (RA) and Declination (Dec).<br>
To view the file <b>[English README.md](SmallProjects/Tools/PlanetTracker/PlanetTracker_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/PlanetTracker/PlanetTracker_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/PlanetTracker/PlanetTracker_English.py)</b>.
### 7. <b>QR code :</b>
This Python script generates a QR code for a given website URL. It prompts the user to input the website address (without the http or https prefix). The script then automatically prepends https:// to the input to create a valid URL. Using the qrcode module, a QR code is generated for the URL and displayed to the user. Additionally, the QR code is saved as a PNG image file in the current directory, and a success message is printed to inform the user that the QR code has been saved successfully.<br>
To view the file <b>[English README.md](SmallProjects/Tools/QRcode/QRcode_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/QRcode/QRcode_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/QRcode/QRcode_English.py)</b>.
### 8. <b>Time Code :</b>
This code measures the execution time of a specific code block using the time module. It records the start and end times, calculates the elapsed time, and displays it.<br>
To view the file <b>[English README.md](SmallProjects/Tools/TimeCode/TimeCode_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/TimeCode/TimeCode_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/TimeCode/TimeCode_English.py)</b>.
### 9. <b>Timer :</b>
The countdown_timer function creates a countdown from the given seconds, displaying the remaining time in MM:SS format every second. Once the time runs out, it shows the message "Time's up!".<br>
To view the file <b>[English README.md](SmallProjects/Tools/Timer/Timer_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/Timer/Timer_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/Timer/Timer_English.py)</b>.
### <b>10. Safe Pass Generator :</b>
This program generates a strong and random password of a specified length. The password consists of uppercase and lowercase letters, digits, and special characters. The secrets module is used to ensure high-security random password generation.<br>
To view the file <b>[English README.md](SmallProjects/Tools/safe_pass_generator/Safe_Pass_English.md)</b> and <b>[Persian README.md](SmallProjects/Tools/safe_pass_generator/Safe_Pass_Persian.md)</b> And the complete code <b>[Python Code](SmallProjects/Tools/safe_pass_generator/Safe_Pass_English.py)</b>.
<hr>
