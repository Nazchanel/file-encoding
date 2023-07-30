import imageio
import os

def video_to_binary(input_video):
    frames = imageio.mimread(input_video)

    # Extract RGB values from frames
    pixels = []
    for frame in frames:
        pixels.extend(list(frame.getdata()))

    # Convert RGB values back to binary data
    binary_data = b''.join([bytes(pixel) for pixel in pixels])

    # Remove any padded zeros at the end
    binary_data = binary_data.rstrip(b'\x00')

    # Extract file type from the video name
    file_type = os.path.splitext(input_video)[0].split('-')[1]

    # Save the binary data to a file with the appropriate extension
    output_file = f"../../output/output.{file_type}"
    with open(output_file, 'wb') as file:
        file.write(binary_data)

    print(f"Binary data saved as {output_file}")

if __name__ == "__main__":
    input_video_path = input("Enter the path to the input video: ")
    video_to_binary(input_video_path)
