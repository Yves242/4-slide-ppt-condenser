import os
from PIL import Image
from reportlab.pdfgen import canvas

def merge_images_to_pdf(input_dir, output_pdf):
    # List all the PNG files in the directory, sorted in order (assuming slide_0.png, slide_1.png, etc.)
    images = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])

    # Check if there are any PNG images
    if not images:
        print("No images found in the directory.")
        return

    # Create a PDF canvas (initially with no size specified)
    c = canvas.Canvas(output_pdf)

    # echo info
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

    print(f"PDF successfully merged as ' {output_pdf}'")

# Example usage:
merge_images_to_pdf('slides', 'merged_output.pdf')
