from board import Board
from game_controller import GameController


def test_constructor():
    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    assert bd.WIDTH == 480
    assert bd.HEIGHT == 480
    assert bd.TOTAL_SQUARE_NUM == 4 * 4
    assert bd.SQUARE_SIDE == 120
    assert bd.switch_turns == 0
    assert bd.gc is g
    assert not bd.file_updated
    assert bd.AI.get_best_move() == (-1, -1)
    assert bd.tiles.total_tiles_num() == 4


def test_human_move_update():
    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    bd.human_move_update(10, 10)
    assert bd.tiles.total_tiles_num() == 4
    assert bd.tiles.black_tiles_num() == 2
    assert bd.gc.human_turn
    assert not bd.gc.AI_turn
    assert bd.tiles.color_to_go == 0
    bd.human_move_update(10, 130)
    assert bd.tiles.total_tiles_num() == 5
    assert bd.tiles.black_tiles_num() == 4
    assert not bd.gc.human_turn
    assert bd.gc.AI_turn
    assert bd.tiles.color_to_go == 255


def test_need_switch_turns():
    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    assert not bd.need_switch_turns()
    bd.tiles.candidates = {}
    assert bd.need_switch_turns()


def test_switch_turns_update():
    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    bd.switch_turns_update()
    assert bd.switch_turns == 1
    assert bd.tiles.color_to_go == 255
    assert bd.gc.AI_turn
    assert not bd.gc.human_turn


def test_reset_switch_turns():
    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    bd.switch_turns_update()
    assert bd.switch_turns == 1
    bd.reset_switch_turns()
    assert bd.switch_turns == 0


def test_game_status_update():
    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    bd.game_status_update()
    assert not bd.gc.human_turn
    assert bd.gc.AI_turn

    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    bd.tiles.black_num = 10
    bd.tiles.white_num = 6
    bd.game_status_update()
    assert not bd.gc.human_turn
    assert not bd.gc.AI_turn
    assert bd.gc.game_over
    assert not bd.gc.display_turn
    assert bd.gc.human_score == 10
    assert bd.gc.black_wins
    assert not bd.gc.white_wins
    assert not bd.gc.tie

    g = GameController(480, 780, 480)
    bd = Board(480, 480, 4, 120, g)
    bd.switch_turns = 2
    bd.game_status_update()
    assert not bd.gc.human_turn
    assert not bd.gc.AI_turn
    assert bd.gc.game_over
    assert not bd.gc.display_turn
    assert bd.gc.human_score == 2
    assert not bd.gc.black_wins
    assert not bd.gc.white_wins
    assert bd.gc.tie
