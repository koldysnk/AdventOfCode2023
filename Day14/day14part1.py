INPUT_FILE = "Day14/day14input.txt"

f = open(INPUT_FILE,"r")

grid = [[x for x in list(line.replace("\n",""))] for line in f.readlines()]

total = 0
for og_x in range(len(grid)):
    for y in range(len(grid[og_x])):
        x = og_x
        spot = grid[x][y]
        movable = spot=="O"

        while movable:
            if x>0 and grid[x-1][y] == ".":
                grid[x][y] = "."
                x -= 1
                grid[x][y] = "O"
            else:
                movable = False
                total += len(grid)-x

print(total)

#109561 is too high