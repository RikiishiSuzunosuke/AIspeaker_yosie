import datetime
import sc_News
import sc_Weather
import os
import time
def cron():
	print("cron start")
	dt_now = datetime.datetime.now()
	hour = dt_now.hour
	while True:
		dt_now = datetime.datetime.now()
		print("running:"+str(dt_now))
		dt_hour = dt_now.hour

		if hour != dt_hour:
			hour = dt_hour
			sc_News
			os.system('./news_make.sh')
			print("news ok")

			if hour in [2,5,8,11,14,15,17,20]:
				sc_Weather
				os.system('./weather-m.sh')
				print("weather ok")

		time.sleep(300)
cron()