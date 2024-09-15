print("hello world")
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
page = requests.get(URL, headers=HEADERS, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")
divs = soup.find_all("div",class_='column is-half')
for div in divs:
    job = div.find("h2").get_text()
    company = div.find("h3").get_text()
    postDate = div.find("time").get_text()
    print(f'{job} for {company} (posted on {postDate})')