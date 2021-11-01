import fasttext as ft

<<<<<<< HEAD
model = ft.train_supervised('train_data.txt', label_prefix = '__label__', neg = 10, dim = 200,  epoch = 40, loss = 'hs')
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')

print(model.predict('時間'))
=======
model = ft.train_supervised('train_data.txt', label_prefix = '__label__', dim = 40, epoch = 5000, loss = 'softmax')
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')

print(model.predict('ニュース'))

#results = model.test('train_data.txt')
#print(results)
#テストデータとlabelの一致の割合が見える
>>>>>>> 53bd248914e05b4feaf724d6f4617870ec09bc0a
