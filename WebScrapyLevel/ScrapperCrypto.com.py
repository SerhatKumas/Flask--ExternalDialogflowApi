import requests
from bs4 import BeautifulSoup

url = "https://help.crypto.com/en/"

web_content = requests.get(url)
soup = BeautifulSoup(web_content.content, features="lxml")

for a in soup.find_all('a', href=True):
    print("Found the URL:", a['href'])
