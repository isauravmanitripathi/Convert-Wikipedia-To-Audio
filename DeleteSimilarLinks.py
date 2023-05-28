def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Read the content of wikipedia_links.txt and LinkToBeFetched.txt
wiki_links = read_file('/Users/sauravmanitripathi/Desktop/content upsc/wikipedia_links.txt')
to_fetch_links = read_file('/Users/sauravmanitripathi/Desktop/content upsc/LinkToBeFetched.txt')

# Find the similar links
similar_links = set(wiki_links) & set(to_fetch_links)

# Remove similar links from both files
wiki_links = [link for link in wiki_links if link not in similar_links]
to_fetch_links = [link for link in to_fetch_links if link not in similar_links]

# Write the updated content back to the files
write_file('/Users/sauravmanitripathi/Desktop/content upsc/wikipedia_links.txt', wiki_links)
write_file('/Users/sauravmanitripathi/Desktop/content upsc/LinkToBeFetched.txt', to_fetch_links)
