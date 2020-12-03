import numpy as np

with open("input.txt") as f:
    inp = f.readlines()


grid = [[1 if c=="#" else 0 for c in line.strip()] for line in inp]
grid = np.array(grid)

trees, row, col = 0, 0

while(row < grid.shape[0]):
    row = row + 1
    col = col + 3

    if col >= grid.shape[1]:
        grid = np.concatenate([grid,grid],axis=1)
    trees += grid[row,col]



print(trees)
