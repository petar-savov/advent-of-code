import Base: -,/

struct D <: Number
    val::Int64
end

-(x::D, y::D) = D(x.val * y.val) 
/(x::D, y::D) = D(x.val + y.val) 

f = open("day18/input.txt")
inp = readlines(f)
close(f)

inp = [replace(line, "*" => "-") for line in inp]
inp = [replace(line, "+" => "/") for line in inp]

function conv(line)
    num_inds = findall(r"\d", line)
    nums = Set([line[index] for index in num_inds])
    for n in nums
        line = replace(line, n => string("D(", n, ")"))
    end
    return line
end

s = 0
for line in inp
    sym = Meta.parse(conv(line))
    s += eval(sym).val
end
print(s)

