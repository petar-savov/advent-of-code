from itertools import count

with open("input-test.txt") as f:
    inp = [line.strip() for line in f.readlines()][1]
    inp = inp.split(",")

nums = [(i, int(n)) for i, n in enumerate(inp) if n != "x"]

ans = nums[0][1]
step = 1

for i, n in nums:

    while True:
        if (ans + i) % n == 0:
            ans = ans + step
            # ans = next(c for c in count(ans, step) if (c + i) % n == 0)
            break
        step *= n

print(ans)


next(count(100, 10))

