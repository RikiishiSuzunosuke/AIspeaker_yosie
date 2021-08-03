import requests
from bs4 import BeautifulSoup
def yosie_action(func):
	if func == "天気":
		print("wether")
	elif func == "ニュース":
		print("news")
	else:
		print("error")

func = input("関数を指定してください(天気 or ニュース)：")
yosie_action(func)






