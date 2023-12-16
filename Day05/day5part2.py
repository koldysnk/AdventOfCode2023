INPUT_FILE = "Day5/day5input.txt"

f = open(INPUT_FILE,"r")

seedMap = f.readline().replace("\n","").split(" ")[1:]
nextMap = []
i=0
while i<len(seedMap):
    nextMap.append((int(seedMap[i]),int(seedMap[i+1])))
    i+=2
seedMap = nextMap

transformations = []
counter = -1

line = f.readline()
while line:
    if not len(line) < 2:
        if not line[0].isdigit():
            counter += 1
            transformations.append([])
        else:
            transformations[counter].append(line.replace("\n","").split(" "))
    line = f.readline()




for transformation in transformations:
    nextMap = []
    while len(seedMap) > 0:
        source, ran2 = seedMap.pop()
        top2 = source+ran2-1
        found = False
        for mapping in transformation:
            sStart = int(mapping[1])
            dStart = int(mapping[0])
            ran = int(mapping[2])
            top = sStart+ran-1
            if source >= sStart and source < sStart + ran:
                if source+ran2<=sStart+ran:
                    nextMap.append((dStart + source - sStart,ran2))
                else:
                    diff = source+ran2-ran-sStart
                    nextMap.append((dStart + source - sStart,ran2-diff))
                    seedMap.append((sStart + ran,diff))
                found = True
                break
            elif source < sStart and source+ran2 >= sStart:
                diff = source+ran2-sStart
                if diff > ran:
                    seedMap.append((sStart+ran,diff-ran))
                    nextMap.append((dStart,ran))
                else:
                    nextMap.append((dStart,diff))
                    
                ran2 = sStart-source
        if not found:
            nextMap.append((source,ran2))
    seedMap = nextMap

minimum = 922337203685477580
for x, y in seedMap:
    minimum = min(minimum,x)
print(minimum)
