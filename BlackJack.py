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

    def dealCard(self):
        return(self.deckOfCards.pop())

class hand:

    def __init__(self):
        self.cardsInHand = []
        self.totalScore = 0

    def __str__(self,):
        return ', '.join(str(c) for c in self.cardsInHand)

    def addCard(self,listOfCards):
        self.LoC = listOfCards
        try:
            self.cardsInHand.append(self.LoC.dealCard()) #Adding a card from the DECK
            #print("mydeck")
        except:
            self.cardsInHand.append(self.LoC.cardsInHand.pop()) #Adding a card from another hand (this is meant for splitting your hand)
            #print("adding from other hand")

    def handScore(self):
        self.totalScore = 0
        for card in self.cardsInHand:
            self.totalScore = self.totalScore + card.value
        return self.totalScore

class handOptions:

    def __init__(self,currentHand):
        self.currentHand = currentHand

    def hit(self):
        self.currentHand.addCard(theDeck)

    def split(self):
        self.hand2 = hand()
        self.hand1 = self.currentHand
        self.hand2.addCard(self.hand1)

        return(self.hand1,self.hand2)

    def decideAce(self):
        pass

def askPlayer(handoption1):
    playerInput = input("input your move")
    if playerInput == "0":                 #Stand and proceed
        return handoption1.currentHand
    elif playerInput == "1":
        handoption1.hit()
        return handoption1.currentHand
    elif playerInput == "2":
        options.split()
        split1 = handoption1[0]
        split2 = handoption1[1]
        return split1,split2
    else:
        print("Not valid")

def gamePrep():
    myHand.addCard(theDeck)
    dealerHand.addCard(theDeck)
    myHand.addCard(theDeck)
    dealerHand.addCard(theDeck)


if __name__ == '__main__':
    theDeck = deck()
    myHand = hand()
    dealerHand = hand()
    gamePrep()
    end = False
    while(end == False):
        print(f'Dealers hand = {dealerHand.cardsInHand[0]}')
        print(f'Your hand = {myHand}')

        options = handOptions(myHand)
        myHand = askPlayer(options)
