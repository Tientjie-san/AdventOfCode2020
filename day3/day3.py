def part1(input, slope):
    count = 0
    row = 0
    col = 0

    # om index error te voorkomen
    bottom = len(input)-1
    col_max = len(input[0])

    # voor ieder rij behalve de laatste vanwege index error
    while row != bottom:
        col += slope[0]
        row += slope[1]

        if col >= col_max:
            col -= col_max

        if row > bottom:
            row = bottom

        if input[row][col] == '#':
            count += 1

    return count


def part2(input, slopes):
    total = 1
    for slope in slopes:
        print(slope)
        total *= part1(input, slope)
    return total


input_file = open('input.txt', "r")  # opens the file in read mode
input = [list(line) for line in input_file.read().splitlines()]
input_file.close()

print(part1(input, (3, 1)))
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(part2(input, slopes))



