class Cow006Card:
    def __init__(self, n):
        self.n = n
        self.score = self.card_score()  # todo
        
    def __repr__(self):
        return str(self.n)
        
    def __lt__(self, other):
        return self.n < other.number()
        
    def __eq__(self, other):
        return self.n == other.number()
        
    def __hash__(self):
        return self.n

    def number(self):
        return self.n

    def card_score(self):
        n = self.n
        score = 1
        if n == 55:
            score = 7
        elif not (n % 11):
            score = 5
        elif not (n % 10):
            score = 3
        elif not (n % 5):
            score = 2
        return score


    @staticmethod
    def all_cards(maxsize=104):
        return [Cow006Card(i+1) for i in range(maxsize)] 
        
def test1():
    # test __init__, __repr__, __eq__, __lt__
    c1 = Cow006Card(5)
    c2 = Cow006Card(47)
    c3 = Cow006Card(47)

    assert(c1 != c2)
    assert(c2 == c3)
    
    assert(c1 < c2)
    assert(c2 > c1)
    assert(str(c2) == '47')
    assert(c2.number() == 47)

def test2():
    assert (Cow006Card(55).card_score() == 7)
    assert (Cow006Card(22).card_score() == 5)
    assert (Cow006Card(20).card_score() == 3)
    assert (Cow006Card(15).card_score() == 2)
    assert (Cow006Card(13).card_score() == 1)
    
if __name__ == "__main__":
    test1()
    test2()
        
