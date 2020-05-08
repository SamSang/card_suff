"""
Just messing around with classes
by building a deck of cards
"""
import random
from itertools import combinations

suits = ["spade", "heart", "diamond", "club"]
numbers = [
    {
        "name": "Ace",
        "number": "A",
        "point": 1,
        "seq": 1,
    },
    {
        "name": "King",
        "number": "K",
        "point": 10,
        "seq": 13,
    },
    {
        "name": "Queen",
        "number": "Q",
        "point": 10,
        "seq": 12,
    },
    {
        "name": "Jack",
        "number": "J",
        "point": 10,
        "seq": 11,
    },
    {
        "name": "Ten",
        "number": "10",
        "point": 10,
        "seq": 10,
    },
    {
        "name": "Nine",
        "number": "9",
        "point": 9,
        "seq": 9,
    },
    {
        "name": "Eight",
        "number": "8",
        "point": 8,
        "seq": 8,
    },
    {
        "name": "Seven",
        "number": "7",
        "point": 7,
        "seq": 7,
    },
    {
        "name": "Six",
        "number": "6",
        "point": 6,
        "seq": 6,
    },
    {
        "name": "Five",
        "number": "5",
        "point": 5,
        "seq": 5,
    },
    {
        "name": "Four",
        "number": "4",
        "point": 4,
        "seq": 4,
    },
    {
        "name": "Three",
        "number": "3",
        "point": 3,
        "seq": 3,
    },
    {
        "name": "Two",
        "number": "2",
        "point": 2,
        "seq": 2,
    },
]

class Card():
    def __init__(self, suit, name, number, point, seq):
        self.suit = suit
        self.name = name
        self.number = number
        self.point = point
        self.seq = seq
    #full_name = 
    def fullName(self):
        return "{} of {}s".format(self.name, self.suit)
    def shortName(self):
        smallSuit = name[0]
        return "{number} {suit}".format(number=number, suit=smallSuit)

def cribbage_points(hand):
    """
    TODO Add cut parameter, append cut to hand
    TODO Jack in the suit
    TODO Flush including the cut
    """
    score = 0
    #print("Check for jack in the suit")
    print("Check for a flush")
    # I'm implementing for the full hand,
    # but it also needs to check the cut in the future
    suits = []
    for card in hand:
        suits.append(card.suit)
    #print(suits)
    suit = set(suits)
    #print(suit)
    if len(suit) == 1:
        print(f"A flush of {list(suit)[0]}s")
        score = score + len(hand)
    # if the cut matches the suit, an extra point

    print("Compute the pairs")
    # have to loop through all of the possible combinations of two cards
    # rewrite using combination([], 2)
    for card in hand:
        #print("holding {}".format(card.fullName()))
        index = hand.index(card) + 1
        while index < len(hand):
            #print("looking at {}".format(hand[index].name))
            if card.name == hand[index].name:
                score = score + 2
                print("Pair!")
            index = index + 1
    print("Compute the 15s")
    # look at all combinations of cards and see if the sum of their numbers is 15
    for i in range(len(hand)+1):
        comb = combinations(hand, i)
        for fifteen in comb:
            total = 0
            # I suspect there's a way to do this without a loop
            for card in fifteen:
                total = total + card.point
            if total == 15:
                print("Fifteen two!")
                score = score + 2
    print("Compute the runs")
    # look at all non-overlapping combinations of cards

    # look for sequence n, can only have n - len() + 1 sequences, points of n
    # start with len(), through len() - 3, step of -1

    for i in range(len(hand), len(hand) - 3, -1):
        #print(f"Runs of {str(i)}?")
        comb = combinations(hand, i)
        runs = []
        for run in comb:
            numbers = []
            for card in run:
                numbers.append(card.seq)
            numbers.sort()
            #print(numbers)
            consecutive = 0
            for j in range(len(numbers) - 1):
                diff = numbers[j+1] - numbers[j]
                #print(f"{str(diff)}")
                if diff == 1:
                    consecutive = consecutive + 1
            #print(f"does {consecutive + 1} equal {len(numbers)}?")
            # this handles runs, but what about if there are aces?
            # if there are len() -1 matches and the first card is an ace and the last is a 13, then yes
            if len(numbers) == consecutive + 1:
                print("Run of {}".format(str(len(numbers))))
                #print(numbers)
                runs.append(numbers)
            #print(f"is the first card {str(numbers[0])} an ace?")
            #print(f"is the last card {str(numbers[i-1])} a king ace?")
            if len(numbers) ==  consecutive + 2 and numbers[0] == 1 and numbers[i-1] == 13:
                print("Run of {} with an ace!".format(str(len(numbers))))
                print(numbers)
                runs.append(numbers)
        if runs:
            #print("Count points of runs")
            for run in runs:
                score = score + len(run)
            #print("need to stop counting runs")
            break
    return score
def draw_hand(deck, handsize):
    hand = []
    while len(hand) < handsize:
        hand.append(deck.pop(0))
    return hand
def make_deck():
    cards = []
    for suit in suits:
        for number in numbers:
            number["suit"] = suit
            card = Card(**number)
            cards.append(card)
    #for card in cards:
    #    print(card.fullName())
    return cards

deck = make_deck()
#print(deck)
random.shuffle(deck)
print("deck shuffled")
#for card in cards:
#    print(card.fullName())
hand = []
handsize = 5
#hand = draw_hand(deck, handsize)
hand = [
    Card(suit="spade", name="king", number="K", point=10, seq=13),
    Card(suit="spade", name="queen", number="Q", point=10, seq=12),
    Card(suit="spade", name="jack", number="J", point=10, seq=11),
    Card(suit="spade", name="ten", number="10", point=10, seq=10),
    Card(suit="spade", name="ace", number="A", point=1, seq=1),
]
for card in hand:
    print(card.fullName())
score = cribbage_points(hand)
print(str(score))