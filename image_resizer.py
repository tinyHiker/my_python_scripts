from PIL import Image
import pyfiglet

ascii_art = pyfiglet.figlet_format("Image Resizer", font="slant")
print(ascii_art)

class ImageResizer:
    
    def __init__(self, height = 200, width = 200):
        self.height = height
        self.width = width 
        
        self.original_path = ""
        self.original_image = None
        
        self.resized_image = None
        self.resized_path = ""
        
        self.resizing = False
        
        
    def set_original(self):
        while True:
            try:
                self.original_path= input("Please enter the path of the image you wish to resize: ").strip()
                print()
                self.original_image = Image.open(self.original_path)
                return
            except FileNotFoundError:
                print("Image does not exist! ", end = "")
                
                
    def set_resized_path(self):
        self.resized_path = input("Please enter the path of the new_image: ").strip()
        
    
    def set_dimension(self, dim_string):
        while True: 
            try:
                dim = int(input(f"Enter the {dim_string} of the new image: ").strip())
                print()
                break
            except ValueError:
                print("Enter a valid number! ", end= "")
                
        return dim
        
            
    def set_height_width(self):
        self.height = self.set_dimension('height')
        self.width = self.set_dimension('width')
    
    
    def retrieve_conversion_info(self):
        self.set_original()
        self.set_height_width()
        self.set_resized_path()
        
        
    def main(self):
        try:
            self.retrieve_conversion_info()
            self.resized_image = self.original_image.resize((self.height, self.width))
            self.resized_image.save(self.resized_path)
        except Exception as e:
            print(e)
        else:
            print("Image suzzessfully resized")
            print(self.resized_path)

resizer = ImageResizer()
resizer.main()



