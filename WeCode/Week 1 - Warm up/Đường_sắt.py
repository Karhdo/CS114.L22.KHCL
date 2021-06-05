k, t = map(int, input().split())
if (t//k) % 2 == 0:
	kq = t % k
else:
	kq = k - (t % k)
print(kq)
