import subprocess

files_to_run = [
    "FetchWikiLink.py",
    "WikiLinksToBeFetched.py",
    #"SavedWikiLinks.py",
    "CheckingOldLinks.py",
    "CopyFetchedLink.py",
    "fetchArticle.py",
    #"textToSpeech.py",
    #"AudioToHTMLConvert.py",
    #"TxtHtmlConvert.py",
    #"CopyHTMLfile.py",
    #"ClearUnderscore.py",
    #"UpdateIndexHTML.py",
    #"deleteDuplicateRowsInHTML.py",
    #"DeleteSimilarLinks.py",
    "ClearEveryFileAndFolder.py"
]

for file in files_to_run:
    subprocess.run(["python", file])
