
import argparse
import sys
import re

def _parse():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--DD", type=str,nargs='+', help="DD challenge [rating] [bonus]")
    parser.add_argument("-p", "--dice", type=str,nargs='+', help="Dice parser [kdn] <+ j>")
    parser.add_argument("--debug", action="store_true", help="prints debug info")


    args = parser.parse_args()
    return args

def _printDebug(args):

    # DEBUG:
    print("******************************** DEBUG ********************************")
    print("Argument \t \t Type \t \t \t  Value")
    print("***********************************************************************")
    for arg in vars(args):
        if len(arg) < 8:
            print(arg, "\t \t \t", type(getattr(args, arg)), "\t \t", getattr(args, arg), sep="")
        else:
            print(arg, "\t \t", type(getattr(args, arg)), "\t \t", getattr(args, arg), sep="")
    print("\nSystem exec : ", sys.executable)
    print("***********************************************************************")


def computeStats(raw_rating, raw_bonus, *, display=True):
    """ succedes on equality"""
    rating, bonus = int(raw_rating), int(raw_bonus)

    chance = 5*bonus - (rating-10)*5 + 55

    renormalized_chance = min(95, max(5, chance))

    if display:
        if renormalized_chance == 5:
            print("\033[91m"  f"{renormalized_chance} % (crit only)"+"\033[0m" +f" chances to succed against a rating of {rating} with a {bonus} bonus.")
        elif renormalized_chance < 50:
            print("\033[93m"  f"{renormalized_chance} %"+"\033[0m" +f" chances to succed against a rating of {rating} with a {bonus} bonus.")
        else:
            print("\033[92m"  f"{renormalized_chance} %"+"\033[0m" +f" chances to succed against a rating of {rating} with a {bonus} bonus.")

    return renormalized_chance

def parseRoll(raw_roll):
    """ parses dice rolls"""
    roll = ""
    for r in raw_roll:
        roll += r.strip(" ")

    summands = re.split('([+-])',roll) # [] for a list of possible separators, () to keep them
    return summands

def computeDice(raw_roll):
    sum = 0
    summands = parseRoll(raw_roll)
    sign = 1
    for elt in summands:
        if isDie(elt):
            sum += avgDice(elt)*sign
            sign = 1
        elif isNumber(elt):
            sum += int(elt)*sign
            sign = 1
        if elt == '-':
            sign = -1
    print(f"Roll : {' '.join(summands)}\n"
            f"Average : {sum}")
    return sum

def isDie(s):
    """returns whether a string is a dice roll"""
    die_expr = re.compile(r"\d+d\d+")
    return die_expr.match(s) is not None

def isNumber(s):
    """returns whether a string is a dice roll"""
    nb_expr = re.compile(r"\d+")
    return nb_expr.match(s) is not None

def avgDice(dice):
    n_dice, n_faces = dice.split('d')
    return int(n_dice) * (int(n_faces) + 1)/2

def main():
    args = _parse()
    if args.debug:
        _printDebug(args)

    if args.DD:
        computeStats(*args.DD)

    elif args.dice:
        computeDice(args.dice)

if __name__ == "__main__":
    # execute only if run as a script
    main()
