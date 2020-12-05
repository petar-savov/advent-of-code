with open("input.txt") as f:
    inp = f.readlines()

inp = [line.strip() for line in inp]

def score(ticket: str):
    row = ticket[:7].replace("F","0").replace("B","1")
    col = ticket[7:].replace("L","0").replace("R","1")
    row = int(row,2)
    col = int(col,2)

    return row*8 + col

max_score = 0

for ticket in inp:
    max_score = max(max_score, score(ticket))

print(max_score)