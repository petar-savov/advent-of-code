with open("input.txt") as f:
    inp = [x.strip() for x in f.readlines()]

x, y = 0, 0
wx, wy = 10, 1

for instr in inp:
    action = instr[0]
    arg = int(instr[1:])

    if action == "F":
        x += wx * arg
        y += wy * arg
    elif action == "N":
        wy += arg
    elif action == "S":
        wy -= arg
    elif action == "W":
        wx -= arg
    elif action == "E":
        wx += arg
    elif action == "L":
        # rotate once for 90 deg in angle
        while arg:
            wx, wy = -wy, wx
            arg -= 90
    elif action == "R":
        while arg:
            wx, wy = wy, -wx
            arg -= 90
print(abs(x) + abs(y))

