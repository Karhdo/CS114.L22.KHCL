from sys import stdin
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def Insert(self, data):
    if data < self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.Insert(data)
    elif data > self.data:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.Insert(data)
  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print(self.data, end = ' ')
    if self.right:
      self.right.PrintTree()

def height_tree(Node):
	if Node is None:
		return 0
	else:
		left = height_tree(Node.left)
		right = height_tree(Node.right)

	if left > right:
		return left + 1
	else:
		return right + 1

list_ans = []
while True:
  k = [int(i) for i in stdin.readline().split()]
  if k[0] == 0:
    try:
      position = list_ans.index(k[1])
      list_ans.pop(position)
      list_ans.insert(0,k[1])
    except:
      list_ans.insert(0,k[1])
  elif k[0] == 1:
    if k[1] not in list_ans:
      list_ans.append(k[1])
  elif k[0] == 2:
    try:
      position_a=list_ans.index(k[1])
      if k[2] in list_ans:
        position_b = list_ans.index(k[2])
        if position_a < position_b:
          list_ans.pop(position_b)
          list_ans.insert(position_a+1, k[2])
      else:
        list_ans.insert(position_a+1, k[2])
    except:
      list_ans.insert(0, k[2])
  else:
    root = Node(list_ans[0])
    break

for i in range(1, len(list_ans)):
  root.Insert(list_ans[i])

print(height_tree(root))
