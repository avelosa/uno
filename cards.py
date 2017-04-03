class Card:
    """ UNO card object """
    def __init__(self):
        self.available = True
        self.type = ''

    def isDrawn(self):
        self.available = False

    def card_type(self):
        return self.type

class NumCard(Card):
    """ Normal colored number card """
    def __init__(self, color, num):
        self.type = 'number'
        self.color = color
        self.num = num

    def card_type(self):
        return '{color} {num}'.format(color=self.color, num=self.num)

class DrawTwoCard(Card):
    """ Next player draws two cards of a specific color """
    def __init__(self, color):
        self.type = 'draw two'
        self.color = color

    def card_type(self):
        return '{color} {card_type}'.format(color=self.color, card_type=self.type)


class ReverseCard(Card):
    """ Reverse the order of play direction """
    def __init__(self, color):
        self.type = 'reverse'
        self.color = color

    def card_type(self):
        return '{color} {card_type}'.format(color=self.color, card_type=self.type)

class SkipCard(Card):
    """ Skips the next players turn """
    def __init__(self, color):
        self.type = 'skip'
        self.color = color

    def card_type(self):
        return '{color} {card_type}'.format(color=self.color, card_type=self.type)

class WildCard(Card):
    """  Player declares what color to match next """
    def __init__(self):
        self.type = 'wild'

class WildDrawCard(WildCard):
    """ Next player draws 4 cards and current player declares what color to
    match next """
    def __init__(self):
        self.type = 'wild draw 4'

