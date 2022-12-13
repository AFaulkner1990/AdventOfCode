if __name__ == '__main__':
    with open('../input.txt', 'r') as input_file:
        head_x = 0
        head_y = 0
        tail_x = 0
        tail_y = 0
        tail_positions = ["00"]
        for line in input_file:
            stripped = line.strip()
            actions = stripped.split(" ")
            direction = actions[0]
            moves = int(actions[1])

            match direction:
                case "U":
                    for i in range(0, moves):
                        head_y += 1
                        if head_y > tail_y + 1:
                            tail_y = head_y - 1
                            tail_x = head_x
                            tail_positions.append(f"{tail_x}{tail_y}")
                case "D":
                    for i in range(0, moves):
                        head_y -= 1
                        if head_y < tail_y - 1:
                            tail_y = head_y + 1
                            tail_x = head_x
                            tail_positions.append(f"{tail_x}{tail_y}")
                case "L":
                    for i in range(0, moves):
                        head_x -= 1
                        if head_x < tail_x - 1:
                            tail_x = head_x + 1
                            tail_y = head_y
                            tail_positions.append(f"{tail_x}{tail_y}")
                case "R":
                    for i in range(0, moves):
                        head_x += 1
                        if head_x > tail_x + 1:
                            tail_x = head_x - 1
                            tail_y = head_y
                            tail_positions.append(f"{tail_x}{tail_y}")
        unique = list(set(tail_positions))
        print(len(tail_positions))
        print(len(unique))