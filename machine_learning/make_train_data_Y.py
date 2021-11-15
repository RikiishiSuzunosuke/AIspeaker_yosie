import MeCab

tagger = MeCab.Tagger('-Owakati')
count_label = []
#各ラベルのカウントを初期化&リスト生成 (のちの処理を書きやすくするため)
weather, news, date, fortune = 0, 0, 0, 0
func_list = [weather, news, date, fortune]
#トレーニングデータを書き込むファイルをopen
f = open('train_data_Y.txt', 'a')
while True:
	try:
		print('天気0：ニュース1：日時2：占い3：終了999')
		#inputにintキャストしてるため、文字が入った場合エラーを吐くのでtry_exceptで処理
		label = input('label：')
		if 0<= int(label) and int(label)<=3 :
			#labelが0~4の時に正常処理
			count_label.append(label)
			text = input('text：')
			f.write('__label__' + str(label) +  '  ' + tagger.parse(text))
		elif int(label) == 999:
			#labelに'999'が入力されたら処理を終了
			break
		else:
			print('error')
	except ValueError:
		print('error')
#ファイルをclose
f.close()