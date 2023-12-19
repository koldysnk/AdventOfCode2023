import time
tic = time.perf_counter()
INPUT_FILE = "Day16/day16input.txt"

f = open(INPUT_FILE,"r")

lines = f.readlines()

grid = [[x for x in line.replace("\n","")] for line in lines]

RIGHT, LEFT, UP, DOWN = 1,2,3,4
total = 0

energized = set([])

beams = [(0,0,RIGHT)]
history = [(0,0,RIGHT)]

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

print(len(energized))
toc = time.perf_counter()
print(f"Attempt 1 took {toc-tic} seconds")
print(f"Part 2 is expected to take {(toc-tic)*440} seconds or {(toc-tic)*440/60} minutes")
