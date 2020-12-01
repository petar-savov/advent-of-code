f = open("./input.txt")
numbers = [parse(Int32, i) for i in readlines(f)]
close(f)


function solve(target = 2020) 
    diffs = Dict()

    for num1 in numbers
        for num2 in numbers

            diff = target - num1 - num2
            if num2 in keys(diffs)
                return num1*num2*diff
            end
            diffs[diff] = [num1,num2]
        end
    end
    print(diffs)
end

print(solve(), "\n")


