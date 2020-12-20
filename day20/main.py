import numpy as np
import re


with open("day20/input-test.txt") as f:
    inp = f.read()

inp = inp.split("\n\n")

tiles = {}
for tile in inp:

    ind = int(re.findall("\d+", tile)[0])
    tile = tile.split("\n")[1:]
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
    return [arr[0, :], arr[-1, :], arr[:, 0], arr[:, -1]]

