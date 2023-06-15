import numpy as np
import re


with open("day20/input.txt") as f:
    inp = f.read()

inp = inp.split("\n\n")[:-1]

tiles = {}
for tile in inp:
    tile = tile.split("\n")
    ind = int(re.findall(r"\d+", tile[0])[0])
    tile = tile[1:]
    tile = [[1 if c == "#" else 0 for c in line] for line in tile]
    tile = np.array(tile)
    tiles[ind] = tile


def get_flips(arr) -> list:
    flips = [arr]
    flips.extend([np.rot90(arr, k) for k in [1, 2, 3]])
    flips.extend([np.flip(arr, axis) for axis in [0, 1]])

    flips.append(np.rot90(np.fliplr(arr)))
    flips.append(np.rot90(np.flipud(arr)))

    return flips


def get_edges(arr) -> list:
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

tl_index = corners[0]
topleft = tiles[tl_index]
tl_edges = get_edges(topleft)

for edge in tl_edges:
    s = 0
    for j in edges:
        if j != tl_index:
            s += sum([np.array_equal(edge, other) for other in edges[j]])
    if s == 0:
        print(edge)

img = np.rot90(topleft, k=2)
tiles.pop(tl_index)

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
expand = np.zeros((110, 120)) - 1
img = np.vstack((img, expand))

hmin, hmax = 0, 10
vmin, vmax = 10, 20

while True:
    if hmin == 0:
        for tile in tiles:
            flips = get_flips(tiles[tile])
            br = False
            for flip in flips:
                if np.array_equal(img[vmin - 1, hmin:hmax], flip[0, :]):
                    img[vmin:vmax, hmin:hmax] = flip
                    br = True
                    to_pop = tile
                    break
            if br:
                break
    else:
        for tile in tiles:
            flips = get_flips(tiles[tile])
            br = False
            for flip in flips:
                if np.array_equal(img[vmin - 1, hmin:hmax], flip[0, :]) and np.array_equal(
                    img[vmin:vmax, hmin - 1], flip[:, 0]
                ):
                    img[vmin:vmax, hmin:hmax] = flip
                    br = True
                    to_pop = tile
                    break
            if br:
                break

    tiles.pop(to_pop)

    if (vmax, hmax) == img.shape:
        break
    if hmax == img.shape[1]:
        hmin, hmax = 0, 10
        vmin += 10
        vmax += 10

    else:
        hmin += 10
        hmax += 10

with open("day20/monster.txt") as f:
    monster = f.read()

monster = monster.split("\n")
monster = [[1 if c == "#" else 0 for c in line] for line in monster]
monster = np.array(monster)

# delete tiles borders
to_drop = [(i, i + 1) for i in range(9, 119, 10)]
img = np.delete(img, to_drop, 0)
img = np.delete(img, to_drop, 1)
img = np.delete(img, (0, -1), 0)  # outside borders
img = np.delete(img, (0, -1), 1)


def check_monster(monster, arr):
    if monster.shape != arr.shape:
        raise Exception("Shapes don't match.")
    ones = list(zip(np.where(monster == 1)[0], np.where(monster == 1)[1]))

    return all([arr[pair] == 1 for pair in ones])


img_ones = np.sum(img)
imgs = get_flips(img)

for img in imgs:
    score = img_ones
    m_ones = np.sum(monster)
    inds = []
    ylen, xlen = monster.shape
    ymin, ymax = 0, ylen
    xmin, xmax = 0, xlen

    while True:
        temp = img[ymin:ymax, xmin:xmax]
        if check_monster(monster, temp):
            score -= m_ones

        if (ymax, xmax) == img.shape:
            break
        if xmax == img.shape[1]:
            xmin, xmax = 0, xlen
            ymin += 1
            ymax += 1

        else:
            xmin += 1
            xmax += 1

    if score < img_ones:
        print(score)
