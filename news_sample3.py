import requests
from bs4 import BeautifulSoup
import sys
import datetime
import re
import random

#yahooニュースのトップページのURL
URL = "https://www.yahoo.co.jp/"
rest = requests.get(URL)

#ページの読み込み
soup = BeautifulSoup(rest.text, "html.parser")

#見出しとURLの情報を取得
data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

#見出しのURLをループで取得、リストに格納
headline_link_list = [data.attrs["href"] for data in data_list]

#yahooニュースの構造　top→要約→本文

#独自改変　すべてでなく、ランダムでニュースを取得（８パターン）
headline_link = headline_link_list[random.randrange(8)]

#見出しURLから、要約ページの内容取得, 解析できるようにする
summary = requests.get(headline_link)
summary_soup = BeautifulSoup(summary.text, "html.parser")
print(summary_soup.title.text)

datail_text = summary_soup.find('p', class_="highLightSearchTarget")
#本文を出力
#hasattrで指定のオブジェクトが特定の属性を持っているか確認
#detail_text.textがNoneだった場合は何も表示しない
print(datail_text.text)