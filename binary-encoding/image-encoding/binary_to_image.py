from PIL import Image
import os

def binary_to_image(binary_file):
    file_type = os.path.splitext(binary_file)[1][1:]
    output_image = f"../../output/output-{file_type}.png"

    with open(binary_file, "rb") as file:
        binary_data = file.read()

    # Calculate the size of the square image based on the binary data length
    image_size = int(len(binary_data) ** 0.5)
    if image_size * image_size < len(binary_data):
        image_size += 1

    # Pad the binary data to make it square-shaped
    padded_binary = binary_data + b'\x00' * (image_size * image_size - len(binary_data))

    # Convert binary data to RGB values
    pixels = [(padded_binary[i], padded_binary[i+1], padded_binary[i+2])
              for i in range(0, len(padded_binary), 3)]

    # Create the image and save it
    image = Image.new('RGB', (image_size, image_size))
    image.putdata(pixels)
    image.save(output_image)
    print(f"Image saved as {output_image}")

if __name__ == "__main__":
    binary_file_path = input("Enter the path to the binary file: ")
    binary_to_image(binary_file_path)
