
INPUT_FILE = "day2/day2input.txt"



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
        minimum = {
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
                minimum[color] = max(minimum[color],num)
        line = f.readline()
        total += minimum["red"]*minimum["green"]*minimum["blue"]
        print(total)
    print(total)
    return total


def main():
    attempt1()


main()
