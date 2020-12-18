import re

with open("day18/input.txt") as f:
    inp = [line.strip() for line in f.readlines()]


def evaluate(expr: str) -> int:
    nums = [int(x) for x in re.findall("\d+", expr)]
    ops = re.findall("[\+\*]", expr)

    res = nums[0]
    for i, n in enumerate(nums[1:]):
        if ops[i] == "+":
            res += n
        else:
            res *= n

    return res


def unnest(instr):

    pattern = re.compile("(\(\d[\+\*\d\s]+\d\))")

    while "(" in instr:
        brackets = re.findall(pattern, instr)
        new = [evaluate(b) for b in brackets]

        for b, n in zip(brackets, new):
            instr = instr.replace(b, str(n))

    return evaluate(instr)


total = 0
for line in inp:
    total += unnest(line)
print(total)
