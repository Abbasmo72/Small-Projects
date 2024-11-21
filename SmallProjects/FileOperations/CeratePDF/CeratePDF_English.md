## Performance and type of project performance Cerate PDF 
This project is a graphical application using the Tkinter library that allows the user to input text and convert it into a PDF file. The process works as follows:

1. <b>User Interface Design:<b> Tkinter is used to create a window titled "PDF Generator." This window contains a text box for entering text and a button to generate the PDF file.
2. <b>Text Input:</b> The user can enter text, which may span multiple lines. Once the text is entered, pressing the "Create PDF" button converts it into a PDF format.
3. <b>Text to PDF Conversion:</b> After receiving the text, the ReportLab library is used to create the PDF file. This library allows the text to be written into a PDF file graphically.
4. <b>PDF Settings:</b> Initially, the 'B Nazanin' Persian font is registered and set as the default font for writing the text in the PDF. Then, the input text is written line by line into the PDF. If the text reaches the bottom of the page, a new page is created to continue the text properly.
5. <b>Saving the PDF:</b> Finally, the converted text is saved into a file named "output.pdf."

In summary, this program allows the user to easily convert text they input into a PDF file, saved in a printable format with Persian font.

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
