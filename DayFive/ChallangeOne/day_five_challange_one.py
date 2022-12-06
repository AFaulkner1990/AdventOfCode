from collections import namedtuple
import re

if __name__ == '__main__':
    Instruction = namedtuple("Instruction", ["move_items", "from_container", "to_container"])
    top_containers = []

    def clean_containers(container: str) -> list[chr]:
        cleaned_container = []
        for i in range(1, 37, 4):
            cleaned_container.append(container[i])
        return cleaned_container

    def clean_instruction(instruction: str) -> Instruction[int, int, int]:
        numbers: list[str] = re.findall(r'[0-9]+', instruction)
        return Instruction(move_items=(int(numbers[0])), from_container=(int(numbers[1])), to_container=(
            int(numbers[2])))

    def rotate_2d_array(array: list[list[any]]) -> list[tuple[any]]:
        return list(zip(*array))[::-1]

    with open('../input.txt', 'r') as input_file:
        lines: list[str] = input_file.readlines()
        containers: list[list[chr]] = list(map(clean_containers, lines[:8]))
        rotated_containers: list[tuple[chr]] = rotate_2d_array(containers)
        labelled_containers: dict[int, list[chr]] = {}
        for (i, container) in enumerate(rotated_containers):
            labelled_containers[i+1] = list(filter(lambda c: c and not c.isspace(), container))

        instructions: list[Instruction[int, int, int]] = list(map(clean_instruction, lines[10:]))
        for instruction in instructions:
            labelled_containers[instruction.to_container].extend(labelled_containers[instruction.from_container][-instruction.move_items:])
            labelled_containers[instruction.from_container] = labelled_containers[instruction.from_container][0:instruction.move_items - 1]

        for key in labelled_containers.keys():
            container = labelled_containers.get(key)
            if (len(container) > 0):
                top_container = container[-1]
                top_containers.append(top_container)
    print(str.join("", top_containers))
