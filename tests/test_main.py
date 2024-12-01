from DiceTools.main import (
    computeStats,
    avgDice,
    isDie,
    computeDice,
    rollDie,
    computeExpectationWait,
    computeDistribution,
)
import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal_nulp


def test_computeStats():
    assert computeStats(10, 0, display=False) == 55
    assert computeStats(8, -5, display=False) == 40
    assert computeStats(10, 7, display=False) == 90

    # extreme cases
    assert computeStats(10, 555, display=False) == 95
    assert computeStats(-1000, 0, display=False) == 95

    assert computeStats(9999, 0, display=False) == 5
    assert computeStats(10, -400, display=False) == 5

    # advantage / disadvantage

    assert computeStats(10, 0, display=False, adv=True) == 79.75
    assert computeStats(8, -5, display=False, adv=True) == 64
    assert computeStats(10, 7, display=False, adv=True) == 99
    assert computeStats(10, 30, display=False, adv=True) == 99.75
    assert computeStats(10, -50, display=False, adv=True) == 0.25

    assert computeStats(10, 0, display=False, disadv=True) == 30.25
    assert computeStats(8, -5, display=False, disadv=True) == 16
    assert computeStats(10, 7, display=False, disadv=True) == 81
    assert computeStats(10, 30, display=False, disadv=True) == 99.75
    assert computeStats(10, -50, display=False, disadv=True) == 0.25


def test_avgDice():
    assert avgDice("1d10") == 5.5
    assert avgDice("2d10") == 11
    assert avgDice("1d2") == 1.5
    assert avgDice("1d256") == 128.5
    assert avgDice("6d6") == 21


def test_isDie():
    assert isDie("1d6")
    assert isDie("515d52")
    assert not isDie("1d")
    assert not isDie("d6")
    assert not isDie("568")


def test_computeDice():
    assert computeDice("1d6") == 3.5
    assert computeDice("2d20") == 21
    assert computeDice("-3d8") == -13.5
    assert computeDice("1d6+3") == 6.5
    assert computeDice("1d6-5") == -1.5
    assert computeDice("1d20 + 7") == 17.5

    assert computeDice("1d6+3+ 7d8   +14 -5+12d18- 3") == 158  # with odd spacing

    assert computeDice(["1d20", "+", "7"]) == 17.5
    assert computeDice(["1d20 + 7"]) == 17.5


def test_rollDie():
    assert rollDie("1d1") == [1]
    assert rollDie("53d1") == [1] * 53
    assert len(rollDie("67d20")) == 67


def test_computeExpectationWait():
    assert np.isclose(computeExpectationWait(-20), 20.0)
    assert np.isclose(computeExpectationWait(-5), 10 / 3)
    assert np.isclose(computeExpectationWait(-1), 2)
    assert np.isclose(computeExpectationWait(5), 1.25)
    assert np.isclose(computeExpectationWait(21), 20 / 19)


def test_computeDistribution():
    res, dis = computeDistribution("1d6")
    assert_array_equal(res, np.arange(6) + 1)
    assert_array_equal(dis, np.ones((6)) / 6)

    res, dis = computeDistribution("2d6")
    assert_array_almost_equal_nulp(res, np.arange(2, 13))
    assert_array_almost_equal_nulp(
        dis, np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36
    )

    res, dis = computeDistribution("2d4 + 3")
    assert_array_almost_equal_nulp(res, np.arange(2, 9) + 3)
    assert_array_almost_equal_nulp(dis, np.array([1, 2, 3, 4, 3, 2, 1]) / 16)
