import re

with open("day16/input.txt") as f:
    inp = f.read()

constraints, your_ticket, tickets = inp.split("\n\n")

fields = re.findall("(.*):", constraints)
lims = re.findall(" (\d+)-(\d+) or (\d+)-(\d+)", constraints)
lims = [((int(x[0]), int(x[1])), (int(x[2]), int(x[3]))) for x in lims]
ref = dict(zip(fields, lims))

tickets = tickets.split("\n")[1:-1]
tickets = [[int(x) for x in line.split(",")] for line in tickets]


def check(n, lim):
    if (lim[0][0] <= n <= lim[0][1]) or (lim[1][0] <= n <= lim[1][1]):
        return True
    return False


# drop invalid tickets
to_keep = []
for ticket in tickets:
    valid = True
    for num in ticket:
        if any(check(num, lim) for lim in lims):
            pass
        else:
            valid = False
    if valid:
        to_keep.append(ticket)

poss = {}
for i in range(len(to_keep[0])):
    for name in ref:
        if all(check(t[i], ref[name]) for t in to_keep):
            if name not in poss:
                poss[name] = set([i])
            else:
                poss[name].add(i)


res = {}
while len(res) < len(poss):
    for key in poss:
        if len(poss[key]) == 1:
            ind = poss[key].pop()
            res[key] = ind
            for k2 in poss:
                poss[k2].discard(ind)

your_ticket = [int(x) for x in your_ticket.split("\n")[1].split(",")]

prod = 1
for key in res:
    if key.split()[0] == "departure":
        prod *= your_ticket[res[key]]

print(prod)
