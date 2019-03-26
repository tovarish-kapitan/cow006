from abc import ABCMeta, abstractmethod

from cow006_table import Table
from cow006_container import Container
from cow006_hand import Hand

class Cow006Player(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self._score = 0
    
    def __repr__(self):
        return '{}: {}'.format(self.name, self.hand)

    def init_hand(self, deck, maxhand=10):
        """ берем из колоды deck maxhand карт (в начале игры)"""
        for i in range(maxhand):
            self.hand.add_card(deck.draw())

    @abstractmethod
    def choose_card(self, table=None):
        """ выбираем какую карту играть (в начале хода)"""
        # todo: случайную
        return self.hand.draw()

    @abstractmethod
    def choose_row(self, table, card):
        """ выбирает, какой ряд взять со стола и положить в начало ряда карту card"""
        # todo: случайную
        return table[0]
        
    def score(self):
        """ считаем очки игрока """
        return self._score

    def add_score(self, card_list):
        """ добавляем в очки игрока очки из карт card_list """
        for card in card_list:
            self._score += card.card_score()


class Cow006ComputerPlayer(Cow006Player):
    def choose_card(self, table=None):
        c = min(self.hand)
        self.hand.remove(c)
        return c

    def choose_row(self, table, card):
        return table.find_min_score_row()


class Cow006HumanPlayer(Cow006Player):
    def choose_card(self, table=None):
        while True:
            print(self.hand.cards())
            s = int(input('Choose card'))
            if Card(s) in self.hand.cards():
                self.hand.remove_card(Card(s))
                return Card(s)

    def choose_row(self, table, card):
        while True:
            print(card)
            s = int(input("Choose row"))
            if s in (0, 1, 2, 4):
                return table[s]



