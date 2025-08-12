import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        sys.exit("Input file does not exist")
    if not input_file.lower().endswith((".png", "jpg", "jpeg")):
        sys.exit("Invalid Input")

    in_ext = os.path.splitext(input_file)[1].lower()
    out_ext = os.path.splitext(output_file)[1].lower()

    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        input_image = Image.open(input_file)

        re_image = ImageOps.fit(input_image, shirt.size)

        re_image.paste(shirt, (0, 0), shirt)

        re_image.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
