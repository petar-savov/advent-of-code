import re
from itertools import product

with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

instr = {}

for line in inp:
    if re.match("mask", line):
        mask = line.split(" = ")[1]
        instr[mask] = {}
    else:
        mem = int(re.findall("mem\[(.*)\]", line)[0])
        val = int(line.split(" = ")[1])
        instr[mask][mem] = val


def unmask(addr: int, mask: str) -> list:

    addrbin = bin(addr)[2:]
    addrbin = (len(mask) - len(addrbin)) * "0" + addrbin

    masked = []
    slot_ids = []
    for i, c in enumerate(mask):
        if c == "0":
            masked.append(addrbin[i])
        elif c == "X":
            slot_ids.append(i)
            masked.append(c)
        else:
            masked.append(c)

    addresses = []
    perms = product("10", repeat=len(slot_ids))
    for p in perms:
        new = masked.copy()
        for i, c in enumerate(p):
            new[slot_ids[i]] = c
        addresses.append("".join(new))

    if len(slot_ids) == 0:
        addresses.append("".join(masked))

    return list(set(addresses))


result = {}

for mask in instr:
    for addr in instr[mask]:
        new_addresses = unmask(addr, mask)
        for r in new_addresses:
            result[r] = instr[mask][addr]

print(sum(result.values()))
