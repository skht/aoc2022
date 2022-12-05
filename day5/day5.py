import sys
from itertools import islice

cargo_sample = {
    1 : ["Z","N"],
    2 : ["M","C","D"],
    3 : ["P"]
}

cargo_input = {
    1 : ["F","C","P","G","Q","R"],
    2 : ["W","T","C","P"],
    3 : ["B","H","P","M","C"],
    4 : ["L","T","Q","S","M","P","R"],
    5 : ["P","H","J","Z","V","G","N"],
    6 : ["D","P","J"],
    7 : ["L","G","P","Z","F","J","T","R"],
    8 : ["N","L","H","C","F","P","T","J"],
    9 : ["G","V","Z","Q","H","T","C","W"]
}


def is_move_instruction(instr):
    if(instr.startswith("move")):
        return True
    return False

def decode_instruction(instr):
    splitted = instr.split(" ")
    return(int(splitted[1]),int(splitted[3]),int(splitted[5]))

def move_action(source, target):
    bag = cargo_input[source].pop()
    print(f"Taking {bag} from {source} to {target}")
    cargo_input[target].append(bag)

def move_action_9001(source, target, num_el):
    full_bag = list()
    for _ in range(num_el):
        bag = cargo_input[source].pop()
        full_bag.append(bag)
    print(f"Taking {reversed(full_bag)} from {source} to {target}")
    cargo_input[target] = cargo_input[target] + list(reversed(full_bag))

if __name__ == '__main__':
    input = open("input.txt", "r")
    cleaned_lines = [line.strip() for line in input.readlines()]
    instruction_lines = list(filter(is_move_instruction, cleaned_lines))
    for line in instruction_lines:
        decoded_line = decode_instruction(line)
        print(decoded_line)
        #for i in range(1,decoded_line[0]+1):
        #    print(f"Runnign action {decoded_line} {i} time")
        #    move_action(decoded_line[1],decoded_line[2])
        move_action_9001(decoded_line[1],decoded_line[2],decoded_line[0])
        print("Status")
        for i in range(1,10):
            print(cargo_input[i])

print(f"Final result {cargo_input[1].pop()}{cargo_input[2].pop()}{cargo_input[3].pop()}{cargo_input[4].pop()}{cargo_input[5].pop()}{cargo_input[6].pop()}{cargo_input[7].pop()}{cargo_input[8].pop()}{cargo_input[9].pop()}")
