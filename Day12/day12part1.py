INPUT_FILE = "Day12/day12input.txt"

f = open(INPUT_FILE,"r")

line = f.readline()
total = 0
row = 1
while line:

    print(row,total)
    row+=1
    guide = line.replace("\n","").split(" ")
    gears = [list(guide[0])]
    nums = guide[1].split(",")
    nums = [int(x) for x in nums]

    while len(gears)>0:
        current = gears.pop()
        
        if "?" in current:
            a = [x for x in current]
            b = [x for x in current]
            a[current.index("?")] = "."
            b[current.index("?")] = "#"
            gears.append(a)
            gears.append(b)
        else:
            #if total ==13:
                #print("bad")
            match = True
            sections = 0
            i = 0
            while match and i < len(current):
                gear = current[i]
                if gear == "#":
                    if sections >= len(nums):
                        match = False
                    else:
                        section = current[i:i+nums[sections]]

                        match = "." not in section
                        if len(section)!=nums[sections] or (i+nums[sections] < len(current) and current[i+nums[sections]]=="#"):
                            match = False
                        i += nums[sections]+1
                        sections +=1
                else:
                    i+=1

            if match and sections == len(nums):
                total += 1
                #print(f"{current} matches {nums} total {total}")
            #else:
                #print(f"{current} does not match {nums} total {total}")

    #print("\n\n")
    line = f.readline()

print(total)

#12097 is wrong
