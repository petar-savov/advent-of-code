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

    get_flips = [arr]
    get_flips.extend([np.rot90(arr, k) for k in [1, 2, 3]])
    get_flips.extend([np.flip(arr, axis) for axis in [0, 1]])

    get_flips.append(np.rot90(np.fliplr(arr)))
    get_flips.append(np.rot90(np.flipud(arr)))

    return get_flips


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

prod = 1
for k in matches:
    if matches[k] == 4:
        prod *= k
print(prod)
