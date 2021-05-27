n = int(input())
arr = list(map(int, input().strip().split()))[:n]
k, x = map(int, input().split())

less_x = []
greater_x = []
ans = []

for i in range(len(arr)):
  if arr[i] <= x:
    less_x.append(arr[i])
  else:
    greater_x.append(arr[i])

if len(greater_x) == 0:
  for i in range(len(less_x)):
    if i >= len(less_x) - k:
      print(arr[i], end = ' ')
elif len(less_x) == 0:
  for i in range(0, k):
    print(arr[i], end = ' ')
else:
  count = 0 
  l = 0
  r = 0

  while (count < k) and (len(less_x) - 1 - l >= 0) and (r < len(greater_x)):
    if x - less_x[len(less_x) - 1 - l] <= greater_x[r] - x:
      ans.append(less_x[len(less_x) - 1 - l])
      l += 1
    else:
      ans.append(greater_x[r])
      r += 1
    count += 1

  while count < k and len(less_x) - 1 - l >= 0:
    ans.append(less_x[len(less_x) - 1 - l])
    l += 1
    count += 1

  while count < k and len(greater_x) > r:
    ans.append(greater_x[r])
    r += 1
    count += 1

  ans.sort()
  for i in range(len(ans)):
    print(ans[i], end = ' ')
