INPUT_FILE = "Day17/day17input.txt"

f = open(INPUT_FILE,"r")

grid = [[x for x in list(line.replace("\n",""))] for line in f.readlines()]

UP, DOWN, LEFT, RIGHT = 1,2,3,4
path=[(0,0,0,0,0)]

#The idea here is to treat this as a maze solver.
#Analyze the best path by using the cost of each move. 
#Start by just finding the fastest path. Then find fasest path with cost. Then add direction rules.
