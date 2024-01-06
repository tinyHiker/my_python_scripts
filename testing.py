from PIL import Image
import pyfiglet


# Open an existing image
original_image = Image.open("")

# Define the new size
new_size = (800, 600)  # For example, 800x600 pixels

# Resize the image
resized_image = original_image.resize(new_size)

# Save the resized image
resized_image.save("path/to/your/resized_image.jpg")
