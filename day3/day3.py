import string

def priority(letter):
    dict = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return dict.index(letter) + 1

def shared_item(rucksack):
    rucksack_size = len(rucksack)
    item_1 = rucksack[0:int(rucksack_size/2)]
    item_2 = rucksack[int(rucksack_size/2):rucksack_size]
    return next(iter(set(item_1) & set(item_2)))

if __name__ == "__main__":
    input = open("input.txt","r")
    cleaned_lines = list(map(lambda x: x.strip(), input.readlines()))
    processed_lines = list(map(lambda x: shared_item(x), cleaned_lines))
    calc = sum(list(map(lambda x: priority(x), processed_lines)))
    print(calc)
