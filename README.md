AddLogo-ForAll-Photos-Automation-PythonApp
Description
This Python script automates the process of adding a logo to all images in a directory. It uses the Python Imaging Library (PIL) to open, modify, and save images. The script prompts the user for the logo image file and the name of a new folder to store the modified images.

Features
Prompts user for the logo image and the new folder name.
Opens and processes all image files in the current directory (excluding the logo image).
Ensures both the logo and target images are in RGBA mode for proper transparency handling.
Pastes the logo at the bottom right corner of each image.
Saves the modified images in a specified new folder.
