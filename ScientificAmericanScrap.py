import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def extract_text_from_url(url):
    options = Options()
    options.headless = True  # Run the browser in headless mode (without a visible window)

    # Provide the path to the Firefox binary (optional)
    # options.binary_location = '/path/to/firefox-binary'  # Uncomment and replace with the actual path if needed

    # Provide the path to the GeckoDriver executable
    # Update the path based on your actual GeckoDriver location
    geckodriver_path = '/path/to/geckodriver'  # Replace with the actual path

    driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
    driver.get(url)

    # Wait for the page to load (adjust the delay if needed)
    driver.implicitly_wait(10)

    # Find the elements that contain the text you want to extract
    # Customize the CSS selectors according to the specific structure of the webpage
    text_elements = driver.find_elements_by_css_selector('.article-body__text')

    # Extract the text from the selected elements
    extracted_text = '\n'.join([element.text for element in text_elements])

    driver.quit()
    return extracted_text


# Create the folder to store the fetched articles if it doesn't exist
folder_path = "/Users/sauravmanitripathi/Desktop/content upsc/Fetched Article"
os.makedirs(folder_path, exist_ok=True)

# Ask the user to input the URLs
urls = []
num_urls = int(input("Enter the number of URLs: "))
for i in range(num_urls):
    url = input(f"Enter URL {i + 1}: ")
    urls.append(url)

# Fetch and save the extracted text for each URL as a .txt file
for i, url in enumerate(urls):
    extracted_text = extract_text_from_url(url)
    if extracted_text:
        file_name = f"article_{i + 1}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        print(f"Article {i + 1} saved as {file_path}")
    else:
        print(f"Failed to extract text from {url}.")
