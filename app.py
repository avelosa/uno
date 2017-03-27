import random
import argparse

# UNO in python
class Uno:
    """ main game class """

    def __init__(self, player_count):
        self.players = []
        self.deck = Deck()
        self.current_card = ''

        # Initial deck of cards
        # 108 cards
        # 4 types of colors numbers  0-9
        # 8 skip cards
        # 8 reverse cards
        # 8 draw two cards
        # 4 wild cards
        # 4 wild draw four cards
        self.setup_game(player_count)
        user_input = ''
        print('To show a list of help options type `help`\n')
        while user_input != 'exit':
            user_input = raw_input('[UNO] Please enter a valid command:')
            if (user_input == 'help'):
                self.game_help()
            if (user_input == 'start'):
                self.start()

    def setup_game(self, player_count):
        i = 0
        while(i < player_count):
            # each player is given 7 cards to begin with
            hand = self.draw_cards(7)
            self.players.insert(i, Player(i, hand))
            i += 1

    def draw_cards(self, count):
        # draw cards based on count
        return dict()

    def start(self):
        begin = raw_input('Begin a new game of Uno? ')
        if (begin == 'yes'):
            # set color to match
            print('Begin game!')
            # flip over top card of deck
            # create a discard pile
            return

    def game_help(self):
        help_table = {
                'start': 'starts an uno game',
                'exit': 'exits uno game session',
                #'playing' : 'how to play the game'
                }
        for command, desc in help_table.items():
            print('{0:10} - {1:10}').format(command, desc)
        return

class Player:
    def __init__(self, number, hand):
        # p1, p2, p3, p4...?
        self.number = number
        # players hand of cards
        self.hand = hand


class Card:
    """ UNO card object """
    def __init__(self, color=''):
        self.color = color
        self.available = True

    def isDrawn(self):
        self.available = False

class NumCard(Card):
    """ Normal colored number card """
    def __init__(self, color, num):
        self.num = num

class DrawTwoCard(Card):
    """ Next player draws two cards of a specific color """

class ReverseCard(Card):
    """ Reverse the order of play direction """

class SkipCard(Card):
    """ Skips the next players turn """

class WildCard(Card):
    """  Player declares what color to match next """

class WildDrawCard(WildCard):
    """ Next player draws 4 cards and current player declares what color to
    match next """


class Deck:
    def __init__(self):
        self.cards = [
            WildCard(), WildCard(), WildCard(), WildCard(),
            WildDrawCard(), WildDrawCard(), WildDrawCard(), WildDrawCard(),
        ]
        self.cards.append(self.create_num_cards('red'))
        self.cards.append(self.create_num_cards('blue'))
        self.cards.append(self.create_num_cards('yellow'))
        self.cards.append(self.create_num_cards('green'))
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
        i = 0
        hand = []
        while(i < count):
            # pop returns last item in list
            hand[i] = self.cards.pop()
            i += 1

        return hand
if __name__ == '__main__':
    game = Uno(2)
