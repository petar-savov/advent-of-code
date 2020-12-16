import re

with open("day16/input.txt") as f:
    inp = f.read()

constraints, your_ticket, nearby_tickets = inp.split("\n\n")

pattern = re.compile(" (\d+)-(\d+)")
matches = re.findall(pattern, constraints)
lims = [(int(x[0]), int(x[1])) for x in matches]

vals = [int(x) for x in re.findall("(\d+)", nearby_tickets)]

out = 0
for v in vals:
    valid = False
    for mn, mx in lims:
        if v >= mn and v <= mx:
            valid = True
            break
    if not valid:
        out += v

print(out)

