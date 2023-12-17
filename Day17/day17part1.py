import time
import math

DEBUG = False
#Possible directions
UP, DOWN, LEFT, RIGHT = 1,2,3,4
#A node is represented as (x,y,cost,priority,previous direction, prev dir count,path)
COST_SPOT = 2
PRIORITY_SPOT = 3
DIR_SPOT = 4
DIR_COUNT_SPOT = 5
PATH_SPOT=6

def getManhattanDistance(cX,cY,gX,gY):
    return abs(cX-gX)+abs(cY-gY)

#Euclidian is slower for the test
def getEuclidianDistance(cX,cY,gX,gY):
    return math.sqrt(abs(cX-gX)**2+abs(cY-gY)**2)

#The heuristic value must be equal to or lower than the best case scenario.
#Two simple examples are manhattan distance and euclidian distance.
def getHeuristic(cX,cY,gX,gY):
    return getManhattanDistance(cX,cY,gX,gY)

def getPriority(current_cost,cX,cY,gX,gY):
    priority = current_cost + getHeuristic(cX,cY,gX,gY)
    return priority

def insertionAdd(q:list,node):
    p = node[PRIORITY_SPOT]
    i = len(q)

    while i > 0 and q[i-1][PRIORITY_SPOT]<=p:
        i -=1
    q.insert(i,node)

def insertionReplace(q:list,node):
    p = node[PRIORITY_SPOT]
    i = len(q)-1

    while i > 0 and (q[i][0], q[i][1])!=(node[0],node[1]):
        i -=1
    if p<q[i][PRIORITY_SPOT]:
        q[i] = node

#Add to the priority queue with in the correct position. 
#The queue should be sorted from a high priority value to a low one.
def priorityAdd(q:list,node):
    insertionAdd(q,node)

def color_text(text):
    return f"\033[31m{text}\033[0m"

def displaySG(sg, path):
    for x, i in enumerate(sg):
        j = ["S" if (x,y) in path else a for y,a in enumerate(i)]
        print(j)
    print()

#This method works for the sample but explores 3393 nodes
def attempt1():
    INPUT_FILE = "Day17/day17input.txt"

    f = open(INPUT_FILE,"r")

    grid = [[int(x) for x in list(line.replace("\n",""))] for line in f.readlines()]

    gX = len(grid)-1
    gY = len(grid[gX])-1
    
    #A node is represented as (x,y,cost,priority,previous direction, prev dir count)
    priority_queue=[(0,0,0,getPriority(0,0,0,gX,gY),0,0,[(0,0)])]
    search_grid = [['.' for x in y] for y in grid]
    #The priority queue should be sorted from highest to lowest priorities
    #The low priority numbers should come out of the queue first
    end = False
    count = 0

    #The idea here is to treat this as a maze solver or a path finder.
    #Analyze the best path by using the cost of each move. 
    #Start by just finding the fastest path. Then find fasest path with cost. Then add direction rules.
    #I will try to use the A* algorithm
    while not end:
        node = priority_queue.pop()
        node_cost = node[COST_SPOT]
        node_dir = node[DIR_SPOT]
        node_dir_count = node[DIR_COUNT_SPOT]
        node_path = node[PATH_SPOT]
        x = node[0]
        y = node[1]

        if search_grid[x][y] == "X":
            #print("node previously searched")
            pass
        else:
            search_grid[x][y] = "X"

        count += 1
        #Goal state
        if x ==gX and y ==gY:
            end = True
            print(f"{count}: {node_cost}")
        else:
            #Identify possible children and add to the queue
            #Rules: cannot go backwards, cannot excede grid, cannot move 3x in one direction
            #Should not move to a node that has already been visited

            #Move up
            if node_dir != DOWN and x > 0 and not (node_dir == UP and node_dir_count == 3):
                nX, nY = x-1, y
                new_cost = node_cost + grid[nX][nY]
                new_priority = getPriority(new_cost,nX,nY,gX,gY)
                new_dir = UP
                new_dir_count = node_dir_count + 1 if node_dir == new_dir else 1
                new_path = [x for x in node_path] if DEBUG else []
                new_path.append((nX,nY))
                new_node = (nX,nY,new_cost,new_priority,new_dir,new_dir_count,new_path)
                if search_grid[nX][nY] == ".":
                    search_grid[nX][nY] = "O"
                    priorityAdd(priority_queue,new_node)
                elif search_grid[nX][nY] == "O":
                    priorityAdd(priority_queue,new_node)
                    #May need to explore removing previously queued items here
                else:
                    pass#print("node previously queued")
            #Move right
            if node_dir != LEFT and y < len(grid[x])-1 and not (node_dir == RIGHT and node_dir_count == 3):
                nX, nY = x, y+1
                new_cost = node_cost + grid[nX][nY]
                new_priority = getPriority(new_cost,nX,nY,gX,gY)
                new_dir = RIGHT
                new_dir_count = node_dir_count + 1 if node_dir == new_dir else 1
                new_path = [x for x in node_path] if DEBUG else []
                new_path.append((nX,nY))
                new_node = (nX,nY,new_cost,new_priority,new_dir,new_dir_count,new_path)
                if search_grid[nX][nY] == ".":
                    search_grid[nX][nY] = "O"
                    priorityAdd(priority_queue,new_node)
                elif search_grid[nX][nY] == "O":
                    priorityAdd(priority_queue,new_node)
                    #May need to explore removing previously queued items here
                else:
                    pass#print("node previously queued")
                    
            #Move down
            if node_dir != UP and x < len(grid)-1 and not (node_dir == DOWN and node_dir_count == 3):
                nX, nY = x+1, y
                new_cost = node_cost + grid[nX][nY]
                new_priority = getPriority(new_cost,nX,nY,gX,gY)
                new_dir = DOWN
                new_dir_count = node_dir_count + 1 if node_dir == new_dir else 1
                new_path = [x for x in node_path] if DEBUG else []
                new_path.append((nX,nY))
                new_node = (nX,nY,new_cost,new_priority,new_dir,new_dir_count,new_path)
                if search_grid[nX][nY] == ".":
                    search_grid[nX][nY] = "O"
                    priorityAdd(priority_queue,new_node)
                elif search_grid[nX][nY] == "O":
                    priorityAdd(priority_queue,new_node)
                    #May need to explore removing previously queued items here
                else:
                    pass#print("node previously queued")
            #Move left
            if node_dir != RIGHT and y > 0 and not (node_dir == LEFT and node_dir_count == 3):
                nX, nY = x, y-1
                new_cost = node_cost + grid[nX][nY]
                new_priority = getPriority(new_cost,nX,nY,gX,gY)
                new_dir = LEFT
                new_dir_count = node_dir_count + 1 if node_dir == new_dir else 1
                new_path = [x for x in node_path] if DEBUG else []
                new_path.append((nX,nY))
                new_node = (nX,nY,new_cost,new_priority,new_dir,new_dir_count,new_path)
                if search_grid[nX][nY] == ".":
                    search_grid[nX][nY] = "O"
                    priorityAdd(priority_queue,new_node)
                elif search_grid[nX][nY] == "O":
                    priorityAdd(priority_queue,new_node)
                    #May need to explore removing previously queued items here
                else:
                    pass#print("node previously queued")
        if DEBUG:
            displaySG(search_grid, node_path)

def main():
    tic = time.perf_counter()
    attempt1()
    toc = time.perf_counter()
    print(f"Attempt 1 took {toc-tic} seconds")
main()