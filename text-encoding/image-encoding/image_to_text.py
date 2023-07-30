# Run `text_to_image.py` first to generate the image file, then run this script to convert the image back to text.

from PIL import Image
from os import chdir

def image_to_text(input_image, output_file):
    # Open the image
    image = Image.open(input_image)

    # Get the pixel data
    pixel_data = list(image.getdata())

    # Calculate the dimensions of the square image
    image_width, image_height = image.size
    square_size = min(image_width, image_height)

    # Extract RGB values and convert back to text (3 characters at a time)
    text = ''
    for y in range(square_size):
        for x in range(square_size):
            rgb = pixel_data[y * image_width + x]
            text += chr(rgb[0]) + chr(rgb[1]) + chr(rgb[2])

    # Remove trailing spaces if any (if text length was not divisible by 3)
    text = text.rstrip()

    # Save the text to a file
    with open(output_file, 'w') as file:
        file.write(text)

# Usage example:
input_image = '../../output/output_image.png'
output_file = '../../output/output.txt'
image_to_text(input_image, output_file)
