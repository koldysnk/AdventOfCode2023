import re
INPUT_FILE = "Day12/day12input.txt"

f = open(INPUT_FILE,"r")

line = f.readline()
total = 0
row = 1
while line:

    print(row,total)
    row+=1
    guide = line.replace("\n","").split(" ")
    og_guide = guide[0]
    gears = [guide[0]]
    nums = guide[1].split(",")
    og_nums = guide[1].split(",")
    
    potentials = []
    for i in range(4):
        gears[0]+="?"+og_guide
        nums.extend(og_nums)
    p = "\.*#{"+"}\.+#{".join(nums)+"}\.*"
    pattern = re.compile(p)

    p2 = "(\.|\?)*(#|\?){"+"}(\.|\?)+(#|\?){".join(nums)+"}(\.|\?)*"
    partial_pattern = re.compile(p2)

    while len(gears)>0:
        current = gears.pop()
        
        if "?" in current:
            a = current.replace("?",".",1)
            b = current.replace("?","#",1)
            if partial_pattern.fullmatch(a):
                gears.append(a)
            if partial_pattern.fullmatch(b):
                gears.append(b)
        else:

            match = pattern.fullmatch(current)
                
            '''
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
            '''
            if match:
                total += 1
            #    print(f"{current} matches {nums} total {total}")
            #else:
            #    print(f"{current} does not match {nums} total {total}")

    #print("\n\n")
    line = f.readline()

print(total)

#This attempt is too slow. Try by building up from the bottom.
#For example, before adding a new potential gear set, check if 
# it matches the guide up to that point

'''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''
