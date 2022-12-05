import sys


def is_fully_covered(range_1, range_2):
    first_left = int(range_1.split("-")[0])
    first_right = int(range_1.split("-")[1])
    second_left = int(range_2.split("-")[0])
    second_right = int(range_2.split("-")[1])
    #print(f"{first_left} {first_right} vs {second_left} {second_right}")
    if(first_left >= second_left and first_right <= second_right):
        #print(f"{range_1} fully covered in {range_2}")
        return True
    if(second_left >= first_left and second_right <= first_right):
        #print(f"{range_1} fully covered in {range_2}")
        return True
    else:
        #print(f"{range_1} not covered in {range_2}")
        return False

def is_overlapped(range_1, range_2):
    first_left = int(range_1.split("-")[0])
    first_right = int(range_1.split("-")[1])
    second_left = int(range_2.split("-")[0])
    second_right = int(range_2.split("-")[1])
    #print(f"{first_left} {first_right} vs {second_left} {second_right}")
    if(first_right >= second_left and first_left <= second_right):
        print(f"{range_1} overlapped {range_2}")
        return True
    else:
        #print(f"{range_1} not covered in {range_2}")
        return False


if __name__ == '__main__':
    input = open(sys.argv[1], "r")
    input_lines = input.readlines()
    cleared_lines = list(map(lambda x: x.strip(), input_lines))
    boolean_lines = list(map(lambda x: is_fully_covered( x.split(",")[0],x.split(",")[1]),cleared_lines))
    num_of_fully_covered = sum(list(map(lambda x: int(x == True), boolean_lines)))
    print(f"Fully covered {num_of_fully_covered}")

    boolean_lines = list(map(lambda x: is_overlapped( x.split(",")[0],x.split(",")[1]),cleared_lines))
    overlapped = sum(list(map(lambda x: int(x == True), boolean_lines)))
    print(f"Overlapped {overlapped}")
