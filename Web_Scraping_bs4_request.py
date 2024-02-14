import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.select('.quoteText')  
        descriptions = soup.select('.authorOrTitle')
        likes = soup.select('.smallText')
        
        data = []
        for title, description, like in zip(titles, descriptions, likes):
            data.append({
                'author': description.get_text(),
                'text': title.get_text(),
                'likes': like.get_text()
            })
        return data
    else:
        print(f"Failed to fetch {url}")
        return []

urls = [f'https://www.goodreads.com/quotes?page={i}' for i in range(1, 101)]

all_data = []
for url in urls:
    page_data = scrape_page(url)
    all_data.extend(page_data)

df = pd.DataFrame(all_data)

file_name = 'scraped_data.xlsx'
df.to_excel(file_name, index=False)

print(f"Data has been scraped and saved to {file_name}")