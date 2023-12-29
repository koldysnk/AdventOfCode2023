INPUT_FILE = "Day18/day18input.txt"

def getDir(num):
    if num == "0":
        return "R"
    if num == "1":
        return "D"
    if num == "2":
        return "L"
    if num == "3":
        return "U"    

def getHex(hex):
    return int(hex,16)

f = open(INPUT_FILE)
lines = f.readlines()

#For the first attempt I tried the shoelace formula

instructions = [{"dir":line.split(" ")[0],"dist":int(line.split(" ")[1]),"color":line.split(" ")[2]} for line in lines]
instructions = [{"dir":getDir(line.replace("\n","")[-2]),"dist":getHex(line.replace("\n","")[-7:-2])} for line in lines]
#The logic will depend on if the path is being built in a clockwise or a counter clockwise fashion.
clockwise = True

x,y = 0,0
print(x,y)
count = 0
moves = 0

for i, instruction in enumerate(instructions):
    dir = instruction["dir"]
    dist = instruction["dist"] 
    nextDir = instructions[i+1]["dir"] if i+1<len(instructions) else instructions[0]["dir"]
    nX,nY = x,y
    moves += dist

    if clockwise:
        if dir == "R":
            #if nextDir == "D":
            #    nX+=1
            nX+=dist
        elif dir == "L":
            #if nextDir == "U":
            #    nX-=1
            nX-=dist
        elif dir == "U":
            #if nextDir == "R":
            #    nY+=1
            nY+=dist               
        elif dir == "D":
            #if nextDir == "L":
            #    nY-=1
            nY-=dist

    count += (y+nY)*(x-nX)
    print(dir,dist,"->",nX,nY)
    x,y = nX,nY

count = abs(count//2)
moves //=2
moves +=1
print(count)
print(count+moves)

