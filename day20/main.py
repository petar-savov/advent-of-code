import numpy as np
import re


with open("day20/input.txt") as f:
    inp = f.read()

inp = inp.split("\n\n")[:-1]

tiles = {}
for tile in inp:
    tile = tile.split("\n")
    ind = int(re.findall("\d+", tile[0])[0])
    tile = tile[1:]
    tile = [[1 if c == "#" else 0 for c in line] for line in tile]
    tile = np.array(tile)
    tiles[ind] = tile


def get_flips(arr: np.array) -> list:

    flips = [arr]
    flips.extend([np.rot90(arr, k) for k in [1, 2, 3]])
    flips.extend([np.flip(arr, axis) for axis in [0, 1]])

    flips.append(np.rot90(np.fliplr(arr)))
    flips.append(np.rot90(np.flipud(arr)))

    return flips


def get_edges(arr: np.array) -> list:
    return [
        arr[0, :],
        arr[-1, :],
        arr[:, 0],
        arr[:, -1],
        arr[0, :][::-1],
        arr[-1, :][::-1],
        arr[:, 0][::-1],
        arr[:, -1][::-1],
    ]


edges = {}
for k in tiles:
    edges[k] = get_edges(tiles[k])

matches = {}
for k in edges:
    current = edges[k]
    s = 0
    for edge in current:
        for j in edges:
            if k != j:
                s += sum([np.array_equal(edge, other) for other in edges[j]])
    matches[k] = s

corners = []
prod = 1
for k in matches:
    if matches[k] == 4:
        corners.append(k)
        prod *= k
print(prod)

# part 2
# corners = [2749, 2713, 1487, 1063]

tl_index = corners[0]
topleft = tiles[tl_index]
tl_edges = get_edges(topleft)

for edge in tl_edges:
    s = 0
    for j in edges:
        if j != 2749:
            s += sum([np.array_equal(edge, other) for other in edges[j]])
    if s == 0:
        print(edge)

img = np.rot90(topleft, k=2)
tiles.pop(2749)

while True:
    for tile in tiles:
        flips = get_flips(tiles[tile])
        br = False
        for flip in flips:
            if np.array_equal(img[:, -1], flip[:, 0]):
                img = np.hstack((img, flip))
                br = True
                to_pop = tile
                break
        if br:
            break
    tiles.pop(to_pop)
    if to_pop in corners[1:]:
        tr_index = to_pop
        break

# img is now the first row
expand = np.empty((110, 120))
img = np.vstack((img, expand))

