from cow006_card import Cow006Card as Card
from cow006_container import Container
from cow006_deck import Cow006Deck

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
        return len(self.cards) >= self.maxinrow

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
        candidate = None
        for row in self.rows:
            if candidate == None and row.acceptable(card):
                candidate = row
            if  (not candidate == None) and row.acceptable(card):
                if row > candidate:
                    candidate = row
        return candidate

    def find_min_score_row(self):
        min_score_row = self.rows[0]
        for row in self.rows:
            if row.row_score() < min_score_row.row_score():
                min_score_row = row
        return min_score_row

    def __getitem__(self, i):
        return self.rows[i]


def test1():
    row = Row(Card(11))
    row.add_card(Card(12))
    row.add_card(Card(13))
    row.add_card(Card(14))
    row.add_card(Card(15))
    assert (row.overflow() == False)
    row.add_card(Card(16))
    assert (row.overflow() == True)
    assert (row.acceptable(Card(17)) == True)
    assert (row.acceptable(Card(5)) == False)
    assert (row.top() == Card(16))
    assert (row.cut() == [Card(11), Card(12), Card(13), Card(14), Card(15)])
    assert (str(row) == '16')

    #print(row)

def test2():
    table = Table(Cow006Deck())
    print(table)
    print(table.find_row(Card(104)))


if __name__ == '__main__':
    test2()
