import numpy as np

with open("day17/input.txt") as f:
    inp = [line.strip() for line in f.readlines()]


def read(square: str) -> np.array:

    square = [[1 if c == "#" else 0 for c in line] for line in square]
    square = np.array(square)
    shape = np.expand_dims(square, 0)

    return shape


def rules(pt_val, neighbours):

    if pt_val == 1:
        return int(neighbours in [2, 3])

    return int(neighbours == 3)


def count_neighbours(pt, box) -> int:

    z, y, x = pt[0], pt[1], pt[2]
    zmin = max(0, z - 1)
    zmax = min(z + 2, box.shape[0])
    ymin = max(0, y - 1)
    ymax = min(y + 2, box.shape[1])
    xmin = max(0, x - 1)
    xmax = min(x + 2, box.shape[2])

    nearby_points = box[zmin:zmax, ymin:ymax, xmin:xmax]
    result = nearby_points.sum() - box[pt]

    return result


def transform(input_shape: np.array) -> np.array:

    # pad every dimension of input with zeros here
    input_shape = np.pad(input_shape, 1)
    output_shape = np.zeros(input_shape.shape)
    dims = [d for d in input_shape.shape]
    for z in range(dims[0]):
        for y in range(dims[1]):
            for x in range(dims[2]):
                neighbours = count_neighbours(pt=(z, y, x), box=input_shape)
                output_shape[z, y, x] = rules(
                    pt_val=input_shape[z, y, x], neighbours=neighbours
                )

    return output_shape


box = transform(read(inp))
for i in range(5):
    box = transform(box)
print(box.sum())
