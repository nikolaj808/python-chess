test = {}

for i in range(8):
	for j in range(8):
		test['{}{}'.format(chr(97+i), j+1)] = ''

print(test)