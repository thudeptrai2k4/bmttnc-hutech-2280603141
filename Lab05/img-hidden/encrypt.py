import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size

    # Convert message to binary + delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # delimiter to mark end of message

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for color_channel in range(3):  # Only RGB channels, ignore alpha if any
                if data_index < len(binary_message):
                    # Replace least significant bit with message bit
                    pixel[color_channel] = (pixel[color_channel] & ~1) | int(binary_message[data_index])
                    data_index += 1
            img.putpixel((col, row), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print(f"Message encoded and saved to {encoded_image_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    image_path = sys.argv[1]  # fixed typo from sys.agrv to sys.argv
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()
