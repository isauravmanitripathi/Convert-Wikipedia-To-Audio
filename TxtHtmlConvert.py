import os
import markdown
import re

# define the path
input_dir = 'Fetched Article'
output_dir = 'TxtToHtml'

# check if output directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# iterate over files in the directory
for filename in os.listdir(input_dir):
    # check if file is a text file
    if filename.endswith('.txt'):
        # open the text file
        with open(os.path.join(input_dir, filename), 'r') as file:
            data = file.read()

            # remove numbers in brackets
            data = re.sub(r'\[\d+\]', '', data)

            # convert the markdown text to HTML
            html_data = markdown.markdown(data)

            # create HTML file with the same name in the output directory
            html_filename = os.path.splitext(filename)[0] + '.html'
            with open(os.path.join(output_dir, html_filename), 'w') as html_file:
                html_file.write(html_data)
        print(f'Converted {filename} to HTML.')
