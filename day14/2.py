import re
from itertools import product
from collections import OrderedDict
import copy

with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

# parse input
instr = OrderedDict()
for line in inp:
    if re.match("mask", line):
        mask = line.split(" = ")[1]
        instr[mask] = OrderedDict()
    else:
        mem = int(re.findall("mem\[(.*)\]", line)[0])
        val = int(line.split(" = ")[1])
        instr[mask][mem] = val


def mask_address(adr: int, mask: str) -> list:

    addrbin = bin(adr)[2:]
    addrbin = (len(mask) - len(addrbin)) * "0" + addrbin

    masked = []
    slot_ids = []
    for i, c in enumerate(mask):
        if c == "1":
            masked.append(addrbin[i])
        elif c == "X":
            slot_ids.append(i)
            masked.append(c)
        else:
            masked.append(c)

    addresses = []
    perms = product("10", repeat=len(slot_ids))
    for p in perms:
        new = copy.deepcopy(masked)
        for i, c in enumerate(p):
            new[slot_ids[i]] = c
        addresses.append("".join(new))

    if len(slot_ids) == 0:
        addresses.append("".join(masked))

    return list(set(addresses))


mem = OrderedDict()

for mask in instr:
    for addr in instr[mask]:
        res = mask_address(addr, mask)
        for r in res:
            mem[r] = instr[mask][addr]

print(sum(mem.values()))
