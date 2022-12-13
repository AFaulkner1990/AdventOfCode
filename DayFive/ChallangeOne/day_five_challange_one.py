from collections import namedtuple
import re

if __name__ == '__main__':
    Instruction = namedtuple("Instruction", ["move_items", "from_container", "to_container"])
    top_containers = []

    def clean_containers(cont: str) -> list[chr]:
        cleaned_container = []
        for index in range(1, 37, 4):
            cleaned_container.append(cont[index])
        return cleaned_container

    def clean_instruction(inst: str) -> Instruction[int, int, int]:
        numbers: list[str] = re.findall(r'[0-9]+', inst)
        return Instruction(move_items=(int(numbers[0])), from_container=(int(numbers[1])), to_container=(
            int(numbers[2])))

    def rotate_2d_array(array: list[list[any]]) -> list[tuple[any]]:
        return list(zip(*array))[::-1]

    def get_items_to_move(no_of_items: int, cont: list[chr]) -> list[chr]:
        if len(cont) > no_of_items:
            return cont[-no_of_items:].copy()
        else:
            return cont.copy()

    def remove_items_from_stack(no_of_items: int, cont: list[chr]) -> list[chr]:
        if len(cont) > no_of_items:
            return cont[0: len(cont) - no_of_items].copy()
        else:
            return []

    def add_items_to_stack(items: list[chr], cont: list[chr]) -> list[chr]:
        copied = cont.copy()
        copied.extend(items[::-1].copy())
        return copied

    with open('../input.txt', 'r') as input_file:
        lines: list[str] = input_file.readlines()
        containers: list[list[chr]] = list(map(clean_containers, lines[:8]))
        rotated_containers: list[tuple[chr]] = rotate_2d_array(containers)
        labelled_containers: dict[int, list[chr]] = {}
        for (i, container) in enumerate(rotated_containers):
            labelled_containers[len(rotated_containers) - i] = \
                list(filter(lambda c: c and not c.isspace(), container))[::-1]

        instructions: list[Instruction[int, int, int]] = list(map(clean_instruction, lines[10:]))
        for instruction in instructions:
            items = get_items_to_move(instruction.move_items, labelled_containers[instruction.from_container])
            labelled_containers[instruction.from_container] = remove_items_from_stack(instruction.move_items, labelled_containers[instruction.from_container])
            labelled_containers[instruction.to_container] = add_items_to_stack(items, labelled_containers[instruction.to_container])

        for key in labelled_containers.keys():
            container = labelled_containers.get(key)
            if len(container) > 0:
                top_container = container[-1]
                top_containers.append(top_container)
    print(str.join("", top_containers))
