from cow006_card import Cow006Card as Card
from cow006_container import Container

class Row(Container):
    def __init__(self, card, maxinrow = 6):
        self.cards = [card]
        self.maxinrow = maxinrow        # какая корова "проваливает" ряд
        
    def __repr__(self):
        return ' '.join(map(str, self.cards))
        
    def __lt__(self, other):
        return self.top() < other.top()
        
    def top(self):
        """ возвращает последнюю карту в ряду """
        return self.cards[-1]
        
    def overflow(self):
        """ проверяет, есть 6 коров в ряду (True) или еще нет (False)"""
        return len(self.cards) >= 6

    def acceptable(self, card):
         """ эту карту card можно положить в конец этого ряда? """
         return card > self.top()
        
    def cut(self):
        """ Убирает из ряда все карты, кроме последней. Возвращает список убранных карт"""
        cutted = []
        while len(self.cards) > 1:
            cutted.append(self.cards.pop(0))
        return cutted

class Table:
    def __init__(self, deck, rows = 4, maxinrow = 6):
        self.maxinrow = maxinrow
        self.rows = [Row(deck.draw(), maxinrow) for r in range(rows)]
        
    def __repr__(self):
        return '\n'.join(['Row{} : {}'.format(i, r) for i, r in enumerate(self.rows)] )

    def find_row(self, card):
        """ ищет, в какие ряды можно положить эту карту, возвращает ряд или None, 
        если карту нельзя положить ни в один ряд """
        pass
        
    def __getitem__(self, i):
        return self.rows[i]
        
   