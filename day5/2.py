with open("input.txt") as f:
    inp = f.readlines()

inp = [line.strip() for line in inp]

def get_id(ticket: str):
    row = ticket[:7].replace("F","0").replace("B","1")
    col = ticket[7:].replace("L","0").replace("R","1")
    row = int(row,2)
    col = int(col,2)

    return row*8 + col

ids = [get_id(x) for x in inp]

all_ids = set(range(min(ids),max(ids)))
print(all_ids.difference(set(ids)))