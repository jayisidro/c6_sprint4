from bs4 import BeautifulSoup
from IPython import embed
import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

time.sleep(2)

BASE_URL = "https://albertyumol.github.io/"

def extract_html_content(target_url):
    response=requests.get(target_url,headers)
    return response.text

def main():
    target_page = BASE_URL + "index.html"

    html_content = extract_html_content(target_page)

    soup = BeautifulSoup(html_content, 'html.parser')
    bash = soup.find_all('div', 'list_item')

    for list_ in bash:
        print(list_.find('a').get_text('href'))


if __name__ == "__main__":
    main() 