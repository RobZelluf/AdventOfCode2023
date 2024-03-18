

digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digit_words_count = {k: 0 for k in digit_words}


lines = open("data.txt", "r").read().splitlines()


total_sum = 0

for line in lines:
    digits = []

    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(int(char))

        else:
            for j, digit_word in enumerate(digit_words):
                if line[i:].startswith(digit_word):
                    digits.append(j)

    num = int(f'{digits[0]}{digits[-1]}')
    total_sum += num

print(total_sum)

print(digit_words_count)