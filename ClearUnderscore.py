import os

# Specify the directory where the HTML files are located
audio_directory_path = "Audio HTML Page"

# Get the list of HTML file names in the directory
audio_files = [filename for filename in os.listdir(audio_directory_path) if filename.lower().endswith(".html")]

# Iterate over the HTML file names to rename files with "_"
for filename in audio_files:
    if "_" in filename:
        new_filename = filename.replace("_", " ")
        os.rename(os.path.join(audio_directory_path, filename), os.path.join(audio_directory_path, new_filename))
