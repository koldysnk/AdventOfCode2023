X, Y, Z = 0, 1, 2

class Brick():
    
    
    
    def __init__(self,input:str,name) -> None:
        input = input.replace("\n","")
        self.origin = input
        self.name = name
        coords = input.split("~")
        self.startCoord = [int(x) for x in coords[0].split(",")]
        self.endCoord = [int(x)+1 for x in coords[1].split(",")]
        self.volume = abs(self.endCoord[X]-self.startCoord[X]) * abs(self.endCoord[Y]-self.startCoord[Y]) * abs(self.endCoord[Z]-self.startCoord[Z])
        self.shadow = set()
        self.zone = set()
        self.on = set()
        self.under = set()
        pass

    def __lt__(self,other):
        return self.startCoord[Z] < other.startCoord[Z]
    
    def settled(self):
        settled = False
        for brick in self.shadow:
            if brick.endCoord[Z] == self.startCoord[Z]:
                self.on.add(brick)
                brick.under.add(self)
                settled = True
        return settled


    #returns whether or not the brick moved
    #Moves the brick down until it colides with the foor or another brick
    def fall(self):
        moved = False
        while self.startCoord[Z]>0 and not self.settled():
            self.endCoord[Z] -=1
            self.startCoord[Z] -= 1
            moved = True
        return moved
        
    def __str__(self):
        return f"{self.name}: {self.startCoord} -> {self.endCoord}"

    #Finds the bricks under and above it
    def displaySupport(self):
        print("#####")
        print("Name: ", str(self))
        print("Supporting:")
        for brick in self.under:
            print(brick)
        print("Supported by:")
        for brick in self.on:
            print(brick)
        pass

    def inZone(self,brick):
        if self.endCoord[X]<=brick.startCoord[X] or brick.endCoord[X]<=self.startCoord[X]:
            return False
        if self.endCoord[Y]<=brick.startCoord[Y] or brick.endCoord[Y]<=self.startCoord[Y]:
            return False
        self.zone.add(brick)
        brick.zone.add(self)
        #print(self,"overlaps",brick)
        return True
    
    def inShadow(self,brick):
        if self.inZone(brick) and brick.__lt__(self):
            self.shadow.add(brick)
            return True
        return False

    #Sets the bricks that are in is shadow from the list
    def setShadow(self,bricks):
        for brick in bricks:
            self.inShadow(brick)


def main():
    INPUT_FILE = "Day22/day22input.txt"

    f = open(INPUT_FILE,"r")
    lines = f.readlines()

    bricks = [Brick(line,i) for i, line in enumerate(lines)]
    bricks.sort()

    for i, brick in enumerate(bricks):
        brick.setShadow(bricks[:i])
        #Loop through all the bricks until none of them are falling.
        brick.fall()


    #Loop through all the bricks to determine what they are supporting
    count = 0
    for brick in bricks:
        removable = True
        for b in brick.under:
            if len(b.on)==1:
                removable = False
        if removable:
            count += 1

    print(count)

main()