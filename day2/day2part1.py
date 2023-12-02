import time
INPUT_FILE = "Day2/day2input.txt"

KEY = {
    "red": 12,
    "green": 13,
    "blue": 14
}


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
        for game in games:
            pulls = game.strip().split(",")
            for pull in pulls:
                temp = pull.split()
                num = temp[0]
                color = temp[1]
                if color not in KEY or KEY[color] < int(num):
                    successful = False
        line = f.readline()
        if successful:
            total += int(ids)
    print(total)
    return total

#About twice as fast
def attempt2():
    f = open(INPUT_FILE,"r")
    total = 0
    line = f.read()
    line = line.replace('\n'," ").replace(",","").replace(";",'').replace(":","").split()
    game_id = 0
    success = True
    i = 0
    while i < len(line):
        if line[i] == "Game":
            if success:
                total += game_id
            success = True
            game_id = int(line[i+1])
        else:
            color = line[i+1]
            num = line[i]
            if KEY[color] < int(num):
                success = False
        i += 2
            

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
