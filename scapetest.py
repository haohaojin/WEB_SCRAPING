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
        return title[0].getText()
    except AttributeError as e:
        return None

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        h3list = bsObj.find_all("h3")
        for recipe in h3list:
            if "圣诞" in recipe.getText() and "糖霜" in recipe.getText():
                print(getRank(recipe.find("a").attrs['href']) + "|" + recipe.getText() + "|" + recipe.find("a").attrs['href'])
        title = bsObj.find_all(lambda tag: tag.getText() == '下一页')
        if (len(title) != 0):
            #print(title)
            newpage = title[0].find("a").attrs['href']
            #print(newpage)
            newpage_decoded = newpage.replace("圣诞 糖霜","%E5%9C%A3%E8%AF%9E%20%E7%B3%96%E9%9C%9C")
            #print(newpage_decoded)
            getTitle(newpage_decoded)
    except AttributeError as e:
        return None


# Breadmum http://www.douguo.com/u/u30362766298239/recipe
# 胡小may http://www.douguo.com/u/u55783496151049/recipe
# 圣诞糖霜 http://www.douguo.com/search/recipe/%E5%9C%A3%E8%AF%9E+%E7%B3%96%E9%9C%9C
getTitle("http://www.douguo.com/search/recipe/%E5%9C%A3%E8%AF%9E+%E7%B3%96%E9%9C%9C")