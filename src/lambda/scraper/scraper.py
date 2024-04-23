# scraper.py - The core scraping logic
import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    # Send a request to the website
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant data (example: article titles)
    articles = [article.get_text() for article in soup.find_all('h2')]

    return articles
