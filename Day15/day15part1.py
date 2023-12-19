INPUT_FILE = "Day15/day15input.txt"

f = open(INPUT_FILE,"r")
items = f.readline().replace("\n","").split(",")

total = 0

for item in items:
    current = 0
    for i in item:
        current += ord(i)
        current *= 17
        current = current%256
    total += current

print(total)