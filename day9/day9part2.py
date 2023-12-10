INPUT_FILE = "Day9/day9input.txt"
f = open(INPUT_FILE,"r")

line = f.readline()

total = 0

while line:
    values = [int(x) for x in line.split(" ")]
    values.reverse()
    lasts = []
    while len(set(values)) > 1:
        i = 0
        while i <len(values)-1:
            values[i] = values[i]-values[i+1]
            i+=1
        lasts.append(values.pop())
    lasts.append(values[-1])
    while len(lasts) >1:
        lasts[-1] = lasts[-2]-lasts.pop()
    total += lasts[-1]
    line = f.readline()

print(total)
