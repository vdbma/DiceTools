from DiceTools.main import computeStats

def test_computeStats():
    assert computeStats(10,0, display=False) == 55
    assert computeStats(8,-5, display=False) == 40
    assert computeStats(10,7, display=False) == 90

    # extreme cases
    assert computeStats(10, 555, display=False) == 95
    assert computeStats(-1000, 0, display=False) == 95

    assert computeStats(9999, 0, display=False) == 5
    assert computeStats(10, -400, display=False) == 5
