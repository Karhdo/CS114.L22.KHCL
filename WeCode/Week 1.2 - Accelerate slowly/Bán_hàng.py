q = int(input())
kq = []

for i in range(q):

	n = int(input())
	a = list(map(int, input().strip().split()))[:n]

	tong = sum(a, 0)
	if(tong % n == 0):
		gia_tb = tong // n
	else:
		gia_tb = (tong // n) + 1

	kq.append(gia_tb)

for i in range(len(kq)):
	print (kq[i])
