def findFirst(s,v):
  a = s.find(v)
  if a == -1:
    return 9999999999
  return a

def attempt1():
  total = 0
  f = open("day1input.txt","r")
  line = f.readline()
  while line:
    aList = [
      min(findFirst(line,"1"),findFirst(line,"one")),
      min(findFirst(line,"2"),findFirst(line,"two")),
      min(findFirst(line,"3"),findFirst(line,"three")),
      min(findFirst(line,"4"),findFirst(line,"four")),
      min(findFirst(line,"5"),findFirst(line,"five")),
      min(findFirst(line,"6"),findFirst(line,"six")),
      min(findFirst(line,"7"),findFirst(line,"seven")),
      min(findFirst(line,"8"),findFirst(line,"eight")),
      min(findFirst(line,"9"),findFirst(line,"nine"))
    ]
    a = aList.index(min(aList)) + 1
    bList = [
      max(line.rfind("1"),line.rfind("one")),
      max(line.rfind("2"),line.rfind("two")),
      max(line.rfind("3"),line.rfind("three")),
      max(line.rfind("4"),line.rfind("four")),
      max(line.rfind("5"),line.rfind("five")),
      max(line.rfind("6"),line.rfind("six")),
      max(line.rfind("7"),line.rfind("seven")),
      max(line.rfind("8"),line.rfind("eight")),
      max(line.rfind("9"),line.rfind("nine")),
    ]
    b = bList.index(max(bList)) + 1
    total += 10*a+b
    line = f.readline()

  print(total)
  return total

def main():
  attempt1()

main()
