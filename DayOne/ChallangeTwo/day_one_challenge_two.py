
if __name__ == '__main__':
    top_three_calories: list = [0, 0, 0]
    with open('../input.txt', 'r') as input_file:
        elf_calorie: int = 0
        for line in input_file:
            stripped_line:str = line.strip()
            if len(stripped_line) > 0:
                elf_calorie += int(stripped_line)
            else:
                if elf_calorie > top_three_calories[0]:
                    top_three_calories[2] = top_three_calories[1]
                    top_three_calories[1] = top_three_calories[0]
                    top_three_calories[0] = elf_calorie
                elif elf_calorie > top_three_calories[1]:
                    top_three_calories[2] = top_three_calories[1]
                    top_three_calories[1] = elf_calorie
                elif elf_calorie > top_three_calories[2]:
                    top_three_calories[2] = elf_calorie
                elf_calorie = 0
    print(sum(top_three_calories))
