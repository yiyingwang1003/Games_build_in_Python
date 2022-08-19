from tile import Tile


def test_constructor():
    t = Tile(0, 0, 0, 120)
    assert t.color == 0
    assert t.x == 120 * 0 + 120 / 2
    assert t.y == 120 * 0 + 120 / 2

    t = Tile(0, 1, 3, 120)
    assert t.color == 0
    assert t.x == 120 * 1 + 120 / 2
    assert t.y == 120 * 3 + 120 / 2
