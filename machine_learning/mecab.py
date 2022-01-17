import MeCab

tagger = MeCab.Tagger("-Owakati")
while True:
	str = input("input:")
	node = tagger.parseToNode(str)

	#形態素解析を実行して表示
	# mecab = tagger.parse(str)
	# print(mecab)

	present = ""
	#名詞　一般の単語のみを抽出して表示
	while node:
	    if node.surface != "":  # ヘッダとフッタを除外
	    	#ここを替えると、好きな品詞を抽出可能
	        if (node.feature.split(",")[0] == "名詞") and (node.feature.split(",")[1] == "一般"):
	            present = present + node.feature.split(",")[6] + " "
	        elif (node.feature.split(",")[0] == "名詞") and (node.feature.split(",")[1] == "接尾"):
	            present = present + node.feature.split(",")[6] + " "
	        elif "時間" in str:
	        	present = present + "時間 "
	        	str = str.replace("時間","")
	    node = node.next
	print(present)
