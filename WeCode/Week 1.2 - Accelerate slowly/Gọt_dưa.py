n = int(input())

def check(n):
	if(n == 2):
		return 0
	if (n % 2 == 0):
		return 1
	else:
		return 0

kt = check(n)
if(kt == 1):
	print('YES')
else:
	print('NO')
