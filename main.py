from inputReader import *
from userInterface import *


def init_match_info() -> Match:
    # read match info from user
    num_players = read_num_players()
    num_overs = read_num_overs()

    team1 = Team("CSK", num_players)
    team2 = Team("MI", num_players)

    match = Match(team1, team2, num_overs)
    match.set_toss_info(team1)

    return match


def main():
    print("Hello, welcome to online scorecard system")

    match = init_match_info()

    # read players for first team
    players = read_players(1, match.team1.num_players)
    match.team1.set_players(players)
    # read players of second ream
    players = read_players(2, match.team2.num_players)
    match.team2.set_players(players)
    # start the match
    print("team1 batting")
    match.start_inning(1)
    print("team2 batting")
    match.start_inning(2)


if __name__ == '__main__':
    main()