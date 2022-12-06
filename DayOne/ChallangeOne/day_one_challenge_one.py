
if __name__ == '__main__':
    max_calories: int = 0
    with open('../input.txt', 'r') as input_file:
        elf_calorie: int = 0
        for line in input_file:
            stripped_line:str = line.strip()
            if len(stripped_line) > 0:
                elf_calorie += int(stripped_line)
            else:
                if elf_calorie > max_calories:
                    max_calories = elf_calorie
                elf_calorie = 0
    print(max_calories)
