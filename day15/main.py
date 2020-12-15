with open("day15/input.txt") as f:
    inp = [int(x) for x in f.readlines()[0].split(",")]

steps = 30_000_000

last, track = inp[-1], {n: i + 1 for i, n in enumerate(inp)}
for i in range(len(inp), steps):
    track[last], last = i, i - track.get(last, i)

print(last)
