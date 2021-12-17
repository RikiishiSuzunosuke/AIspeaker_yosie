import fasttext as ft
import MeCab

mecab = MeCab.Tagger("-Owakati")

inp = mecab.parse(input())

print(inp)

model = ft.train_supervised('train_data.txt', label_prefix = '__label__',  dim = 200,  epoch = 53000, loss = 'hs')

#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')
#model.binを生成

print(model.predict(inp))

results = model.test('train_data.txt')
print(results)
#テストデータとlabelの一致の割合が見える
