import datetime
import sc_News
import sc_Weather
import os
def cron():
	hour = 99
	while True:
		#現在時刻を取得
		dt_now = datetime.datetime.now()
		#hourを取得
		dt_hour = dt_now.hour

		#hourが更新された場合
		if hour != dt_hour:
			hour = dt_hour
			#一時間毎にニュースを取得して更新する
			sc_News　#ニュースをスクレイピング
			os.system('./news_make.sh')　#音声ファイル作成
			print("news ok")

			#天気予報は2時、5時、8時、11時、14時、15時、17時、20時に発表
			if hour in [2,5,8,11,14,15,17,20]:
				sc_Weather　#天気予報をスクレイピング
				os.system('./weather-m.sh')
				print("weather ok")
cron()