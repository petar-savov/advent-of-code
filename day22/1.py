from collections import deque

with open("day22/input.txt") as f:
    inp = f.read()

inp = inp.split("\n\n")
p1, p2 = [p.split("\n") for p in inp]
p1 = [int(x) for x in p1[1:]]
p2 = [int(x) for x in p2[1:-1]]

p1, p2 = deque(p1), deque(p2)

while p1 and p2:

    one = p1.popleft()
    two = p2.popleft()

    if one > two:
        p1.append(one)
        p1.append(two)
    else:
        p2.append(two)
        p2.append(one)

s = 0
for i in range(1, len(p1) + 1):
    s += i * p1.pop()
print(s)
