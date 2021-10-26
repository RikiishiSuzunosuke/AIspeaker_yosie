import fasttext as ft

model = ft.train_supervised('train_data.txt', label_prefix = '__label__', epoch = 100000, loss = 'softmax',lr=0.3,dim=200)
model.save_model('model.bin')

result = model.predict('今日の運勢を教えて。星座占いどう？')
print(result)

