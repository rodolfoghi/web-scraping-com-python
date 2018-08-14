from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getHtml(url):
    try:
        return urlopen(url)
    except HTTPError:
        return None

html = getHtml("http://pythonscraping.com/pages/warandpeace.html")

if html is None:
    print("HTML was not found")
else:
    bsObj = BeautifulSoup(html)
    nameList = bsObj.find_all("span", {"class": "green"})
    for name in nameList:
        print(name.get_text())