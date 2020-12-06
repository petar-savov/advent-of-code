f = open("day6/input.txt") 
answers = read(f, String)
close(f)

answers = split(answers, "\n\n")
answers = [replace(x, "\n" => "") for x in answers]

print(sum([length(Set(x)) for x in answers]))