# initialize deck of 52 cards
#create method for deal, where you add two cards to player and to dealer
# Create methods for Hit (add card from deck to target hand)
# Create method for Stand (switch from player to dealer)
# Create gameplay loop that pulls all methods and starts the game, checks for inputs.
import random
deck = []
playerhand = []
dealerhand = []
suits = ["Diamonds","Hearts","Spades", "Clubs"]
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.name = ""
class GameplayLoop:
    def __init__(self):
        for suit in suits:
            for x in list(range(1,14)):
                deck.append(Card(suit,x))
        for card in deck:
            if card.value == 11:
                card.name = str("Jack of " + card.suit)
                card.value = 10
            elif card.value == 12:
                card.name = str("Queen of " + card.suit)
                card.value = 10
            elif card.value == 13:
                card.name = str("King of " + card.suit)
                card.value = 10
            elif card.value == 1:
                card.name = str("Ace of " + card.suit)
                card.value = 11
            else:
                card.name = str(str(card.value) + " of " + card.suit)
    def shuffle(self):
        random.shuffle(deck)
    
    def deal(self):
        playerhand.append(deck[0])
        del deck[0]
        playerhand.append(deck[0])
        del deck[0]
        dealerhand.append(deck[0])
        del deck[0]
        dealerhand.append(deck[0])
        del deck[0]
    
    def hit(self, target):
        if target == "p":
            playerhand.append(deck.pop())
        else:
            dealerhand.append(deck.pop())

    def checkvalue(self):
        sum = 0
        acecount = 0
        for card in playerhand:
            sum +=  card.value
            if card.value == 11:
                acecount += 1
        while sum > 21 and acecount > 0:
            for card in playerhand:
                if card.value == 11:
                    sum -= 10
                    acecount -= 1
                else:
                    pass
        return sum

    def checkdealer(self):
        dsum = 0
        acecount = 0
        for card in dealerhand:
            dsum += card.value
            if card.value ==1:
                acecount += 1
        while dsum > 21 and acecount > 0:
            for card in dealerhand:
                if card.value == 11:
                    dsum -= 10
                    acecount -= 1
                else:
                    pass
            break
        return dsum
    def gamestart(self):
        self.shuffle()
        self.deal()
        print("Your cards:")
        for card in playerhand:
            print(card.name)
        print("Dealer is showing:")
        print(dealerhand[0].name)
        while self.checkvalue() < 21:
            print("What's your Move? 'h' for hit, and 's' to stand.")
            myinput = input()
            if myinput == "hit" or myinput == "h": 
                self.hit("p")
                print("Your cards:")
                for card in playerhand:
                    print(card.name)

            elif myinput == "stand" or  myinput == "s":
                print("Dealer's Turn: ")
                while self.checkdealer() < 17:
                    self.hit("d")
                for card in dealerhand:
                        print(card.name)
                if self.checkdealer() > 21:
                    print("Dealer Busts, You Win!")
                elif self.checkdealer() == 21:
                    print("Dealer Blackjack, You Lose.")
                else:
                    if self.checkdealer() < self.checkvalue():
                        print("You Win")
                    elif self.checkdealer() == self.checkvalue():
                        print("The Game ends in a Draw, You and the Dealer both have " + str(self.checkvalue()))
                    else:
                        print("You Lose")
                break
            else:
                print("invalid input")
        if self.checkvalue() == 21:
            print("Blackjack! You won!")
        elif self.checkvalue() > 21:
            print("Bust, you lose.")
Mygame = GameplayLoop()
Mygame.gamestart()
