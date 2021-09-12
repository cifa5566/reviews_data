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
