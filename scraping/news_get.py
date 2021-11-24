import random

def news_get():
	f = open('news.txt', 'r')
	news_list = f.readlines()
	news = news_list[random.randrange(8)]
	f.close()

	f = open('news_read.txt', 'w')
	f.write(news)
	f.close()