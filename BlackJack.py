## 1 player game of BlackJack against dealer ##
import random

class card:
    def __init__(self,name,suit):
        self.name = name
        self.suit = suit
        self.value = 0

        #get value of card
        self.getValue()
        #paackage characteristics of instance in label
        self.label = f"{self.name} of {self.suit} with score of {self.value}"

    def __str__(self):
        return(self.label)

    #method to get numerical value of the card instance
    def getValue(self):
        if self.name == "10" or self.name in "AJQK":
            self.value = 10
        elif int(self.name) >0 and int(self.name) <10:
            self.value = int(self.name)


if __name__ == '__main__':
    card1 = card('10','Spades')
    print(card1)



## Future failed code unready

# class deck:
#     def __init__(self):
#         self.cards = []
#         self.buildDeck()
#         self.shuffleDeck()
#
#
#     def buildDeck(self):
#         suitVec = ["Heart", "Spades", "Diamons", "Clubs"]
#         nameVec = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "J ", "Q ", "K ", "A "]
#
#         for suit in suitVec:
#             for name in nameVec:
#                 self.cards.append(card(name,suit))
#
#     def shuffleDeck(self):
#         random.shuffle(self.cards)
#
#     def dealCard(self):
#         return self.cards.pop()
#
# class hand:
#
#     def __init__(self):
#         self.cards = []
#         self.addingCard(deck().dealCard())
#         self.cardValue = 0
#         self.score = 0
#
#     def __str__(self):
#         return ', '.join(str(c) for c in self.cards) ## Why cant I just return self.cards or str(self.cards).... I have to str() each letter in the self.cards to get english output
#
#     def addingCard(self,card):
#         self.cards.append(card)
##