with open("input.txt") as f:
    inp = [int(x.strip()) for x in f.readlines()]

#part 1
for i,n in enumerate(inp):
    if i>24:
        prev = inp[i-25:i+1]

        pair_sums = set()
        for j in prev:
            for k in prev:
                pair_sums.add(j+k)

        if n not in pair_sums:
            answer = n
            break

print(answer)

#part 2
target = answer

for size in range(2,len(inp)):
    for i,_ in enumerate(inp):
        if i>=size:
            sub = inp[i-size:i]
            csum = sum(sub)
            if csum == target:
                print(min(sub)+max(sub))
                break


