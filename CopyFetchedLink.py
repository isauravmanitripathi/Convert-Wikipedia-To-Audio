import os

# Path to the input file
input_file_path = 'LinkToBeFetched.txt'

# Path to the output file
output_file_path = 'FetchedLinksTillDate/Fetches.txt'

# Read the content of the input file
with open(input_file_path, 'r') as input_file:
    new_links = input_file.read().splitlines()

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Initialize a set to hold all existing links
existing_links = set()

# If the output file already exists, read its content
if os.path.exists(output_file_path):
    with open(output_file_path, 'r') as output_file:
        existing_links = set(line.strip() for line in output_file)

# Filter out any links that already exist in the output file
new_links = [link for link in new_links if link not in existing_links]

# If there are any new links, append them to the output file
if new_links:
    with open(output_file_path, 'a') as output_file:
        for link in new_links:
            output_file.write(link + '\n')
