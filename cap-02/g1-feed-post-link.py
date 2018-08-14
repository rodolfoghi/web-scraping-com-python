from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getHtml(url):
    try:
        return urlopen(url)
    except HTTPError:
        return None

html = getHtml("https://g1.globo.com/")

if html is None:
    print("HTML was not found")
else:
    bsObj = BeautifulSoup(html, "html.parser")
    feed_post_link_List = bsObj.find_all("a", {"class": "feed-post-link"})
    for feed_post_link in feed_post_link_List:
        print("=" * 150)
        print("Título: " + feed_post_link.get_text())
        print("Link: " + feed_post_link.attrs['href'])
        print("=" * 150)