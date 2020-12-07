import re
from collections import defaultdict
with open("input.txt") as f:
    inp = f.readlines()

def parse(inp):
    contained_in = defaultdict(set)
    for line in inp:
        line = line.split("contain")
        parent_bag = line[0].split("bags")[0].strip()
        
        for bag in line[1].split(','):
            bag = bag.split()
            colour = bag[1] + " " + bag[2]
            if re.search('\d',bag[0]):
                if colour in contained_in:
                    contained_in[colour].append(parent_bag)
                else:
                    contained_in[colour] = [parent_bag]

    return contained_in

bags = parse(inp)

shiny_gold_parents = set()
def get_all_parents(color):
    for i in bags[color]:
        shiny_gold_parents.add(i)
        get_all_parents(i)

get_all_parents('shiny gold')
print(len(shiny_gold_parents))

