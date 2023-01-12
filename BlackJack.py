## 1 player game of BlackJack against dealer ##
import random

class card:
    def __init__(self,name,suit):
        #Variables in each instance
        self.name = name
        self.suit = suit
        self.value = 0
        self.label = ""
        #get value of card
        self.getValue()


    def __str__(self):
        return(self.label)

    #method to get numerical value of the card instance
    def getValue(self):
        try:
            self.value = int(self.name)
            if self.value >=2 and self.value <=10:
                self.label = f"{self.name} of {self.suit}" # with score of {self.value}"
            else:
                self.label = "Incorrect Input, please input the correct card info"

        except:
            if self.name in "AJQKajqk":
                self.value = 10
                self.label = f"{self.name} of {self.suit}" # with score of {self.value}"
            else:
                self.label = "Incorrect Input, please input the correct card info"

class deck:

    def __init__(self):
        self.deckOfCards = []
        self.dealCard = []

        self.createDeck()
        self.shuffleDeck()

    #Used for testing - Temporary  Not sure the proper way of doing this. I created one return, but mainly used it for testing
    def __str__(self):
        return ', '.join(str(cards) for cards in self.deckOfCards)
        #return self.dealCard

    def createDeck(self):
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for s in suits:
            for n in names:
                test = card(n,s)
                self.deckOfCards.append(test)

    def shuffleDeck(self):
        random.shuffle(self.deckOfCards)

    #def dealingCard(self):
        #self.dealCard = self.deckOfCards.pop()

class hand:

    def __init__(self,currentDeck):
        self.deck = currentDeck
        self.cardsInHand = []
        self.totalScore = 0

    def __str__(self,):
        return ', '.join(str(c) for c in self.cardsInHand)

    def addCard(self):
        self.cardsInHand.append(self.deck.deckOfCards.pop())

    def handScore(self):
        self.totalScore = 0
        for card in self.cardsInHand:
            self.totalScore = self.totalScore + card.value
        return self.totalScore


if __name__ == '__main__':
    theDeck = deck()
    print(theDeck)
    myHand = hand(theDeck)
    myHand.addCard()
    print(myHand)
    print(myHand.handScore())
    myHand.addCard()
    print(myHand)
    print(myHand.handScore())