'''
import os
from difflib import SequenceMatcher
import re

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def strip_number_and_copy(filename):
    # remove extension
    base = os.path.splitext(filename)[0]
    # remove any numbers at the end
    base = re.sub(r'\d+$', '', base)
    # remove any " copy" at the end
    base = re.sub(r' copy$', '', base)
    return base

dir1 = "/Users/sauravmanitripathi/Desktop/content upsc/Fetched Article"
dir2 = "/Users/sauravmanitripathi/Desktop/content upsc/TxtToHtml"

dir1_files = set(os.listdir(dir1))
dir2_files = set(os.listdir(dir2))

for file1 in dir1_files:
    base1 = strip_number_and_copy(file1)
    for file2 in dir2_files:
        base2 = strip_number_and_copy(file2)
        if base1 == base2 or similarity(base1, base2) > 0.9:
            file_to_delete = os.path.join(dir2, file2)
            os.remove(file_to_delete)
            print(f"Deleted file: {file_to_delete}")

'''