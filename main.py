from inputReader import *
from userInterface import *


def init_match_info() -> Match:
    # read match info from user
    num_players = read_num_players()
    num_overs = read_num_overs()

    team1 = Team("CSK", num_players)
    team2 = Team("MI", num_players)

    match = Match(team1, team2, num_overs)

    return match


def main():
    print("Hello, welcome to online scorecard system")

    match = init_match_info()
    # read players for first team
    match.team1.add_players(1)
    # read players of second ream
    match.team1.add_players(2)

    for p in match.team1.players:
        print(p.get_name())
    for p in match.team2.players:
        print(p.get_name())


if __name__ == '__main__':
    main()