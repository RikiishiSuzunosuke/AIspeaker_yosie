import MeCab

tagger = MeCab.Tagger('-Owakati')
label_list = []
while True:
	print('天気0：ニュース1：日時2：占い3：')
	label = input('labelを選んでください：')

	if label == 'q':
		break

	if label in ["0","1","2","3"]:
		label_list.append(label)
		train_text = input('ここにテキストを入れてください：')

		f = open('train_data.txt', 'a')
		f.write('__label__'+label + '  ' + tagger.parse(train_text))
		f.close()
	else:
		print("error")

f = open('count.txt', 'r')
count = f.readline()
weather = int(count)
count = f.readline()
news = int(count)
count = f.readline()
date = int(count)
count = f.readline()
fortune = int(count)

weather += label_list.count('0')
news += label_list.count('1')
date += label_list.count('2')
fortune += label_list.count('3')

f.close()

f = open('count.txt','w')
f.write(str(weather)+"\n")
f.write(str(news)+"\n")
f.write(str(date)+"\n")
f.write(str(fortune))

f.close()

print("天気：" + str(weather))
print("ニュース：" + str(news))
print("日時：" + str(date))
print("占い：" + str(fortune))