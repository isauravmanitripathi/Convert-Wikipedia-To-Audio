import os
from datetime import datetime

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def get_new_file_name(folder_path):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %I:%M %p")
    file_name = f"{timestamp}.txt"
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        return get_new_file_name(folder_path)
    else:
        return file_path

# Read the content of wikipedia_links.txt and LinkToBeFetched.txt
wiki_links = read_file('wikipedia_links.txt')
to_fetch_links = read_file('LinkToBeFetched.txt')

# Combine the links and remove duplicates
all_links = set(wiki_links + to_fetch_links)

# Specify the destination folder for saving the links
destination_folder = 'Saved Links'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Generate the new file name with date and time
new_file_path = get_new_file_name(destination_folder)

# Create the necessary folders if they don't exist
folder_path = os.path.dirname(new_file_path)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Write the links to the new file
write_file(new_file_path, all_links)
