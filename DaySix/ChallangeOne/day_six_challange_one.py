

if __name__ == '__main__':
    with open('../input.txt', 'r') as input_file:
        current_string = ""
        index = 0
        for line in input_file:
            stripped: str = line.strip()
            for char in stripped:
                index += 1
                current_string += char
                if index >= 4:
                    if len(set(current_string[index - 4:index])) == 4:
                        print(index)
                        break
