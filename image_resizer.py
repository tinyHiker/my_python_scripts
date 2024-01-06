from PIL import Image
import pyfiglet

ascii_art = pyfiglet.figlet_format("Image Resizer", font="slant")
print(ascii_art)


def get_original():
    while True:
        try:
            original_path= input("Please enter the path of the image you wish to resize: ").strip()
            print()
            original_image = Image.open(original_path)
            return original_image
        except FileNotFoundError:
            print("Image does not exist! ", end = "")
    
def get_dimensions():
    while True: 
        try:
            height = int(input("Enter the height of the new image: ").strip())
            print()
            break
        except ValueError:
            print("Enter a valid number! ", end= "")
        
    while True: 
        try:
            width = int(input("Enter the width of the new image: ").strip())
            print()
            break
        except ValueError:
            print("Enter a valid number! ", end= "")
    
    
    new_size = (height, width)  # For example, 800x600 pixels
    return new_size
    
try:
    original_image = get_original()
    new_size = get_dimensions()
    resized_image = original_image.resize(new_size)
    new_path= input("Please enter the path of the new_image: ").strip()
    print()
    resized_image.save(new_path)
except Exception as e:
    print(e)
else:
    print("Image suzzessfully resized")
    print(new_path)
        
    