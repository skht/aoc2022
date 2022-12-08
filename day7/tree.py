
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.dir = dir

class DirectoryNode:
    def __init__(self, name):
        self.dirs = []
        self.files = []
        self.name = name
        self.parent = None

    def add_dir(self, dir_node):
        print(f"Adding directory {dir_node.name}")
        self.dirs.append(dir_node)
        dir_node.parent = self
        return self

    def add_file(self, file_node):
        print(f"Adding file {file_node.name} with size {file_node.size}")
        self.files.append(file_node)
        return self

    def size(self):
        # all files in dirs
        size = sum(map(lambda file: file.size, self.files))
        dir_size = sum(map(lambda dir: dir.size(), self.dirs))
        return size + dir_size
