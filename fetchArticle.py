import os
import requests
from bs4 import BeautifulSoup
import re

def fetch_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if 'wikipedia.org' in url:
        # This is a Wikipedia page
        title = soup.find('h1', {'id': 'firstHeading'}).text
        content_div = soup.find('div', {'id': 'mw-content-text'}).div

        # remove the references part
        for ref in content_div.find_all("div", {"class": "reflist"}):
            ref.decompose()

        content = []
        # add headers and paragraphs, but ignore 'li' tags
        for tag in content_div.find_all(['h2', 'h3', 'h4', 'h5', 'h6', 'p']):
            # remove the citation parts
            clean_text = re.sub(r'\[\d+(,\d+)*\]', '', tag.get_text())
            content.append(clean_text)

    elif 'scientificamerican.com' in url:
        # This is a Scientific American page
        title = soup.find('h1', {'class': 'article__headline'}).text.strip()
        content_div = soup.find('div', {'class': 'article__body'})

        content = []
        # add headers and paragraphs
        for tag in content_div.find_all(['h2', 'h3', 'h4', 'h5', 'h6', 'p']):
            content.append(tag.get_text())

    else:
        raise ValueError(f"URL {url} is not recognized. This script can only fetch articles from Wikipedia or Scientific American.")

    return title, '\n'.join(content)




def write_to_file(directory, filename, title, content, url):
    # Make sure the directory exists, if not, create it
    os.makedirs(directory, exist_ok=True)

    filepath = os.path.join(directory, filename)

    with open(filepath, 'w') as f:
        f.write(f'This article is from this: {url}\n\n{title}\n\n{content}\n\nThis article is from this: {url}')


def main():
    filepath = '/Users/sauravmanitripathi/Desktop/content upsc/LinkToBeFetched.txt'
    directory = '/Users/sauravmanitripathi/Desktop/content upsc/Fetched Article'

    with open(filepath, 'r') as f:
        urls = f.readlines()

    for url in urls:
        url = url.strip()  # remove any trailing newline
        try:
            title, content = fetch_article(url)
            filename = title.replace(' ', '_') + '.txt'
            write_to_file(directory, filename, title, content, url)
            print(f"Article saved at {directory}/{filename}")
        except Exception as e:
            print(f"Failed to fetch article from {url}: {str(e)}")


if __name__ == "__main__":
    main()
