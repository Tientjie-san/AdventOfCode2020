input_file = open('input.txt', "r")  # opens the file in read mode
boarding_pass_list = input_file.read().split()
input_file.close()


def part1(boarding_pass_list):
    boarding_pass = [calc_id(boarding_pass) for boarding_pass in boarding_pass_list]
    boarding_pass.sort()
    return boarding_pass[-1]


def part2(boarding_pass_list):
    seat_list = [calc_id(boarding_pass) for boarding_pass in boarding_pass_list]
    seat_list.sort()
    prev = seat_list[0]
    print(seat_list)
    for i in range(1, len(seat_list)):
        if seat_list[i] - prev == 2:
            return prev + 1
        prev = seat_list[i]


def calc_id(boarding_pass):
    row = calc_row(boarding_pass[:7])
    col = calc_col(boarding_pass[7:])
    return row*8+col


def calc_row(row_code):
    bottom = 0
    row = 127
    for char in row_code:
        if char == 'F':
            row -= ((row-bottom + 1) >> 1)

        else:
            bottom += ((row-bottom + 1) >> 1)

    return row


def calc_col(col_code):
    bottom = 0
    col = 7
    for char in col_code:
        if char == 'L':
            col -= ((col-bottom + 1) >> 1)

        else:
            bottom += ((col-bottom + 1) >> 1)

    return col

print(part2(boarding_pass_list))
