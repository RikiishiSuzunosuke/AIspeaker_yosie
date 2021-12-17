def news_get():
	f = open('news.txt', 'r')
	news_list = f.readlines()

	for i in range(8):
		news = news_list[i]
		f2 = open('news_' + str(i) + '.txt', 'w')
		f2.write(news)
		f2.close()
	f.close()

news_get()