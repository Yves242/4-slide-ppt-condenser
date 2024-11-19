import os
from PIL import Image
from reportlab.pdfgen import canvas
import re

def numeric_sort_key(filename):
    # Extract the number from the filename, assuming the format "slide_<number>.png"
    match = re.match(r"slide_(\d+)\.png", filename)
    if match:
        return int(match.group(1))  # Return the numeric part as an integer
    return filename  # If no match, return the filename itself (fallback)

def merge_images_to_pdf(input_dir, output_pdf):
    # List all the PNG files in the directory, sorted by the numeric part of the filename
    images = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')], key=numeric_sort_key)

    # Check if there are any PNG images
    if not images:
        print("No images found in the directory.")
        return

    # Create a PDF canvas (initially with no size specified)
    c = canvas.Canvas(output_pdf)

    # Echo info
    print(f"Merging files...")

    for idx, image_file in enumerate(images):
        # Open each image
        img_path = os.path.join(input_dir, image_file)
        image = Image.open(img_path)

        # Get the dimensions of the image (width and height)
        img_width, img_height = image.size

        # Set the canvas size to match the image size
        c.setPageSize((img_width, img_height))

        # Draw the image on the canvas (positioned at the bottom-left corner)
        c.drawImage(img_path, 0, 0, width=img_width, height=img_height)

        # If it's not the last image, create a new page for the next one
        if idx < len(images) - 1:
            c.showPage()

    # Save the PDF file
    c.save()

    print(f"PDF successfully merged as '{output_pdf}'")

# Example usage:
merge_images_to_pdf('slides', 'merged_output.pdf')
