if __name__ == '__main__':
    with open('../input.txt', 'r') as input_file:
        arial_view: list[list[int]] = []
        for line in input_file:
            stripped = line.strip()
            arial_view.append([int(t) for t in stripped])

        total = len(arial_view) * len(arial_view[0])
        trees_not_seen = 0
        for i in range(1, len(arial_view) - 1):
            for j in range(1, len(arial_view[i]) - 1):
                cant_be_seen = True
                tree = arial_view[i][j]
                if cant_be_seen and max(arial_view[i][0:j]) < tree:
                    cant_be_seen = False
                if cant_be_seen and max(arial_view[i][j+1: len(arial_view[i])]) < tree:
                    cant_be_seen = False
                current_tallest_up = 0
                for z in range(0, i):
                    if arial_view[z][j] > current_tallest_up:
                        current_tallest_up = arial_view[z][j]
                if cant_be_seen and current_tallest_up < tree:
                    cant_be_seen = False
                current_tallest_down = 0
                for y in range(i + 1, len(arial_view)):
                    if arial_view[y][j]> current_tallest_down:
                        current_tallest_down = arial_view[y][j]
                if cant_be_seen and current_tallest_down < tree:
                    cant_be_seen = False


                if cant_be_seen:
                    trees_not_seen += 1
        print(total)
        print(total - trees_not_seen)

