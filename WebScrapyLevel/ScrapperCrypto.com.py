import requests
from bs4 import BeautifulSoup

url = "https://help.crypto.com/en/"
all_main_page_anchors = []
all_in_page_anchors = []
one_page_anchors = []
intent_content = ""
final_content_array = []

content = requests.get(url)
soup = BeautifulSoup(content.content, features="lxml")

for main_page_anchors in soup.find_all('a', href=True):
    if main_page_anchors['href'] != "/en/" and main_page_anchors['href'] != "https://facebook.com/CryptoComOfficial" and \
            main_page_anchors['href'] != "https://twitter.com/cryptocom" and main_page_anchors[
        'href'] != "https://linkedin.com/company/cryptocom" \
            and main_page_anchors['href'] != "https://www.crypto.com":
        all_main_page_anchors.append("https://help.crypto.com"+main_page_anchors['href'])

for anchor in all_main_page_anchors:
    content = requests.get(anchor)
    soup = BeautifulSoup(content.content, features="lxml")
    for in_page_anchors in soup.find_all('a', href=True):
        if in_page_anchors['href'] != "/en/" and in_page_anchors['href'] != "https://facebook.com/CryptoComOfficial" and \
                in_page_anchors['href'] != "https://twitter.com/cryptocom" and in_page_anchors['href'] != "https://linkedin.com/company/cryptocom" \
                and in_page_anchors['href'] != "https://www.crypto.com":
            one_page_anchors.append("https://help.crypto.com"+in_page_anchors['href'])


for link in one_page_anchors:
    content = requests.get(link)
    soup = BeautifulSoup(content.content, features="lxml")
    for tag in soup.find_all(["h2", "p"]):
        # print(tag.name + ' ' + tag.text.strip())
        if tag.name == "h2":
            if intent_content != "":
                final_content_array.append(intent_content)
                intent_content = ""
            final_content_array.append(tag.text.strip())
        if tag.name == "p":
            intent_content += " " + tag.text.strip()

print(final_content_array)
f = open("intent.txt", "w")
for part in final_content_array:
    f.write(part + "\n")
f.close()
