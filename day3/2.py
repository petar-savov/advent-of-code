import numpy as np

with open("input.txt") as f:
    inp = f.readlines()

grid = [[1 if c=="#" else 0 for c in line.strip()] for line in inp]
grid = np.array(grid)

slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]
tree_list = []

for down, right in slopes:

    trees, row, col = 0, 0, 0
    while(row < grid.shape[0] -1):
        row = row + down
        col = col + right

        if col >= grid.shape[1]:
            grid = np.concatenate([grid,grid],axis=1)
        trees += grid[row,col]

    tree_list.append(trees)

print(np.prod(tree_list))

