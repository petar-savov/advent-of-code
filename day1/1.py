with open("input.txt") as f:
    numbers = [int(num) for num in f.readlines()]

def solve(target = 2020):

    diffs = {}
    for num in numbers:
        diff = target - num

        if num in diffs:
            return num*diff

        diffs[diff] = num

if __name__ == "__main__":
    print(solve())

