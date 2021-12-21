import datetime
def cron():
	minute = 99
	while True:
		dt_now = datetime.datetime.now()
		dt_minute = dt_now.minute
		if minute != dt_minute:
			minute = dt_minute
			print(str(minute) + "分")
cron()
