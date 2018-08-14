from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.h1
    except AttributeError:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title cloud not be found")
else:
    print(title)
