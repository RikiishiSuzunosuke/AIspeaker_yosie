import fasttext as ft


model = ft.train_supervised('train_data.txt', label_prefix = '__label__',  dim = 200,  epoch = 3000, loss = 'hs')
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')

print(model.predict('ニュース'))

results = model.test('test_data_label_1.txt')
print(results)
#テストデータとlabelの一致の割合が見える

