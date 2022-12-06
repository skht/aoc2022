import sys

def is_all_unique(part):
    #return len(set(part)) == 4
    return len(set(part)) == 14

def find_marker(buffer):
    for index in range(len(buffer)):
        #part_buffer=buffer[index:index+4]
        part_buffer=buffer[index:index+14]
        print(f"{index} - unique {part_buffer} - {is_all_unique(part_buffer)} ")
        if(is_all_unique(part_buffer)):
            #return index + 4
            return index + 14

if __name__ == '__main__':
    buffer = open(sys.argv[1]).read()

    print("Start")
    print(f"Analyze of {buffer}")
    print(f"Marker found at {find_marker(buffer)}")
