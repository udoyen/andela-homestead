import random

from pip.backwardcompat import raw_input


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in Card.SUITE for r in Card.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def setup_hands(self, players):
        hands = [player.hand for player in players]
        while len(self.cards) >= len(players):
            for hand in hands:
                hand.add_card(self.cards.pop())
        return hands


class Card:
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10'.split()

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return '{}-{}'.format(self.rank, self.suite)

    @property
    def value(self):
        return self.RANKS.index(self.rank)


class Play:
    def __init__(self):
        # create new deck instance
        d = Deck()
        pass

    @staticmethod
    def give_cards():
        # ask for how many players will be playing
        # get the number and use it to ask for their names
        player_num = int(raw_input("How many players will be playing today:>> "))
        player_dic = {}
        for i in range(0, player_num):
            player_name = raw_input("Please give names of players:>> ")
            player_dic[str(i)] = player_name
            print(player_dic[str(i)])

        return


class Player:
    def __init__(self, name):
        """
        player class
        :param name:
        """
        self.name = name
        self.hand = []
        pass


d = Deck()
print(d.cards[1])
c = Card('H', '2')
print(c)
