with open("input.txt") as f:
    inp = [int(x.strip()) for x in f.readlines()]

# part 1
for i, n in enumerate(inp):
    if i > 24:
        prev = inp[i - 25 : i + 1]

        pair_sums = set()
        for j in prev:
            for k in prev:
                pair_sums.add(j + k)

        if n not in pair_sums:
            answer = n
            break

print(answer)

# part 2
target = answer

start, end = 0, 1
csum = inp[0] + inp[1]

while csum != target:
    while csum < target:
        end += 1
        csum += inp[end]
        
    while csum > target:
        csum -= inp[start]
        start += 1

print(min(inp[start:end]) + max(inp[start:end]))

