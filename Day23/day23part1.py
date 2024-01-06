import copy
import time

INPUT_FILE = "Day23/day23input.txt"

def attempt1():
    f = open(INPUT_FILE)
    lines = f.readlines()

    grid = [list(x.replace("\n","")) for x in lines]

    start = (0,1,0,{(0,1)})
    queue = [start]
    maxDist = 0
    distances = set()

    while len(queue)>0:
        cX, cY, dist, visited = queue.pop()
        spot = grid[cX][cY]
        
        if cX == len(grid)-1:
            print(dist)
            maxDist = max(dist,maxDist)
            distances.add(dist)
            continue

        #Move up 
        if cX > 0 and spot not in [">","<","v"]:
            nX, nY = cX-1, cY
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))

        #Move left
        if cY > 0 and spot not in [">","^","v"]:
            nX, nY = cX, cY-1
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))

        #Move down
        if cX < len(grid)-1 and spot not in [">","^","<"]:
            nX, nY = cX+1, cY
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))

        #Move right
        if cY < len(grid[cX])-1 and spot not in ["v","^","<"]:
            nX, nY = cX, cY+1
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))


    print(distances)
    print(maxDist)


def main():
    attempt1()

main()