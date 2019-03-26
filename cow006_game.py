from cow006_player import Cow006ComputerPlayer
from cow006_table import Table, Row
from cow006_deck import Cow006Deck

class Cow006Game:
    def __init__(self, players, rows=4, maxinrow=6, maxhand=10):
        self.players = players
        self.maxhand = maxhand
        
        # из колоды раздают карты на стол и игрокам, больше она не нужна
        deck = Cow006Deck()
        deck.shuffle()
        
        self.table = Table(deck, rows, maxinrow)
        for p in self.players:
            p.init_hand(deck, maxhand)
        
    def run(self):
        # пока не закончатся карты на руке
        for step in range(self.maxhand):
            print('------------ Begin step {}'.format(step))
            print(self.table)
            # все игроки кладут закрытые карты
            choosen_cards = {}
            for p in self.players:
                choosen_cards[p.choose_card(self.table)] = p
            print('Choose cards:'+ ', '.join(['{} ({})'.format(c, p.name) for c, p in choosen_cards.items()]))    
            # карты открываются и выкладываются на стол
            for card, player in sorted(choosen_cards.items()):
                print('Resolve {} from {}'.format(card, player))
                self.resolve_card(card, player)
                print(self.table)
    
    def end(self):
        # считаем очки, возвращаем список игроков по возрастанию очков
        # winlist = [(p.score(), p) for p in self.players]
        # winlist.sort()
        
        # напечатать этот список, поздравить победителя
        # todo
        pass
        
    def resolve_card(self, card, player):
        # ищем в какой ряд подходит эта карта
        row = self.table.find_row(card)
        print('Row is', row)

        # если карту нельзя положить ни в один ряд (она очень маленькая)
        if row is None:
            ''' My card is too small'''
            # игрок выбирает, в какой ряд положить
            r = player.choose_row(self.table, card)
            # кладет карту в конец ряда
            r.add_card(card)
            # забирает все карты, кроме последней
            cutted = r.cut()
            # карты, что забрал игрок, добавляются на его счет
            player.add_score(cutted)
            
        else:
            # если карту можно положить в ряд, кладем ее в ряд
            row.add_card(card)
            # это шестая карта?
            if row.overflow():
                # забираем карты, кроме последней и добавляем их в счет игрока
                cutted = row.cut()
                player.add_score(cutted)
        
        
if __name__ == '__main__':
    g = Cow006Game([
            Cow006ComputerPlayer("Alice"),
            Cow006ComputerPlayer("Bob"),
            Cow006ComputerPlayer("Charle")
            ],
            rows=3, maxinrow=4, maxhand=5
            )
    g.run()
    g.end()
    
