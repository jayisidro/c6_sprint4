from bs4 import BeautifulSoup
from IPython import embed
import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (Xll; Linux x86_64)'}

time.sleep(2)

BASE_URL = "https://albertyumol.github.io/"

def extract_html_content(target_url):
    response=requests.get(target_url,headers)
    return response.text

def main():
    html_doc = extract_html_content()
    soup = BeautifulSoup(html_doc, 'html.parser')
    target = soup.find(id="h2")
    print(target.get_text())

if __name__ == "__main__":
    main() 