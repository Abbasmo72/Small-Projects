## Python Syntax Checker with Line Number Display
This code creates a simple graphical application in Python to check the syntax of Python code. Using the Tkinter library, it provides a graphical user interface (GUI) that includes a frame displaying code lines with line numbers and a button to check the syntax. Below is a detailed explanation of the code:

1. Importing Libraries:<br>
The tkinter module is used for creating the GUI, messagebox for displaying error or success messages, and ast for parsing Python code to verify its syntax.
2. check_syntax Function:<br>
This function retrieves the code entered by the user and attempts to parse it using ast.parse.
   - If the code has no issues, a success message is shown.
   - If there's a syntax error, an error message displays the error and the line number.
3. update_line_numbers Function:<br>
This function updates the line numbers displayed alongside the code:
   - It clears the current line numbers.
   - It calculates the total number of lines in the code and updates the line numbers in the corresponding text widget.
4. Creating the Main Window:
   - The main window is initialized using tk.Tk() and titled via root.title.
5. GUI Layout:
   - A frame is used to organize the line numbers and code input side by side.
   - A Text Widget is added for line numbers, which is non-editable and styled with a gray background.
   - Another Text Widget is added for the user to input Python code, preloaded with a default example code.
6. Binding Events:
   - The program binds key release events in the code input box to the update_line_numbers function so that the line numbers update dynamically when the code changes.
7. Syntax Check Button:
   - A button labeled "Check Syntax" is added, and clicking it triggers the check_syntax function
8. Running the Application:
   - The root.mainloop() call starts the event loop to keep the application running and manage user interactions.

## Features and Key Points:
1. The AST (Abstract Syntax Tree) module is used to validate code syntax, offering a reliable and efficient approach.
2. Line numbers are dynamically updated to stay in sync with the user's code using the update_line_numbers function.
3. Separating line numbers from the main code makes the display cleaner and more user-friendly.
4. Error messages include the line number of the issue, helping users quickly identify and fix problems.
5. The simple and intuitive GUI is designed to be beginner-friendly.

This code demonstrates an excellent use of Tkinter for creating educational tools and utilities that support programmers, especially those who are just starting out.
