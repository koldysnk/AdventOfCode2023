def attempt1():
  total = 0 
  f = open("day1input.txt","r")
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
    line = f.readlin()
  print(total)
  return total

def main()
  attempt1()

main()
