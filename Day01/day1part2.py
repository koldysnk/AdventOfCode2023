import time
INPUT_FILE = "Day1/day1input.txt"


def findFirst(s, v):
  a = s.find(v)
  if a == -1:
    return 9999999999
  return a

# Very inefficient
def attempt1():
  total = 0
  f = open(INPUT_FILE, "r")
  line = f.readline()
  while line:
    aList = [
        min(findFirst(line, "1"), findFirst(line, "one")),
        min(findFirst(line, "2"), findFirst(line, "two")),
        min(findFirst(line, "3"), findFirst(line, "three")),
        min(findFirst(line, "4"), findFirst(line, "four")),
        min(findFirst(line, "5"), findFirst(line, "five")),
        min(findFirst(line, "6"), findFirst(line, "six")),
        min(findFirst(line, "7"), findFirst(line, "seven")),
        min(findFirst(line, "8"), findFirst(line, "eight")),
        min(findFirst(line, "9"), findFirst(line, "nine"))
    ]
    a = aList.index(min(aList)) + 1
    bList = [
        max(line.rfind("1"), line.rfind("one")),
        max(line.rfind("2"), line.rfind("two")),
        max(line.rfind("3"), line.rfind("three")),
        max(line.rfind("4"), line.rfind("four")),
        max(line.rfind("5"), line.rfind("five")),
        max(line.rfind("6"), line.rfind("six")),
        max(line.rfind("7"), line.rfind("seven")),
        max(line.rfind("8"), line.rfind("eight")),
        max(line.rfind("9"), line.rfind("nine")),
    ]
    b = bList.index(max(bList)) + 1
    total += 10*a+b
    line = f.readline()

  print(total)
  return total

#Not really any more efficient
def attempt2():
    total = 0
    f = open(INPUT_FILE, "r")
    line = f.readline()
    while line:
        l = len(line)
        i, a, b = 0, -1, -1
        while i < l and (a < 0 or b < 0):
            start = line[i:]
            end = line[:l-i]
            if a == -1:
                if start.startswith("1") or start.startswith("one"):
                    a = 1
                elif start.startswith("2") or start.startswith("two"):
                    a = 2
                elif start.startswith("3") or start.startswith("three"):
                    a = 3
                elif start.startswith("4") or start.startswith("four"):
                    a = 4
                elif start.startswith("5") or start.startswith("five"):
                    a = 5
                elif start.startswith("6") or start.startswith("six"):
                    a = 6
                elif start.startswith("7") or start.startswith("seven"):
                    a = 7
                elif start.startswith("8") or start.startswith("eight"):
                    a = 8
                elif start.startswith("9") or start.startswith("nine"):
                    a = 9
            if b == -1:
                if end.endswith("1") or end.endswith("one"):
                    b = 1
                elif end.endswith("2") or end.endswith("two"):
                    b = 2
                elif end.endswith("3") or end.endswith("three"):
                    b = 3
                elif end.endswith("4") or end.endswith("four"):
                    b = 4
                elif end.endswith("5") or end.endswith("five"):
                    b = 5
                elif end.endswith("6") or end.endswith("six"):
                    b = 6
                elif end.endswith("7") or end.endswith("seven"):
                    b = 7
                elif end.endswith("8") or end.endswith("eight"):
                    b = 8
                elif end.endswith("9") or end.endswith("nine"):
                    b = 9

            i += 1
        total += 10*a+b
        line = f.readline()
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
