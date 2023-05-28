import os
from bs4 import BeautifulSoup

# Open the index.html file
index_file_path = "/Users/sauravmanitripathi/Desktop/content upsc/index.html"
with open(index_file_path, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Get the table in the HTML
table = soup.find("table", {"id": "myTable"})

# Get the list of all rows in the table
table_rows = table.findAll("tr")

# Create a dictionary to store unique names
unique_names = {}

# For each row in the table
for row in table_rows:
    cells = row.findAll("td")
    # Check if row has name cell and if the name is unique
    if len(cells) > 0 and cells[0].text.strip() not in unique_names:
        # Store unique name
        unique_names[cells[0].text.strip()] = True
    elif len(cells) > 0 and cells[0].text.strip() in unique_names:
        # Remove the duplicate row
        row.decompose()

# Write the updated HTML back to the file
with open(index_file_path, "w") as f:
    for line in soup.prettify().split('\n'):
        f.write(line.rstrip())
        f.write('\n')
