
if __name__ == '__main__':
    total_priority = 0
    priority_dictionary = {}

    starting_char = 'a'
    for i in range(1, 27):
        priority_dictionary[starting_char] = i
        starting_char = chr(ord(starting_char) + 1)

    starting_char = 'A'
    for i in range(27, 53):
        priority_dictionary[starting_char] = i
        starting_char = chr(ord(starting_char) + 1)

    with open('../input.txt', 'r') as input_file:
        lines = input_file.readlines()
        for i in range(0, len(lines), 3):
            elf_one = lines[i].strip()
            elf_two = lines[i + 1].strip()
            elf_three = lines[i + 2].strip()
            if len(elf_one) > len(elf_two) and len(elf_one) > len(elf_three):
                for j in range(0, len(elf_one)):
                    if elf_one[j] in elf_two and elf_one[j] in elf_three:
                        total_priority += priority_dictionary.get(elf_one[j])
                        break
            elif len(elf_two) > len(elf_one) and len(elf_two) > len(elf_three):
                for j in range(0, len(elf_two)):
                    if elf_two[j] in elf_one and elf_two[j] in elf_three:
                        total_priority += priority_dictionary.get(elf_two[j])
                        break
            else:
                for j in range(0, len(elf_three)):
                    if elf_three[j] in elf_one and elf_three[j] in elf_two:
                        total_priority += priority_dictionary.get(elf_three[j])
                        break
    print(total_priority)
