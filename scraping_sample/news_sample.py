import requests
from bs4 import BeautifulSoup
import sys
import datetime
import re

#yahooニュースのトップページのURL
URL = "https://www.yahoo.co.jp/"
rest = requests.get(URL)

#ページの読み込み
soup = BeautifulSoup(rest.text, "html.parser")

#見出しとURLの情報を取得
data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for data in data_list:
	print(data.span.string)
	print(data.attrs["href"])