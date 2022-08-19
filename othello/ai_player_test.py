from ai_player import AI


def test_constructor():
    ai = AI(4)
    assert ai.SQUARE_NUM == 4
    assert ai.corner_set == {0, 4-1}
    assert ai.x == -1
    assert ai.y == -1


def test_decide_best_move():
    ai = AI(4)
    candidates = {(0, 3): [(1, 2), (2, 2)], (1, 0): [(1, 2)],
                  (1, 3): [(1, 2), (2, 2), (2, 3)]}
    ai.decide_best_move(candidates)
    assert ai.x == 0
    assert ai.y == 3

    ai = AI(4)
    candidates = {(0, 2): [(1, 2), (2, 2)], (1, 0): [(1, 2)],
                  (1, 3): [(1, 2), (2, 2), (2, 3)]}
    ai.decide_best_move(candidates)
    assert ai.x == 1
    assert ai.y == 3


def test_get_best_move():
    ai = AI(4)
    assert ai.get_best_move() == (-1, -1)
    candidates = {(0, 3): [(1, 2), (2, 2)], (1, 0): [(1, 2)],
                  (1, 3): [(1, 2), (2, 2), (2, 3)]}
    ai.decide_best_move(candidates)
    assert ai.get_best_move() == (0, 3)
