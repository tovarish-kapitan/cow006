import random

from cow006_card import Cow006Card as Card

class Container:
    def __init__(self):
        self.cards = []

    def cards(self):
        return self.cards
        
    def add_card(self, c):
        self.cards.append(c)
        
    def draw(self):
        return self.cards.pop()
        
    def shuffle(self):
        #random.seed(4)
        random.shuffle(self.cards)

    def remove_card(self, c):
        return self.cards.remove(c)

    def __len__(self):
        return len(self.cards)
        
    def __getitem__(self, i):
        return self.cards[i]
        
    def __repr__(self):
        return ' '.join(map(str, self.cards))

def test1():
    deck = Container()
    deck.add_card(Card(44))
    deck.add_card(Card(5))
    deck.add_card(Card(81))

    assert(len(deck) == 3)
    assert(str(deck) == '44 5 81')
    assert(deck[0] == Card(44))

    deck.draw()
    assert (str(deck) == '44 5')
    #deck.shuffle()
    deck.remove_card(Card(5))
    assert (str(deck) == '44')
    #print(deck)



if __name__ == "__main__":

    test1()
