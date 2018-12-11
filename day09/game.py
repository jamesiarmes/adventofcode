import operator
from marble import Marble
from collections import deque


class Game:
    def __init__(self, players):
        self.players = players
        self.marbles = deque([Marble(0)])

    def high_score(self):
        return max(self.players, key=operator.attrgetter('score')).score

    def board(self):
        return [marble.value for marble in self.marbles]

    def restart(self):
        self.marbles = [Marble(0)]

    def add_marble(self, marble, player):
        if marble.value % 23 == 0:
            self.marbles.rotate(7)
            player.score += marble.value + self.marbles.pop().value
            self.marbles.rotate(-1)
        else:
            self.marbles.rotate(-1)
            self.marbles.append(marble)

