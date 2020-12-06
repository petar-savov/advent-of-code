with open("input.txt") as f:
    answers = f.read()

answers = answers.split("\n\n")
answers = [x.strip().replace("\n","") for x in answers]

answers = [len(set(x)) for x in answers]
print(sum(answers))