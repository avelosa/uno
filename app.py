from deck import Deck
from player import Player

# UNO in python
class Uno:
    """ main game class """

    def __init__(self, player_count):
        self.players = []
        self.deck = Deck()
        self.current_card = None
        self.discard_pile = []

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

    def game_loop(self):
        '''move_options = {
            'draw': draw(),
            'cards': list_cards(),
            'play': play(),
            'end': end_turn(),
        }'''

        print('current card: {card}').format(card=self.current_card.card_type())
        # main game loop
        for player in self.players:
            move_prompt = 'player {number} move: '.format(number=player.number)
            move = raw_input(move_prompt)
            return

    # move methods
    def draw_a_card(self):
        return
    def list_card(self):
        return
    def play_card(self):
        return
    def end_trun(self):
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

if __name__ == '__main__':
    game = Uno(2)
