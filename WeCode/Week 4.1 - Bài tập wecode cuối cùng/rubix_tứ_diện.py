from sys import stdin

def swap(a, b):
  temp = a
  a = b
  b = temp
  return a,b

list_colors = [i for i in stdin.readline().split()]
answer = [i for i in stdin.readline().split()]

Pyraminx = []
temp_arr = []

for i in range(4):
  temp_arr = [list_colors[i] for j in range(9)]
  Pyraminx.append(temp_arr)

for i in range(len(answer)-1, -1, -1):
    if answer[i] == "U'":
        Pyraminx[0][0], Pyraminx[3][8] = swap(Pyraminx[0][0], Pyraminx[3][8])
        Pyraminx[0][0], Pyraminx[2][4] = swap(Pyraminx[0][0], Pyraminx[2][4])
    elif answer[i] == "B'":
        Pyraminx[1][0], Pyraminx[2][8] = swap(Pyraminx[1][0], Pyraminx[2][8])
        Pyraminx[1][0], Pyraminx[3][4] = swap(Pyraminx[1][0], Pyraminx[3][4])
    elif answer[i] == "L'":
        Pyraminx[2][0], Pyraminx[1][8] = swap(Pyraminx[2][0], Pyraminx[1][8])
        Pyraminx[2][0], Pyraminx[0][4] = swap(Pyraminx[2][0], Pyraminx[0][4])
    elif answer[i] == "R'":
        Pyraminx[3][0], Pyraminx[0][8] = swap(Pyraminx[3][0], Pyraminx[0][8])
        Pyraminx[3][0], Pyraminx[1][4] = swap(Pyraminx[3][0], Pyraminx[1][4])
    elif answer[i] == "U":
        Pyraminx[0][0], Pyraminx[2][4] = swap(Pyraminx[0][0], Pyraminx[2][4])
        Pyraminx[0][0], Pyraminx[3][8] = swap(Pyraminx[0][0], Pyraminx[3][8])
    elif answer[i] == "B":
        Pyraminx[1][0], Pyraminx[3][4] = swap(Pyraminx[1][0], Pyraminx[3][4])
        Pyraminx[1][0], Pyraminx[2][8] = swap(Pyraminx[1][0], Pyraminx[2][8])
    elif answer[i] == "L":
        Pyraminx[2][0], Pyraminx[0][4] = swap(Pyraminx[2][0], Pyraminx[0][4])
        Pyraminx[2][0], Pyraminx[1][8] = swap(Pyraminx[2][0], Pyraminx[1][8])
    elif answer[i] == "R":
        Pyraminx[3][0], Pyraminx[1][4] = swap(Pyraminx[3][0], Pyraminx[1][4])
        Pyraminx[3][0], Pyraminx[0][8] = swap(Pyraminx[3][0], Pyraminx[0][8])
    elif answer[i] == "u'":
    	
        Pyraminx[0][0], Pyraminx[3][8] = swap(Pyraminx[0][0], Pyraminx[3][8])
        Pyraminx[0][1], Pyraminx[3][3] = swap(Pyraminx[0][1], Pyraminx[3][3])
        Pyraminx[0][2], Pyraminx[3][7] = swap(Pyraminx[0][2], Pyraminx[3][7])
        Pyraminx[0][3], Pyraminx[3][6] = swap(Pyraminx[0][3], Pyraminx[3][6])

        Pyraminx[0][0], Pyraminx[2][4] = swap(Pyraminx[0][0], Pyraminx[2][4])
        Pyraminx[0][1], Pyraminx[2][6] = swap(Pyraminx[0][1], Pyraminx[2][6])
        Pyraminx[0][2], Pyraminx[2][5] = swap(Pyraminx[0][2], Pyraminx[2][5])
        Pyraminx[0][3], Pyraminx[2][1] = swap(Pyraminx[0][3], Pyraminx[2][1])
    elif answer[i] == "b'":

        Pyraminx[1][0], Pyraminx[2][8] = swap(Pyraminx[1][0], Pyraminx[2][8])
        Pyraminx[1][1], Pyraminx[2][3] = swap(Pyraminx[1][1], Pyraminx[2][3])
        Pyraminx[1][2], Pyraminx[2][7] = swap(Pyraminx[1][2], Pyraminx[2][7])
        Pyraminx[1][3], Pyraminx[2][6] = swap(Pyraminx[1][3], Pyraminx[2][6])

        Pyraminx[1][0], Pyraminx[3][4] = swap(Pyraminx[1][0], Pyraminx[3][4])
        Pyraminx[1][1], Pyraminx[3][6] = swap(Pyraminx[1][1], Pyraminx[3][6])
        Pyraminx[1][2], Pyraminx[3][5] = swap(Pyraminx[1][2], Pyraminx[3][5])
        Pyraminx[1][3], Pyraminx[3][1] = swap(Pyraminx[1][3], Pyraminx[3][1])
    elif answer[i] == "l'":

        Pyraminx[2][0], Pyraminx[1][8] = swap(Pyraminx[2][0], Pyraminx[1][8])
        Pyraminx[2][1], Pyraminx[1][3] = swap(Pyraminx[2][1], Pyraminx[1][3])
        Pyraminx[2][2], Pyraminx[1][7] = swap(Pyraminx[2][2], Pyraminx[1][7])
        Pyraminx[2][3], Pyraminx[1][6] = swap(Pyraminx[2][3], Pyraminx[1][6])

        Pyraminx[2][0], Pyraminx[0][4] = swap(Pyraminx[2][0], Pyraminx[0][4])
        Pyraminx[2][1], Pyraminx[0][6] = swap(Pyraminx[2][1], Pyraminx[0][6])
        Pyraminx[2][2], Pyraminx[0][5] = swap(Pyraminx[2][2], Pyraminx[0][5])
        Pyraminx[2][3], Pyraminx[0][1] = swap(Pyraminx[2][3], Pyraminx[0][1])
    elif answer[i] == "r'":

        Pyraminx[3][0], Pyraminx[0][8] = swap(Pyraminx[3][0], Pyraminx[0][8])
        Pyraminx[3][1], Pyraminx[0][3] = swap(Pyraminx[3][1], Pyraminx[0][3])
        Pyraminx[3][2], Pyraminx[0][7] = swap(Pyraminx[3][2], Pyraminx[0][7])
        Pyraminx[3][3], Pyraminx[0][6] = swap(Pyraminx[3][3], Pyraminx[0][6])

        Pyraminx[3][0], Pyraminx[1][4] = swap(Pyraminx[3][0], Pyraminx[1][4])
        Pyraminx[3][1], Pyraminx[1][6] = swap(Pyraminx[3][1], Pyraminx[1][6])
        Pyraminx[3][2], Pyraminx[1][5] = swap(Pyraminx[3][2], Pyraminx[1][5])
        Pyraminx[3][3], Pyraminx[1][1] = swap(Pyraminx[3][3], Pyraminx[1][1])
    elif answer[i] == "u":

        Pyraminx[0][0], Pyraminx[2][4] = swap(Pyraminx[0][0], Pyraminx[2][4])
        Pyraminx[0][1], Pyraminx[2][6] = swap(Pyraminx[0][1], Pyraminx[2][6])
        Pyraminx[0][2], Pyraminx[2][5] = swap(Pyraminx[0][2], Pyraminx[2][5])
        Pyraminx[0][3], Pyraminx[2][1] = swap(Pyraminx[0][3], Pyraminx[2][1])

        Pyraminx[0][0], Pyraminx[3][8] = swap(Pyraminx[0][0], Pyraminx[3][8])
        Pyraminx[0][1], Pyraminx[3][3] = swap(Pyraminx[0][1], Pyraminx[3][3])
        Pyraminx[0][2], Pyraminx[3][7] = swap(Pyraminx[0][2], Pyraminx[3][7])
        Pyraminx[0][3], Pyraminx[3][6] = swap(Pyraminx[0][3], Pyraminx[3][6])
    elif answer[i] == "b":

        Pyraminx[1][0], Pyraminx[3][4] = swap(Pyraminx[1][0], Pyraminx[3][4])
        Pyraminx[1][1], Pyraminx[3][6] = swap(Pyraminx[1][1], Pyraminx[3][6])
        Pyraminx[1][2], Pyraminx[3][5] = swap(Pyraminx[1][2], Pyraminx[3][5])
        Pyraminx[1][3], Pyraminx[3][1] = swap(Pyraminx[1][3], Pyraminx[3][1])

        Pyraminx[1][0], Pyraminx[2][8] = swap(Pyraminx[1][0], Pyraminx[2][8])
        Pyraminx[1][1], Pyraminx[2][3] = swap(Pyraminx[1][1], Pyraminx[2][3])
        Pyraminx[1][2], Pyraminx[2][7] = swap(Pyraminx[1][2], Pyraminx[2][7])
        Pyraminx[1][3], Pyraminx[2][6] = swap(Pyraminx[1][3], Pyraminx[2][6])
    elif answer[i] == "l":

        Pyraminx[2][0], Pyraminx[0][4] = swap(Pyraminx[2][0], Pyraminx[0][4])
        Pyraminx[2][1], Pyraminx[0][6] = swap(Pyraminx[2][1], Pyraminx[0][6])
        Pyraminx[2][2], Pyraminx[0][5] = swap(Pyraminx[2][2], Pyraminx[0][5])
        Pyraminx[2][3], Pyraminx[0][1] = swap(Pyraminx[2][3], Pyraminx[0][1])

        Pyraminx[2][0], Pyraminx[1][8] = swap(Pyraminx[2][0], Pyraminx[1][8])
        Pyraminx[2][1], Pyraminx[1][3] = swap(Pyraminx[2][1], Pyraminx[1][3])
        Pyraminx[2][2], Pyraminx[1][7] = swap(Pyraminx[2][2], Pyraminx[1][7])
        Pyraminx[2][3], Pyraminx[1][6] = swap(Pyraminx[2][3], Pyraminx[1][6])
    elif answer[i] == "r":

        Pyraminx[3][0], Pyraminx[1][4] = swap(Pyraminx[3][0], Pyraminx[1][4])
        Pyraminx[3][1], Pyraminx[1][6] = swap(Pyraminx[3][1], Pyraminx[1][6])
        Pyraminx[3][2], Pyraminx[1][5] = swap(Pyraminx[3][2], Pyraminx[1][5])
        Pyraminx[3][3], Pyraminx[1][1] = swap(Pyraminx[3][3], Pyraminx[1][1])

        Pyraminx[3][0], Pyraminx[0][8] = swap(Pyraminx[3][0], Pyraminx[0][8])
        Pyraminx[3][1], Pyraminx[0][3] = swap(Pyraminx[3][1], Pyraminx[0][3])
        Pyraminx[3][2], Pyraminx[0][7] = swap(Pyraminx[3][2], Pyraminx[0][7])
        Pyraminx[3][3], Pyraminx[0][6] = swap(Pyraminx[3][3], Pyraminx[0][6])
if input() == ".":
    for i in range(4):
        print(' '.join(map(str, Pyraminx[i])))
