import os
import tkinter as tk
from tkinter import messagebox

# Function to search for files with a specific extension in a directory and its subdirectories
def search_files(directory, file_extension):
    result = []
    for root, dirs, files in os.walk(directory):  # Walk through all directories and files
        for file in files:
            if file.endswith(file_extension):  # Check if the file has the specified extension
                result.append(os.path.join(root, file))  # Add the full file path to the result
    return result

# Function to handle the search button click event
def on_search_button_click():
    search_term = entry.get()  # Get the search term from the entry field
    if not search_term:  # If the search term is empty, show a warning message
        messagebox.showwarning("Empty Input", "Please enter a file name")
        return
    # Search for all .py files in the system
    results = search_files("/", ".py")  
    # Filter the results to include only those files that contain the search term
    found_files = [file for file in results if search_term in file]
    
    if found_files:
        result_list.delete(0, tk.END)  # Clear previous results
        for file in found_files:  # Add found files to the listbox
            result_list.insert(tk.END, file)
    else:
        messagebox.showinfo("Result", "No files found.")  # Show message if no files were found

# Create the main Tkinter window
root = tk.Tk()
root.title("Python File Search")

# Create input section
label = tk.Label(root, text="Enter file name:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)  # Create input field for the search term
entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=on_search_button_click)  # Create search button
search_button.pack(pady=5)

# Create result display section
result_list = tk.Listbox(root, width=80, height=20)  # Listbox to display search results
result_list.pack(pady=5)

root.mainloop()  # Start the Tkinter event loop
