import sys
from termcolor import colored, cprint

class Player:
    def __init__(self, number, hand):
        # p1, p2, p3, p4...?
        self.number = number
        self.points = 0
        # players hand of cards
        self.hand = hand

    def list_cards(self):
        for card in self.hand:
            color = card.color
            card_text = colored(card.card_type(), color)
            print('{card}, ').format(card=card_text)
