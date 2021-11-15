def text_change(text):
	text = text.replace('[s]', '')
	text = text.replace('[/s]', '')
	text_split = []
	text_split = text.split(' ')

	output = ""
	for i in range(len(text_split)):
		output = text_split[i] + output
	return output
text = "[/s]かな 曇り は 今日[s]"
print(text_change(text))