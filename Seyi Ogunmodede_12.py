# A class can be considered a outline made by the user for creating objects
# An object is an instance of the class with actual values.

# Objects consist of:

# State: attributes/properties of an object

# Behavior: the methods of the object and also its response to other objects

# Identity: gives a unique name to the object and that allows for interaction between objects.

# How to declare an object from the class
# We can't really do anything with that class, 
# we can't look up the attributes, run the functions or methods inside that class
# unless we make an object of that class

class CAR:
    #attibute
    attr1 = "red"
    attr2 = "fast"
    coolfeature = "Apple CarPlay"
    year = "2022"

    #sample method
    #self refers to the class of which the method belongs
    def fun(self):
        print("The car is", self.attr1)
        print("The car is", self.attr2)
        
        
# Let us make a specific object of the class car and call it Miata


# object instantiaton

Miata = CAR()


# this display that Miata is an object of that class CAR

print(Miata)


# We can run the function side and see what it does
# it print out what differnt attributes are

Miata.fun()

Miata.attr1

Miata.attr2

Miata.coolfeature

Miata.year

class KITCHEN:
    # attribute
    attr1="neat"
    attr2="lot of pantries"
    attr3="good illumination"
    available="cooking gas"
    year="2023"
    
    def fun(self):
        print("The kitchen is",self.attr1)
        print("The kitchen has",self.attr2)
        print("The kitchen has",self.attr3)
        
        
        
COOK = KITCHEN()

print(COOK)

COOK.fun()

COOK.attr1

COOK.attr2

COOK.attr3

COOK.available

COOK.year

# Python function inside a class is called a method

class Card:
#mapping each possible card number(2-10,J,Q,K,A) to a numerical value
    _value_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8, "9":9, "10": 10, "j": 11, "q": 12, "k": 13, "a": 14}
    def __init__(self, number, suit):
        if str(number).lower() not in [str(num) for num in range(2, 11)] + list("jqka"):
            raise Exception("Number wasn't 2-10 or J, Q, K, or A.")
        else:
            self.number = str(number).lower()
        if suit.lower() not in ["clubs", "hearts", "diamonds", "spades"]:
            raise Exception("Suit wasn't one of: clubs, hearts, spades, or diamonds.")
        else:
            self.suit = suit.lower()

    def __str__(self):
        return(f'{self.number} of {self.suit.lower()}')

    def __repr__(self):
        return(f'Card(str({self.number}), "{self.suit}")')

    def __eq__(self, other):
        if self.number == other.number:
            return True
        else:
            return False

    def __lt__(self, other):
        if self._value_dict[self.number] < self._value_dict[other.number]:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._value_dict[self.number] > self._value_dict[other.number]:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.number)
    
    
    
class Deck:
    brand = "Bicycle"
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _numbers = [str(num) for num in range(2, 11)] + list("jqka")

    def __init__(self):
        self.cards = [Card(number, suit) for suit in self._suits for number in self._numbers]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

        
        
        
my_card = Card("10", "spades")


# It displays a card with a string 10 and then a spades when object is printed by itself

my_card

# This code just give the output as 10 of spades 

print(my_card)

my_deck = Deck()

len(my_deck)


class Deck:
    brand = "Bicycle"
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _numbers = [str(num) for num in range(2, 11)] + list("jqka")

    def __init__(self):
        self.cards = [Card(number, suit) for suit in self._suits for number in self._numbers]
        
    def __str__(self):
        return(f' A {self.brand} deck with {len(self)} card.')


    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

        
        
my_deck1 = Deck()

print(my_deck1)

# we want to make a Player class and then make an object of 
# type player that can start drawing some cards out of a deck.
# so our class called player needs to have something like:
# A deck to draw the card from
# A hand of card of its own
# A name for the player
# A method by which it can draw some cards from the deck 


# The class will be called a player
# We will initiallize a player
# We want it name to be whatever we pass in
# And we want to have a hand that start out empty
# And we want to have a deck that is whatever deck we passed in as well
# Also we need to have a method by which we can draw some cards
# So all i need to do is tell it which player we are using to draw the cards
# Then we go off of that players' deck and get the last card
# -1 means getting the very last card
# Then off of that deck, we will pop a card
# Because we have stored the last one, then we will pop it off, so that it is not on the deck anymore
# Then append the card to our hand
# Then we will return that card


class Player:
   
    def __init__(self, name, deck):
        self.name = name
        self.hand = []
        self.deck = deck
        
    def draw(self):
        card = self.deck.cards[-1]
        self.deck.cards.pop()
        self.hand.append(card)
        return card
    
    
    
my_deck1 = Deck()

len(my_deck1)

player1 = Player("Liz", my_deck1)


card = player1.draw()

print(card)

# a card has been taken off

len(my_deck1)


anothercard1=player1.draw()

print(card)


len(my_deck1)

# and we have not shuffle our deck 
# if Liz keep going there will be reduction in the number