INPUT_FILE = "Day13/day13input.txt"

f = open(INPUT_FILE,"r")

line = f.readline()

all_lines = []
current = []
total = 0
while line:
    if len(line)>1:
        current.append(list(line.replace("\n","")))
    else:
        mirror = False
        i = 0
        while i<len(current)-1:
            mini_mirror = False
            end = 0
            if i == 0 and current[i] == current[i+i]:
                mini_mirror = True
                end = i+i
            elif (len(current)-i)%2 == 0  and current[i] == current[-1]:
                mini_mirror = True
                end = len(current)-1
            for j in range(1,end-(i+1)):
                if current[i+j] != current[end-j]:
                    mini_mirror = False

            if mini_mirror:
                total+= 100*(i+(end-i)/2)


            i+=1


        all_lines.append(current)
        current = []
    line = f.readline()
