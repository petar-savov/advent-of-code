f = open("day6/input.txt") 
answers = read(f, String)
close(f)

answers = split(answers, "\n\n")
answers = [replace(x, "\n" => "") for x in answers]
answers = [split(x) for x in answers]

function all_yes(group::Array)
    common = group[1]
    if length(group) > 1
        for i in 2:length(group)
            common = intersect(common,group[i])
        end
    end
    return common
end

print(sum([length(all_yes(x)) for x in answers]))