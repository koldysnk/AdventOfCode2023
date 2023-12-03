INPUT_FILE = "Day3/day3input.txt"

f = open(INPUT_FILE,"r")


grid = [list(x.replace("\n","")) for x in f.readlines()]
total = 0
print(total)

gears = {}

for x in range(len(grid)):
    start = -1
    end = -1
    current = 0
    for y in range(len(grid[x])):
        spot = grid[x][y]
        if spot.isdigit():
            if start == -1:
                start = y
            current = current*10 + int(spot)
        elif start != -1:
            end = y-1
            #Number is gotten
            valid = False
            if start>0:
                if grid[x][start-1] == '*':
                    if f"{x}-{start-1}" not in gears:
                        gears[f"{x}-{start-1}"] = []
                    gears[f"{x}-{start-1}"].append(current)
            if end < len(grid[x])-1:
                if grid[x][end+1] == '*':
                    if f"{x}-{end+1}" not in gears:
                        gears[f"{x}-{end+1}"] = []
                    gears[f"{x}-{end+1}"].append(current)
            if x > 0:
                for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                    if grid[x-1][i] == '*':
                        if f"{x-1}-{i}" not in gears:
                            gears[f"{x-1}-{i}"] = []
                        gears[f"{x-1}-{i}"].append(current)
            if x < len(grid)-1:
                for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                    if grid[x+1][i] == '*':
                        if f"{x+1}-{i}" not in gears:
                            gears[f"{x+1}-{i}"] = []
                        gears[f"{x+1}-{i}"].append(current)
            end=-1
            start = -1
            current = 0
    if start != -1:
        end = y-1
        #Number is gotten
        valid = False
        if start>0:
            if grid[x][start-1] == '*':
                if f"{x}-{start-1}" not in gears:
                    gears[f"{x}-{start-1}"] = []
                gears[f"{x}-{start-1}"].append(current)
        if end < len(grid[x])-1:
            if grid[x][end+1] == '*':
                if f"{x}-{end+1}" not in gears:
                    gears[f"{x}-{end+1}"] = []
                gears[f"{x}-{end+1}"].append(current)
        if x > 0:
            for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                if grid[x-1][i] == '*':
                    if f"{x-1}-{i}" not in gears:
                        gears[f"{x-1}-{i}"] = []
                    gears[f"{x-1}-{i}"].append(current)
        if x < len(grid)-1:
            for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                if grid[x+1][i] == '*':
                    if f"{x+1}-{i}" not in gears:
                        gears[f"{x+1}-{i}"] = []
                    gears[f"{x+1}-{i}"].append(current)
        end=-1
        start = -1
        current = 0
    #handle end of line

for part in gears.values():
    if len(part) == 2:
        total += part[0]*part[1]
print(total)
