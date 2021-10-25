print('注意！！ このコードを実行すると、train_data.txtとcount.txtがすべて初期化されます。\n実行する場合は、yを入力してください。')
done = input()
if done == 'y':
	f = open("train_data.txt", 'r+') 
	f.truncate(0)
	f.close()

	f = open('count.txt', 'w')
	for i in range(4):
		f.write('0' + '\n')
	f.close()