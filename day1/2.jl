f = open("./input.txt")
numbers = [parse(Int32, i) for i in readlines(f)]
close(f)


function solve(target = 2020) 

    for num1 in numbers
        for num2 in numbers
            diff = target - num1 - num2
            if diff in numbers
                return num1*num2*diff
            end
        end
    end
    print(diffs)
end

print(solve(), "\n")


