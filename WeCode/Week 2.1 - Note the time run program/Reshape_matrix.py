m , n = [int(i) for i in input().split()]
r, c = [int(i) for i in input().split()]
if r*c == m*n:
    matrix = []
    count = 0
    for i in range(m):
        q = input()
        matrix += q.split(" ")
        if len(matrix) > c:
            print(*matrix[0:c])
            matrix = matrix[c:]
            count += 1
    for i in range(0, c):
        print(matrix[i], end = ' ')
else:
    for i in range(m):
        q = input()
        print(q)
