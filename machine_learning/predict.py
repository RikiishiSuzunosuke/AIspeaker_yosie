import fasttext as ft

def predict(text):

	if '今日の' in text:
		text = text.replace('今日の', '')
	elif '今の' in text:
		text = text.replace('今の', '')
	elif '今' in text:
		text = text.replace('今', '')
	if 'を教えて':
		text = text.replace('を教えて', '')
	elif 'か教えて':
		text = text.replace('か教えて', '')
		
	model = ft.load_model('model.bin')
	result = model.predict(text)
	re = str(result[0])
	index11 = re[11]
	return index11

