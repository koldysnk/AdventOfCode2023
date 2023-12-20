def cutDown(current,letter,val,dest):
    if current[letter+"_end"]<val:
        current["step"] = dest
        return [current]
    elif current[letter+"_start"]>=val :
        return [current]
    else:
        a = dict(current)
        b = dict(current)
        a[letter+"_start"] = val
        b[letter+"_end"] = val-1
        b["step"] = dest
        return [a,b]
    
def cutUp(current,letter,val,dest):
    if current[letter+"_start"]>val:
        current["step"] = dest
        return [current]
    elif current[letter+"_end"]<val :
        return [current]
    else:
        a = dict(current)
        b = dict(current)
        a[letter+"_end"] = val
        b[letter+"_start"] = val+1
        b["step"] = dest
        return [a,b]

def noCut(current, dest):
    current["step"] = dest
    return [current]

def buildSplit(eval,dest):
    if eval == "auto":
        return lambda current: noCut(current, dest)
    elif "<" in eval:
        letter = eval[0]
        return lambda current: cutDown(current, letter, int(eval[2:]),dest)
    elif ">" in eval:
        letter = eval[0]
        return lambda current: cutUp(current, letter, int(eval[2:]),dest)
    
def countCombos(current):
    return (current["x_end"] - current["x_start"]+1) * (current["m_end"] - current["m_start"]+1) * (current["a_end"] - current["a_start"]+1) * (current["s_end"] - current["s_start"]+1)

INPUT_FILE = "DAY19/day19input.txt"

f = open(INPUT_FILE,"r")

workflows = {}

line = f.readline()

workflows_ingested = False
total = 0
while line and not workflows_ingested:
    if line == "\n":
        workflows_ingested = True
    elif not workflows_ingested:
        name = line[:line.find("{")]
        parts = []
        for x in line[line.find("{")+1:line.find("}")].split(","):
            if ":" in x:
                sections = x.split(":")
                parts.append({"og":x,"eval":buildSplit(sections[0],sections[1]),"dest":sections[1]})
            else:
                parts.append({"og":x,"eval":buildSplit("auto",x),"dest":x})
        workflows[name] = parts
    

    line = f.readline()

#once all the workflows are added. Put 1 in as a group. 
current = {"x_start":1,"x_end":4000,"m_start":1,"m_end":4000,"a_start":1,"a_end":4000,"s_start":1,"s_end":4000,"step":"in"}

items = [current]

while len(items)> 0:
    item = items.pop()
    print(item)
    queue = workflows[item["step"]]
    print(item["step"])
    i = 0
    current = item
    while len(queue)>0:
        task = queue.pop(0)
        dest = current["step"]
        splits = task["eval"](current)
        for current in reversed(splits):
            print(current)
            print(current["step"])
            if current["step"] == "R":
                pass
            elif current["step"] == "A":
                total += countCombos(current)
            elif dest != current["step"]:
                items.append(current)


print(total)
