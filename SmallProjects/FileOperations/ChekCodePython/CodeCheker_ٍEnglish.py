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
