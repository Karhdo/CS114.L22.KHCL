n = int(input())
S = 0
for i in range(1,n):
	if n % i == 0 :
		S += i
print (S)
