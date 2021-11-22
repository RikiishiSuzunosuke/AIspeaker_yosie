import fasttext as ft


<<<<<<< HEAD
model = ft.train_supervised('train_data2.txt', label_prefix = '__label__',  dim = 100,  epoch = 153000, loss = 'hs')
=======
model = ft.train_supervised('train_data2.txt', label_prefix = '__label__',  dim = 200,  epoch = 133000, loss = 'hs')
>>>>>>> 0e841794b7d81059114d8bf91a1470361101b0f1
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')
#model.binを生成

<<<<<<< HEAD
print(model.predict('今日の占いの結果'))
=======
print(model.predict('今日の星座占いの順位は'))
>>>>>>> 0e841794b7d81059114d8bf91a1470361101b0f1

results = model.test('train_data.txt')
print(results)
#テストデータとlabelの一致の割合が見える

