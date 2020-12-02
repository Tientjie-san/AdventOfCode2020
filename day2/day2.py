input_file = open('input.txt', "r")  # opens the file in read mode
input = [line.replace('-', ' ').replace(': ', ' ').split(' ') for line in input_file.read().splitlines()]
input_file.close()


def part1(input):
    count = 0
    for password in input:
        char_count = password[3].count(password[2])
        if int(password[0]) <= char_count <= int(password[1]):
            count += 1
    return count


def part2(input):
    count = 0
    for password in input:
        letter1 = password[3][int(password[0])-1]
        letter2 = password[3][int(password[1])-1]
        gezocht = password[2]
        if (letter1 == gezocht and letter2 != gezocht) or (letter1 != gezocht and letter2 == gezocht):
            count += 1
    return count


print(part1(input))
print(part2(input))