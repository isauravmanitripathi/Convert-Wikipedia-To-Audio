import os
import re
from bs4 import BeautifulSoup

# Specify the directory where the HTML files are located
html_directory_path = "/Users/sauravmanitripathi/Desktop/content upsc/HTML_Files"

# Open the index.html file
index_file_path = "/Users/sauravmanitripathi/Desktop/content upsc/index.html"
with open(index_file_path, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Get the table in the HTML
table = soup.find("table", {"id": "myTable"})

# Get the list of HTML file names in the directory
html_files = [filename for filename in os.listdir(html_directory_path) if filename.lower().endswith(".html")]

# Get the list of all rows in the table
table_rows = table.findAll("tr")

# For each HTML file, check if it already exists in the table
for filename in html_files:
    # Remove the file extension
    file_name_cleaned = os.path.splitext(filename)[0]

    # Remove underscores and hyphens from the filename
    file_name_cleaned = re.sub(r"[_-]", " ", file_name_cleaned)

    # If the filename already exists in the table, remove the row and continue to the next filename
    for row in table_rows:
        cells = row.findAll("td")
        if len(cells) > 0 and cells[0].text.strip() == file_name_cleaned:
            print(f"Duplicated file path: {os.path.join(html_directory_path, filename)}")
            row.decompose()
            break

# Iterate over the HTML file names again to add new entries
for i, filename in enumerate(html_files, start=1): # start enumeration from 1
    # Remove the file extension
    file_name_cleaned = os.path.splitext(filename)[0]

    # Remove underscores and hyphens from the filename
    file_name_cleaned = re.sub(r"[_-]", " ", file_name_cleaned)

    # Create a new row with unique id
    tr = soup.new_tag("tr", id=f"row{i}")

    # Add the filename in the 'Name' column
    td = soup.new_tag("td")
    td.string = file_name_cleaned
    tr.append(td)

    # Add the file path in the 'View' column
    td = soup.new_tag("td")
    a = soup.new_tag("a", href="HTML_Files/" + filename)
    a.string = "View"
    td.append(a)
    tr.append(td)

    # Add empty 'Podcast' column
    td = soup.new_tag("td")
    tr.append(td)

    # Add empty 'Contact' column
    td = soup.new_tag("td")
    tr.append(td)

    # Add 'Completed' column with dropdown menu
    td = soup.new_tag("td")
    select = soup.new_tag("select", class_="completionStatus",
                          onchange=f"saveCompletionStatus('row{i}', 'completionStatus', this.value)")
    option1 = soup.new_tag("option", value="")
    option1.string = ""
    option2 = soup.new_tag("option", value="Yes")
    option2.string = "Yes"
    option3 = soup.new_tag("option", value="No")
    option3.string = "No"
    select.append(option1)
    select.append(option2)
    select.append(option3)
    td.append(select)
    tr.append(td)

    # Append the new row to the table
    table.append('\n')
    table.append(tr)
    table.append('\n')

# Write the updated HTML back to the file line by line
with open(index_file_path, "w") as f:
    for line in soup.prettify().split('\n'):
        f.write(line.rstrip())
        f.write('\n')

