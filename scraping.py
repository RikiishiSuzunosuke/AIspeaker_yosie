import requests
from bs4 import BeautifulSoup
import sys
import datetime
import re
import random

def yosie_action(func):
	if func == "天気":
		url = "https://weather.yahoo.co.jp/weather/jp/14/"
		target = "今日の天気"

		html = requests.get(url)
		soup = BeautifulSoup(html.text, 'lxml')

		anounce = soup.find('span', class_='time').text
		place = soup.find('h1').text
		weather = soup.find('dd', class_='forecast').p.img.get('alt')
		high = soup.find('em', class_='high').get_text()
		low = soup.find('em', class_='low').get_text()
		precip = soup.find('p', class_='precip').get_text()

		phrase = anounce + " " + place + " " + target + 'は、' + weather + 'です。' + " " + '最高気温は、' + high + "度" + " " + '最低気温は、' + low + '度、' + '降水確率は、' + precip + 'です。'
		#resultに出力テキストを入力
		result = phrase
		
	elif func == "ニュース":
		URL = "https://www.yahoo.co.jp/"
		rest = requests.get(URL)

		soup = BeautifulSoup(rest.text, "html.parser")

		data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

		headline_link_list = [data.attrs["href"] for data in data_list]

		headline_link = headline_link_list[random.randrange(8)]

		summary = requests.get(headline_link)
		summary_soup = BeautifulSoup(summary.text, "html.parser")
		#ニュースタイトル
		text = summary_soup.title.text 
		datail_text = summary_soup.find('p', class_="highLightSearchTarget")
		#要約記事
		text = text + datail_text.text
		text.strip()
		result = text

	elif func == "日時":
		dt_now = datetime.datetime.now()
		
		month = str(dt_now.month)
		day = str(dt_now.day)
		hour = str(dt_now.hour)
		minute = str(dt_now.minute)
		date = '現在の日時は、' + month + '月' + day + '日' + hour + '時' + minute + '分です'
		result = date
	elif func == "占い":
		url = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
		rest = requests.get(url)

		soup = BeautifulSoup(rest.text, 'html.parser')
		today = soup.find(class_='txt').text

		text = today + "の占い" + " "

		span_list = soup.find_all('span')
		del span_list[0]
		text_list = soup.find_all('p', class_='ft01')

		rank = 0
		for s,t in zip(span_list, text_list):
			rank+=1
			seiza = s.find('img').get('alt')
			text = text + str(rank) + "位　" + seiza+"　"+t.text + " "

		text = text + "以上、本日の占いでした。"

		result = text

	elif func == "占い2":
		myseiza = input("あなたの星座を入力してください(ひらがな+座)：")
		seiza_list = ["おとめ座","かに座","やぎ座","おひつじ座","さそり座","おうし座","うお座","いて座","てんびん座","しし座","みずがめ座","ふたご座",]
		for s in seiza_list:
			if myseiza == s:
				stars = s

		url = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
		rest = requests.get(url)

		soup = BeautifulSoup(rest.text, 'html.parser')
		today = soup.find(class_='txt').text
		text = today + "の占い" + " "

		span_list = soup.find_all('span')
		del span_list[0]
		text_list = soup.find_all('p', class_='ft01')

		rank = 0
		for s,t in zip(span_list, text_list):
			rank+=1
			seiza = s.find('img').get('alt')
			if seiza == stars:
				text = text + seiza + "は"+ str(rank) + "位です" + "　"+t.text + " "
				break

		text = text + "以上、"+stars+"の占いでした。" + " "

		result = text

	else:
		print("error")

	f = open('./result.txt', 'w')
	f.write(result)
	f.close()

func = input("関数を指定してください(天気 or ニュース or 日時 or 占い or 占い2)：")
yosie_action(func)