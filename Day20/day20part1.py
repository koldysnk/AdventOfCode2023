INPUT_FILE = "Day20/day20input.txt"
NO, LOW, HIGH = 0,1,2

class Broadcaster():
    def __init__(self, dest,name) -> None:
        self.dest = dest
        self.name = name

    def pulse(self,level,src):
        return [(d,level,self.name) for d in self.dest]

class FlipFlop():
    def __init__(self,dest,name) -> None:
        self.on = False
        self.dest = dest
        self.name = name

    def pulse(self,level,src):
        if level == HIGH:
            return []
        if level == LOW:
            temp = self.on
            self.on = not temp
            temp = LOW if temp else HIGH
            return [(d,temp,self.name) for d in self.dest]
        
class Conjunction():
    def __init__(self, dest, src,name) -> None:
        self.dest = dest
        self.name = name
        self.memory = {s:LOW for s in src}

    def pulse(self,level,src):
        self.memory[src] = level
        temp = HIGH if LOW in self.memory.values() else LOW
        return [(d,temp,self.name) for d in self.dest]
    

def attempt1():
    f = open(INPUT_FILE)
    line = f.readline()

    setup = []
    components = {}

    sources = {}
    while line:
        parts = line.replace(" ","").replace("\n","").split("->")
        src = parts[0]
        if src.startswith("b"):
            kind = "*"
        else:
            kind = src[0]
            src = src[1:]
        dests = parts[1].split(",")
        for d in dests:
            if d not in sources:
                sources[d] =[src]
            else:
                sources[d].append(src)
        
        setup.append((kind,src,dests))

        line = f.readline()

    for c in setup:
        kind, name, dest = c
        if kind == "*":
            components[name] = Broadcaster(dest,name)
        elif kind == "%":
            components[name] = FlipFlop(dest,name)
        elif kind == "&":
            components[name] = Conjunction(dest,sources[name],name)
        

    presses = 1000
    count = [0,0,0]

    for i in range(presses):
        queue = [("broadcaster",LOW,"button")]
    
        while len(queue) > 0:
            name, level,src = queue.pop(0)
            #print(name, level)
            count[level] += 1

            if name in components:
                results = components[name].pulse(level,src)
                queue.extend(results)

    print(count[1]*count[2])
    print(count)


def main():
    attempt1()

main()
'''
button -low-> broadcaster
broadcaster -low-> a
broadcaster -low-> b
broadcaster -low-> c
a -high-> b
b -high-> c
c -high-> inv
inv -low-> a
a -low-> b
b -low-> c
c -low-> inv
inv -high-> a
'''