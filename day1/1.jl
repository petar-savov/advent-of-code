f = open("./day1/input.txt")
numbers = [parse(Int32, i) for i in readlines(f)]
close(f)



function solve(target = 2020) 
    diffs = Dict()

    for num in numbers

        diff = target - num

        if num in keys(diffs)
            return num*diff
        end
        diffs[diff] = num
    end
            
end

print(solve(), "\n")


