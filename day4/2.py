with open("input.txt") as f:
    inp = f.read()

inp = inp.split('\n\n')
inp = [x.replace("\n", " ").replace(":"," ") for x in inp]
passports = [dict([(k,v) for (k,v) in zip(x.split()[0::2],x.split()[1::2])]) for x in inp]

req_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def check(passport, req_fields = req_fields):
    try:
        for key in req_fields:
            if key not in passport.keys():
                return False

        if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            return False

        if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            return False
        
        if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            return False
        
        height = int(passport['hgt'][:-2])
        height_unit = passport['hgt'][-2:]
        if height_unit == 'cm':
            if height < 150 or height > 193:
                return False
        elif height_unit =='in':
            if height < 59 or height > 76:
                return False
        else:
            return False
            
        if passport['hcl'][0] != '#' or len(passport['hcl'])!=7:
            return False
        
        for char in passport['hcl'][1:]:
            if char not in "0123456789abcdef":
                return False
        
        if passport['ecl'] not in ["amb","blu","brn","gry","grn","hzl", "oth"]:
            return False

        if len(passport['pid']) != 9:
            return False

        for char in passport['pid']:
            if char not in "0123456789":
                return False
        
        return True

    except:
        return False

print(sum([check(x) for x in passports]))