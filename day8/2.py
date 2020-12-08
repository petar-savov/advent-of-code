with open("input.txt") as f:
    inp = f.readlines()

inp = [x.strip() for x in inp]

moves = [x.split()[0] for x in inp]
vals = [int(x.split()[1]) for x in inp]

def flip(move):
    d = {'jmp':'nop', 'nop':'jmp'}
    return d[move]

def run(moves):
    visited_ind = set()
    acc = 0
    i = 0
    
    while i not in visited_ind and i < len(moves):
        
        move = moves[i]
        visited_ind.add(i)

        if move == 'acc':
            acc += vals[i]
            i += 1
        elif move == 'nop':
            i += 1
        else:
            i = i + vals[i]

    if i >= len(moves):
        print(acc)

to_flip = [i for i in visited_ind if moves[i] in ['jmp','nop']]

for i in to_flip:
    new_moves = moves.copy()
    new_moves[i] = flip(new_moves[i])
    run(new_moves)