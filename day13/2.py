import re

with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()][1]
    inp = inp.split(',')


diff = 1
nums = []
diffs = []
for i in inp:
    if i =='x':
        diff+=1
    else:
        diffs.append(diff)
        diff = 1
        nums.append(int(i))

diffs[0] = 0

def check(x):
    return all([(x+sum(diffs[:i+1]))%nums[i] == 0 for i, _ in enumerate(nums)])

mult = 1
while True:
    attempt = mult*nums[0]
    if check(attempt):
        print(f"The answer is {attempt}.")
        break
    mult += 1