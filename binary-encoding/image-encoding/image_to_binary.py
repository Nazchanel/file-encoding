from PIL import Image
import os

def image_to_binary(input_image):
    with Image.open(input_image) as image:
        pixels = list(image.getdata())

    # Convert RGB values back to binary data
    binary_data = b''.join([bytes(pixel) for pixel in pixels])

    # Remove any padded zeros at the end
    binary_data = binary_data.rstrip(b'\x00')

    # Extract file type from the image name
    file_type = os.path.splitext(input_image)[0].split('-')[1]

    # Save the binary data to a file with the appropriate extension
    output_file = f"../../output/output.{file_type}"
    with open(output_file, 'wb') as file:
        file.write(binary_data)

    print(f"Binary data saved as {output_file}")

if __name__ == "__main__":
    input_image_path = input("Enter the path to the input image: ")
    image_to_binary(input_image_path)
