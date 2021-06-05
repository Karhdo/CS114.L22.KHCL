class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def Insert(self, data):
    if self.data:
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
    else:
      self.data = data

  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print(self.data, end = ' ')
    if self.right:
      self.right.PrintTree()

data = int(input())
root = Node(data)
while True:
  x = int(input())
  if x == 0:
    break
  root.Insert(x)

def Count_Leaft(Node): 
  if Node is None: 
      return 0 
  if(Node.left is None and Node.right is None): 
      return 1 
  else: 
      return Count_Leaft(Node.left) + Count_Leaft(Node.right) 

num = Count_Leaft(root)
print(num)
