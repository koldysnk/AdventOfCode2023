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
while line and not workflows_ingested:
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
    

    line = f.readline()

#once all the workflows are added. Put 1 in as a group. 

print(total)
