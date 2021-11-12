import fasttext as ft


model = ft.train_supervised('train_data2.txt', label_prefix = '__label__',  dim = 200,  epoch = 100000, loss = 'softmax')
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')
#model.binを生成

print(model.predict('今日の一番のニュース'))

results = model.test('train_data.txt')
print(results)
#テストデータとlabelの一致の割合が見える

