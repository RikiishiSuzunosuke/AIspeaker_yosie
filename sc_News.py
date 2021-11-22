import requests
from bs4 import BeautifulSoup
import sys
import re
import random

URL = "https://www.yahoo.co.jp/"

rest = requests.get(URL)
soup = BeautifulSoup(rest.text, "html.parser")

#"news.yahoo.co.jp/pickup"を含むコードをすべてリストに格納
data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
#URLのみを再度抽出してリストに格納
headline_link_list = [data.attrs["href"] for data in data_list]

f = open('news.txt', 'w')

for i in range(8):
	headline_link = headline_link_list[i]

	#取得したURLのページを解析
	summary = requests.get(headline_link)
	summary_soup = BeautifulSoup(summary.text, "html.parser")
	#ニュースタイトルを取得、textに代入
	text = summary_soup.title.text + " "
	#class名がhighLightSearchTargetのpタグから要約記事を取得
	datail_text = summary_soup.find('p', class_="highLightSearchTarget")
	#要約記事をtextに追記
	text = text + datail_text.text

	#OpenJtalkが改行に対応していないため、strip()で改行を削除
	text.strip()
	#resultに出力テキストを入力
	result = text
	f.write(result+"\n")
f.close()
