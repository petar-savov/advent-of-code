with open("input.txt") as f:
    answers = f.read()

answers = answers.split("\n\n")
answers = [x.strip() for x in answers]
answers = [x.split("\n") for x in answers]

def all_yes(group: list):
    first = set(group[0])
    return len(first.intersection(*group[1:]))

print(sum([all_yes(x) for x in answers]))