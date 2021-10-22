import fasttext as ft

model = ft.train_supervised('train_data.txt', label_prefix = '__label__', epoch = 1000, loss = 'hs')
model.save_model('model.bin')

print(model.predict('可愛い芳江'))
