import fast_text as ft

def lm():
		model = ft.load_model('model.bin')
		result = model.predict("今日の天気は晴れかな")
		return result
print(lm())
