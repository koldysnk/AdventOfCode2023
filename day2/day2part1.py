
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
                    print("fail")
                    successful = False
                else:
                    print("pass")
        line = f.readline()
        if successful:
            total += int(ids)
        print(total)
    print(total)
    return total


def main():
    attempt1()


main()
