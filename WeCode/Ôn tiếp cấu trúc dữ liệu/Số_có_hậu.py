n , m = map(int, input().split())
count = len(str(n))
kq = ((m - n) // (10 ** count)) + 1
print(kq)
