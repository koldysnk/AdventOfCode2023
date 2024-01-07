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
            maxDist = max(dist,maxDist)
            print(dist," -> ",maxDist)
            distances.add(dist)
            continue

        #Move down
        if cX < len(grid)-1:
            nX, nY = cX+1, cY
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))

        #Move right
        if cY < len(grid[cX])-1:
            nX, nY = cX, cY+1
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))

        #Move up 
        if cX > 0 and spot:
            nX, nY = cX-1, cY
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))

        #Move left
        if cY > 0 and spot:
            nX, nY = cX, cY-1
            if grid[nX][nY] != "#" and (nX,nY) not in visited:
                newVisited = {i for i in visited}
                newVisited.add((nX,nY))
                queue.append((nX,nY,dist+1,newVisited))


    print(distances)
    print(maxDist)

#The goal of attempt 2 is to group each direction into one node.
#For example: a new node will only be added when a decision needs to be made.
#Hopefully this will greatly reduce the number of nodes that will be analyzed.
def attempt2():
    pass

def main():
    attempt1()

main()

#6146 is too low