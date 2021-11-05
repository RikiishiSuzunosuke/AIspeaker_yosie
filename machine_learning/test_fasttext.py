import fasttext as ft


model = ft.train_supervised('train_data.txt', label_prefix = '__label__',  dim = 200,  epoch = 1000, loss = 'hs')
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')

print(model.predict('天気を教えて'))

#results = model.test('test_data_label_2.txt')
#print(results)
#テストデータとlabelの一致の割合が見える

