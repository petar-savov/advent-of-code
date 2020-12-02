with open("input.txt") as f:
    inp = f.readlines()

inp = list(map(lambda x: x.split(), inp))

def solve(line):
    
    min_count, max_count = line[0].split('-')
    min_count, max_count = int(min_count), int(max_count)

    char = line[1][0]

    return min_count <= line[2].count(char) <= max_count

if __name__=="__main__":
    print(sum(list(map(solve, inp))))