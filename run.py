import subprocess

files_to_run = [
    "FetchWikiLink.py",
    "WikiLinksToBeFetched.py",
    "SavedWikiLinks.py",
    "fetchArticle.py",
    "textToSpeech.py",
    "TxtHtmlConvert.py",
    "CopyHTMLfile.py",
    "DeleteCopy.py",
    "UpdateIndexHTML.py",
    "deleteDuplicateRowsInHTML.py",
    "DeleteSimilarLinks.py",
    "ClearEveryFileAndFolder.py"
]

for file in files_to_run:
    subprocess.run(["python", file])
