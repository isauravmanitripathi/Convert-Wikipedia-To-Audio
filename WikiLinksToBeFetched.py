# Open the wikipedia_links.txt file
wiki_links_file_path = "/Users/sauravmanitripathi/Desktop/content upsc/wikipedia_links.txt"
with open(wiki_links_file_path, "r") as f:
    links = f.readlines()

# Print the total number of links
total_links = len(links)
print(f"Total number of links: {total_links}")

# Ask the user how many links they want
num_links = int(input("How many links do you want? "))

# Check if the input number is valid
if num_links > total_links or num_links < 0:
    print("Invalid number of links!")
else:
    # Get the selected links
    selected_links = links[:num_links]

    # Write the selected links to LinkToBeFetched.txt
    link_to_fetch_file_path = "/Users/sauravmanitripathi/Desktop/content upsc/LinkToBeFetched.txt"
    with open(link_to_fetch_file_path, "w") as f:
        f.writelines(selected_links)

    print(f"{num_links} links have been written to {link_to_fetch_file_path}")
