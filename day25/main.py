with open("day25/input.txt") as f:
    inp = [int(x.strip()) for x in f.readlines()]


def find(n):
    for i in range(50_000_000):
        if pow(7, i, 20201227) == n:
            return i


print(pow(inp[0], find(inp[1]), 20201227))
