import re

with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

start = int(inp[0])
buses = re.findall("\d+", inp[1])
buses = [int(x) for x in buses]

depart = max(buses) + start
for bus in buses:
    dep = start - start % bus + bus
    if dep < depart:
        depart = dep
        bus_id = bus

print((depart - start) * bus_id)

