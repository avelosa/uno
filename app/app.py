from termcolor import colored, cprint

from deck import Deck
from player import Player

main_help_table = {
    'start': 'starts an uno game',
    'exit': 'exits uno game session',
}
move_help_table = {
    'play <card>': 'play one card',
    'cards': 'lists all cards in player\'s hand',
    'draw': 'draw a card from the deck',
    'current_card': 'what the last card played was',
    'done': 'end player turn',
}

# UNO in python
class Uno:
    """ main game class """

    def __init__(self, player_count):
        self.players = []
        self.deck = Deck()
        self.current_card = None
        self.current_color = None
        self.cards_played = []
        self.game_over = False

        user_input = ''
        print('To show a list of help options type `help`\n')
        while user_input != 'exit':
            user_input = raw_input('[UNO] enter command:')
            if (user_input == 'help'):
                self.game_help(main_help_table)
            if (user_input == 'start'):
                self.start(player_count)

    def start(self, player_count):
        # set color to match
        self.setup_game(player_count)
        # flip over top card of deck
        self.current_card = self.deck.draw(1)[0]
        self.current_color = self.current_card.color
        while (not self.game_over):
            self.game_loop()

    def setup_game(self, player_count):
        i = 1
        while(i <= player_count):
            # each player is given 7 cards to begin with
            hand = self.deck.draw(7)
            self.players.insert(i, Player(i, hand))
            i += 1

    def set_current_color(self, color):
        if (color == 'red' or color == 'blue' or color == 'green' or color ==
                'yellow'):
            self.current_color = color
            return True
        else:
            print('Invalid color selection')
            return False

    def validate_card_played(self, card):
        curr_type = self.current_card.type
        curr_color = self.current_card.color

        # one option is to match the current color
        if (card.type == 'wild' or card.type == 'wild_draw4'):
            # special case: wild cards
            # make the user select the new current color
            select_color_prompt = 'Please select a new color (red, green, blue, or yellow): '
            new_color = raw_input(select_color_prompt)
            return self.set_current_color(new_color)
        elif (card.color == curr_color):
            return True
        elif (curr_type == card.type):
            # player can also match based on equal card types
            return True
        else:
            print('invalid card played')
            return False

    def play_card(self, card_name, player):
        # find the card obect for the card the user played
        matching_cards = [c for c in player.hand if c.card_type() == card_name]
        # check if card is valid to play next
        if matching_cards != []:
            card = matching_cards.pop()
            # validate that the card can be played
            if (self.validate_card_played(card)):
                # remove card from player's hand and add the card to the play pile
                player.hand.remove(card)
                self.cards_played.append(card)
                self.current_card = card
                self.current_color = card.color
                print 'card in hand'
                return True

        print('{} not in hand, draw or play another card').format(card_name)
        return False

    def print_current_card(self):
        curr_card_output = colored(self.current_card.card_type(),
                self.current_card.color)
        print('current card: {}').format(curr_card_output)

    def should_player_draw_cards(self):
        if (self.current_card.type == 'draw2'):
            return 2
        elif (self.current_card.type == 'wild_draw4'):
            return 4

    def game_loop(self):
        self.print_current_card()
        # main game loop
        for player in self.players:
            is_turn = True
            # TODO: check if current_card in play is a reverse or skip card
            move_prompt = 'player {number} move: '.format(number=player.number)
            while (is_turn):
                # TODO: check if deck is empty

                # check if current_card in play is a draw card
                cards_to_draw = self.should_player_draw_cards()
                if (cards_to_draw > 0):
                    new_cards = self.deck.draw(cards_to_draw)
                    # add cards to player's hand
                    player.hand.extend(new_cards)

                input_str = raw_input(move_prompt)
                # create argument list
                move = input_str.split()

                if (move[0] == 'play'):
                    print len(move)
                    if len(move) == 2:
                        is_valid_play = self.play_card(move[1], player)
                        if not is_valid_play:
                            print('Invalid number of args: play <card>')

                elif (move[0] == 'draw'):
                    # darw 1 card from the game deck
                    player.hand.append(self.deck.draw(1).pop())

                elif (move[0] == 'cards'):
                    player.list_cards()

                elif (move[0] == 'current_card'):
                    self.print_current_card()

                elif (move[0] == 'help'):
                    self.game_help(move_help_table)

                elif(move[0] == 'done'):
                    print 'next turn...'
                    is_turn = False
                    continue

                else:
                    print 'invalid move'
                    self.game_help(move_help_table)

    def game_help(self, table):
        for command, desc in table.items():
            print('{0:12} - {1:10}').format(command, desc)
        return

if __name__ == '__main__':
    game = Uno(2)
