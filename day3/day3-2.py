import string

def priority(letter):
    dict = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return dict.index(letter) + 1

def shared_item_across_3(tuple_3):
    item_1 = tuple_3[0]
    item_2 = tuple_3[1]
    item_3 = tuple_3[2]
    return next(iter(set(item_1) & set(item_2) & set(item_3)))

if __name__ == "__main__":
    input = open("input.txt","r")
    cleaned_lines = list(map(lambda x: x.strip(), input.readlines()))
    grouped_lines = list(zip(*(iter(cleaned_lines),) * 3))
    processed_lines = list(map(lambda x: shared_item_across_3(x), grouped_lines))
    calc = sum(list(map(lambda x: priority(x), processed_lines)))
    print(calc)
