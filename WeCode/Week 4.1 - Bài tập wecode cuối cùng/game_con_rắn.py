from sys import *


head_directions = {
    'v': (1, 0),
    '^': (-1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

directions = {
    'v': {'L': '>', 'R': '<'},
    '^': {'L': '<', 'R': '>'},
    '<': {'L': 'v', 'R': '^'},
    '>': {'L': '^', 'R': 'v'}
}


def routeSnake(matrix):
    snake = []

    def DFS(x, y):
        for step, d in head_directions.items():
            newX, newY = x + d[0], y + d[1]
            if newX in range(len(matrix)) and newY in range(len(matrix[0])):
                if (newX, newY) not in snake:
                    if matrix[newX][newY] == '*':
                        return (newX, newY)
        return None

    for i, row in enumerate(matrix):
        for head in head_directions:
            if head in row:
                snake.append((i, row.index(head)))

    while True:
        pos = DFS(snake[-1][0], snake[-1][1])
        if pos is None:
            break
        snake.append(pos)
    return snake


def moveSnake(board, snake):
    head = board[snake[0][0]][snake[0][1]]
    x = snake[0][0] + head_directions[head][0]
    y = snake[0][1] + head_directions[head][1]

    if x not in range(len(board)):
        return None
    if y not in range(len(board[0])):
        return None
    if (x, y) in snake[:-1]:
        return None

    newSnake = [(x, y)]
    for i in range(len(snake) - 1):
        newSnake.append(snake[i])
    return newSnake


def control(board, snake, steps):
    for step in steps:
        if step == 'L' or step == 'R':
            x, y = snake[0][0], snake[0][1]
            board[x][y] = directions[board[x][y]][step]
        else:
            tmp = moveSnake(board, snake)

            if tmp is None:
                for i in snake:
                    board[i[0]][i[1]] = 'X'
                return board

            if (tmp[0] == snake[-1]) and (len(tmp) == 2):
                board[tmp[0][0]][tmp[0][1]] = board[snake[0][0]][snake[0][1]]
                board[tmp[1][0]][tmp[1][1]] = '*'
                snake = tmp
            else:
                for a, b in zip(snake, tmp):
                    board[b[0]][b[1]] = board[a[0]][a[1]]
                board[snake[-1][0]][snake[-1][1]] = '.'
                snake = tmp

    return board


matrix = []
m, n, c = list([int(i) for i in input().split()])
for i in range(m):
    tmp = [i for i in input()]
    matrix.append(tmp)
snake = routeSnake(matrix)
steps = input()
board = control(matrix, snake, steps)
for i in range(m):
    for j in range(n):
        print(*matrix[i][j], end="")
    print()
