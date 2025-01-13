import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader
from PIL import Image
import io

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extract images from a PDF and save them to a folder.
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the PDF
    pdf_reader = PdfReader(pdf_path)
    image_count = 0

    for page_number, page in enumerate(pdf_reader.pages):
        if '/XObject' in page['/Resources']:
            x_objects = page['/Resources']['/XObject'].get_object()
            for obj_name in x_objects:
                x_object = x_objects[obj_name]
                if x_object['/Subtype'] == '/Image':
                    try:
                        # Extract image data
                        size = (x_object['/Width'], x_object['/Height'])
                        data = x_object.get_data()
                        mode = 'RGB' if x_object['/ColorSpace'] == '/DeviceRGB' else 'P'

                        # Convert and save image
                        img = Image.open(io.BytesIO(data))
                        img = img.convert(mode)  # Ensure the mode is set correctly
                        image_count += 1
                        img_path = os.path.join(output_folder, f"image_{page_number + 1}_{image_count}.png")
                        img.save(img_path)
                        print(f"Saved: {img_path}")
                    except Exception as e:
                        print(f"Error processing image on page {page_number + 1}: {e}")

    if image_count > 0:
        print(f"Extraction complete! {image_count} images saved to '{output_folder}'.")
    else:
        print("No images found in the PDF.")

def select_pdf_and_extract_images():
    """
    Open a file dialog to select a PDF and extract its images.
    """
    # Open file dialog
    Tk().withdraw()  # Hide the root window
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        print("No file selected.")
        return

    # Set output folder
    output_folder = os.path.join(os.path.dirname(pdf_path), "extracted_images")

    # Extract images
    extract_images_from_pdf(pdf_path, output_folder)

if __name__ == "__main__":
    select_pdf_and_extract_images()
