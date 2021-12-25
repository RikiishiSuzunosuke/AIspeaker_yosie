f = open('train_J_nw.txt', 'r')
f2 = open('train_J_delete_word.txt', 'w')
for line in f:
	if '今日の' in line:
		line = line.replace('今日の', '')
	elif '今の' in line:
		line = line.replace('今の', '')
	elif '今' in line:
		line = line.replace('今', '')
	if 'を教えて':
		line = line.replace('を教えて', '')
	elif 'か教えて':
		line = line.replace('か教えて', '')

	f2.write(line)
f.close()
f2.close()
