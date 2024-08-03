import os

from PIL import Image

# Get logo name and new folder name from user input
LOGO_NAME = input('Enter the logo name with extension: ')
NEW_FOLDER_NAME = input('Enter the new folder name: ')

# Open the logo image
logo_image = Image.open(LOGO_NAME)
logo_width, logo_height = logo_image.size

# Ensure the logo image is in the correct mode
if logo_image.mode != 'RGBA':
    logo_image = logo_image.convert('RGBA')

# Create the new folder if it doesn't exist
if not os.path.exists(NEW_FOLDER_NAME):
    os.makedirs(NEW_FOLDER_NAME)

for filename in os.listdir('.'):
    # Check if the file is an image and not the logo itself
    if (filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg")) and filename != LOGO_NAME:
        img = Image.open(filename)
        width, height = img.size

        # Convert the image to RGBA if it's not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Add the logo to the image
        img.paste(logo_image, (width - logo_width, height - logo_height), logo_image)

        # Save the modified image in the new folder
        img.save(os.path.join(NEW_FOLDER_NAME, filename))

print('Done')
