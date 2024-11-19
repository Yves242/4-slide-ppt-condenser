import os
from PIL import Image
import numpy as np

def remove_white_images(input_dir):
    # List all files in the directory
    files = [f for f in os.listdir(input_dir) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]

    # Check if there are any image files
    if not files:
        print("No images found in the directory.")
        return

    # Iterate through each file
    has_acquired_once = False
    for image_file in files:
        img_path = os.path.join(input_dir, image_file)
        
        try:
            # Open the image
            image = Image.open(img_path)
            
            # Convert image to an array (NumPy array)
            img_array = np.array(image)
            
            # Check if all pixels are white (255, 255, 255 for RGB images)
            if np.all(img_array == 255):
                if (not has_acquired_once):
                    has_acquired_once = True
                    print(f"Removing unnecessary white images...")
                print(f"Removing white image: {image_file}")
                os.remove(img_path)  # Remove the image file
                
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    if (has_acquired_once):
        print(f"Removed white images.\n")
        
    
# Example usage:
remove_white_images('slides')  # Adjusted to use the "slides" folder directly
