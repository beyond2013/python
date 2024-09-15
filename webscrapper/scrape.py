import requests
from bs4 import BeautifulSoup

# Function to handle both cases (direct hit or list of search results)
def scrape_search_results(base_url, search_path, keyword):
    # Step 1: Construct the search URL
    search_url = f"{base_url}{search_path}?term={keyword}"

    # Step 2: Send a GET request to the search URL
    response = requests.get(search_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Step 3: Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Step 4: Determine if it's a direct hit or a list of results
        # Adjust these selectors based on the actual site structure
        search_results = soup.find_all('div', class_='search_result')  # Example: list of search results
        if search_results:
            # Case 1: A list of search results is returned
            print("Multiple search results found. Scraping the first result...")

            # Extract the first result's URL (assuming it's inside an <a> tag)
            first_result = search_results[0]
            first_link = first_result.find('a')['href']

            # If the link is relative, add the base URL
            if not first_link.startswith('http'):
                first_link = base_url + first_link

            # Step 5: Scrape the first search result page
            scrape_page_content(first_link)
        else:
            # Case 2: It's a direct hit (no list of results)
            print("Direct hit found. Scraping the content...")

            # Scrape the current page content (which is the exact match)
            scrape_page_content(search_url)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Helper function to scrape content from a specific page URL
def scrape_page_content(page_url):
    # Step 6: Send a GET request to the specific page
    response = requests.get(page_url)
    
    if response.status_code == 200:
        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the title and paragraphs
        title = soup.find('title').get_text()
        paragraphs = soup.find_all('p')
        content = '\n'.join([para.get_text() for para in paragraphs])

        # Display the scraped content
        print(f"\nTitle: {title}")
        print("\nContent:")
        print(content)
    else:
        print(f"Failed to retrieve the content page. Status code: {response.status_code}")

# Usage example
base_url = "https://store.steampowered.com"  # Replace with the target site's base URL
search_path = "/search/"           # Replace with the actual search path for the site
keyword = "cs4"    # Replace with your keyword

scrape_search_results(base_url, search_path, keyword)
