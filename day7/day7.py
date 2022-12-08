import sys

from tree import File,DirectoryNode

def update_size_dict(root, dict):
    for dir in root.dirs:
        print(f"{dir.name} {dir.size()}")
        dict[dir.name] = dir.size()
        update_size_dict(dir, dict)
    return dict

def size_with_limit(root, flatten_size):
    for dir in root.dirs:
        flatten_size.append(dir.size())
        size_with_limit(dir, flatten_size)
    return flatten_size

def print_dir_size(root, limit):
    for dir in root.dirs:
        print_dir_size(dir, limit)
    if(root.size() <= limit):
        print(f"{root.name} {root.size()}")

def parse(input, root):
    head, *tail = input
    print(f"Processing {head}")
    if(head == "$ cd .."):
        print(f"Return to parent {root.parent.name}")
        parse(tail, root.parent)
        return
    elif(head.startswith("$ cd") and head != "$ cd .."):
        print(f"Creating subdir {head.split(' ')[2]}")
        sub_dir = DirectoryNode(head.split(" ")[2])
        root.add_dir(sub_dir)
        parse(tail, sub_dir)
        return
    elif(head[0].isdigit()):
        s = head.split(" ")
        print(f"Creating file {s[1]} of size {s[0]} inside {root.name}")
        file = File(s[1], int(s[0]))
        root.add_file(file)
    # ignore commands
    # $ ls
    # dir [name]
    # break condition
    if(tail == []):
        print(" #!# End of lines")
        return 0
    parse(tail, root)
    # parse loop

def print_tree(dir, offset, deep):
    print(offset * deep + dir.name)
    for file in dir.files:
        print(offset * deep + f"*{file.name} {file.size}")
    for dir in dir.dirs:
        print_tree(dir, " ", deep+1)

if __name__ == "__main__":
    input = open(sys.argv[1], "r")
    input_content = [line.strip() for line in input.readlines()]
    start_node = DirectoryNode("/")
    start_node.parent = None
    print("     ")
    print(" Start of parsing ")
    print("     ")
    parse(input_content[1:], start_node)
    print(input_content)

    print_tree(start_node, "", 0)
    total_size = print_dir_size(start_node, 100000)
    print(f"Total size {total_size}")
    flatten_size = [start_node.size()]
    total_size = size_with_limit(start_node,flatten_size)
    print(f"Total size {total_size}")
    limited_flatten_size = sum(filter(lambda x: x < 100000, flatten_size))
    print(f"Total size with limit {limited_flatten_size}")

    to_free_up = 70000000 - total_size[0]
    to_free_up_2 = 30000000 - to_free_up
    print(f"{to_free_up} {to_free_up_2} {total_size[0]}")
    dir_to_del = list(filter(lambda x: x > to_free_up_2, total_size))
    dir_to_del.sort()
    print(f"Delete size {dir_to_del}")
    print(f"Total free space after delete size {dir_to_del[0] + to_free_up}")
