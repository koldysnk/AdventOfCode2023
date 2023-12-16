INPUT_FILE = "Day1/day1input.txt"

def attempt1():
  total = 0 
  f = open(INPUT_FILE,"r")
  line = f.readline()
  while line:
    a = -1
    b = 0
    for i in line:
      if i.isdigit() and a == -1:
        a = i
        b = i
      elif i.isdigit():
        b = i
    total += int(a+b)
    line = f.readline()
  print(total)
  return total

def main():
  attempt1()

main()
