import re

with open("input.txt") as f:
    inp = f.readlines()

inp = [line.strip() for line in inp]

def get_id(bpass: str):
    bpass = re.sub("F|L", "0", bpass)
    bpass = re.sub("B|R", "1", bpass)
    return int(bpass,2)

ids = [get_id(x) for x in inp]
print(max(ids))