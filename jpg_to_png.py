import os
from sys import argv
from PIL import Image

if len(argv) == 3:
    image_folder = argv[1]
    output_folder = argv[2]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(image_folder):
        img = Image.open(f'{image_folder}/{filename}')
        cleaned_name_tuple = os.path.splitext(filename)
        clean_file_name = cleaned_name_tuple[0]
        img.save(f'{output_folder}/{clean_file_name}.png', 'png')
        print(f'Done converting {filename} to {clean_file_name}.png !!!')
else:
    print("Please give valid arguments to the script.")
    print("Usage: ./jpg_to_png.py <Input folder> <Output folder>")
