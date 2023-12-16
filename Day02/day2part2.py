import time
INPUT_FILE = "Day2/day2input.txt"



def attempt1():
    f = open(INPUT_FILE,"r")
    total = 0
    line = f.readline()
    while line:
        line = line[5:]
        colon = line.find(":")
        ids = line[:colon]
        games = line[colon+1:].strip().split(";")
        successful = True
        maximum = {
            "red":0,
            "green":0,
            "blue":0
        }
        for game in games:
            pulls = game.strip().split(",")
            for pull in pulls:
                temp = pull.split()
                num = int(temp[0])
                color = temp[1]
                maximum[color] = max(maximum[color],num)
        line = f.readline()
        total += maximum["red"]*maximum["green"]*maximum["blue"]
    print(total)
    return total

#About twice as fast
def attempt2():
    f = open(INPUT_FILE,"r")
    total = 0
    line = f.read()
    line = line.replace('\n'," ").replace(",","").replace(";",'').replace(":","").split()
    i = 0
    current = {
        "red":0,
        "blue":0,
        "green":0
    }
    while i < len(line):
        if line[i] == "Game":
            total += current["red"]*current["blue"]*current["green"]
            
            current = {
                "red":0,
                "blue":0,
                "green":0
            }
        else:
            color = line[i+1]
            num = int(line[i])
            current[color] = max(num,current[color])
        i +=2
    total += current["red"]*current["blue"]*current["green"]
    print(total)
    return total


def main():
    tic = time.perf_counter()
    attempt1()
    toc = time.perf_counter()
    print(f"Attempt 1 took {toc-tic} seconds")
    tic = time.perf_counter()
    attempt2()
    toc = time.perf_counter()
    print(f"Attempt 2 took {toc-tic} seconds")


main()
