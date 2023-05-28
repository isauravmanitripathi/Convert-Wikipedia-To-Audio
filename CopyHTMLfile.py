import os
import shutil

# Source and destination directories
source_dir = "/Users/sauravmanitripathi/Desktop/content upsc/TxtToHtml"
destination_dir = "/Users/sauravmanitripathi/Desktop/content upsc/HTML_Files"

# Copy files from source to destination
for filename in os.listdir(source_dir):
    source_file_path = os.path.join(source_dir, filename)
    destination_file_path = os.path.join(destination_dir, filename)

    # Copy the file
    shutil.copy2(source_file_path, destination_file_path)

print("All files have been copied from the source to the destination directory.")
