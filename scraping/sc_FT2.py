import requests
from bs4 import BeautifulSoup
import sys
import re

url = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
rest = requests.get(url)

soup = BeautifulSoup(rest.text, 'html.parser')
#記載されている日付を取得
today = soup.find(class_='txt').text
#日付を入れてタイトル作成、textに代入
text = today + "の占いです" + " "

#spanタグで書かれている星座の名前をすべて取得
span_list = soup.find_all('span')
#一番先頭は不要なspanタグの要素なので削除
del span_list[0]
#class名がft01のpタグから、各星座の運勢を抽出する
text_list = soup.find_all('p', class_='ft01')

#for文で回して、1位から順番に星座と運勢をtextに追記
rank = 0
for s,t in zip(span_list, text_list):
	rank+=1
	seiza = s.find('img').get('alt')
	text = seiza + "は" +str(rank) + "位" + "です。" +"　"+t.text + "、とのことです"
	f2 = open(seiza + '_ft.txt', 'w')
	f2.write(text)
	f2.close()