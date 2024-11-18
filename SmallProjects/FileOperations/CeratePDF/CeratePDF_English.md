## Performance and type of project performance Cerate PDF 
This project is a graphical application using the Tkinter library that allows the user to input text and convert it into a PDF file. The process works as follows:

1. <b>User Interface Design:<b> Tkinter is used to create a window titled "PDF Generator." This window contains a text box for entering text and a button to generate the PDF file.
2. <b>Text Input:</b> The user can enter text, which may span multiple lines. Once the text is entered, pressing the "Create PDF" button converts it into a PDF format.
3. <b>Text to PDF Conversion:</b> After receiving the text, the ReportLab library is used to create the PDF file. This library allows the text to be written into a PDF file graphically.
4. <b>PDF Settings:</b> Initially, the 'B Nazanin' Persian font is registered and set as the default font for writing the text in the PDF. Then, the input text is written line by line into the PDF. If the text reaches the bottom of the page, a new page is created to continue the text properly.
5. <b>Saving the PDF:</b> Finally, the converted text is saved into a file named "output.pdf."

In summary, this program allows the user to easily convert text they input into a PDF file, saved in a printable format with Persian font.
