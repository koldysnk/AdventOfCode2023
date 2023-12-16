import time
import math
INPUT_FILE = "Day8/day8input.txt"

def attempt1():
    f = open(INPUT_FILE,"r")

    instructions = f.readline().replace("\n","")
    f.readline()
    line = f.readlines()
    current = []
    path = {}
    for x in line:
        temp = x.replace("(","").replace(",","").replace(")","").replace("\n","").split(" ")
        path[temp[0]] = {"L":temp[2], "R":temp[3]}
        if temp[0].endswith("A"):
            current.append(temp[0])
    #print(path)
    print(len(current))
    
    end_pos = []

    for spot in [x for x in current]:
        count = 0
        pos = 0
        x = spot
        while not x.endswith("Z"):
            direction = instructions[pos]
            x = path[x][direction]
            count+=1
            pos = pos+1 if pos<len(instructions)-1 else 0
        current.remove(spot)
        end_pos.append(count)
        print(f"{len(end_pos)} - {x} - {count}")

    print(end_pos)
    print(current)

    total = 1

    for x in end_pos:
        total = math.lcm(total,x)
    print(total)

def main():
    tic = time.perf_counter()
    attempt1()
    toc = time.perf_counter()
    print(f"Attempt 1 took {toc-tic} seconds")

main()
