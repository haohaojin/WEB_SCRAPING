from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.find_all("h3")
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.douguo.com/u/u30362766298239/recipe")

if title == None:
    print("Title could not be found")
else:
    print(len(title))

for t in title:
    print(t.getText())