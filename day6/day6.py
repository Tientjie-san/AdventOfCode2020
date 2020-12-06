def part1():
    input_file = open('input.txt', "r")  # opens the file in read mode
    line = True
    count = 0
    group_answers = set()
    while line:
        line = input_file.readline()

        if line == '\n' or not line:
            count += len(group_answers)
            group_answers.clear()
            continue

        answers = list(line.strip())
        group_answers.update(answers)

    input_file.close()
    return count


def part2():
    input_file = open('input.txt', "r")  # opens the file in read mode
    line = True
    count = 0
    individual_answers = []
    while line:
        line = input_file.readline()

        if line == '\n' or not line:
            if len(individual_answers) == 1:
                count += len(individual_answers[0])
            else:
                common_answers = individual_answers[0]
                for i in range(1, len(individual_answers)):
                    common_answers &= individual_answers[i]
            count += len(common_answers)
            common_answers.clear()
            individual_answers.clear()
            continue

        answers = set(list(line.strip()))
        individual_answers.append(answers)

    input_file.close()
    return count


print(part2())
