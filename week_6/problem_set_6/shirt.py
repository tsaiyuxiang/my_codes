# shirt.py
import sys
import os
from PIL import Image, ImageOps

def main():
    len1 = len(sys.argv)
    if len1 < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len1 > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 比對 png jpg or jpeg
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Check if the input file exists
    if not os.path.isfile(input_file):
        sys.exit("Input file does not exist")

    try:
        # Open the shirt image
        shirt = Image.open("shirt.png")
        size = shirt.size  # Get shirt image size

        # Open the input image and resize it to shirt size
        input_image = Image.open(input_file)
        cropped = ImageOps.fit(input_image, size)

        # Overlay the shirt on the cropped image
        cropped.paste(shirt, shirt)

        # Save the result
        cropped.save(output_file)

    except Exception as e:
        sys.exit(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
