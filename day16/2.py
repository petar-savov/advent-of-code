import re

with open("day16/input.txt") as f:
    inp = f.read()

constraints, your_ticket, tickets = inp.split("\n\n")

fields = re.findall("(.*):", constraints)
lims = re.findall(" (\d+)-(\d+) or (\d+)-(\d+)", constraints)
lims = [((int(x[0]), int(x[1])), (int(x[2]), int(x[3]))) for x in lims]

tickets = tickets.split("\n")[1:-1]
tickets = [[int(x) for x in line.split(",")] for line in tickets]


def check(n, lim):
    if (n >= lim[0][0] and n <= lim[0][1]) or (n >= lim[1][0] and n <= lim[1][1]):
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

