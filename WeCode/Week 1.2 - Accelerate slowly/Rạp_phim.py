n, m, a = map(int, input().split())

if(n % a != 0):
	x1 = (n // a) + 1
else:
	x1 = n // a

if(m % a != 0):
	x2 = (m // a) + 1
else:
	x2 = m // a

print(x1 * x2)
