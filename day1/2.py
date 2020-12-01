with open("input.txt") as f:
    numbers = [int(num) for num in f.readlines()]

def solve(target = 2020):

    diffs = {}

    for num1 in numbers:
        for num2 in numbers:
            diff = target - num1 - num2

            if num2 in diffs:
                return num1*num2*diff

            diffs[diff] = [num1,num2]

if __name__ == "__main__":
    print(solve())


