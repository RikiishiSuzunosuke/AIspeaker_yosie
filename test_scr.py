import requests
from bs4 import BeautifulSoup

load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser") #htmlを解析

#print(soup)  #html全体を表示

#タグを探して要素を取り出す
# print(soup.find("title")) #タグを探して表示
# print(soup.find("h2"))
# print(soup.find("li"))

#タグを探してその文字列を表示
print(soup.find("title").text) #.textを追加
print(soup.find("h2").text)
print(soup.find("li").text)