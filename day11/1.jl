f = open("input.txt")
inp = readlines(f)
close(f)

remap = Dict([('L', 0), ('#', 1), ('.', -1)])

grid = [[remap[x] for x in line] for line in inp]
grid = transpose(reduce(hcat,grid))

function neighbours(ind, grid)

    y, x = ind[1], ind[2]

    xmin = max(x-1, 1)
    xmax = min(size(grid)[2], x+1)

    ymin = max(y-1, 1)
    ymax = min(size(grid)[1], y+1)

    nearby_sum = sum(grid[ymin:ymax,xmin:xmax].==1) - grid[y,x]

    return nearby_sum
end

function run(grid, fn, threshold)
    new_grid = zeros(Int8,size(grid))
    for col in 1:size(grid)[2]
        for row in 1:size(grid)[1]
            if grid[row,col] != -1
                nbs = fn((row,col),grid)
                if grid[row,col] == 0 && nbs == 0
                    new_grid[row,col] = 1
                elseif grid[row,col] == 1 && nbs >= threshold
                    new_grid[row,col] = 0
                else
                    new_grid[row,col] = grid[row,col]
                end
            else
                new_grid[row,col] = -1
            end
        end
    end
    return new_grid
end

next = run(grid, neighbours, 4)
while next!=grid
    grid = next
    next = run(grid, neighbours, 4)
end
print(sum(next.==1))
