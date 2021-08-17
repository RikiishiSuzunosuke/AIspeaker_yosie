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
		print(phrase)
		
	elif func == "ニュース":
		URL = "https://www.yahoo.co.jp/"
		rest = requests.get(URL)

		soup = BeautifulSoup(rest.text, "html.parser")

		data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

		headline_link_list = [data.attrs["href"] for data in data_list]

		headline_link = headline_link_list[random.randrange(8)]

		summary = requests.get(headline_link)
		summary_soup = BeautifulSoup(summary.text, "html.parser")

		summary_soup_a = summary_soup.select("a:contains('続きを読む')")[0]

		news_body_link = summary_soup_a.attrs["href"]

		news_body = requests.get(news_body_link)
		news_soup = BeautifulSoup(news_body.text, "html.parser")
		print(news_soup.title.text)

		datail_text = news_soup.find(class_=re.compile("Direct"))

		print(datail_text.text if hasattr(datail_text, "text") else '', end="\n\n\n")

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






