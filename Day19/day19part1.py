def buildEval(eval):
    if eval == "auto":
        return lambda current: True
    elif "<" in eval:
        letter = eval[0]
        return lambda current: current[letter]<int(eval[2:])
    elif ">" in eval:
        letter = eval[0]
        return lambda current: current[letter]>int(eval[2:])

INPUT_FILE = "DAY19/day19input.txt"

f = open(INPUT_FILE,"r")

workflows = {}

line = f.readline()

workflows_ingested = False
total = 0
while line:
    if line == "\n":
        workflows_ingested = True
    elif not workflows_ingested:
        name = line[:line.find("{")]
        parts = []
        for x in line[line.find("{")+1:line.find("}")].split(","):
            if ":" in x:
                sections = x.split(":")
                parts.append({"og":x,"eval":buildEval(sections[0]),"dest":sections[1]})
            else:
                parts.append({"og":x,"eval":buildEval("auto"),"dest":x})
        workflows[name] = parts
    else:
        current = {}
        vals = line[1:line.find("}")].split(",")
        for val in vals:
            current[val[:val.find("=")]] = int(val[val.find("=")+1:])
        
        print(current)
        queue = workflows["in"]
        print("in")
        approved = False
        i = 0
        while True:
            task = queue[i]
            if task["eval"](current):
                print(task["dest"])
                if task["dest"] == "R":
                    break
                elif task["dest"] == "A":
                    total += current["x"] + current["m"] + current["a"] + current["s"]
                    break
                else:
                    queue = workflows[task["dest"]]
                    i = 0
            else:
                i+=1

    line = f.readline()

print(total)
