with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]


class Ship:
    def __init__(self):
        self.orientation = "E"
        self.hdim = 0
        self.vdim = 0

    def mdistance(self):
        return abs(self.hdim) + abs(self.vdim)

    def move(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == "N":
            self.vdim += distance
        elif direction == "S":
            self.vdim -= distance
        elif direction == "E":
            self.hdim += distance
        elif direction == "W":
            self.hdim -= distance
        else:
            self.move(instruction=self.orientation + instruction[1:])

    def rotate(self, instruction):
        direction = instruction
        if self.orientation == "E":
            dirs = {
                "L90": "N",
                "R270": "N",
                "L180": "W",
                "R180": "W",
                "L270": "S",
                "R90": "S",
            }
            self.orientation = dirs[direction]
            return
        if self.orientation == "N":
            dirs = {
                "L90": "W",
                "R270": "W",
                "L180": "S",
                "R180": "S",
                "L270": "E",
                "R90": "E",
            }
            self.orientation = dirs[direction]
            return
        if self.orientation == "W":
            dirs = {
                "L90": "S",
                "R270": "S",
                "L180": "E",
                "R180": "E",
                "L270": "N",
                "R90": "N",
            }
            self.orientation = dirs[direction]
            return
        if self.orientation == "S":
            dirs = {
                "L90": "E",
                "R270": "E",
                "L180": "N",
                "R180": "N",
                "L270": "W",
                "R90": "W",
            }
            self.orientation = dirs[direction]
            return


my_ship = Ship()

for i in inp:
    if i[0] in ["R", "L"]:
        my_ship.rotate(i)
    else:
        my_ship.move(i)

print(my_ship.mdistance())
