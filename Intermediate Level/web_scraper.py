import requests
from bs4 import BeautifulSoup
def scrape_shadowfox_blog():
    url = "https://shadowfox.in/"  
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2') 
        print("🔍 Top Blog Titles:")
        for i, article in enumerate(articles[:5], start=1):
            print(f"{i}. {article.text.strip()}")
    else:
        print("Failed to fetch the page. Status code:", response.status_code)
if __name__ == "__main__":
    scrape_shadowfox_blog()
