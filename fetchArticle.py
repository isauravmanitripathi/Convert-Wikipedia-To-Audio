import os
import requests
from bs4 import BeautifulSoup


def fetch_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1', {'id': 'firstHeading'}).text
    content_div = soup.find('div', {'id': 'mw-content-text'}).div

    # remove the references part
    for ref in content_div.find_all("div", {"class": "reflist"}):
        ref.decompose()

    content = []
    # add headers and paragraphs
    for tag in content_div.find_all(['h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']):
        if tag.name == 'li':
            content.append('  * ' + tag.get_text())
        else:
            content.append(tag.get_text())

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
