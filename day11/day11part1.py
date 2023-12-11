INPUT_FILE = "Day11/day11input.txt"

f = open(INPUT_FILE,"r")
line = f.readline()

space = []
empty = []


while line:
    line = line.replace("\n","")
    sector = list(line)
    space.append(sector)
    if "#" not in sector:
        space.append([x for x in sector])
    else:
        if len(empty)==0:
            empty = [False if x=="#" else True for x in sector]
        else:
            for i, galaxy in reversed(list(enumerate(sector))):
                if galaxy == "#":
                    empty[i] = False

    line = f.readline()

for i, x in reversed(list(enumerate(empty))):
    if x:
        for y in space:
            y.insert(i,".")

galaxies = []
for x, sector in enumerate(space):
    for y, galaxy in enumerate(sector):
        if galaxy == "#":
            galaxies.append((x,y))

total = 0
for g1 in galaxies:
    for g2 in galaxies:
        total += abs(g1[0]-g2[0])+abs(g1[1]-g2[1])

print(total//2)
