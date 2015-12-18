from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getRank(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.find_all("font", {"id":"collectsnum"}) # .parent.previous_sibling.get_text()
        print(title[0].getText())
    except AttributeError as e:
        return None


getRank("http://www.douguo.com/cookbook/1301535.html")