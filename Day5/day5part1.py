INPUT_FILE = "Day5/day5input.txt"

f = open(INPUT_FILE,"r")

seeds = f.readline().replace("\n","").split(" ")[1:]

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

minimum = 922337203685477580

for seed in seeds:
    i=0
    source = int(seed)
    for transformation in transformations:
        found = False
        for mapping in transformation:
            sStart = int(mapping[1])
            dStart = int(mapping[0])
            ran = int(mapping[2])
            if source >= sStart and source < sStart + ran:
                source = dStart + source - sStart
                if i == len(transformations)-1:
                    minimum = min(minimum, source)
                found = True
                break
        if not found:
            if i == len(transformations)-1:
                    minimum = min(minimum, source)
        i+=1

print(minimum)
