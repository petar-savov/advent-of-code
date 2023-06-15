import numpy as np

with open("day17/input.txt") as f:
    inp = [line.strip() for line in f.readlines()]


def read(square: str):
    square = [[1 if c == "#" else 0 for c in line] for line in square]
    square = np.array(square)
    shape = np.expand_dims(square, 0)
    shape = np.expand_dims(shape, 0)
    return shape


def rules(pt_val, neighbours):
    if pt_val == 1:
        return int(neighbours in [2, 3])

    return int(neighbours == 3)


def count_neighbours(pt, box) -> int:
    a, z, y, x = pt[0], pt[1], pt[2], pt[3]
    amin = max(0, a - 1)
    amax = min(a + 2, box.shape[0])
    zmin = max(0, z - 1)
    zmax = min(z + 2, box.shape[1])
    ymin = max(0, y - 1)
    ymax = min(y + 2, box.shape[2])
    xmin = max(0, x - 1)
    xmax = min(x + 2, box.shape[3])

    nearby_points = box[amin:amax, zmin:zmax, ymin:ymax, xmin:xmax]
    result = nearby_points.sum() - box[pt]

    return result


def transform(input_shape):
    input_shape = np.pad(input_shape, 1)
    output_shape = np.zeros(input_shape.shape)

    for index, val in np.ndenumerate(input_shape):
        neighbours = count_neighbours(pt=index, box=input_shape)
        output_shape[index] = rules(pt_val=val, neighbours=neighbours)

    return output_shape


box = read(inp)
for i in range(6):
    box = transform(box)
print(box.sum())
