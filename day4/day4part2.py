INPUT_FILE = "Day4/day4input.txt"

f = open(INPUT_FILE,"r")

lines = f.readlines()
winners = [x[x.find(":")+2:x.find("|")-1].split(" ") for x in lines]
picks = [x.replace("\n","")[x.find("|")+2:].split(" ") for x in lines]
copies = [1 for x in lines]

for i in range(len(picks)):
    
    pick = picks[i]
    current = 0
    for num in pick:
        if num != "" and num in winners[i]:
            current += 1
    for x in range(i+1,min(len(copies),i+1+current)):
        copies[x] += copies[i]
    
print(sum(copies))
