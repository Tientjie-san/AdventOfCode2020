def part1(input):
    count = 0
    row = 0
    col = 0

    # om index error te voorkomen
    col_max = len(input[0])

    # voor ieder rij behalve de laatste vanwege index error
    for _ in range(len(input)-1):
        col += 3
        row += 1

        if col >= col_max:
            col -= col_max

        if input[row][col] == '#':
            count += 1

    return count


def part2(input, slopex, slopey):
    pass


input_file = open('input.txt', "r")  # opens the file in read mode
input = [list(line) for line in input_file.read().splitlines()]
input_file.close()

print(part1(input))
# print(part2(input))


