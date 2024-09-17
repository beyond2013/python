import requests
from bs4 import BeautifulSoup
import markdown

def scrape_content(url):
    """Scrapes the content of the div with id "aboutThisGame" from a given URL.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        The extracted content as a string.
    """

    print("Fetching URL...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not fetch URL. Status code: {response.status_code}")
        return None

    print("Parsing HTML...")
    soup = BeautifulSoup(response.content, 'html.parser')

    print("Finding div with id 'appHubAppName'...")
    content_div = soup.find('div', id='appHubAppName')

    if content_div is None:
        print("Error: Could not find the title of the Game")
    html_content = "<title>" + content_div.text.strip() + "</title>"
    #print(html_content)
    print("Finding div with id 'game_area_description'...")
    content_div = soup.find('div', id='game_area_description')
   
    if content_div is None:
        print("Error: Could not find div with id 'game_area_description'")
        return None

    print("Extracting content...")
    inner_html = "".join(str(child) for child in content_div.contents)
    pretty_html = BeautifulSoup(inner_html, 'html.parser').prettify()
    html_content += pretty_html 
    markdown_content = markdown.markdown(html_content)

    return markdown_content

if __name__ == "__main__":
    url = "https://store.steampowered.com/app/730/CounterStrike_2/"  # Replace with the actual URL
    content = scrape_content(url)

    if content:
        print("Content extracted successfully:")
        print(content)
    else:
        print("Content extraction failed.")