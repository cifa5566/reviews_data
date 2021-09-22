data = []
count = 0

with open('reviews.txt', 'r') as f:

	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('Total', count,'data')

sum_len = 0

for dat in data:
	length = len(dat)
	sum_len = length + sum_len #也可以直接寫成 sum_len += len(dat)

print('average length =', sum_len / count, 'data')

wc = {} # word_count
for d in data:
	words = d.strip().split() #split() 預設為切空白鍵 且可以切割連續空白
	for word in words:
		if word in wc:
			wc[word] +=1
		if word not in wc:
			wc[word] = 1
	
	

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc)) 
	
while True:
	x=input('請輸入你想找得字: ')
	if x == 'q':
		break
	if word in wc:
		print(wc[x])
	if word not in wc:
		print("查無此字")

print("感謝使用")


new = []

for d in data:
	if len(d) < 100:
		new.append(d)
print('There are',len(new),'data shorter than 100')


# list comprehension

good = [d for d in data if 'good' in data]

print(len(good))
