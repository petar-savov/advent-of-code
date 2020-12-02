with open("input.txt") as f:
    inp = f.readlines()

inp = list(map(lambda x: x.split(), inp))

def solve(line):
    
    pos1, pos2 = line[0].split('-')
    pos1, pos2 = int(pos1), int(pos2)

    char = line[1][0]

    return (line[2][pos1-1] == char) ^ (line[2][pos2-1] == char)

if __name__=="__main__":
    print(sum(list(map(solve, inp))))