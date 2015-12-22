from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getRank(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return "e"
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        collectsnum = bsObj.find_all("font", {"id":"collectsnum"}) # .parent.previous_sibling.get_text()
        title = bsObj.find_all("h1") # .parent.previous_sibling.get_text()
        if collectsnum != None and len(collectsnum) > 0:
            if int(collectsnum[0].getText()) > 100:
                print(collectsnum[0].getText() + "|" + title[0].getText() + "|" + url)
    except AttributeError as e:
        return "e2"

for cookbookid in range(100000,10000000):
    #print(cookbookid)
    urlstring = "http://www.douguo.com/cookbook/" + str(cookbookid) + ".html"
    getRank(urlstring)