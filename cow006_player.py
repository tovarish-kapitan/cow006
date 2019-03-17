from cow006_table import Table
from cow006_container import Container
from cow006_hand import Hand

class Cow006Player:
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
        
    def choose_card(self, table=None):
        """ выбираем какую карту играть (в начале хода)"""
        # todo: случайную
        return self.hand.draw()
        
    def choose_row(self, table, card):
        """ выбирает, какой ряд взять со стола и положить в начало ряда карту card"""
        # todo: случайную
        return table[0]
        
    def score(self):
        """ считаем очки игрока """
        return self._score

    def add_score(self, card_list):
        """ добавляем в очки игрока очки из карт card_list """
        pass
