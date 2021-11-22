import fasttext as ft

def lm():
		model = ft.load_model('model.bin')
		result = model.predict("今日の天気は晴れかな")
		return result[0]
print(lm())