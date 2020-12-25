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
print(sum([cell for cell in changed.values() if cell % 2 == 1]))

