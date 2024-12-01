import argparse
import sys
import re
import numpy as np
import numpy.random as nr


def _parse():
    parser = argparse.ArgumentParser(
        description="Use this programm to compute properties of dice rolls !"
    )

    parser.add_argument(
        "-d",
        "--DD",
        type=str,
        nargs="+",
        help="DD challenge [rating] [bonus]: returns the probability to pass the challenge.",
    )
    parser.add_argument("-A", action="store_true", help="Advatage for the DD challenge")
    parser.add_argument(
        "-D", action="store_true", help="Disadvantage for the DD challenge"
    )

    parser.add_argument(
        "-a",
        "--average",
        type=str,
        nargs="+",
        help="Compute average [kdn] <+ k'dn' + ...> <+ j>: Computes the average of a complex roll ",
    )
    parser.add_argument(
        "-s",
        "--statistics",
        type=str,
        nargs="+",
        help="Compute distribution [kdn] <+ k'dn' + ...> <+ j>: Computes the distribution of a comlex roll ",
    )
    parser.add_argument(
        "-r",
        "--roll",
        type=str,
        nargs="+",
        help="Dice roller [kdn] <+ k'dn' + ...> <+ j>",
    )
    parser.add_argument(
        "-w",
        "--wait",
        type=int,
        help="Expectation value #rolls for save roll with WAIT [bonus/malus].",
    )

    parser.add_argument(
        "--mpl", action="store_true", help="Uses matplotlib to plot statistics"
    )

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
            print(
                arg,
                "\t \t \t",
                type(getattr(args, arg)),
                "\t \t",
                getattr(args, arg),
                sep="",
            )
        else:
            print(
                arg,
                "\t \t",
                type(getattr(args, arg)),
                "\t \t",
                getattr(args, arg),
                sep="",
            )
    print("\nSystem exec : ", sys.executable)
    print("***********************************************************************")


def computeStats(raw_rating, raw_bonus, *, display=True, adv=False, disadv=False):
    """succedes on equality"""
    rating, bonus = int(raw_rating), int(raw_bonus)

    adv_str = ""
    chance = min(100, max(0, 5 * bonus - (rating - 10) * 5 + 55))

    if adv:
        chance = 2 * chance - chance * chance / 100
        renormalized_chance = min(99.75, max(0.25, chance))
        adv_str = " \033[92m" + "with advantage" + "\033[0m"
    elif disadv:
        chance = chance * chance / 100
        renormalized_chance = min(99.75, max(0.25, chance))
        adv_str = " \033[91m" + "with disadvantage" + "\033[0m"
    else:
        renormalized_chance = min(95, max(5, chance))

    if display:
        disp_bonus = str(bonus)
        if bonus >= 0:
            disp_bonus = "+" + disp_bonus

        if renormalized_chance == 5:
            print(
                "\033[91m"
                f"{renormalized_chance:.2f} % (crit only)"
                + "\033[0m"
                + f" chances to succed against a rating of {rating} with a {disp_bonus} bonus{adv_str}."
            )
        elif renormalized_chance < 50:
            print(
                "\033[93m"
                f"{renormalized_chance:.2f} %"
                + "\033[0m"
                + f" chances to succed against a rating of {rating} with a {disp_bonus} bonus{adv_str}."
            )
        else:
            print(
                "\033[92m"
                f"{renormalized_chance:.2f} %"
                + "\033[0m"
                + f" chances to succed against a rating of {rating} with a {disp_bonus} bonus{adv_str}."
            )

    return renormalized_chance


def parseRoll(raw_roll):
    """parses dice rolls"""
    roll = ""
    for item in raw_roll:
        if "+" in item or "-" in item:
            for r in re.split("([+-])", item):
                roll += r.strip(" ")
        else:
            roll += item.strip(" ")

    summands = re.split(
        "([+-])", roll
    )  # [] for a list of possible separators, () to keep them
    return summands


def computeDice(raw_roll):
    """computed the average of the roll"""
    tot = 0
    summands = parseRoll(raw_roll)
    # print(f"{summands = }")
    sign = 1
    for elt in summands:
        if isDie(elt):
            tot += avgDice(elt) * sign
            sign = 1
        elif isNumber(elt):
            tot += int(elt) * sign
            sign = 1
        if elt == "-":
            sign = -1
    print(f"Roll : {' '.join(summands)}\n" f"Average : {tot}")
    return tot


