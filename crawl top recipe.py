from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import csv


html = urlopen("http://www.douguo.com/cookbook/1301535.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
title = bsObj.find_all("span", {"id":"collectsnum"})[0].previous_sibling.previous_sibling.getText() # .parent.previous_sibling.get_text()
print(title)
