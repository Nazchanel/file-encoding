from PIL import Image
import imageio
import os

def binary_to_video(binary_file):
    file_type = os.path.splitext(binary_file)[1][1:]
    output_video = f"../../output/output-{file_type}.mp4"

    with open(binary_file, "rb") as file:
        binary_data = file.read()

    # Calculate the size of the square frame based on the binary data length
    frame_size = int(len(binary_data) ** 0.5)
    if frame_size * frame_size < len(binary_data):
        frame_size += 1

    # Pad the binary data to make it square-shaped
    padded_binary = binary_data + b'\x00' * (frame_size * frame_size - len(binary_data))

    # Convert binary data to RGB values
    pixels = [(padded_binary[i], padded_binary[i+1], padded_binary[i+2])
              for i in range(0, len(padded_binary), 3)]

    # Create frames from RGB values
    frames = [Image.new('RGB', (frame_size, frame_size)) for _ in range(len(pixels))]
    for i, pixel in enumerate(pixels):
        frames[i].putpixel((i % frame_size, i // frame_size), pixel)

    # Save frames as an MP4 video
    imageio.mimwrite(output_video, frames, fps=30, quality=10)

    print(f"Video saved as {output_video}")

if __name__ == "__main__":
    binary_file_path = input("Enter the path to the binary file: ")
    binary_to_video(binary_file_path)
