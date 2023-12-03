INPUT_FILE = "Day3/day3input.txt"

f = open(INPUT_FILE,"r")


grid = [list(x.replace("\n","")) for x in f.readlines()]
total = 0
print(total)

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
                valid = True if grid[x][start-1] != '.' else valid
            if end < len(grid[x])-1:
                valid = True if grid[x][end+1] != '.' else valid
            if x > 0:
                for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                    valid = True if grid[x-1][i] != '.' else valid
            if x < len(grid)-1:
                for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                    valid = True if grid[x+1][i] != '.' else valid
            if valid:
                total+=current
            end=-1
            start = -1
            current = 0
    if start != -1:
        end = y
        #Number is gotten
        valid = False
        if start>0:
            valid = True if grid[x][start-1] != '.' else valid
        if end < len(grid[x])-1:
            valid = True if grid[x][end+1] != '.' else valid
        if x > 0:
            for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                valid = True if grid[x-1][i] != '.' else valid
        if x < len(grid)-1:
            for i in range(max(0,start-1),min(end+2,len(grid[x]))):
                valid = True if grid[x+1][i] != '.' else valid
        if valid:
            total+=current
        end=-1
        start = -1
        current = 0
    #handle end of line

print(total)
