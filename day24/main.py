from collections import defaultdict
import re

with open("day24/input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

steps = {
    "e": (1, 0),
    "se": (0, -1),
    "sw": (-1, -1),
    "w": (-1, 0),
    "nw": (0, 1),
    "ne": (1, 1),
}

changed = defaultdict(int)

for line in inp:
    moves = re.findall("e|se|sw|w|nw|ne", line)
    x, y = 0, 0
    for move in moves:
        step = steps[move]
        x += step[0]
        y += step[1]

    changed[(x, y)] += 1
print(sum([cell for cell in changed.values() if cell % 2]))


def flip(board):

    black = defaultdict(int)
    for ind in board:
        if board[ind] % 2 == 0:
            continue
        for d in steps.values():
            cell = (ind[0] + d[0], ind[1] + d[1])
            black[cell] += 1

    new = {}
    for ind, cnt in board.items():
        if cnt % 2:
            if black.get(ind, 0) in (1, 2):
                new[ind] = 1

    for ind, cnt in black.items():
        if cnt == 2 and board.get(ind, 0) % 2 == 0:
            new[ind] = 1
    return new


board = changed
for i in range(100):
    board = flip(board)

print(sum([cell for cell in board.values() if cell % 2]))
