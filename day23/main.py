with open("day23/input.txt") as f:
    inp = [int(x) for x in f.readlines()[0]]


# inp = [int(x) for x in "389125467"]


def to_dict(inp):

    d = {}
    for i, n in enumerate(inp[:-1]):
        d[n] = inp[i + 1]

    d[inp[-1]] = inp[0]

    return d


def step(d, current):

    one = d[current]
    two = d[one]
    three = d[two]

    dest = current - 1
    if dest == 0:
        dest = 9

    while dest in [one, two, three]:
        dest -= 1
        if dest == 0:
            dest = 9

    after_dest = d[dest]
    nxt = d[three]

    d[dest] = one
    d[one] = two
    d[two] = three
    d[three] = after_dest
    d[current] = nxt

    return d, nxt


def tostr(d):
    out = [d[1]]
    while out[-1] != 1:
        ind = d[out[-1]]
        out.append(ind)

    return "".join(str(x) for x in out[:-1])


current = inp[0]
d = to_dict(inp)
for i in range(100):
    d, current = step(d, current)

print("".join(tostr(d)))

