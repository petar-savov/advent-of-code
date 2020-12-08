with open("input.txt") as f:
    inp = f.readlines()

inp = [x.strip() for x in inp]

moves = [x.split()[0] for x in inp]
vals = [int(x.split()[1]) for x in inp]
visited_ind = set()

acc = 0
i = 0

while i not in visited_ind:
    
    move = moves[i]
    visited_ind.add(i)

    if move == 'acc':
        acc += vals[i]
        i += 1
    elif move == 'nop':
        i += 1
    else:
        i = i + vals[i]

print(acc)