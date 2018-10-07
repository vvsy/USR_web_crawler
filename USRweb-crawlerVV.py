# -*- encoding: utf8-*-
from bs4 import BeautifulSoup
import requests
res = requests.get('https://www.ntpu.edu.tw/college/e4/')
res.encoding = 'big5'


soup = BeautifulSoup(res.text, 'html.parser')
tag_name = 'a.news'
tag_date = 'tr td.news'
date = soup.select(tag_date)

date = date[1].text


articles = soup.select(tag_name)
for art in articles:
    path = art['href']
    title = art.text
    break


pathE = "https://www.ntpu.edu.tw/college/e4/%s" % path
print(title)
print(pathE)
print('===========================================')
res2 = requests.get(pathE)
res2.encoding = 'big5'
soup2 = BeautifulSoup(res2.text, 'html.parser')
tag2_name = 'tr td.ch'
strong = soup2.select(tag2_name)
content = strong[1].text
print(content)
print('===========================================')


import re

reg_img = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')
images = reg_img.findall(res2.text)
print(images)

# response.encoding = 'big5'
# soup = BeautifulSoup(response.text, 'html')
# print(soup.find('社會實踐'))
# tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
# for drink in soup.select('{}'.format(tag)):
#    print(drink.get_text())
