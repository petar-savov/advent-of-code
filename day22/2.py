with open("day22/input.txt") as f:
    inp = f.read()

inp = inp.split("\n\n")
p1, p2 = [p.split("\n") for p in inp]
p1 = [int(x) for x in p1[1:]]
p2 = [int(x) for x in p2[1:-1]]


def play(p1, p2):
    prev = set()
    while p1 and p2:
        # need to use entire p1, p2 not just the last elements
        if (tuple(p1), tuple(p2)) in prev:
            return True
        prev.add((tuple(p1), tuple(p2)))

        one = p1.pop(0)
        two = p2.pop(0)

        if len(p1) >= one and len(p2) >= two:
            winner = play((p1[:one]), p2[:two])
            if winner:
                p1.extend([one, two])
            else:
                p2.extend([two, one])

        else:
            if one > two:
                p1.extend([one, two])
            else:
                p2.extend([two, one])
    return len(p1) > 0


play(p1, p2)


s = 0
for i in range(1, len(p1) + 1):
    s += i * p1.pop()
print(s)
