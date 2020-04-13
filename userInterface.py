from typing import List
import utils
import sys


class Over:
    def __init__(self, balls: List[str]):
        self.balls = balls


class Player:
    def __init__(self, name: str):
        self.name = name
        self.runs_scored = 0
        self.fours = 0
        self.sixes = 0
        self.balls_faced = 0
        self.overs_bowled = 0
        self.balls_bowled = 0
        self.runs_conceded = 0
        self.fours_conceded = 0
        self.sixes_conceded = 0
        self.wickets_taken = 0

    def get_name(self) -> str:
        return self.name

    def play_ball(self, runs: int, fours: int, sixes: int):
        self.runs_scored += runs
        self.fours += fours
        self.sixes += sixes
        self.balls_faced += 1

    def bowl_ball(self, runs: int, fours: int, sixes: int, wicket: int, wide: int, nb: int):
        self.runs_conceded += runs
        self.fours_conceded += fours
        self.sixes_conceded += sixes
        self.wickets_taken += wicket
        if wide != 0 or nb != 0:
            return
        self.balls_bowled += 1
        if self.balls_bowled == 6:
            self.balls_bowled = 0
            self.overs_bowled += 1


class Team:
    def __init__(self, name, num_players):
        self.name = name
        self.num_players = num_players
        self.players = []
        self.batting_order = []
        self.bowling_order = []
        self.runs_scored = 0
        self.overs_faced = 0
        self.balls_faced = 0
        self.wickets_lost = 0
        self.runs_conceded = 0
        self.overs_bowled = 0
        self.balls_bowled = 0


    def set_players(self, players: List[str]):
        for name in players:
            p = Player(name)
            self.batting_order.append(p)
            self.bowling_order.append(p)
            self.players.append(p)

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

    def get_winner(self) -> Team:
        return self.winner

    def start_inning(self, inning_num: int):
        batting_team = self.team1
        bowling_team = self.team2
        if inning_num == 2:
            batting_team = self.team2
            bowling_team = self.team1

        strike = 1
        non_strike = 0
        for current_over in range(1, self.overs + 1):
            # bowler to bowl the current over
            bowler = (current_over-1) % bowling_team.num_players
            # after ever over, change the batting end
            strike, non_strike = non_strike, strike

            print("Over {0}:".format(current_over))
            num_balls = 0
            while num_balls < 6:
                # check if all the players in batting team are out
                if max(strike, non_strike) >= batting_team.num_players:
                    print_scorecard(batting_team, bowling_team, inning_num)
                    if inning_num == 1:
                        return
                    print("Result: Team 1 won the match by {0} runs".
                          format(bowling_team.runs_scored - batting_team.runs_scored))
                    sys.exit()

                ball = input()
                runs, wicket, wides, nbs, fours, sixes = utils.read_ball(ball)
                if wides == 0 and nbs == 0:
                    num_balls += 1
                    if num_balls == 6:
                        batting_team.balls_faced = 0
                        batting_team.overs_faced += 1
                        bowling_team.balls_bowled = 0
                        bowling_team.overs_bowled += 1
                    else:
                        batting_team.balls_faced += 1
                        bowling_team.balls_bowled += 1

                #bowling_team.bowling_order[bowler].bowl_ball(runs, fours, sixes, wicket, wides, nbs)

                runs_by_batmans = runs
                # for no ball, ball and runs(except 1 run of no ball) will be counted for batsman
                if nbs != 0:
                    runs_by_batmans -= 1

                # batsman score will change only if ball is not wide
                if wides == 0:
                    batting_team.batting_order[strike].play_ball(runs_by_batmans, fours, sixes)

                if wicket != 0:
                    strike = max(strike, non_strike) + 1
                    batting_team.wickets_lost += 1
                    continue

                batting_team.runs_scored += runs
                bowling_team.runs_conceded += runs

                if inning_num == 2 and batting_team.runs_scored > bowling_team.runs_scored:
                    print_scorecard(batting_team, bowling_team, inning_num)
                    print("Result: Team 2 won the match by {0} wickets".
                          format(batting_team.num_players - batting_team.wickets_lost - 1))
                    sys.exit()

                # change the strike of batsman if needed
                if wides != 0:
                    runs_by_batmans -= 1
                if runs_by_batmans % 2 == 1:
                    strike, non_strike = non_strike, strike

            # print score at the end of over
            print_scorecard(batting_team, bowling_team, inning_num)


def print_scorecard(team1: Team, team2: Team, team_num: int):
    print("\nScorecard for Team {}:".format(team_num))
    print("Player Name\tScore\t4s\t6s\tBalls")
    for p in team1.batting_order:
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(p.name, p.runs_scored, p.fours, p.sixes, p.balls_faced))
    print("Total: {0}/{1}".format(team1.runs_scored, team1.wickets_lost))
    print("Overs: {0}.{1}\n".format(team1.overs_faced, team1.balls_faced))
    return None