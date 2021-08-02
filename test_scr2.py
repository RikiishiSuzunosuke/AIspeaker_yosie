import requests
from bs4 import BeautifulSoup

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

#print(soup.find_all("li")) これだとリストで返ってきちゃう
for element in soup.find_all("li"):
	pass
	#print(element.text)

#id, classを絞り込む
chap1 = soup.find(id="chap1") #idがchap1の範囲の要素を表示
#print(chap1)
for element in chap1.find_all("li"):
	print(element.text)

#ページのソースを表示でタグやid, class名を確認、抽出