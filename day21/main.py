import re


with open("day21/input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

allergens = {}

for line in inp:
    cont = re.findall("\(contains (.*)\)", line)
    cont = cont[0].split(", ")
    code = line.split(" (contains")[0].split()
    for ingr in cont:
        if ingr not in allergens:
            allergens[ingr] = [code]
        else:
            allergens[ingr].append(code)

possible = {}

for k in allergens:
    possible[k] = set(allergens[k][0]).intersection(*allergens[k][1:])

while True:
    for k in possible:
        if len(possible[k]) == 1:
            for j in possible:
                if k != j:
                    possible[j].discard(list(possible[k])[0])
    if all([len(possible[k]) == 1 for k in possible]):
        break


enc_allerg = [list(s)[0] for s in possible.values()]

app = 0

for line in inp:
    for code in line.split(" (contains")[0].split():
        if code not in enc_allerg:
            app += 1

print(app)

# part 2

canonical = sorted(possible.items())
canonical = [list(canonical[i][1])[0] for i, _ in enumerate(canonical)]
print(",".join(canonical))
