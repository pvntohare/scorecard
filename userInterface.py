from typing import List


class Player:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def set_players(self, players: List[str]):
        for name in players:
            self.players.append(Player(name))

    def get_players(self) -> List[Player]:
        return self.players


class Match:
    def __init__(self, team1: Team, team2: Team, overs: int):
        self.team1 = team1
        self.team2 = team2
        self.overs = overs
        self.toss = None
        self.location = None

    def set_location(self, location: str):
        self.location = location

    def get_location(self) -> str:
        return self.location

    def set_toss_info(self, toss_winner: Team):
        self.toss = toss_winner

    def get_toss_info(self) -> Team:
        return self.toss

    def set_winner(self, match_winner: Team):
        self.winner = match_winner

    def get_winner(self) -> Team:
        return self.winner
