label=[]
f = open("train_data.txt", 'r')
for line in f:
	label.append(line[9])
f.close()

f = open('count.txt','w')
for i in range(4):
	f.write(str(label.count(str(i))) + '\n')
f.close()