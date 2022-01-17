import fast_text as ft

def predict(text):
	model = ft.load_model('Jonny_model.bin')
	result = model.predict(text)
	re = str(result[0])
	index11 = re[11]
	return index11

