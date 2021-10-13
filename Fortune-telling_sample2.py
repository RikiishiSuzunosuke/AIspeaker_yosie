import requests
from bs4 import BeautifulSoup
import sys
import datetime
import re


myseiza = input("あなたの星座を入力してください(ひらがな+座)：")
seiza_list = ["おとめ座","かに座","やぎ座","おひつじ座","さそり座","おうし座","うお座","いて座","てんびん座","しし座","みずがめ座","ふたご座",]
for s in seiza_list:
	if myseiza == s:
		stars = s

url = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
rest = requests.get(url)

soup = BeautifulSoup(rest.text, 'html.parser')
today = soup.find(class_='txt').text
print(today + "の占い")

span_list = soup.find_all('span')
del span_list[0]
text_list = soup.find_all('p', class_='ft01')

rank = 0
for s,t in zip(span_list, text_list):
	rank+=1
	seiza = s.find('img').get('alt')
	if seiza == stars:
		print(seiza + "は"+ str(rank) + "位です" + "　"+t.text)
		break

print("以上、"+stars+"の占いでした。")


