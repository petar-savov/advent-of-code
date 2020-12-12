import numpy as np

with open("input.txt") as f:
    inp = [x.strip() for x in f.readlines()]


def read(board: str) -> np.array:

    board = [[0 if c == "L" else -1 for c in line] for line in board]
    board = np.array(board)

    return board

def transform(input_board: np.array, fn, thr) -> np.array:

    output_board = np.zeros(input_board.shape)

    for i, row in enumerate(input_board):
        for j, _ in enumerate(row):
            neighbours = fn(pt=(i, j), board=input_board)
            output_board[i, j] = rules(pt_val=input_board[i, j], neighbours=neighbours, thr=thr)

    return output_board


def rules(pt_val, neighbours, thr):
    if pt_val == 1 and neighbours >= thr:
        return 0
    elif pt_val == 0 and neighbours == 0:
        return 1
    return pt_val


# part 1

def count_neighbours(pt, board) -> int:
    x, y = pt[0], pt[1]
    xmin = max(0, x - 1)
    xmax = min(x + 2, board.shape[0])
    ymin = max(0, y - 1)
    ymax = min(y + 2, board.shape[1])

    nearby_points = board[xmin:xmax, ymin:ymax]
    result = nearby_points == 1
    result = result.sum()
    if board[pt] == 1:
        result -= 1
    return result


board = read(inp)
step = transform(board, count_neighbours, thr=4)
while not np.all(board == step):
    board = np.copy(step)
    step = transform(board, count_neighbours, thr=4)

print(np.sum(board == 1))

# part 2

def count_visible(pt, board) -> int:
    
    nrows, ncols = board.shape
    counted = set()
    #for dr, dc in [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,0),(-1,1),(-1,-1)]:
    for dr, dc in [(0,1),(1,0)]:
        row, col = pt[0],pt[1]
        while True:
            newr = row + dr
            newc = col + dc
            
            if newr > nrows - 1 or newr < 0:
                print("got here")
                break
            if newc > ncols - 1 or newc < 0:
                print("HELOOO")
                break
            
            if board[newr,newc] == 1:
                print("------------")
                counted.add((newr,newc))
                break
    
    return len(counted)


test = np.array([[1,0,0],[1,1,1]])
count_visible((0,0),test)


board = read(inp)
step = transform(board, fn = count_visible, thr=5)
while not np.all(board == step):
    board = np.copy(step)
    step = transform(board, fn = count_visible, thr=5)

print(np.sum(board == 1))