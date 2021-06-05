r , c = map(int, input().split())

matrix = []
length = []

for i in range(r):
	a = [int(i) for i in input().split()]
	matrix.append(a)

for i in range(c):
	max = 0
	for j in range(r):
		if len(str(matrix[j][i])) > max:
			max = len(str(matrix[j][i]))
	length.append(max)

for i in range(r):
	for j in range(c):
		space = length[j] - len(str(matrix[i][j]))
		print(space * ' ' + str(matrix[i][j]), end = ' ')
	print()
