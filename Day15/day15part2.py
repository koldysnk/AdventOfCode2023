INPUT_FILE = "Day15/day15input.txt"

f = open(INPUT_FILE,"r")
items = f.readline().replace("\n","").split(",")

total = 0
boxes = [[] for x in range(256)]


for item in items:
    current = 0
    label = ''
    for i in item:
        if i not in ["=","-"]:
            current += ord(i)
            current *= 17
            current = current%256
            label += i
        elif i == "-":
            for x in range(len(boxes[current])-1,-1,-1):
                if boxes[current][x]["label"] == label:
                    del boxes[current][x]
                    break
        else:
            lens = int(item[-1])
            replaced = False
            for i, thing in enumerate(boxes[current]):
                if label == thing["label"]:
                    thing["lens"] = lens
                    replaced = True
            if not replaced:
                boxes[current].append({"label":label,"lens":lens})
            break

for x, box in enumerate(boxes):
    for y, thing in enumerate(box):
        total += (x+1)*(y+1)*thing["lens"]

print(total)