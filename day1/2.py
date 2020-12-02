with open("input.txt") as f:
    numbers = [int(num) for num in f.readlines()]

def solve(target = 2020):

    for num1 in numbers:
        for num2 in numbers:
            diff = target - num1 - num2

            if diff in numbers:
                return num1*num2*diff

if __name__ == "__main__":
    print(solve())


