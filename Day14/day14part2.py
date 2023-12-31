INPUT_FILE = "Day14/day14input.txt"

f = open(INPUT_FILE,"r")

grid = [[x for x in list(line.replace("\n",""))] for line in f.readlines()]

total = 0
cycles = 1000000000
pattern = [str(grid)]
totals = [0]
pattern_started = False
pattern_pos = 0
pattern_start_pos = 0
i = 0
while len(pattern)<cycles:

    #Shift North
    for og_x in range(len(grid)):
        for y in range(len(grid[og_x])):
            x = og_x
            spot = grid[x][y]
            movable = spot=="O"

            while movable:
                if x>0 and grid[x-1][y] == ".":
                    grid[x][y] = "."
                    x -= 1
                    grid[x][y] = "O"
                else:
                    movable = False
                    #total += len(grid)-x
    #Shift West
    for og_x in range(len(grid)):
        for y in range(len(grid[og_x])):
            x = og_x
            spot = grid[x][y]
            movable = spot=="O"
    
            while movable:
                if y>0 and grid[x][y-1] == ".":
                    grid[x][y] = "."
                    y -= 1
                    grid[x][y] = "O"
                else:
                    movable = False
                    #total += len(grid)-x
    #Shift South
    for og_x in range(len(grid)-1,-1,-1):
        for y in range(len(grid[og_x])):
            x = og_x
            spot = grid[x][y]
            movable = spot=="O"
    
            while movable:
                if x<len(grid)-1 and grid[x+1][y] == ".":
                    grid[x][y] = "."
                    x += 1
                    grid[x][y] = "O"
                else:
                    movable = False
                    #total += len(grid)-x
    #Shift East
    for og_x in range(len(grid)):
        for y in range(len(grid[og_x])-1,-1,-1):
            x = og_x
            spot = grid[x][y]
            movable = spot=="O"
    
            while movable:
                if y<len(grid[x])-1 and grid[x][y+1] == ".":
                    grid[x][y] = "."
                    y += 1
                    grid[x][y] = "O"
                else:
                    movable = False
                    total += len(grid)-x

    new_str = str(grid)
    if new_str in pattern:
        ind = pattern.index(new_str)
        print("repeat for ",i," found at ",ind,total)
        #print(totals)
        pos = (cycles-i+1)%(i-ind)+ind+1
        guess = totals[pos]
        print("guess is: ",guess)
        break
    else:
        pattern.append(new_str)
        totals.append(total)
    
    '''
    if pattern_started:
        if pattern_pos < len(pattern)-1 and pattern[pattern_pos+1] == total:
            pattern_pos +=1
            print(f"{i}: {total} pattern continued")
            if (cycles-pattern_start_pos)%(pattern_pos-pattern_start_pos):
                print(f"{i}: {total} might be a winner")
                break
        elif pattern[pattern_start_pos] == total:
            print(f"{i}: {total} pattern looped")
        else:
            pattern.extend(pattern[pattern_start_pos:pattern_pos+1])
            pattern.append(total)
            print(f"{i}: {total} pattern ended")
            pattern_started = False
    else:
        if total in pattern:
            pattern_pos = pattern.index(total)
            pattern_start_pos = pattern_pos
            pattern_started = True
            print(f"{i}: {total} pattern started")
        else:
            pattern.append(total)
            print(f"{i}: {total} pattern not started")
    '''
        


    total = 0
    i+=1



#Finishes