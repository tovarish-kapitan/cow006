from cow006_container import Container
from cow006_card import Cow006Card as Card

class Cow006Deck(Container):
    def __init__(self):
        super().__init__()
        for c in Card.all_cards():
            self.add_card(c)
