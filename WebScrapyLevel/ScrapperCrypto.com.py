import requests
from bs4 import BeautifulSoup

url = "https://help.crypto.com/en/"
all_main_page_anchors = []
all_in_page_anchors = []
one_page_anchors = []

content = requests.get(url)
soup = BeautifulSoup(content.content, features="lxml")

for main_page_anchors in soup.find_all('a', href=True):
    all_main_page_anchors.append("https://help.crypto.com"+main_page_anchors['href'])

all_main_page_anchors = all_main_page_anchors[2:len(all_main_page_anchors) - 4]

for anchor in all_main_page_anchors:
    content = requests.get(anchor)
    soup = BeautifulSoup(content.content, features="lxml")
    for in_page_anchors in soup.find_all('a', href=True):
        one_page_anchors.append("https://help.crypto.com"+in_page_anchors['href'])
    all_in_page_anchors.append(one_page_anchors[2:len(one_page_anchors) - 4])

print(str(all_in_page_anchors))
