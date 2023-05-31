import os

# Path to the directory where output files are stored
output_dir_path = 'FetchedLinksTillDate'

# Path to the Wikipedia links file
wikipedia_links_file_path = 'wikipedia_links.txt'

# Initialize an empty set to hold all links from the files in the output directory
all_links = set()

# Iterate over each file in the output directory
for file_name in os.listdir(output_dir_path):
    file_path = os.path.join(output_dir_path, file_name)
    # Read the content of the file with 'latin-1' encoding and add each link to the set
    with open(file_path, 'r', encoding='latin-1') as file:
        links = file.read().splitlines()
        all_links.update(links)

# Read the content of the Wikipedia links file
with open(wikipedia_links_file_path, 'r', encoding='latin-1') as file:
    wikipedia_links = file.read().splitlines()

# Filter out any links that also exist in the output directory files
filtered_links = [link for link in wikipedia_links if link not in all_links]

# Write the filtered links back to the Wikipedia links file
with open(wikipedia_links_file_path, 'w', encoding='latin-1') as file:
    file.write('\n'.join(filtered_links))
