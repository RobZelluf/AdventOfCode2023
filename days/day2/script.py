import numpy as np

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

lines = open("data.txt", "r").read().splitlines()


def part_one():
    id_sum = 0

    for line in lines:
        grabs = line.split(": ")[-1].split("; ")

        possible = True
        for grab in grabs:
            grab = grab.split(", ")
            for blocks in grab:
                for color, n_max in max_cubes.items():
                    if color in blocks and int(blocks.split(" ")[0]) > n_max:
                        possible = False
                        break

                if not possible:
                    break

            if not possible:
                break

        if possible:
            id_sum += int(line.split(":")[0][4:])

    print("Sum:", id_sum)


def part_two():
    answer = 0
    for line in lines:
        max_colors = {k: 0 for k in max_cubes}

        grabs = line.split(": ")[-1].split("; ")
        for grab in grabs:
            grab = grab.split(", ")
            for block in grab:

                for color, n_min in max_colors.items():
                    if color in block:
                        max_colors[color] = max(n_min, int(block.split(" ")[0]))

        sum_pow = np.prod([v for k, v in max_colors.items()])
        answer += sum_pow

        print(answer)


part_two()