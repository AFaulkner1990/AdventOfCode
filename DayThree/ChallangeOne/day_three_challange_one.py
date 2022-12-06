
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
        for line in input_file:
            stripped: str = line.strip()
            number_of_items = len(stripped)
            number_items_each_component: int = number_of_items // 2
            compartment_one = stripped[:number_items_each_component]
            compartment_two = stripped[-number_items_each_component:]
            for i in range(0, number_items_each_component):
                if compartment_one[i] in compartment_two:
                    total_priority += priority_dictionary.get(compartment_one[i])
                    break
    print(total_priority)