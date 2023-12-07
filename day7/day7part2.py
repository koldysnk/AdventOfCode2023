INPUT_FILE = "Day7/day7input.txt"

f = open(INPUT_FILE,"r")

line = f.readline()
hands = []

CARD_ORDER=["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
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

def sortHands(hands):
    swaped = True
    while swaped:
        swaped = False
        for i in range(len(hands)-1):
            a, b = hands[i], hands[i+1]
            if compareHands(a,b)>0:
                hands[i] = b
                hands[i+1] = a
                swaped = True
            
    return hands

def formatHand(cards, bet):
    og = [x for x in cards]
    m1 = [0,"A"]
    m2 = [0,"A"]
    for c in set(og):
        c2 = cards.count(c)
        if c != "J":
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
    cards = [m1[1] if x=="J"else x for x in cards]
    cards = sortByOrder(cards)
    cc = len(set(cards))
    hand = {
        "OG":og,
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
    }
    score = 7*OFFSET if hand["5oK"] == True else OFFSET
    score = 6*OFFSET if hand["4oK"] == True else score
    score = 5*OFFSET if hand["FH"] == True else score
    score = 4*OFFSET if hand["3oK"] == True else score
    score = 3*OFFSET if hand["2P"] == True else score
    score = 2*OFFSET if hand["1P"] == True else score

    i=1
    for card in og:
        score += i*CARD_ORDER.index(card)
        i*=100
    hand["score"] = score

    
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
    #print(h1,h2)
    return 0

def formatHandWithJ(cards, bet):
    if "J" not in cards:
        return formatHand(cards,cards,bet)
    if cards.count("J") == 5:
        return formatHand(["A","A","A","A","A"],cards,bet)
    hands = [formatHand(cards,cards,bet)]
    current = list(cards)
    isJ = [x=="J" for x in current]
    if len(set(current)) == 2:
        for c in cards:
            if c != "J":
                return formatHand([c,c,c,c,c],cards,bet)

    while True in isJ:
        index = isJ.index(True)
        next_hands = []
        for hand in hands:
            potentials = set(hand["RJ"])
            if "J" in potentials:
                potentials.remove("J")
            potentials.add("A")
            for c in potentials:
                current = [x for x in hand["RJ"]]
                current[index] = c
                next_hands.append(formatHand(current,cards,bet))
        hands.extend(next_hands)
        isJ[index] = False

    '''
    for i in range(current.count("J")):
        index = isJ.index(True)
        for current2 in hands:
            next_hands = []
            for c in CARD_ORDER[1:]:
                c3 = [x for x in current2["OG"]]
                c3[index] = c
                next_hands.append(formatHand(c3,bet))
        hands.extend(next_hands)
        isJ[index]=False
    '''
    hands2 = [x["OG"] for x in hands]
    hands = sortHands(hands)
    result = hands[-1]
    return result

'''
def formatHandWithJ(cards, bet):
    if "J" not in cards:
        return formatHand(list(cards),bet)
    if cards.count("J") == 5:
        return formatHand(list(["A","A","A","A","A"]),bet)
    hands = [formatHand(list(cards),bet)]
    for i in range(len(cards)):
        if cards[i] == "J":
            for c in CARD_ORDER[1:]:
                og = [x for x in cards]
                og[i] = c
                hands.append(formatHandWithJ(og, bet))
    
    hands2 = [x["OG"] for x in hands]
    hands = sortHands(hands)
    return hands[-1]
'''

z=0
while line:
    #add to list of hands in order
    hand = line.replace("\n","").split(" ")
    cards = hand[0]
    bet = hand[1]
    hand=formatHand(list(cards),int(bet))
    
    if cards.find("J") >=0:
        print(f"{cards}->{hand['OG']}")
        z+=1
        print(z)
        pass
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

#Too high 243852021 but sample is right
#Incorrect 243662438
#Too low 242906697 but sample is right

