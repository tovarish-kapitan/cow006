class Cow006Card:
    def __init__(self, n):
        self.n = n
        self.score = 1  # todo
        
    def __repr__(self):
        return str(self.n)
        
    def __lt__(self, other):
        return self.n < other.n
        
    def __eq__(self, other):
        return self.n == other.n
        
    def __hash__(self):
        return self.n

    @staticmethod
    def all_cards(maxsize=104):
        return [Cow006Card(i+1) for i in range(maxsize)] 
        
def test1():
    # test __init__, __repr__, __eq__, __lt__
    c1 = Card(5)
    print(c1)
    
    c2 = Card(47)
    print(c2)
    
    c3 = Card(47)
    print(47)

    assert(c1 != c2)
    assert(c2 == c3)
    
    assert(c1 < c2)
    assert(c2 > c1)
        
