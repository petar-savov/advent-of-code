with open("input.txt") as f:
    answers = f.read()

answers = answers.split("\n\n")
answers = [x.strip() for x in answers]
answers = [x.split("\n") for x in answers]

def all_yes(group: list):
    freq = {}
    for person in group:
        for letter in person:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
    
    group_size = len(group)
    yes = 0
    for f in freq.values():
        if f==group_size:
            yes += 1
    print(freq)
    return yes

print(sum([all_yes(x) for x in answers]))