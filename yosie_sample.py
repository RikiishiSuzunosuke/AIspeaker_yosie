import requests
from bs4 import BeautifulSoup
import sys
import datetime

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
		print(phrase)
		
	elif func == "ニュース":
		print("news")

	elif func == "日時":
		dt_now = datetime.datetime.now()
		
		month = str(dt_now.month)
		day = str(dt_now.day)
		hour = str(dt_now.hour)
		minute = str(dt_now.minute)
		date = '現在の日時は、' + month + '月' + day + '日' + hour + '時' + minute + '分です'
		print(date)
	else:
		print("error")

func = input("関数を指定してください(天気 or ニュース or 日時)：")
yosie_action(func)






