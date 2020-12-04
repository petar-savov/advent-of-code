with open("input.txt") as f:
    inp = f.read()

inp = inp.split('\n\n')
inp = [x.replace("\n", " ").replace(":"," ") for x in inp]
passports = [dict([(k,v) for (k,v) in zip(x.split()[0::2],x.split()[1::2])]) for x in inp]

req_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def check(passport, req_fields = req_fields):
    for key in req_fields:
        if key not in passport.keys():
            return False

    return True

print(sum([check(x) for x in passports]))