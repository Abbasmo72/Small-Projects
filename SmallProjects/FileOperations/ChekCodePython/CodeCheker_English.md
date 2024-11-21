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

## Python Code
```python
import tkinter as tk
from tkinter import messagebox
import ast

def check_syntax():
    code = code_text.get("1.0", tk.END)
    try:
        # Check Python code syntax using ast
        ast.parse(code)
        messagebox.showinfo("Result", "Your code is correct and has no syntax errors.")
    except SyntaxError as e:
        messagebox.showerror("Syntax Error", f"Error on line {e.lineno}: {e.msg}")

def update_line_numbers(event=None):
    # Clear the line numbers text box
    line_numbers_text.delete("1.0", tk.END)
    # Get the number of lines in the code text box
    line_count = code_text.index('end').split('.')[0]
    # Insert line numbers for each line
    line_numbers_text.insert(tk.END, "\n".join(str(i) for i in range(1, int(line_count))))

# Create the main window
root = tk.Tk()
root.title("Python Code Syntax Checker with Line Numbers")

# Create a frame to hold the line numbers and code text side by side
frame = tk.Frame(root)
frame.pack(pady=10)

# Line numbers text box (non-editable)
line_numbers_text = tk.Text(frame, width=4, height=15, padx=3, takefocus=0, border=0, background="lightgrey", state='disabled')
line_numbers_text.pack(side=tk.LEFT, fill=tk.Y)

# Code input text box
code_text = tk.Text(frame, height=15, width=60)
code_text.insert(tk.END, "# Example Python code\nprint('Hello, World!')\n")  # Predefined code
code_text.pack(side=tk.LEFT, fill=tk.BOTH)

# Bind events to update line numbers on any text change
code_text.bind("<KeyRelease>", update_line_numbers)
update_line_numbers()  # Initial call to populate line numbers

# Button to check the code
check_button = tk.Button(root, text="Check Syntax", command=check_syntax)
check_button.pack(pady=5)

root.mainloop()

```
