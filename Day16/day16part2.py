import time
tic = time.perf_counter()
INPUT_FILE = "Day16/day16input.txt"

f = open(INPUT_FILE,"r")

lines = f.readlines()

grid = [[x for x in line.replace("\n","")] for line in lines]

starts =[]
RIGHT, LEFT, UP, DOWN = 1,2,3,4

for y in range(len(grid)):
    starts.append((y,0,RIGHT))
    starts.append((y,len(grid[0])-1,LEFT))

for x in range(len(grid[0])):
    starts.append((0,x,DOWN))
    starts.append((len(grid)-1,x,UP))

total = 0
for start in starts:
    energized = set([])

    beams = [start]
    history = [start]

    while len(beams) >0:
        beam = beams.pop()
        x = beam[0]
        y = beam[1]
        direction = beam[2]


        if x>=0 and y>=0 and x<len(grid) and y<len(grid[x]):
            energized.add((x,y))
            spot = grid[x][y]

            if (spot in [".","-"] and direction==RIGHT) or \
                (spot in ["\\","-"] and direction==DOWN) or \
                    (spot in ["/","-"] and direction==UP):
                new_beam = (x,y+1,RIGHT)
                if new_beam not in history:
                    beams.append(new_beam)
                    history.append(new_beam)
            if (spot in [".","-"] and direction==LEFT) or \
                (spot in ["/","-"] and direction==DOWN) or \
                    (spot in ["\\","-"] and direction==UP):
                new_beam = (x,y-1,LEFT)
                if new_beam not in history:
                    beams.append(new_beam)
                    history.append(new_beam)
            if (spot in [".","|"] and direction==UP) or \
                (spot in ["\\","|"] and direction==LEFT) or \
                    (spot in ["/","|"] and direction==RIGHT):
                new_beam = (x-1,y,UP)
                if new_beam not in history:
                    beams.append(new_beam)
                    history.append(new_beam)
            if (spot in [".","|"] and direction==DOWN) or \
                (spot in ["/","|"] and direction==LEFT) or \
                    (spot in ["\\","|"] and direction==RIGHT):
                new_beam = (x+1,y,DOWN)
                if new_beam not in history:
                    beams.append(new_beam)
                    history.append(new_beam)

    total = max(total,len(energized))
print(total)
toc = time.perf_counter()
print(f"Attempt 1 took {toc-tic} seconds")
