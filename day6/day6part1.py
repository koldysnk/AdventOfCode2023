INPUT_FILE = "Day6/day6input.txt"

f = open(INPUT_FILE, "r")

#Parsed file by hand
times = [55,     82,     64,     90]
records = [246,   1441,   1012,   1111]

total = 1

for i in range(len(times)):
    time = times[i]
    record = records[i]
    current = 0
    for x in range(time):
        distance = x*(time-x)
        if distance > record:
            current += 1

    total *= current

print(total)
