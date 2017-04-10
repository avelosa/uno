from termcolor import colored, cprint

from deck import Deck
from player import Player

# UNO in python
class Uno:
    """ main game class """

    def __init__(self, player_count):
        self.players = []
        self.deck = Deck()
        self.current_card = None
        self.cards_played = []

        user_input = ''
        print('To show a list of help options type `help`\n')
        while user_input != 'exit':
            user_input = raw_input('[UNO] enter command:')
            if (user_input == 'help'):
                self.game_help()
            if (user_input == 'start'):
                self.start(player_count)

    def start(self, player_count):
        # set color to match
        self.setup_game(player_count)
        # flip over top card of deck
        self.current_card = self.deck.draw(1)[0]
        self.game_loop()

    def setup_game(self, player_count):
        i = 1
        while(i <= player_count):
            # each player is given 7 cards to begin with
            hand = self.deck.draw(7)
            # build a list of Player objects each with their player number and
            # hand of cards
            self.players.insert(i, Player(i, hand))
            i += 1

    def play_card(self, card, player):
        card_types = [c.card_type() for c in player.hand]
        if (card in card_types):
            # check if card is valid to play next
            # remove card from player's hand and add the card to the play pile
            player.hand.remove(card)
            self.cards_played.append(card)
            print 'card in hand'
            return True
        print('{} not in hand, please try a different card').format(card)
        return False

    def draw_card(self):
        return

    def game_loop(self):
        curr_card_output = colored(self.current_card.card_type(),
                self.current_card.color)
        print('current card: {}').format(curr_card_output)
        # main game loop
        for player in self.players:
            is_turn = True
            move_prompt = 'player {number} move: '.format(number=player.number)
            while (is_turn):
                input_str = raw_input(move_prompt)
                # create argument list
                move = input_str.split()

                if (move[0] == 'play'):
                    if len(move) == 2:
                        is_valid_play = self.play_card(move[1], player)
                        if is_valid_play:
                            print 'next turn...'
                            is_turn = False
                            continue
                    print('Invalid number of args: play <card>')

                if (move[0] == 'draw'):
                    self.draw_card()

                if (move[0] == 'cards'):
                    player.list_cards()

                if (move[0] == 'help'):
                    self.game_help()

    def game_help(self):
        help_table = {
                'start': 'starts an uno game',
                'exit': 'exits uno game session',
                'play <card>': 'play one card',
                'cards': 'lists all cards in player\'s hand',
                'draw': 'draw a card from the deck',
                'current card': 'what the last card played was',
                }
        for command, desc in help_table.items():
            print('{0:12} - {1:10}').format(command, desc)
        return

if __name__ == '__main__':
    game = Uno(2)
