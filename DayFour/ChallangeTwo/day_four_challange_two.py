if __name__ == '__main__':
    count: int = 0
    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            stripped: str = line.strip()
            cleaning_sections: list[str] = stripped.split(',')
            elf_one: list[int] = list(map(lambda v: int(v), cleaning_sections[0].split('-')))
            elf_two: list[int] = list(map(lambda v: int(v), cleaning_sections[1].split('-')))
            if (elf_two[0] <= elf_one[0] <= elf_two[1]) or \
                    (elf_two[0] <= elf_one[1] <= elf_two[1]) or \
                    (elf_one[0] <= elf_two[0] <= elf_one[1]) or \
                    (elf_one[0] <= elf_two[1] <= elf_one[1]):
                count += 1
    print(count)
