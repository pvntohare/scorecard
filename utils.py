from typing import Tuple
import sys


def read_ball(ball: str) -> Tuple[int, int, int, int]:
    if ball == "W":
        return 0, 1, 0, 0, 0, 0
    elif ball.endswith("Wd") and len(ball) <= 3:
        runs = 1
        if len(ball) == 2:
            return runs, 0, runs, 0, 0, 0
        elif len(ball) == 3 and not ball[0].isdigit():
            print("invalid input {0} for ball in over".format(ball))
            sys.exit
        elif int(ball[0]) <= 6:
            runs += int(ball[0])
            sixes , fours = 0, 0
            if runs == 7:
                sixes = 1
            elif runs == 5:
                fours = 1
            return runs, 0, runs, 0, fours, sixes
        else:
            print("invalid input {0} for ball in over".format(ball))
            sys.exit
    elif ball.endswith("N") and len(ball) <= 2:
        runs = 1
        if len(ball) == 1:
            return runs, 0, 0, runs, 0, 0
        elif len(ball) == 2 and not ball[0].isdigit():
            print("invalid input {0} for ball in over".format(ball))
            sys.exit
        elif int(ball[0]) <= 6:
            runs += int(ball[0])
            sixes , fours = 0, 0
            if runs == 7:
                sixes = 1
            elif runs == 5:
                fours = 1
            return runs, 0, 0, runs, fours, sixes
        else:
            print("invalid input {0} for ball in over".format(ball))
            sys.exit
    elif ball.isdigit() and int(ball) <= 6:
        runs = int(ball)
        sixes , fours = 0, 0
        if runs == 6:
            sixes = 1
        elif runs == 4:
            fours = 1
        return runs, 0, 0, 0, fours, sixes
    else:
        print("invalid input {0} for ball in over", format(ball))
        sys.exit()