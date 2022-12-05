
f = open("input.txt","r")

index = 1
elves = {}
for line in f:
    if(line.strip()):
        elves[index] = elves.get(index,0) + int(line)
        print(str(index) + " " + line)
    if len(line.strip()) == 0:
        index = index + 1

highestElves = 1
for key in elves.keys():
    if(elves.get(key) > elves[highestElves]):
        highestElves = key

print(elves)
print("=====")
print(str(highestElves) + " - " + str(elves.get(highestElves)))
f.close()


elves_sorted = sorted(elves.items(), key=lambda kv: kv[1])
print(elves_sorted)
result = 71502 + 68977 + 67712
print(result)
