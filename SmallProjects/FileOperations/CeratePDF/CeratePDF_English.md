## Performance and type of project performance Cerate PDF 
This code is a simple Python program that allows users to input text in a graphical user interface and save it as a PDF file with support for Persian fonts. Below is a detailed explanation of how the code works:
1. Importing Libraries:
   - Tk, Text, Button, and END are imported from the Tkinter library to create the graphical user interface (GUI).
   - canvas is imported from the reportlab.pdfgen library to generate and manage the PDF file.
   - TTFont and pdfmetrics are imported from reportlab.pdfbase to register and use custom fonts, such as Persian fonts.
2. The save_pdf Function:
   - This function is responsible for saving the user's input as a PDF file.
   - A PDF file is created using canvas.Canvas, and the page size is set to A4.
   - The initial writing position is set at the top of the page, and a Persian font (B Nazanin.ttf) is registered using pdfmetrics.registerFont.
3. Writing to the PDF:
   - The input text is split into lines.
   - Each line is drawn at the specified position on the page.
   - If the end of the page is reached, a new page is started, and writing continues on the new page.
4. The get_text Function:
   - This function retrieves the text entered by the user from the text box in the GUI and passes it to the save_pdf function for saving as a PDF.
5. Creating the GUI:
   - A main window is created using Tk(), and its title and dimensions are set.
   - A text box is added for the user to input their text.
   - A button is created that triggers the get_text function when clicked, allowing the user to save the text as a PDF.
6. Running the Program:
   - The root.mainloop() call starts the GUI, allowing user interaction with the program.

## Features of the Program
1. Support for Persian Text:
   - By using the ReportLab library and registering a custom font, the program can handle and save Persian text in the PDF.
2. Multi-page Capability:
   - If the number of lines exceeds the capacity of one page, a new page is automatically added, and writing continues on the next page.
3. Simple User Interface:
   - The program uses Tkinter, making it easy to use and interactive.
4. Automatic PDF Saving:
   - The PDF is saved as output.pdf in the current directory.
5. Extensibility:
   - Features such as allowing users to choose the file name, font size, or adding additional settings can be easily added to the program.
6. Wide Applications:
   - This program can be used in various projects, such as generating reports, creating Persian documents, or other related use cases.

This program is a simple example of combining a graphical user interface with PDF generation functionality, providing a useful tool for Persian-speaking users.

## Python Code
```python
from tkinter import Tk, Text, Button, END
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def save_pdf(text):
    # PDF settings and font registration
    c = canvas.Canvas("output.pdf", pagesize=A4)
    width, height = A4
    
    # Register Persian font
    pdfmetrics.registerFont(TTFont('Persian', 'B Nazanin.ttf'))
    
    # Initial writing position
    y_position = height - 40
    lines = text.split('\n')

    for line in lines:
        if y_position < 40:  # Start a new page if at the bottom
            c.showPage()
            y_position = height - 40
        c.setFont("Persian", 12)  # Set font to Persian with size 12
        c.drawString(40, y_position, line)
        y_position -= 20

    c.save()

def get_text():
    # Fetch text from the text box
    user_text = text_box.get("1.0", END)
    save_pdf(user_text)

# GUI settings
root = Tk()
root.title("PDF Generator")
root.geometry("400x400")

# Text box for user input
text_box = Text(root, wrap='word', font=("Arial", 12))
text_box.pack(expand=True, fill='both')

# Button to create PDF
save_button = Button(root, text="Create PDF", command=get_text)
save_button.pack()

root.mainloop()

```