def computeDistribution(raw_roll):
    summands = parseRoll(raw_roll)

    dice_list = []
    add = 0
    sign = 1
    min_val = 1

    for elt in summands:
        if isDie(elt):
            n_dice, n_faces = elt.split("d")
            n_dice = int(n_dice)
            n_faces = int(n_faces)
            dice_list += [np.ones((n_faces)) / n_faces] * n_dice
            if sign < 0:
                min_val += -n_dice * n_faces
            else:
                min_val += n_dice

            sign = 1
        elif isNumber(elt):
            add += int(elt) * sign
            min_val += add
            sign = 1
        elif elt == "-":
            sign = -1

    dist = 1

    for d in dice_list:
        dist = np.convolve(dist, d)

    res = np.arange(len(dist)) + min_val - 1

    return res, dist


def plotDistribution(res, dist, *, useMpl=False):
    if useMpl:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.plot(res, dist * 100, ".")
        ax.set_xlabel("Result")
        ax.set_ylabel("Probability (%)")
        plt.show()
    else:
        b = "█"
        width_norm = 250
        left_width = 10
        s = "Distribution :\n"
        for r, p in zip(res, dist):
            s += (
                f"{r}:".ljust(5)
                + f"{p*100:.1f} %".ljust(left_width, " ")
                + int(p * width_norm) * b
                + "\n"
            )
        print(s)


def isDie(s):
    """returns whether a string is a dice roll"""
    die_expr = re.compile(r"\d+d\d+")
    return die_expr.match(s) is not None


def isNumber(s):
    """returns whether a string is a dice roll"""
    nb_expr = re.compile(r"\d+")
    return nb_expr.match(s) is not None


def avgDice(dice):
    n_dice, n_faces = dice.split("d")
    return int(n_dice) * (int(n_faces) + 1) / 2


def rollDie(dice):
    n_dice, n_faces = dice.split("d")
    return [nr.randint(int(n_faces)) + 1 for _ in range(int(n_dice))]


def computeRoll(raw_roll):
    summands = parseRoll(raw_roll)

    tot = 0
    results = []
    sign = 1
    for elt in summands:
        if isDie(elt):
            roll = rollDie(elt)
            results += roll
            tot += np.sum(roll) * sign
            sign = 1
        elif isNumber(elt):
            tot += int(elt) * sign
            sign = 1
        if elt == "-":
            sign = -1

    print(f"Roll : {' '.join(summands)}\n" f"Result : {tot} {tuple(results)}")

    return tot


def computeExpectationWait(bonus):
    """
    P(X = n) = p(1-p)^(n-1)
    Hence the expectation value is 1/p
    """

    p = max(min(bonus * 0.05 + 0.55, 0.95), 0.05)

    disp_bonus = str(bonus)
    if bonus >= 0:
        disp_bonus = "+" + disp_bonus

    exp = 1 / p

    if p == 0.95:  # always succeds on 20
        print(
            f"For a saving throw with bonus {disp_bonus}, the expected number of rolls is \033[92m{exp:.2f}\033[0m."
        )
    elif p == 0.05:  # always fails on 1
        print(
            f"For a saving throw with bonus {disp_bonus}, the expected number of rolls is \033[91m"
            f"{exp:.2f}"
            "\033[0m."
        )
    else:
        print(
            f"For a saving throw with bonus {disp_bonus}, the expected number of rolls is \033[93m{exp:.2f}\033[0m."
        )

    return exp


def main():
    exit = False
    args = _parse()
    if args.debug:
        _printDebug(args)

    if args.A and args.D:
        print("\033[91mERROR :  Can't have both advantage and disadvantage.\033[0m")
        exit = True

    if args.DD and not exit:
        computeStats(*args.DD, adv=args.A, disadv=args.D)

    elif args.average and not exit:
        computeDice(args.average)

    elif args.statistics and not exit:
        computeDice(args.statistics)
        plotDistribution(*computeDistribution(args.statistics), useMpl=args.mpl)

    if args.roll and not exit:
        computeRoll(args.roll)

    if args.wait is not None and not exit:
        computeExpectationWait(args.wait)


if __name__ == "__main__":
    # execute only if run as a script
    main()
