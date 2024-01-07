INPUT_FILE = "Day10/day10input.txt"
f = open(INPUT_FILE,"r")

line = f.readline()
sewer = []
xS=0
yS=0
found = False
while line:
    row = list(line.replace("\n",""))
    if "S" in row:
        yS = row.index("S")
        found = True
    if not found:
        xS+=1
    sewer.append(row)
    line=f.readline()

done = False
steps = 0
UP, RIGHT, DOWN, LEFT = 0,1,2,3
last_move = -1
x,y = xS,yS
p = "S"
while not done:
    moved = False
    '''
    a=last_move != RIGHT
    b=p in ["S","-","L","F"]
    d=y < len(sewer[x])-1
    e=sewer[x][y+1] in ["-","7","J"]'''

    #Can move anywhere
    if p == "S" and last_move >=0:
            done = True
    #Move up
    elif last_move != DOWN and p in ["S","|","L","J"] and x > 0 and sewer[x-1][y] in ["|","7","F","S"]:
        last_move = UP
        steps +=1
        x -=1
        p = sewer[x][y]
    elif last_move != LEFT and p in ["S","-","L","F"] and y < len(sewer[x])-1 and sewer[x][y+1] in ["-","7","J","S"]:
        last_move = RIGHT
        steps +=1
        y +=1
        p = sewer[x][y]
    elif last_move != UP and p in ["S","|","7","F"] and x < len(sewer)-1 and sewer[x+1][y] in ["|","L","J","S"]:
        last_move = DOWN
        steps +=1
        x +=1
        p = sewer[x][y]
    elif last_move != RIGHT and p in ["S","-","7","J"] and y > 0 and sewer[x][y-1] in ["-","L","F","S"]:
        last_move = LEFT
        steps +=1
        y -=1
        p = sewer[x][y]

print(steps//2)
