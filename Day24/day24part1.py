import numpy as np
INPUT_FILE = "Day24/day24input.txt"

class Vector():

    def __init__(self,line: str) -> None:
        self.line = line.replace("\n","")
        nums = line.replace("\n","").replace("@",",").replace(" ","").split(",")
        self.x,self.y,self.z,self.dx,self.dy,self.dz = [int(x) for x in nums]
        pass

    #This returns None if the intersection does not exist.
    #Otherwise it returns the point of intersection.
    def get2Dintersection(self,other):
        denominator = (self.dx * other.dy - other.dx * self.dy)
        if denominator == 0:
            return None
        t = (other.dy * (other.x - self.x) - other.dx * (other.y - self.y)) / denominator
        return (self.x + self.dx * t, self.y + self.dy * t)
    
    def isFuture(self,point):
        return  ((self.dx >=0 and self.x <= point[0]) or (self.dx <=0 and self.x >= point[0])) and \
            ((self.dy >=0 and self.y <= point[1]) or (self.dy <=0 and self.y >= point[1]))
    
    def __str__(self) -> str:
        return self.line

def attempt1():
    f = open(INPUT_FILE)
    lines = f.readlines()
    vectors = [Vector(line) for line in lines]

    LOWER, UPPER = 200000000000000, 400000000000000

    total = 0
    for i, current in enumerate(vectors):
        for other in vectors[i+1:]:
            print(f"Checking {current} and {other}")
            intersection = current.get2Dintersection(other)
            print("\t",intersection)

            if intersection is None:
                print("\tNot Added (Never collides)")
                continue


            if intersection[0] >= LOWER and intersection[0] <= UPPER and \
                intersection[1] >= LOWER and intersection[1] <= UPPER:

                if current.isFuture(intersection) and other.isFuture(intersection):
                    total += 1
                    print("\tAdded")
                else:
                    print("\tNot Added (In past)")
                    pass
            else:
                print("\tNot Added (Out of bounds)")
                pass
    
    print(total)


def main():
    attempt1()

main()