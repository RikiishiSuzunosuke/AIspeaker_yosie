f = open("train_data.txt", 'r')
label = []
for line in f:
	label.append(line[9])
f.close()

f = open('count.txt','w')
for i in range(4):
	f.write(str(label[i]) + '\n')
f.close()