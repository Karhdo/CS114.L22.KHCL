q = int(input())
for i in range(q):
	n ,k = map(int, input().split())
	a = list(map(int, input().strip().split()))[:n]
	print(a.count(k))
