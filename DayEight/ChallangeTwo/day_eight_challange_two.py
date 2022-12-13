if __name__ == '__main__':
    with open('../input.txt', 'r') as input_file:
        arial_view: list[list[int]] = []
        for line in input_file:
            stripped = line.strip()
            arial_view.append([int(t) for t in stripped])

        current_highest_scenic_score = 0
        for i in range(1, len(arial_view) - 1):
            for j in range(1, len(arial_view[i]) - 1):
                tree = arial_view[i][j]
                left_count = 0
                right_count = 0
                up_count = 0
                down_count = 0
                for z in arial_view[i][j - 1::-1]:
                    left_count += 1
                    if z >= tree:
                        break
                for y in arial_view[i][j + 1: len(arial_view[i])]:
                    right_count += 1
                    if y >= tree:
                        break
                for l in range(i - 1, -1, -1):
                    up_count += 1
                    if arial_view[l][j] >= tree:
                        break
                for n in range(i + 1, len(arial_view)):
                    down_count += 1
                    if arial_view[n][j] >= tree:
                        break
                scenery_score = up_count * down_count * left_count * right_count

                if scenery_score > current_highest_scenic_score:
                    current_highest_scenic_score = scenery_score

        print(current_highest_scenic_score)





