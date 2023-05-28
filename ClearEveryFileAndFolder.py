import os
import shutil

# Ask the user if they want to clear all the contents of the file
clear_contents = input("Do you want to clear all the contents of the file? (yes/no) ")

if clear_contents.lower() == "yes":
    # File and directory paths
    wiki_links_file_path = "/Users/sauravmanitripathi/Desktop/content upsc/wikipedia_links.txt"
    fetched_articles_dir = "/Users/sauravmanitripathi/Desktop/content upsc/Fetched Article"
    txt_to_html_dir = "/Users/sauravmanitripathi/Desktop/content upsc/TxtToHtml"

    # Clear file contents
    with open(wiki_links_file_path, "w") as f:
        pass

    # Delete all files in the fetched articles directory
    for filename in os.listdir(fetched_articles_dir):
        file_path = os.path.join(fetched_articles_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    # Delete all files in the TxtToHtml directory
    for filename in os.listdir(txt_to_html_dir):
        file_path = os.path.join(txt_to_html_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    print(f"All contents of {wiki_links_file_path} and files in directories have been cleared.")
elif clear_contents.lower() == "no":
    print("The contents of the file and directories will not be cleared.")
else:
    print("Invalid input!")
