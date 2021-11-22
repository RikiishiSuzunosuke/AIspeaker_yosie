import requests
from bs4 import BeautifulSoup
import sys
import re

URL = "https://weather.yahoo.co.jp/weather/jp/14/"
target = "今日の天気"

#ページを解析
rest = requests.get(URL)
soup = BeautifulSoup(rest.text, 'lxml')

#データを抽出
anounce = soup.find('span', class_='time').text #class名がtimeのspanタグのtextデータを抽出している
place = soup.find('h1').text
weather = soup.find('dd', class_='forecast').p.img.get('alt')
high = soup.find('em', class_='high').get_text()
low = soup.find('em', class_='low').get_text()
precip = soup.find('p', class_='precip').get_text()

#抽出したデータを結合
phrase = anounce + " " + place + " " + target + 'は、' + weather + 'です。' + " " + '最高気温は、' + high + "度" + " " + '最低気温は、' + low + '度、' + '降水確率は、' + precip + 'です。'
#resultに出力テキストを入力
result = phrase

f = open('weather.txt', 'w')
f.write(result)
f.close()