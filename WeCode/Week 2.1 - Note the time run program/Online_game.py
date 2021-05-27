set_1 = set()
array = []
count = 0
while (1):
  k = [int(i) for i in input().split()]
  if k[0] == 0:
    break
  elif k[0] == 1:
    set_1.add(k[1])
  else:
    if k[1] in set_1:
      array.append(1)
    else:
      array.append(0)

for i in range(len(array)):
  print(array[i])
