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
