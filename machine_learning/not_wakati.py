f = open('train_data.txt', 'r')
f2 = open('train_data2.txt', 'w')

for line in f:
	label = line[:12]
	text = line[12:]
	no_space = text.replace(' ', '')
	f2.write(label + no_space)
	
f2.close()
f.close()