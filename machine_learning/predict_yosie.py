import fasttext as ft
import MeCab

def predict(text):
	tagger = MeCab.Tagger("-Owakati")
	node = tagger.parseToNode(text)

	present = ""
	while node:
	    if node.surface != "":  # ヘッダとフッタを除外
	    	#ここを替えると、好きな品詞を抽出可能
	        if (node.feature.split(",")[0] == "名詞") and (node.feature.split(",")[1] == "一般"):
	            present = present + node.feature.split(",")[6] + " "
	        elif (node.feature.split(",")[0] == "名詞") and (node.feature.split(",")[1] == "接尾"):
	            present = present + node.feature.split(",")[6] + " "
	        elif "時間" in text:
	        	present = present + "時間 "
	        	text = text.replace("時間","")
	    node = node.next
	print(present)

	model = ft.load_model('Jonny_model.bin')
	result = model.predict(present)
	re = str(result[0])
	index11 = re[11]
	print(index11)
	return index11