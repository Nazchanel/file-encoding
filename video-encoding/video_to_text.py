import cv2

def pixels_to_text(pixels):
    text = ""
    for pixel in pixels:
        r, g, b = pixel
        ascii_value = r  # We use the red channel to represent the ASCII value
        text += chr(ascii_value)
    return text

def decode_video_to_text(input_file):
    cap = cv2.VideoCapture(input_file)
    pixels_list = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        pixels = list(frame.reshape(-1, 3))
        pixels_list.extend(pixels)

    cap.release()
    return pixels_to_text(pixels_list)

if __name__ == "__main__":
    input_video_file = "output.mp4"
    output_text_file = "decoded_output.txt"
    decoded_text = decode_video_to_text(input_video_file)

    with open(output_text_file, "w") as file:
        file.write(decoded_text)
