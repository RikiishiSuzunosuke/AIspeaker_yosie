import fasttext as ft

model = ft.train_supervised('Jonny.txt', label_prefix = '__label__',  dim = 200,  epoch = 10000, loss = 'hs')

#model.binを生成
model.save_model('Jonny_model.bin')

print(model.predict('射手 座'))
#results = model.test('train_data.txt')
#print(results)
#テストデータとlabelの一致の割合が見える

