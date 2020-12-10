with open("input.txt") as f:
    inp = [int(x) for x in f.readlines()]

# part 1
inp = sorted(inp)
inp.insert(0, 0)
inp.append(inp[-1] + 3)

diffs = [inp[i] - inp[i - 1] for i in range(1, len(inp))]
ones = sum([1 for d in diffs if d == 1])
threes = sum([1 for d in diffs if d == 3])
print(ones * threes)

# part2
mem = [1] + [0] * (len(inp) - 1)

for i in range(1, len(inp)):
    s = 0
    for j in range(max(i - 3, 0), i):
        if inp[i] <= inp[j] + 3:
            s += mem[j]
    mem[i] = s

print(mem[-1])
