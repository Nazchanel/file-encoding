from PIL import Image, ImageDraw
import cv2
import numpy as np

def text_to_pixels(text, width, height):
    image = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(image)
    font_size = 20
    try:
        # Use a truetype font if available
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # Fallback to a default font if truetype is not available
        font = ImageFont.load_default()
    
    current_h, pad = 10, 5
    for line in text.split('\n'):
        w, h = draw.textsize(line, font=font)
        draw.text(((width - w) // 2, current_h), line, fill="white", font=font)
        current_h += h + pad

    return list(image.getdata())

# Rest of the code remains the same


def create_video_from_text(input_file, output_file, width=1920, height=1080, fps=10):
    with open(input_file, "r") as file:
        text = file.read()

    pixels = text_to_pixels(text, width, height)
    frames = [pixels[i:i+width] for i in range(0, len(pixels), width)]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    for frame_pixels in frames:
        frame = Image.new("RGB", (width, height))
        frame.putdata(frame_pixels)
        frame_array = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        out.write(frame_array)

    out.release()

if __name__ == "__main__":
    input_text_file = "input.txt"
    output_video_file = "output.mp4"
    create_video_from_text(input_text_file, output_video_file)
