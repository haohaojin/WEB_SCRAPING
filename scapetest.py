import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from random import randint
import csv
import datetime
import time
import socket

start_time = time.time()
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

# web scraping page 121

def getBookmark(url):
    try:
        html = urllib.request.urlopen(url,timeout=60)
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
        html = urllib.request.urlopen(url,timeout=60)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = title = bsObj.find_all("span", {"id": "collectsnum"})[0].previous_sibling.previous_sibling.getText()
        return title
    except AttributeError as e:
        return None


def getRecipe(user,url):
    try:
        html = urllib.request.urlopen(url,timeout=60)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        h3list = bsObj.find_all("h3")
        # print(h3list)
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
            print(user + "|" + today.strftime('%Y/%m/%d') + "|" + created_date.strftime('%Y/%m/%d') + "|" + getVisit(
                recipe_url) + "|" + getBookmark(recipe_url) + "|" + recipe.getText() + "|" + recipe.find("a").attrs[
                      'href'])
            writer.writerow((user, today.strftime('%Y/%m/%d'), created_date.strftime('%Y/%m/%d'), getVisit(recipe_url),
                             getBookmark(recipe.find("a").attrs['href']), recipe.getText(),
                             recipe.find("a").attrs['href']))
        title = bsObj.find_all(lambda tag: tag.getText() == '下一页')
        if (len(title) != 0):
            # print(title)
            newpage = title[0].find("a").attrs['href']
            # print(newpage)
            newpage_decoded = newpage.replace("圣诞 糖霜", "%E5%9C%A3%E8%AF%9E%20%E7%B3%96%E9%9C%9C")
            # print(newpage_decoded)
            # time.sleep(randint(5, 9))
            getRecipe(user,newpage_decoded)
    except AttributeError as e:
        return None


# Breadmum  http://www.douguo.com/u/u30362766298239/recipe
# 胡小may   http://www.douguo.com/u/u55783496151049/recipe
# 美国厨娘 http://www.douguo.com/u/u35246655713154/recipe
# 小米554 http://www.douguo.com/u/u21252191430097/recipe
# 爱生活的馋猫 http://www.douguo.com/u/u20468009171777/recipe
# 夏夏夏洛特的烤箱 http://www.douguo.com/u/u42706554805034/recipe
# january0106 http://www.douguo.com/u/u12762231872542/recipe

searchListFull = {'Breadmum': 'http://www.douguo.com/u/u30362766298239/recipe', #
              '胡小may': 'http://www.douguo.com/u/u55783496151049/recipe', #
              '美国厨娘': 'http://www.douguo.com/u/u35246655713154/recipe',
              '小米554': 'http://www.douguo.com/u/u21252191430097/recipe', #
              '爱生活的馋猫': 'http://www.douguo.com/u/u20468009171777/recipe',#
              '夏夏夏洛特的烤箱': 'http://www.douguo.com/u/u42706554805034/recipe',#
              'january0106': 'http://www.douguo.com/u/u12762231872542/recipe'}

searchList = {'Breadmum': 'http://www.douguo.com/u/u30362766298239/recipe', #
              '胡小may': 'http://www.douguo.com/u/u55783496151049/recipe', #
              '美国厨娘': 'http://www.douguo.com/u/u35246655713154/recipe',
              '小米554': 'http://www.douguo.com/u/u21252191430097/recipe', #
              '爱生活的馋猫': 'http://www.douguo.com/u/u20468009171777/recipe',#
              '夏夏夏洛特的烤箱': 'http://www.douguo.com/u/u42706554805034/recipe',#
              'january0106': 'http://www.douguo.com/u/u12762231872542/recipe'}

today = datetime.date.today()


with open("C:/Users/hao.jin/Desktop/Python/" + str(today) + ".csv", 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(('User','Added Date', 'Created Date', 'Visited', 'Bookmarked', 'Name', 'Link'))
    for i in searchList:
        print(i,searchList[i])
        getRecipe(i,searchList[i])
        print("--- %s seconds ---" % (time.time() - start_time))

csvFile.close()
print("--- %s seconds ---" % (time.time() - start_time))