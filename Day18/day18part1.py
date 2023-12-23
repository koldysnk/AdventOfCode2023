INPUT_FILE = "Day18/day18input.txt"

f = open(INPUT_FILE)
lines = f.readlines()

#For the first attempt I tried the shoelace formula

instructions = [{"dir":line.split(" ")[0],"dist":int(line.split(" ")[1]),"color":line.split(" ")[2]} for line in lines]

grid = [["#"]]

x,y = 0,0

for instruction in instructions:
    dir = instruction["dir"]
    dist = instruction["dist"]

    if dir == "R":
        for i in range(dist):
            grid[y].append("#")
            x += 1
            for j in range(len(grid))
    elif dir == "L"
