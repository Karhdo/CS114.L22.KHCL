def Fibonacci (n):
	if n < 0:
		return -1;
	elif n == 0 or n == 1:
		return n;
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

x = int(input())
if x < 1 or x > 30:
	print('So ' + str(x) + ' khong nam trong khoang [1,30].')
else:
	so_fibonacci = Fibonacci(x)
	print (str(so_fibonacci))
