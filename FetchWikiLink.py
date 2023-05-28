import requests
from bs4 import BeautifulSoup
import re

# Ask for a Wikipedia link
url = input("Please enter a Wikipedia link: ")

# Send a GET request to the webpage
response = requests.get(url)

# Check the status of the request
if response.status_code != 200:
    print("Failed to get the page. Check the URL and try again.")
    exit()

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links on the webpage
links = soup.find_all('a', href=True)

# Regular expression to match only Wikipedia links
pattern = re.compile("^/wiki/")
# Regular expression to match links to be ignored
ignore_pattern = re.compile("^/wiki/(Help|File|Portal|Category|Template|Template_talk|Special|Wikipedia|Talk):|^/wiki/Main_Page")

# Initialize a set to hold already written links
written_links = set()

# Open the output file in write mode
with open("wikipedia_links.txt", "w") as file:
    for link in links:
        href = link['href']
        # Prepare the full link
        full_link = f"https://en.wikipedia.org{href}"
        # If the link matches the pattern, does not match the ignore pattern, and is not written before, write it to the file
        if pattern.match(href) and not ignore_pattern.match(href) and full_link not in written_links:
            file.write(full_link + "\n")
            # Add the written link to the set of written links
            written_links.add(full_link)

print("Links have been successfully saved to wikipedia_links.txt")
