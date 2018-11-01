import random

class Card:

    rank_dict = {"A": 1, "J": 11, "Q": 12, "K": 13}
    rank_dict2 = {1: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, rank = 0, suit = ""):
        if type(rank) == str:
            try:
                self.rank = Card.rank_dict[rank]
            except:
                self.rank = 0
        elif rank in range(1,14):
            self.rank = rank
        else:
            self.rank = 0
        if str(suit).lower() in {"h", "s", "d", "c"}:
            self.suit = suit.upper()
        else:
            self.suit = ""

    def __str__(self): 
        if self.is_blank():
            return "blk"
        elif self.rank in Card.rank_dict2:
            return "{:>3}".format(Card.rank_dict2[self.rank] + self.suit)
        else:
            return "{:>3}".format(str(self.rank) + self.suit)
            
    def is_blank(self):
        if self.rank == 0 and self.suit == "":
            return True
        return False

class Deck:

    def __init__(self):
        deck = []
        suits = ("S", "H", "D", "C")
        for i in range(1,14):
            for a_suit in suits:
                a_card = Card(i,a_suit)
                deck.append(a_card.__str__())
        self.deck = deck

    def __str__(self):
        deck_string = ""
        for k in range(4):
            for i in range(13):
                try:
                    deck_string  += self.deck[k*13+i] + " "
                except:
                    pass
            if deck_string != "":
                deck_string += "\n"
        return deck_string

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

class PlayingHand:
    
    NUMBER_CARDS = 13

    def __init__(self):
        self.hand = ["blk" for i in range(1,14)]

    def __str__(self):
        hand_string = ""
        for item in self.hand:
            hand_string += "{:>4}".format(item)
        return hand_string

    def add_card(self, card):
        for index,value in enumerate(self.hand):
            if value == "blk":
                self.hand[index] = card
                break

def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)
def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)
def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())
def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)
    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)

#The main program starts here
random.seed(10)
test_cards()
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
test_hands(deck)
print("The deck after dealing:")
print(deck)