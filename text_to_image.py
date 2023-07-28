import math
from PIL import Image, ImageDraw

def text_to_image(input_file, output_image):
    with open(input_file, 'r') as file:
        text = file.read()

    # Group characters into sets of 3 and convert to RGB values
    rgb_values = []
    for i in range(0, len(text), 3):
        # If the text length is not divisible by 3, pad with spaces
        chunk = text[i:i+3].ljust(3, ' ')
        r, g, b = ord(chunk[0]), ord(chunk[1]), ord(chunk[2])
        rgb_values.append((r, g, b))

    # Calculate the nearest square dimensions based on the total number of characters
    num_pixels = len(rgb_values)
    square_size = int(math.ceil(math.sqrt(num_pixels)))
    image_width = square_size
    image_height = square_size

    # Create a blank RGB image
    image = Image.new('RGB', (image_width, image_height))

    # Set pixel values on the image
    for x, rgb in enumerate(rgb_values):
        image.putpixel((x % image_width, x // image_width), rgb)

    # Save the image
    image.save(output_image)

# Usage example:
input_file = 'input.txt'
output_image = 'output_image.png'
text_to_image(input_file, output_image)
