import re

with open("input.txt") as f:
    inp = f.readlines()

def parse(inp: list) -> dict:
    bags = {}
    for line in inp:
        line = line.split("contain")
        parent_bag = line[0].split("bags")[0].strip()
        
        bag_contents = {}
        for bag in line[1].split(','):

            bag = bag.split()
            key = bag[1] + " " + bag[2]

            if re.search('\d',bag[0]):
                count = int(bag[0])
                bag_contents[key] = count
            else:
                bag_contents = None

        bags[parent_bag] = bag_contents
    
    return bags

bags = parse(inp)

parents = []
children = ['shiny gold']

while True:
    new_parents = []
    for bag_name in bags:
        if bags[bag_name] is not None:
            for name in children:
                if name in bags[bag_name].keys():
                    new_parents.append(bag_name)

    if len(new_parents) == 0:
        break
    else:
        parents.extend(new_parents)
        children = new_parents

print(len(set(parents)))
