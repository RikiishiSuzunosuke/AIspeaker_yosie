import requests
from bs4 import BeautifulSoup
import sys
import datetime
import re
import random

args = sys.argv

def yosie_action(func):
	result = "" #result変数を初期化

	if func == "0": #天気
		#Yahoo天気予報のURLを取得
		URL = "https://weather.yahoo.co.jp/weather/jp/14/"
		target = "今日の天気"

		#ページを解析
		rest = requests.get(URL)
		soup = BeautifulSoup(rest.text, 'lxml')

		#データを抽出
		anounce = soup.find('span', class_='time').text #class名がtimeのspanタグのtextデータを抽出している
		place = soup.find('h1').text
		weather = soup.find('dd', class_='forecast').p.img.get('alt')
		high = soup.find('em', class_='high').get_text()
		low = soup.find('em', class_='low').get_text()
		precip = soup.find('p', class_='precip').get_text()

		#抽出したデータを結合
		phrase = anounce + " " + place + " " + target + 'は、' + weather + 'です。' + " " + '最高気温は、' + high + "度" + " " + '最低気温は、' + low + '度、' + '降水確率は、' + precip + 'です。'
		#resultに出力テキストを入力
		result = phrase
		
	elif func == "1": #ニュース
		#YahooトップページのURLを取得
		URL = "https://www.yahoo.co.jp/"

		rest = requests.get(URL)
		soup = BeautifulSoup(rest.text, "html.parser")

		#"news.yahoo.co.jp/pickup"を含むコードをすべてリストに格納
		data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
		#URLのみを再度抽出してリストに格納
		headline_link_list = [data.attrs["href"] for data in data_list]
		#ランダムで1つのニュースURLを取得
		headline_link = headline_link_list[random.randrange(8)]

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

	elif func == "2": #日時
		#現在の日時を取得
		dt_now = datetime.datetime.now()
		
		#要素ごとに変数を用意
		month = str(dt_now.month)
		day = str(dt_now.day)
		hour = str(dt_now.hour)
		minute = str(dt_now.minute)
		second = str(dt_now.second)
		#要素を文章に取り入れる
		date = '現在の日時は、' + month + '月' + day + '日' + hour + '時' + minute + '分' + second + '秒です'
		#resultに出力テキストを入力
		result = date

	elif func == "3": #全体占い
		#Yahoo星座占いのURLを取得
		url = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
		rest = requests.get(url)

		soup = BeautifulSoup(rest.text, 'html.parser')
		#記載されている日付を取得
		today = soup.find(class_='txt').text
		#日付を入れてタイトル作成、textに代入
		text = today + "の占いです" + " "

		#spanタグで書かれている星座の名前をすべて取得
		span_list = soup.find_all('span')
		#一番先頭は不要なspanタグの要素なので削除
		del span_list[0]
		#class名がft01のpタグから、各星座の運勢を抽出する
		text_list = soup.find_all('p', class_='ft01')

		#for文で回して、1位から順番に星座と運勢をtextに追記
		rank = 0
		for s,t in zip(span_list, text_list):
			rank+=1
			seiza = s.find('img').get('alt')
			text = text + str(rank) + "位　" + seiza+"　"+t.text + " "
		#締めのあいさつを追記
		text = text + "以上、本日の占いでした。"

		result = text

	elif func == "4": #個別占い
		myseiza = input("あなたの星座を入力してください(ひらがな+座)：")
		seiza_list = ["おとめ座","かに座","やぎ座","おひつじ座","さそり座","おうし座","うお座","いて座","てんびん座","しし座","みずがめ座","ふたご座",]
		#入力されたデータとseiza_listを見比べて、starsに代入
		#入力されたデータがどの星座にも該当しない場合、resultにerrorを代入しておく
		for s in seiza_list:
			if myseiza == s:
				stars = s
				break
			else:
				stars = "error"

		#resultがerrorじゃないのであればスクレイピングを実行
		if not stars == "error":
			url = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
			rest = requests.get(url)

			soup = BeautifulSoup(rest.text, 'html.parser')
			today = soup.find(class_='txt').text
			text = today + "の" + stars +"の運勢は"

			span_list = soup.find_all('span')
			del span_list[0]
			text_list = soup.find_all('p', class_='ft01')

			rank = 0
			for s,t in zip(span_list, text_list):
				rank+=1
				seiza = s.find('img').get('alt')
				#入力した星座に合致するデータのみ、textに追記し、終了する。
				if seiza == stars:
					text = text + str(rank) + "位で、" + t.text + "、とのことです。"
					break

			text = text + "以上、"+stars+"の占いでした。" + " "
			result = text
		else:
			result = "指定された星座が見つかりませんでした"

	elif func == "99":
		retult = ""

	else:
		result = "入力エラーです"

	#テキストファイルにresultを上書き保存する
	f = open('./result.txt', 'w')
	f.write(result)
	f.close()

#func = input("機能を数字で指定(0.天気, 1.ニュース, 2.日時, 3.全体占い, 4.個別占い)：")
#yosie_action(func)

#yosie_action(str(args[1]))