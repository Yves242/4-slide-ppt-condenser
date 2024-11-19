import fitz  # PyMuPDF

# Define the areas to crop: 4 quadrants (adjust the coordinates as needed)
x0 = 20
y0 = 115
x1 = 270
y1 = 280

offset = 250
boundary = 320
slide_areas = [
    fitz.Rect(x0 + 10, y0, x1 + 10, y1),  # Top-left
    fitz.Rect(x0 + offset, y0 + 10, x1 + offset, y1 + 10),  # Top-right
    fitz.Rect(x0 + 10, y0 + boundary + 4, x1 + 10, y1 + boundary + 4),  # Top-left
    fitz.Rect(x0 + offset, y0 + boundary, x1 + offset, y1 + boundary),  # Top-right
]

def extract_slides(input_pdf, output_dir, zoom_factor=2.0):
    # Open the document
    doc = fitz.open(input_pdf)
    
    # Loop through each page in the document
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load the current page
        
        # Save the original cropbox (current page area) before changing it
        original_cropbox = page.cropbox

        # Get the media box (dimensions of the entire page)
        page_rect = page.rect  # The full page rectangle (media box)

        # Iterate through each slide area (top-left, top-right, etc.)
        for idx, area in enumerate(slide_areas):
            # Ensure the crop area is within the page's media box
            if area.x0 >= page_rect.x0 and area.y0 >= page_rect.y0 and area.x1 <= page_rect.x1 and area.y1 <= page_rect.y1:
                # Set the new cropbox within the page bounds
                page.set_cropbox(area)

                # Increase resolution by applying a zoom factor via matrix
                matrix = fitz.Matrix(zoom_factor, zoom_factor)  # Apply the zoom factor

                # Create a Pixmap from the cropped page with high resolution
                pix = page.get_pixmap(matrix=matrix)

                # Define the output image file path for each cropped region
                image_output = f"{output_dir}/slide_{((page_num)*4)+idx}.png"

                # Save the Pixmap object as an image (PNG)
                pix.save(image_output)
                
                # echo info
                print(f"Generated image located at {output_dir}/slide_{((page_num)*4)+idx}.png")
            else:
                print(f"Skipping invalid crop area on page {page_num + 1}, part {idx + 1} - Out of bounds!")

        # After processing all areas, restore the original cropbox
        page.set_cropbox(original_cropbox)
        
    print("Slides successfully extracted.\n")

# Example usage:
extract_slides('module7.pdf', 'slides')
