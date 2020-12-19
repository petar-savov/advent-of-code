import re

with open("day19/input.txt") as f:
    inp = f.read()

rules, messages = inp.split("\n\n")
rules = rules.split("\n")
messages = messages.split("\n")[:-1]

rules = dict([line.split(": ") for line in rules])


def parse(ind):

    rule = rules.get(ind, ind)

    if rule == '"a"':
        return "a"
    elif rule == '"b"':
        return "b"
    elif "|" not in rule:
        nums = rule.split(" ")
        return "".join([parse(n) for n in nums])
    else:
        h1, h2 = rule.split(" | ")
        return "(" + parse(h1) + "|" + parse(h2) + ")"


pattern = re.compile("^" + parse("0") + "$")

count = 0
for m in messages:
    if re.match(pattern, m):
        count += 1
print(count)
