INPUT_FILE = "Day8/day8input.txt"

f = open(INPUT_FILE,"r")

instructions = f.readline().replace("\n","")
f.readline()
line = f.readlines()
path = {x.split(" ")[0]:{"L":x.split(" ")[2].replace("(","").replace(",",""), "R":x.split(" ")[3].replace(")","").replace("\n","")} for x in line}
print(path)

current = "AAA"
goal = "ZZZ"

count = 0
pos = 0

while current != goal:
    direction = instructions[pos]
    current = path[current][direction]
    count+=1
    pos = pos+1 if pos<len(instructions)-1 else 0
print(count)
