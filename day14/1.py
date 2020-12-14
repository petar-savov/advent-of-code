import re

with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

# parse input
instr = {}
for line in inp:
    if re.match("mask", line):
        mask = line.split(" = ")[1]
        instr[mask] = {}
    else:
        mem = int(re.findall("mem\[(.*)\]", line)[0])
        val = int(line.split(" = ")[1])
        instr[mask][mem] = val


def flip(n: int, mask: str) -> int:
    nbin = bin(n)[2:]
    nbin = (len(mask) - len(nbin)) * "0" + nbin
    out = []
    for i, c in enumerate(mask):
        if c != "X":
            out.append(c)
        else:
            out.append(nbin[i])

    return int("".join(out), 2)


mem = {}
for mask in instr:
    for addr in instr[mask]:
        mem[addr] = flip(instr[mask][addr], mask)

print(sum(mem.values()))
