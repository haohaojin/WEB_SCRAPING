from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from random import randint
import csv
import datetime
import time

# web scraping page 121

def getBookmark(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.find_all("span", {"id": "collectsnum"})  # .parent.previous_sibling.get_text()
        return title[0].getText()
    except AttributeError as e:
        return None


def getVisit(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = title = bsObj.find_all("span", {"id": "collectsnum"})[0].previous_sibling.previous_sibling.getText()
        return title
    except AttributeError as e:
        return None


def getRecipe(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        h3list = bsObj.find_all("h3")
        for recipe in h3list:
            # if "圣诞" in recipe.getText() and "糖霜" in recipe.getText():
            year = bsObj.find("span", {"class": "yearnum dblok"}).getText()[0:4]
            month_temp = recipe.parent.parent.parent.find("span", {"class": "dblok pts"}).getText()
            if len(month_temp) == 3:
                month = month_temp[0:2]
            else:
                month = "0" + month_temp[0]
            day = month_temp = recipe.parent.parent.parent.find("span", {"class": "tdate"}).getText()
            recipe_url = recipe.find("a").attrs['href']
            created_date = datetime.date(int(year), int(month), int(day))
            diff = today - created_date
            print(created_date.strftime('%Y-%m-%d') + "|" + str(diff.days) + "|" + getVisit(
                recipe_url) + "|" + getBookmark(recipe_url) + "|" + recipe.getText() + "|" + recipe.find("a").attrs[
                      'href'])
            writer.writerow((created_date.strftime('%Y-%m-%d'), str(diff.days), getVisit(recipe_url),
                             getBookmark(recipe.find("a").attrs['href']), recipe.getText(),
                             recipe.find("a").attrs['href']))
        title = bsObj.find_all(lambda tag: tag.getText() == '下一页')
        if (len(title) != 0):
            # print(title)
            newpage = title[0].find("a").attrs['href']
            # print(newpage)
            newpage_decoded = newpage.replace("圣诞 糖霜", "%E5%9C%A3%E8%AF%9E%20%E7%B3%96%E9%9C%9C")
            # print(newpage_decoded)
            time.sleep(randint(5, 9))
            getRecipe(newpage_decoded)
    except AttributeError as e:
        return None


# Breadmum http://www.douguo.com/u/u30362766298239/recipe
# 胡小may http://www.douguo.com/u/u55783496151049/recipe
# 圣诞糖霜 http://www.douguo.com/search/recipe/%E5%9C%A3%E8%AF%9E+%E7%B3%96%E9%9C%9C

today = datetime.date.today()

with open("C:/Users/hao.jin/Desktop/Python/test.csv", 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(('Created Date', 'Elapsed Days', 'Visited', 'Bookmarked', 'Name', 'Link'))
    getRecipe("http://www.douguo.com/u/u30362766298239/recipe")
csvFile.close()
