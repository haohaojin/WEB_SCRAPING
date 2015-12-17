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
        h3list = bsObj.find_all("h3")
        for recipe in h3list:
            print(recipe.getText())
        title = bsObj.find_all(lambda tag: tag.getText() == '下一页')
        if (len(title) != 0):
            #print(title)
            newpage = title[0].find("a").attrs['href']
            #print(newpage)
            getTitle(newpage)
    except AttributeError as e:
        return None


getTitle("http://www.douguo.com/u/u30362766298239/recipe")