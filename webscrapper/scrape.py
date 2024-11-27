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
    html_content=""
    print("Fetching URL...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not fetch URL. Status code: {response.status_code}")
        return None

    print("Parsing HTML...")
    soup = BeautifulSoup(response.content, 'html.parser')

    print("Finding div with id 'appHubAppName'...")
    game_name= soup.find('div', id='appHubAppName')

    if game_name is None:
        print("Error: Could not find the title of the Game")
    html_content = "<title>" + game_name.text.strip() + "</title>"
    #print(html_content)
    # print("Finding div with id 'game_area_description'...")
    game_area_description = soup.find('div', id='game_area_description')
   
    if game_area_description is None:
        print("Error: Could not find div with id 'game_area_description'")
        return None

    #print("Extracting content...")
    inner_html = "".join(str(child) for child in game_area_description.contents)
    pretty_html = BeautifulSoup(inner_html, 'html.parser').prettify()
    html_content += pretty_html 

    sys_req = soup.find('div', class_="game_page_autocollapse sys_req")

    if sys_req is None:
        print("Error: Could not find div with class 'game_page_autocollapse sys_req'")
        return None

    inner_html = "".join(str(child) for child in sys_req.contents)
    pretty_html = BeautifulSoup(inner_html, 'html.parser').prettify()
    html_content += pretty_html 

    #markdown_content = markdown.markdown(html_content)
    return html_content

if __name__ == "__main__":
    url = "https://store.steampowered.com/app/730/CounterStrike_2/"  # Replace with the actual URL
    content = scrape_content(url)

    if content:
        print("Content extracted successfully:")
        print(content)
    else:
        print("Content extraction failed.")