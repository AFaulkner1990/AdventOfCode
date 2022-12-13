

if __name__ == '__main__':
    NO_OF_CHARS = 14
    with open('../input.txt', 'r') as input_file:
        current_string = ""
        index = 0
        for line in input_file:
            stripped: str = line.strip()
            for char in stripped:
                index += 1
                current_string += char
                if index >= NO_OF_CHARS:
                    if len(set(current_string[index - NO_OF_CHARS:index])) == NO_OF_CHARS:
                        print(index)
                        break
