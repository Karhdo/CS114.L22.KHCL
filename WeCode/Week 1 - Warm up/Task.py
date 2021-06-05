n = int(input())
k = int(input())
p = int(input())
q = int(input())

i = (p-1) * 2 + (q-1)

vt_before = i - k
vt_after = i + k

if vt_before >= 0:
    print(vt_before//2+1, vt_before % 2 + 1)
elif vt_after <= n-1:
    print(vt_after//2+1, vt_after % 2 + 1)
else:
    print(-1)
