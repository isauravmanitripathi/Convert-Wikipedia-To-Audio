# Open the wikipedia_links.txt file
wiki_links_file_path = "/Users/sauravmanitripathi/Desktop/content upsc/wikipedia_links.txt"
with open(wiki_links_file_path, "r") as f:
    links = f.readlines()

# Print the total number of links
total_links = len(links)
print(f"Total number of links: {total_links}")


def search_links():
    keyword = input("Enter a keyword to search: ")
    matched_links = [link for link in links if keyword in link]

    if matched_links:
        print("Links found:")
        for i, link in enumerate(matched_links, start=1):
            print(f"{i}. {link}")
        link_number = int(input("Enter the number of the link you want: "))
        if link_number > len(matched_links) or link_number < 1:
            print("Invalid link number!")
        else:
            return matched_links[link_number - 1]  # adjust for 0-indexing
    else:
        print("No matching links found!")


def fetch_specific_link():
    specific_link_number = int(input("Which link number do you want? "))
    if specific_link_number > total_links or specific_link_number < 1:
        print("Invalid link number!")
    else:
        return links[specific_link_number - 1]  # adjust for 0-indexing


def fetch_links():
    selected_links = []

    # Ask the user how many links they want
    num_links = int(input("How many links do you want? "))
    if num_links > total_links or num_links < 0:
        print("Invalid number of links!")
    else:
        selected_links.extend(links[:num_links])

    while True:
        more_links = input("Do you want to fetch a specific link or search for a link? (specific/search/no) ")
        if more_links.lower() == 'specific':
            specific_link = input("Do you want to enter a link number or a specific URL? (number/url) ")
            if specific_link.lower() == 'number':
                selected_link = fetch_specific_link()
                if selected_link:
                    selected_links.append(selected_link)
            elif specific_link.lower() == 'url':
                url_link = input("Enter the specific URL: ")
                selected_links.append(url_link + '\n')
            else:
                print("Invalid option!")
        elif more_links.lower() == 'search':
            searched_link = search_links()
            if searched_link:
                selected_links.append(searched_link)
        else:
            break

    # Write the selected links to LinkToBeFetched.txt
    link_to_fetch_file_path = "/Users/sauravmanitripathi/Desktop/content upsc/LinkToBeFetched.txt"
    with open(link_to_fetch_file_path, "w") as f:
        f.writelines(selected_links)

    print(f"{len(selected_links)} links have been written to {link_to_fetch_file_path}")


fetch_links()
