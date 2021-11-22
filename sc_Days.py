import datetime

def get_days():
	dt_now = datetime.datetime.now()

	month = str(dt_now.month)
	day = str(dt_now.day)
	hour = str(dt_now.hour)
	minute = str(dt_now.minute)
	second = str(dt_now.second)
	weekday = int(dt_now.today().weekday())
	youbi = ["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","日曜日"]

	date = '現在の日時は、' + month + '月' + day + '日' + str(youbi[weekday]) + '　' + hour + '時' + minute + '分' + second + '秒です'

	result = date

	f = open('day.txt', 'w')
	f.write(result)
	f.close()