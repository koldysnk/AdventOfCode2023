INPUT_FILE = "Day4/day4input.txt"

f = open(INPUT_FILE,"r")

lines = f.readlines()
winners = [x[x.find(":")+2:x.find("|")-1].split(" ") for x in lines]
picks = [x.replace("\n","")[x.find("|")+2:].split(" ") for x in lines]

total = 0
for i in range(len(picks)):
    pick = picks[i]
    current = 0
    for num in pick:
        if num != "" and num in winners[i]:
            if current == 0:
                current = 1
            else:
                current *= 2
    total += current
print(total)
