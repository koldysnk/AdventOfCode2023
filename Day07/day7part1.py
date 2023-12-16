INPUT_FILE = "Day7/day7input.txt"

f = open(INPUT_FILE,"r")

line = f.readline()
hands = []

CARD_ORDER=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
OFFSET = 1000000000000
def sortByOrder(cards):
    swaped = True
    while swaped:
        swaped = False
        for i in range(len(cards)-1):
            a, b = cards[i], cards[i+1]
            ai, bi = CARD_ORDER.index(a), CARD_ORDER.index(b)
            if bi < ai:
                cards[i] = b
                cards[i+1] = a
                swaped = True
            
    return cards

def formatHand(cards, bet):
    og = [x for x in cards]
    cards = sortByOrder(cards)
    cc = len(set(cards))
    hand = {
        "bet":bet,
        "5oK":cc == 1,
        "4oK":cc == 2 and (cards[0]==cards[3] or cards[1]==cards[4]),
        "FH":cc == 2 and cards[0]!=cards[3] and cards[1]!=cards[4],
        "3oK":cc == 3 and (cards[0]==cards[2] or cards[1]==cards[3] or cards[2]==cards[4]),
        "2P":cc == 3 and cards[0]!=cards[2] and cards[1]!=cards[3] and cards[2]!=cards[4],
        "1P":cc == 4,
        "HC":cards[-1],
        "cards":cards,
        "M1":"A",
        "M2":"A",
        "OG":og
    }
    score = 7*OFFSET if hand["5oK"] == True else OFFSET
    score = 6*OFFSET if hand["4oK"] == True else score
    score = 5*OFFSET if hand["FH"] == True else score
    score = 4*OFFSET if hand["3oK"] == True else score
    score = 3*OFFSET if hand["2P"] == True else score
    score = 2*OFFSET if hand["1P"] == True else score

    i=1
    for card in cards:
        score += i*CARD_ORDER.index(card)
        i*=100
    hand["score"] = score

    m1 = [0,"A"]
    m2 = [0,"A"]
    for c in set(cards):
        c2 = cards.count(c)
        if c2 > 1:
            if c2 > m1[0]:
                m2 = m1
                m1 = [c2,c]
            elif c2 == m1[0]:
                if CARD_ORDER.index(c)>CARD_ORDER.index(m1[1]):
                    m2 = m1
                    m1 = [c2,c]
                else:
                    m2 = [c2,c]
            elif c2 > m2[0]:
                m2 = [c2,c]
    hand["M1"] = m1[1]
    hand["M2"] = m2[1]

    '''
    hand["4oK"] = not hand["5oK"] and (cards[0]==cards[3] or cards[1]==cards[4])
    hand["FH"] = not hand["5oK"] and cards[0]==cards[1] and cards[2]==cards[4]
    hand["3oK"] = not hand["5oK"] and not hand["4oK"] and (cards[0]==cards[2] or cards[1]==cards[3] or cards[1]==cards[3])
    '''
    return hand

def compareHands(h1,h2):
    s1 = h1["score"]
    so1 = s1//OFFSET
    s2 = h2["score"]
    so2 = s2//OFFSET
    if so1==so2:
        for i in range(len(h1["OG"])):
            if CARD_ORDER.index(h1["OG"][i]) > CARD_ORDER.index(h2["OG"][i]):
                return 1
            if CARD_ORDER.index(h1["OG"][i]) < CARD_ORDER.index(h2["OG"][i]):
                return -1
            
    if s1>s2:
        return 1
    if s1<s2:
        return -1
    print(h1,h2)
    return 0

while line:
    #add to list of hands in order
    hand = line.replace("\n","").split(" ")
    cards = hand[0]
    bet = hand[1]
    hand=formatHand(list(cards),int(bet))

    placed = False
    i = 0
    while not placed:
        if i ==len(hands):
            placed = True
            hands.append(hand)
        else:
            h2 = hands[i]
            c = compareHands(hand, h2)
            if c <= 0:
                placed = True
                hands.insert(i,hand)
            else:
                i += 1



    line = f.readline()
hands2 = [x["OG"] for x in hands]
hands3 = hands2[300:]
hands4 = hands2[600:]
hands5 = hands2[900:]
total = 0
for i in range(len(hands)):
    total+= hands[i]["bet"]*(i+1)
print(total)

#Too high 241458577 but sample is right
#Too high 241445761
#Stuck because array copy
