import sys
from PIL import Image

def decode_image(encode_image_path):
    img = Image.open(encode_image_path)
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):  # R,G,B channels
                # Append the least significant bit of each color channel
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        if char == '\0':  # Null terminator signals end of message
            break
        message += char

    return message
def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encode_image_path>")
        return
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)
if __name__ == "__main__":
    main()