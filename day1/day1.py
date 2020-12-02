def part1(input):
    for num in input:
        num2 = 2020-num
        if num2 in input:
            print(num, num2)
            return num * num2


def part2(input):
    for num in range(len(input)):
        num1 = input[num]
        for num2 in range(num+1, len(input)):
            num2 = input[num2]
            num3 = 2020-num1-num2
            if num3 in input:
                print(num1, num2, num3)
                return num1*num2*num3


input_file = open('input.txt', "r")  # opens the file in read mode
input = [int(line) for line in input_file.read().splitlines()]
input_file.close()
print(part1(input))
print(part2(input))
