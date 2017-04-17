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
            self.players.insert(i, Player(i, hand))
            i += 1

    def play_card(self, card_name, player):
        matching_cards = [c for c in player.hand if c.card_type() == card_name]
        # check if card is valid to play next
        if matching_cards != []:
            card = matching_cards.pop()
            # remove card from player's hand and add the card to the play pile
            player.hand.remove(card)
            self.cards_played.append(card)
            self.current_card = card
            print 'card in hand'
            return True

        print('{} not in hand, draw or play another card').format(card_name)
        return False

    def print_current_card(self):
        curr_card_output = colored(self.current_card.card_type(),
                self.current_card.color)
        print('current card: {}').format(curr_card_output)

    def game_loop(self):
        self.print_current_card()
        # main game loop
        for player in self.players:
            is_turn = True
            # TODO: check if current_card in play is a reverse or skip card
            move_prompt = 'player {number} move: '.format(number=player.number)
            while (is_turn):
                # TODO: check if deck is empty
                # TODO: check if current_card in play is a draw card
                input_str = raw_input(move_prompt)
                # create argument list
                move = input_str.split()

                if (move[0] == 'play'):
                    print len(move)
                    if len(move) == 2:
                        is_valid_play = self.play_card(move[1], player)
                        if not is_valid_play:
                            print('Invalid number of args: play <card>')

                if (move[0] == 'draw'):
                    # darw 1 card from the game deck
                    player.hand.append(self.deck.draw(1).pop())

                if (move[0] == 'cards'):
                    player.list_cards()

                if (move[0] == 'current_card'):
                    self.print_current_card()

                if (move[0] == 'help'):
                    self.game_help()

                if (move[0] == 'done'):
                    print 'next turn...'
                    is_turn = False
                    continue

                else:
                    print 'invalid move'
                    self.game_help()

    def game_help(self):
        help_table = {
                'start': 'starts an uno game',
                'exit': 'exits uno game session',
                'play <card>': 'play one card',
                'cards': 'lists all cards in player\'s hand',
                'draw': 'draw a card from the deck',
                'current_card': 'what the last card played was',
                'done': 'end player turn',
                }
        for command, desc in help_table.items():
            print('{0:12} - {1:10}').format(command, desc)
        return

if __name__ == '__main__':
    game = Uno(2)
