
input_file = open("input.txt","r")

# A - rock,  B - paper, C - scissors
# X - rock,  Y - paper, Z - scissors
#
score_dict = {
        "A X":1+3,
        "A Y":2+6,
        "A Z":3+0,
        "B X":1+0,
        "B Y":2+3,
        "B Z":3+6,
        "C X":1+6,
        "C Y":2+0,
        "C Z":3+3
}
#X - 1
#Y - 2
#Z - 3

score_dict_2 = {
        "A X":3+0,
        "A Y":1+3,
        "A Z":2+6,
        "B X":1+0,
        "B Y":2+3,
        "B Z":3+6,
        "C X":2+0,
        "C Y":3+3,
        "C Z":1+6
}
# X - lose
# Y - draw
# Z - win

def count_score(dict, lines):
    total_score = 0
    for line in lines:
        key = line.strip()
#        print(f"for line {key} have results {dict.get(key,0)} ")
        total_score = total_score + dict.get(key,0)
    return total_score

lines = input_file.readlines()
total_score_1 = count_score(score_dict, lines)
total_score_2 = count_score(score_dict_2, lines)
#print(total_score_2)

# alternative approach #1
def measure_score(lines, func):
    total_score = 0
    for line in lines:
        total_score = total_score + func(line.strip().split(" "))
    return total_score

def round_score_1(round):
    return value_player_figure(round[1]) + count_round_result(round[1], round[0])

def round_score_2(round):
    return value_player_result(round[1]) + count_player_figure(round[1], round[0])

def count_round_result(player, opponent):
    if(player == "X" and opponent == "A"): return 3
    if(player == "X" and opponent == "B"): return 0
    if(player == "X" and opponent == "C"): return 6
    if(player == "Y" and opponent == "A"): return 6
    if(player == "Y" and opponent == "B"): return 3
    if(player == "Y" and opponent == "C"): return 0
    if(player == "Z" and opponent == "A"): return 0
    if(player == "Z" and opponent == "B"): return 6
    if(player == "Z" and opponent == "C"): return 3
    return 0

# A - rock,  B - paper, C - scissors
# X - rock,  Y - paper, Z - scissors
def count_player_figure(result, opponent):
    if(result == "X" and opponent == "A"): return 3
    if(result == "X" and opponent == "B"): return 1
    if(result == "X" and opponent == "C"): return 2
    if(result == "Y" and opponent == "A"): return 1
    if(result == "Y" and opponent == "B"): return 2
    if(result == "Y" and opponent == "C"): return 3
    if(result == "Z" and opponent == "A"): return 2
    if(result == "Z" and opponent == "B"): return 3
    if(result == "Z" and opponent == "C"): return 1
    return 0

def value_player_result(result):
    if(result == "Z"):
        return 6
    if(result == "Y"):
        return 3
    return 0

def value_player_figure(symbol):
    if(symbol == "X"):
        return 1
    if(symbol == "Y"):
        return 2
    return 3

print("Task 1")
print(f"Estimate method: {measure_score(lines, round_score_1)}")
print(f"Dictionary method: {total_score_1}")

print("Task 1")
print(f"Estimate method: {measure_score(lines, round_score_2)}")
print(f"Dictionary method: {total_score_2}")
