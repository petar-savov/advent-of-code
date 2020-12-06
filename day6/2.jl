f = open("day6/input.txt") 
answers = read(f, String)
close(f)

answers = split(answers, "\n\n")
answers = [split(x) for x in answers]

function count_yes(group)
    out = first(group)
    for i in group
        out = intersect(out,i)
    end

    return length(out)
end

print(sum([count_yes(x) for x in answers]))