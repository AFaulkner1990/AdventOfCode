from __future__ import annotations


class DeviceDirectory:
    def __init__(self, name: str, parent_directory: DeviceDirectory | None):
        self._name: str = name
        self._parent_directory: DeviceDirectory = parent_directory
        self._files: list[DeviceFile] = []
        self._directories: list[DeviceDirectory] = []
        self._size: int = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def parent_directory(self):
        return self._parent_directory

    @property
    def name(self):
        return self._name

    @property
    def directories(self):
        return self._directories

    def add_file(self, file_name: str, file_size: int) -> DeviceFile:
        self.__update_directory_sizes(file_size)
        file = DeviceFile(file_name, file_size, self)
        self._files.append(file)
        return file

    def add_directory(self, directory_name: str) -> DeviceDirectory:
        new_dir = DeviceDirectory(directory_name, self)
        self._directories.append(new_dir)
        return new_dir

    def __update_directory_sizes(self, file_size):
        self.size += file_size
        parent_directory = self.parent_directory
        while parent_directory:
            parent_directory.size += file_size
            parent_directory = parent_directory.parent_directory


class DeviceFile:
    _directory: DeviceDirectory
    _size: int
    _name: str

    def __init__(self, name: str, size: int, parent_dir: DeviceDirectory):
        self._name = name
        self._size = size
        self._directory = parent_dir

    @property
    def size(self):
        return self._size


if __name__ == '__main__':
    with open('../input.txt', 'r') as input_file:
        root_directory = DeviceDirectory("/", None)
        current_directory: DeviceDirectory = root_directory
        all_dirs = [root_directory]
        for line in input_file:
            command: str = line.strip()
            if command.startswith("$ cd "):
                location = command[5:]
                if location == "/":
                    current_directory = root_directory
                elif location == ".." and current_directory.parent_directory is not None:
                    current_directory = current_directory.parent_directory
                else:
                    directory = list(filter(lambda d: d.name == location, current_directory.directories))
                    if directory:
                        current_directory = directory[0]
                    else:
                        created_dir = current_directory.add_directory(location)
                        current_directory = created_dir
                        all_dirs.append(created_dir)
            else:
                if command.startswith("dir "):
                    parts = command.split(" ")
                    created_dir = current_directory.add_directory(parts[1])
                    all_dirs.append(created_dir)
                elif not command.startswith("$ ls"):
                    parts = command.split(" ")
                    current_directory.add_file(parts[1], int(parts[0]))
        print(sum(d.size for d in filter(lambda d: d.size <= 100000, all_dirs)))