import random

from cards import (
        WildCard,
        WildDrawCard,
        NumCard,
        ReverseCard,
        SkipCard,
        DrawTwoCard,
    )

# Initial deck of cards
# 108 cards
# 4 types of colors numbers  0-9
# 8 skip cards
# 8 reverse cards
# 8 draw two cards
# 4 wild cards
# 4 wild draw four cards
class Deck:
    def __init__(self):
        self.cards = [
            WildCard(), WildCard(), WildCard(), WildCard(),
            WildDrawCard(), WildDrawCard(), WildDrawCard(), WildDrawCard(),
        ]
        self.cards.extend(self.create_num_cards('red'))
        self.cards.extend(self.create_num_cards('blue'))
        self.cards.extend(self.create_num_cards('yellow'))
        self.cards.extend(self.create_num_cards('green'))
        # shuffle cards
        random.shuffle(self.cards)

    def create_num_cards(self, color):
        # 25 cards of each color
        return [
            NumCard(color, 0), NumCard(color, 1), NumCard(color, 1),
            NumCard(color, 2), NumCard(color, 2), NumCard(color, 3),
            NumCard(color, 3), NumCard(color, 4), NumCard(color, 4),
            NumCard(color, 5), NumCard(color, 5), NumCard(color, 6),
            NumCard(color, 6), NumCard(color, 7), NumCard(color, 7),
            NumCard(color, 8), NumCard(color, 8), NumCard(color, 9),
            NumCard(color, 9), SkipCard(color), SkipCard(color),
            ReverseCard(color), ReverseCard(color), DrawTwoCard(color),
            DrawTwoCard(color)
        ]

    def draw(self, count):
        hand = []
        while(count > 0):
            # pop returns last item in list
            hand.append(self.cards.pop())
            count = count - 1

        return hand

    def print_deck(self):
        # XXX: DEBUGING
        for card in self.cards:
            print('{card_type}').format(card_type=card.type)
