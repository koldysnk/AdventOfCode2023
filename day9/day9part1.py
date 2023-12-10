INPUT_FILE = "Day9/day9input.txt"
f = open(INPUT_FILE,"r")

line = f.readline()

total = 0

while line:
    values = [int(x) for x in line.split(" ")]
    lasts = []
    while len(set(values)) > 1:
        i = 0
        while i <len(values)-1:
            values[i] = values[i+1]-values[i]
            i+=1
        lasts.append(values.pop())
    total+=sum(lasts)+values[-1]
    line = f.readline()
print(total)
