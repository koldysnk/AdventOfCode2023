import time
INPUT_FILE = "Day21/day21input.txt"



def attempt1():
    f = open(INPUT_FILE)

    lines = f.readlines()

    grid = [list(line.replace("\n","")) for line in lines]

    limit = 5000
    sX, sY = 0, 0
    found = False
    xLen, yLen = len(grid), len(grid[0])

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "S":
                found = True
                sX, sY = x, y
                break
        if found:
            break


    print("Start: ",sX,sY)

    queue = [(sX,sY,0)]
    end = {}
    evens = {}
    total = 0

    while len(queue)>0:
        total+=1
        current = queue.pop(0)
        cX, cY = current[0], current[1]
        steps = current[2]

        if steps>=limit:
            end[(cX,cY)] = ""
            continue

        if steps%2==0:
            if (cX,cY) in evens:
                continue
            else:
                end[(cX,cY)] = ""
                evens[(cX,cY)] = ""

        #Move up
        if True:
            nX, nY = cX-1, cY
            if grid[nX%xLen][nY%yLen] != "#":
                queue.append((nX,nY,steps+1))

        #Move left
        if True:
            nX, nY = cX, cY-1
            if grid[nX%xLen][nY%yLen] != "#":
                queue.append((nX,nY,steps+1))

        #Move down
        if True:
            nX, nY = cX+1, cY
            if grid[nX%xLen][nY%yLen] != "#":
                queue.append((nX,nY,steps+1))

        #Move right
        if True:
            nX, nY = cX, cY+1
            if grid[nX%xLen][nY%yLen] != "#":
                queue.append((nX,nY,steps+1))


    print(len(end))
    print(total)

def main():
    tic = time.perf_counter()
    attempt1()
    toc = time.perf_counter()
    print(f"Attempt 1 took {toc-tic} seconds")


main()