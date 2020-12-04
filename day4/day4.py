def part1(required, optional):
    input_file = open('input.txt', "r")  # opens the file in read mode
    line = True
    count = 0
    passport = {}

    while line:
        line = input_file.readline()

        if not line:
            if is_valid(passport, required, optional):
                count += 1
            break

        if line == '\n':
            if is_valid(passport, required, optional):
                count += 1

            passport.clear()
            continue

        keys_values = line.split(' ')
        for key_value in keys_values:
            key, value = key_value.split(":")
            passport[key] = value.strip('\n')

    input_file.close()
    return count


def is_valid(passport, required, optional):

    if not (passport.keys() == required or passport.keys() == required - optional):
        return False

    if not (valid_byr(passport['byr'])):
        return False
    if not (valid_hcl(passport['hcl'])):
        return False
    if not(valid_eyr(passport['eyr'])):
        return False
    if not(valid_hgt(passport['hgt'])):
        return False
    if not(valid_ecl(passport['ecl'])):
        return False
    if not(valid_iyr(passport['iyr'])):
        return False
    if not(valid_pid(passport['pid'])):
        return False

    return True


def valid_byr(byr):
    if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
        return False
    return True


def valid_iyr(iyr):
    if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
        return False
    return True


def valid_eyr(eyr):
    if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
        return False
    return True


def valid_hgt(hgt):
    if hgt[-2:] != 'cm' and hgt[-2:] != 'in':
        return False

    if hgt[-2:] == 'cm':
        num = int(hgt.split('cm')[0])
        if num < 150 or num > 193:
            return False

    if hgt[-2:] == 'in':
        num = int(hgt.split('in')[0])
        if num < 59 or num > 76:
            return False

    return True


def valid_hcl(hcl):
    allowed = '0123456789abcdef'

    if len(hcl) != 7 or hcl[0] != '#':
        return False

    for char in hcl[1:]:
        if char not in allowed:
            return False

    return True


def valid_ecl(ecl):
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    return True


def valid_pid(pid):
    if len(pid) != 9 or not pid.isdigit():
        return False

    return True


print(part1({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}, {'cid'}))
