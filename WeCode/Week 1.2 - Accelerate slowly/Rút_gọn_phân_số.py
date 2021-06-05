n = int(input())
kq_1 = []
kq_2 = []
def UCLN (a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

for i in range(n):
	a, b = map(int, input().split())
	ucln = UCLN(a, b)
	kq_1.append(a // ucln)
	kq_2.append(b // ucln)

for i in range(n):
	if(kq_2[i] != 1):
		print(kq_1[i], end=' ')
		print(kq_2[i])
	else:
		print(kq_1[i])
