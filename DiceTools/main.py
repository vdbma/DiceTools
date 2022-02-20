
import argparse
import sys

def _parse():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--DD", type=str,nargs='+', help="DD challenge [rating] [bonus]")
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


def computeStats(raw_rating, raw_bonus):
    """ succedes on equality"""
    rating, bonus = int(raw_rating), int(raw_bonus)
    chance = 5*bonus - (rating-10)*5 + 50
    renormalized_chance = min(95, max(5, chance))
    if renormalized_chance == 5:
        print("\033[91m"  f"{renormalized_chance} % (crit only)"+"\033[0m" +f" chances to succed against a rating of {rating} with a {bonus} bonus.")
    elif renormalized_chance < 50:
        print("\033[93m"  f"{renormalized_chance} %"+"\033[0m" +f" chances to succed against a rating of {rating} with a {bonus} bonus.")
    else:
        print("\033[92m"  f"{renormalized_chance} %"+"\033[0m" +f" chances to succed against a rating of {rating} with a {bonus} bonus.")

def main():
    args = _parse()
    if args.debug:
        _printDebug(args)

    if args.DD:
        computeStats(*args.DD)

if __name__ == "__main__":
    # execute only if run as a script
    main()
