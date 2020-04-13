from inputReader import *
from userInterface import *


def main():
    print("Hello, welcome to online scorecard system")
    team1 = Team("team1")
    team1.set_players(["p1", "p2", "p3"])
    players = team1.get_players()
    for player in players:
        print(player.get_name())


if __name__ == '__main__':
    main()