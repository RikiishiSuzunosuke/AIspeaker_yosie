import MeCab

<<<<<<< HEAD
tagger = MeCab.Tagger("-Owakati")
=======
tagger = MeCab.Tagger("")
>>>>>>> ad59d242449a05a733c018e8f0705bd7c9f03a90
str = input("input:")
node = tagger.parseToNode(str)

#形態素解析を実行して表示
mecab = tagger.parse(str)
print(mecab)

#名詞　一般の単語のみを抽出して表示
while node:
    if node.surface != "":  # ヘッダとフッタを除外
    	#ここを替えると、好きな品詞を抽出可能
        if (node.feature.split(",")[0] == "名詞") and (node.feature.split(",")[1] == "一般"):
            print(node.feature.split(",")[6])
    node = node.next