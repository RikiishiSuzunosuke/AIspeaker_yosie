import fasttext as ft

<<<<<<< HEAD
model = ft.train_supervised('train_data.txt', label_prefix = '__label__', dim = 200, epoch = 1000, loss = 'hs')
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')

print(model.predict('ニュース'))
=======
model = ft.train_supervised('train_data.txt', label_prefix = '__label__', epoch = 100000, loss = 'softmax',lr=0.3,dim=200)
model.save_model('model.bin')

result = model.predict('今日の運勢を教えて。星座占いどう？')
print(result)

>>>>>>> 4ccad75744531f0b32ddc27aaf448476dc39061c
