import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.cnn.com/world'
headers = {'User-Agent': 'Mozilla/5.0'}

def scrape_headlines():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Example finding all h2 tags (commom for headlines)
    headlines = [h.text.strip() for h in soup.find_all('h2')]

    with open('headlines.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['Headline'])
        for line in headlines:
            writer.writerow([line])
        print("Headlines saved to headlines.csv")

scrape_headlines()