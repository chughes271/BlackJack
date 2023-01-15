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
            if self.name in "JQKjqk":
                self.value = 10
                self.label = f"{self.name} of {self.suit}" # with score of {self.value}"
            elif self.name in "Aa":
                self.value = 11
                self.label = f"{self.name} of {self.suit}"  # with score of {self.value}"
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
        if self.totalScore > 21 and "A" in (', '.join(str(c) for c in self.cardsInHand)):
            for card in self.cardsInHand:
                if card.value == 11:
                    card.value = 1
                    self.totalScore = self.totalScore - 10
        return self.totalScore

class handOptions:

    def __init__(self,currentHand):
        self.currentHand = currentHand

    def hit(self):
        self.currentHand.addCard(theDeck)

    def split(self):
        if self.currentHand.cardsInHand[0].value == self.currentHand.cardsInHand[1].value:

            self.hand2 = hand()
            self.hand1 = self.currentHand
            self.hand2.addCard(self.hand1)

            return(self.hand1,self.hand2)
        else:
            print("Cannot split your hand")
            self.askAgain = askPlayer(options)
            return self.askAgain

def askPlayer(handoption1):
    playerInput = input("input your move")
    stand = False
    if playerInput == "0":                 #Stand and proceed
        stand = gameClosing()
        return(handoption1.currentHand,stand)
    elif playerInput == "1":
        handoption1.hit()
        return(handoption1.currentHand,stand)
    elif playerInput == "2":
        handoption1 = options.split()
        return(handoption1)
    else:
        print("Incorrect input")
        return(askPlayer(options))

def gamePrep():
    myHand.addCard(theDeck)
    dealerHand.addCard(theDeck)
    myHand.addCard(theDeck)
    dealerHand.addCard(theDeck)

def gameClosing():
    while(dealerHand.handScore() < 21 and dealerHand.handScore() <= myHand.handScore()):
        dealerHand.addCard(theDeck)
        #print(f'Dealers hand = {dealerHand}')
    #end = gameEnd(myHand.handScore(),dealerHand.handScore(),True)

    return(True)


def gameEnd(player,dealer,stand):
    #print(player,dealer,stand)

    endGame = False
    win = False
    push = False

    if player > dealer:
        if player > 21:
            endGame = True #lose
        elif stand == True or player == 21:
            gameClosing()
            dealer = dealerHand.handScore()
            endGame = gameEnd(player,dealer,stand)
            return endGame
    elif player < dealer:
        if dealer > 21:
            endGame = True
            win = True
        elif stand == True:
            endGame = True
    elif stand == True:
        endGame = True
        push = True

    if endGame == True:
        if win == True:
            print(f"\nYou won {player}-{dealer}\nYour hand: {myHand}\nDealer's hand: {dealerHand}")
        elif push == True:
            print(f"\nGame pushed {player}-{dealer}\nYour hand: {myHand}\nDealer's hand: {dealerHand}")
        else:
            print(f"\nYou lost {player}-{dealer}\nYour hand: {myHand}\nDealer's hand: {dealerHand}")

    return(endGame)

if __name__ == '__main__':
    end = False
    stand = False

    theDeck = deck()
    myHand = hand()
    options = handOptions(myHand)
    dealerHand = hand()
    gamePrep()

    while(end == False):
        end = gameEnd(myHand.handScore(), dealerHand.handScore(),stand)
        if end != True:
            print(f'Dealers hand = {dealerHand.cardsInHand[0]}')
            print(f'Your hand = {myHand}')
            myHand,stand = askPlayer(options)


