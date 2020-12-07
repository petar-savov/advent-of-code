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

def score(bag_name: str):
    root = bags[bag_name]
    if root is None:
        return 0
    else:
        return sum([root[key]*score(key) + root[key] for key in root])

print(score('shiny gold'))
