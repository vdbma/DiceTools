from DiceTools.main import computeStats, avgDice, isDie, computeDice, rollDie


def test_computeStats():
    assert computeStats(10, 0, display=False) == 55
    assert computeStats(8, -5, display=False) == 40
    assert computeStats(10, 7, display=False) == 90

    # extreme cases
    assert computeStats(10, 555, display=False) == 95
    assert computeStats(-1000, 0, display=False) == 95

    assert computeStats(9999, 0, display=False) == 5
    assert computeStats(10, -400, display=False) == 5


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
