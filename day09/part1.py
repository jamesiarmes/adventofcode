import re
from itertools import cycle
from player import Player
from marble import Marble
from game import Game


def play_game(input):
    matches = re.findall(r'^(\d+) players; last marble is worth (\d+) points$',
                         input)
    match = matches[0]

    players = []
    for i in range(1, int(match[0]) + 1):
        players.append(Player(i))

    game = Game(players)

    player_iter = cycle(players)
    for i in range(1, int(match[1]) + 1):
        player = next(player_iter)
        game.add_marble(Marble(i), player)

    return game.high_score()


assert play_game('9 players; last marble is worth 25 points') == 32
assert play_game('10 players; last marble is worth 1618 points') == 8317
assert play_game('13 players; last marble is worth 7999 points') == 146373
assert play_game('17 players; last marble is worth 1104 points') == 2764
assert play_game('21 players; last marble is worth 6111 points') == 54718
assert play_game('30 players; last marble is worth 5807 points') == 37305

part_one = '400 players; last marble is worth 71864 points'
print('High score: ' + str(play_game(part_one)))

part_two = '400 players; last marble is worth 7186400 points'
print('High score: ' + str(play_game(part_two)))
