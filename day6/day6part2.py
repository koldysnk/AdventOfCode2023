import math
INPUT_FILE = "Day6/day6input.txt"

f = open(INPUT_FILE, "r")

#hand parsed
time = 55826490
record = 246144110121111
'''
This is just the quadratic formula
ax^2 + bx + c = 0
x = (-b +/- sqrt(b^2 - 4ac))/2a

record = x(time-x)
record = timex - x^2
x^2 - timex + record = 0
plug into formula
x = (-(-time) +/- sqrt((-time)^2 - 4record))/2
x = (time +/- sqrt(time^2 - 4record))/2

'''

start = (time - math.sqrt(time**2 - 4 * 246144110121111))//2
end = (time + math.sqrt(time**2 - 4 * 246144110121111))//2


print(start)
print(end)
total = end-start

print(int(total))
