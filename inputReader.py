from typing import List
import sys


def read_num_players() -> int:
    num_players = input("No. of players for each team: ")
    try:
        int(num_players)
        num_players = int(num_players)
    except ValueError:
        print("invalid number of players {0}".format(num_players))
        sys.exit()

    if num_players == 0:
        print("number of players can not be zero")
        sys.exit()

    return num_players


def read_num_overs() -> int:
    num_overs = input("No. of overs: ")
    try:
        int(num_overs)
        num_overs = int(num_overs)
    except ValueError:
        print("invalid number of overs {0}".format(num_overs))
        sys.exit()

    if num_overs == 0:
        print("number of overs can not be zero")
        sys.exit()

    return num_overs


def read_players(team_num: int, num_players: int) -> List[str]:
    players = []
    first_player = input("Batting Order for team {0}: \n".format(team_num))
    players.append(first_player)
    for i in range(1, num_players):
        players.append(input())
    return players