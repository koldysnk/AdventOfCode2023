INPUT_FILE = "Day18/day18input.txt"

def inGrid(grid,x,y):
    return x>=0 and y>=0 and y<len(grid) and x<len(grid[0])

def displayGrid(grid):
    for i in grid:
        for j in i:
            print(j,end="")
        print()

def saveGrid(grid):
    f = open("Day18/day18part1grid.txt","w")

    for i in grid:
        for j in i:
            f.write(j)
        f.write("\n")

    f.close()
def saveGridFill(grid):
    f = open("Day18/day18part1gridFilled.txt","w")

    for i in grid:
        for j in i:
            f.write(j)
        f.write("\n")

    f.close()

f = open(INPUT_FILE)
lines = f.readlines()

#For the first attempt I tried the shoelace formula

instructions = [{"dir":line.split(" ")[0],"dist":int(line.split(" ")[1]),"color":line.split(" ")[2]} for line in lines]

grid = [["#"]]

x,y = 0,0

print(x,y)
firstDir = instructions[0]["dir"]
lastDir = instructions[-1]["dir"]

for instruction in instructions:
    dir = instruction["dir"]
    dist = instruction["dist"] 



    if dir == "R":
        x+=dist
        if inGrid(grid,x,y):
            for i in range(x-dist,x+1):
                grid[y][i]="#"
        else:
            for i in range(x-dist,len(grid[y])):
                grid[y][i] = "#"
            for i in range(len(grid)):
                while len(grid[i])-1<x:
                    grid[i].append("#" if i ==y else ".")
    elif dir == "L":
        x-=dist
        if inGrid(grid,x,y):
            for i in range(x,x+dist):
                grid[y][i]="#"
        else:
            while x <0:
                for i in range(len(grid)):
                    grid[i].insert(0,"#" if i == y else "." )
                x+=1
    elif dir == "U":
        y-=dist
        if inGrid(grid,x,y):
            for i in range(y,y+dist):
                grid[i][x]="#"
        else:
            for i in range(0,y+dist):
                grid[i][x]= "#"
            while y < 0:
                grid.insert(0,["#" if i == x else "." for i in range(len(grid[0]))])
                y+=1
            #for i in range(0,y+dist+2):
                
    elif dir == "D":
        y+=dist
        if inGrid(grid,x,y):
            for i in range(y-dist,y+1):
                while x >= len(grid[i]):
                    grid[i].append(".")
                grid[i][x]="#"
        else:
            for i in range(y-dist,len(grid)):
                grid[i][x]="#"
            while len(grid)-1<y:
                grid.append(["#" if i == x else "." for i in range(len(grid[0]))])

    #print(x,y)
    #displayGrid(grid)
print(x,y)
displayGrid(grid)
saveGrid(grid)

if len(grid)>15:
    x,y = x+1,y-1
else:
    x,y = x+1,y+1

#Start filling

queue = [(x,y)]

while len(queue)>0:
    x,y = queue.pop()
    if grid[y][x] == ".":
        grid[y][x] = "#"
        queue.append((x+1,y))
        queue.append((x-1,y))
        queue.append((x,y+1))
        queue.append((x,y-1))
print()
displayGrid(grid)
saveGridFill(grid)
        
count = 0
for i in grid:
    count+=i.count("#")
print(count)
