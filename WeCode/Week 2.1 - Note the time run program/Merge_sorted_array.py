from sys import stdin
list_ans = []
while True:
  k = [int(i) for i in stdin.readline().split()]
  if k[0] == 0:
    list_ans.insert(0, k[1])
  elif k[0] == 1:
    list_ans.append(k[1])
  elif k[0] == 2:
    try:
      index = list_ans.index(k[1]) + 1
      list_ans.insert(index, k[2])
    except:
      list_ans.insert(0, k[2])
  elif k[0] == 3:
    try:
      index = list_ans.index(k[1])
      list_ans.pop(index)
    except:
      pass
  elif k[0] == 4:
    list_ans[:] = (i for i in list_ans if i != k[1])
  elif k[0] == 5:
    if len(list_ans) != 0:
      list_ans.pop(0)
  elif k[0] == 6:
    break

if len(list_ans)!=0:
    print(*list_ans)
else:
    print("blank")
