INPUT_FILE = "Day11/day11input.txt"

f = open(INPUT_FILE,"r")
line = f.readline()

space = []
empty_Y = []
empty_X = []

expansion = 999999

while line:
    line = line.replace("\n","")
    sector = list(line)
    space.append(sector)
    if "#" not in sector:
        empty_X.append(True)
    else:
        empty_X.append(False)
        if len(empty_Y)==0:
            empty_Y = [False if x=="#" else True for x in sector]
        else:
            for i, galaxy in reversed(list(enumerate(sector))):
                if galaxy == "#":
                    empty_Y[i] = False

    line = f.readline()



galaxies = []
for x, sector in enumerate(space):
    for y, galaxy in enumerate(sector):
        if galaxy == "#":
            galaxies.append((x,y))

total = 0
for g1 in galaxies:
    for g2 in galaxies:
        if g1[0]<g2[0]:
            total += abs(g1[0]-g2[0])+len([x for x in empty_X[g1[0]:g2[0]] if x == True])*expansion
        elif g1[0]>g2[0]:
            total += abs(g1[0]-g2[0])+len([x for x in empty_X[g2[0]:g1[0]] if x == True])*expansion
        if g1[1]<g2[1]:
            total += abs(g1[1]-g2[1])+len([y for y in empty_Y[g1[1]:g2[1]] if y == True])*expansion
        if g1[1]>g2[1]:
            total += abs(g1[1]-g2[1])+len([y for y in empty_Y[g2[1]:g1[1]] if y == True])*expansion
        
print(total//2)

