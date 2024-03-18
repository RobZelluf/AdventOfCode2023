import numpy as np

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

lines = open("data.txt", "r").read().splitlines()


def part_one():
    touching_sum = 0
    non_touching_sum = 0

    for line_num, line in enumerate(lines):
        touching_numbers = []
        not_touching = []

        curr_number = None

        for i, x in enumerate(line + "."):
            if x.isdigit():
                if curr_number is None:
                    curr_number = [(i, x)]
                else:
                    curr_number.append((i, x))

            else:
                if curr_number is not None:
                    """ Process digit """
                    touching = False
                    min_ind = curr_number[0][0] - 1
                    max_ind = curr_number[-1][0] + 1

                    for check_line_num in [line_num - 1, line_num, line_num + 1]:
                        if check_line_num < 0:
                            continue

                        for ind in list(np.arange(min_ind, max_ind + 1)):
                            if ind < 0:
                                continue

                            try:
                                if lines[check_line_num][ind] != "." and not lines[check_line_num][ind].isdigit():
                                    touching = True
                                    break
                            except IndexError:
                                pass

                        if touching:
                            break

                    curr_number = int("".join([x[1] for x in curr_number]))

                    if touching:
                        touching_numbers.append(curr_number)
                        touching_sum += curr_number
                    else:
                        not_touching.append(curr_number)
                        non_touching_sum += curr_number

                    curr_number = None

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22\n")

        if line_num > 0:
            print(lines[line_num - 1])

        print(lines[line_num])

        try:
            print(lines[line_num + 1])
        except IndexError:
            pass

        print("Touching:", touching_numbers)
        print("Not touching:", not_touching)

    print("Solution:", touching_sum)


def part_two():
    touching_sum = 0
    non_touching_sum = 0

    for line_num, line in enumerate(lines):
        if "*" in line:
            gears = [i for i, x in enumerate(line) if x == "*"]
            for gear in gears:
                """ Check top touches """




if __name__ == "__main__":
    part_two()