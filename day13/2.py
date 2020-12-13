with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()][1]
    inp = inp.split(',')

diffs = []
nums = []
for i, n in enumerate(inp):
    if n != 'x':
        n = int(n)
        diffs.append(n - i)
        nums.append(n)

prod = 1
for num in nums:
    prod *= num

ans = 0
for d, num in zip(diffs,nums):
    
    b = prod // num
    ans += d * b * pow(b, num-2, num)
    ans %= prod

print(ans)