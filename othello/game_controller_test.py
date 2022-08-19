from game_controller import GameController


def test_constructor():
    gc = GameController(480, 780, 480)
    assert gc.ABS_WIDTH == 780 - 480
    assert gc.BOARD_WIDTH == 480
    assert gc.HEIGHT == 480
    assert gc.display_turn
    assert gc.human_turn
    assert not gc.AI_turn
    assert not gc.game_over
    assert not gc.tie
    assert not gc.black_wins
    assert gc.human_score == 0
