with open("day15/input.txt") as f:
    inp = [int(x) for x in f.readlines()[0].split(",")]

track = dict((n, i) for i, n in enumerate(inp))


target = 30_000_000  # change to 2020 for part 1
for i in range(len(inp) - 1, target - 1):
    n = inp[-1]
    if n not in track:
        track[n] = i
        inp.append(0)
    else:
        inp.append(len(inp) - 1 - track[n])
        track[n] = i

print(inp[-1])
