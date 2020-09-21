import sys

inn = sys.stdin
board =  4 * [[]]
for i in range(4):
    board[i] = [int(i) for i in next(inn).split(" ")]
action = int(next(inn))
if action == 0:
    # left
    for r in range(4):
        for c in range(3):
            for d in range(1, 4):
                print(c, d)
                if board[r][c] == 0:
                    board[r][c], board[r][d]=board[r][d], board[r][c]
    print(board)
elif action == 1:
    # up
    pass
elif action == 2:
    # right
    pass
else:
    # down
    pass
