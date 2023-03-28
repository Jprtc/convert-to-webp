# Convert images to webp

from PIL import Image
import os

def convert_to_webp(filename, input_path, output_path):
    extension = filename.split('.')[-1]
    fname = filename.split('.')[0]
    img = Image.open(os.path.join(input_path, filename))

    if extension == "png":
        img.save((os.path.join(output_path, fname + ".webp")), "webp", lossless=True)
        print(f"Converted {filename} to webp format with lossless compression.")
    elif extension == "jpg" or extension == "jpeg":
        img.save((os.path.join(output_path, fname + ".webp")), "webp", quality=85)
        print(f"Converted {filename} to webp format with 85% quality compression.")


def convert_all(input_path="input/", output_path="output/"):
    # create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, dirs, files in os.walk(input_path):
        for imagefile in files:
            if imagefile.endswith(".png") or imagefile.endswith(".jpg") or imagefile.endswith(".jpeg"):
                convert_to_webp(imagefile, os.path.join(root, ""), output_path)

if __name__ == "__main__":
    convert_all()
    print("All images in the specified directory have been converted to webp format.")