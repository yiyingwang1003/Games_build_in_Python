from tiles import Tiles


def test_constructor():
    ts = Tiles(4, 120)
    assert ts.SQUARE_NUM == 4
    assert ts.SQUARE == 120
    assert ts.color_to_go == 0
    assert ts.tiles[1][1].color == 255
    assert ts.tiles[2][1].color == 0
    assert ts.tiles[1][2].color == 0
    assert ts.tiles[2][2].color == 255
    assert ts.black_num == 2
    assert ts.white_num == 2


def test_calculate_candidates():
    ts = Tiles(4, 120)
    assert ts.candidates == {(0, 1): [(1, 1)], (2, 3): [(2, 2)],
                             (1, 0): [(1, 1)], (3, 2): [(2, 2)]}


def test_check_around():
    ts = Tiles(4, 120)
    assert ts.check_around(0, 1, 1, 0) == [(1, 1)]


def test_is_valid_candidate():
    ts = Tiles(4, 120)
    assert ts.is_valid_candidate(0, 1)
    assert not ts.is_valid_candidate(1, 1)


def test_get_candidates():
    ts = Tiles(4, 120)
    assert ts.get_candidates() == {(0, 1): [(1, 1)], (2, 3): [(2, 2)],
                                   (1, 0): [(1, 1)], (3, 2): [(2, 2)]}


def test_remain_valid_candidate():
    ts = Tiles(4, 120)
    assert ts.remain_valid_candidate()


def test_switch_turns():
    ts = Tiles(4, 120)
    ts.switch_turns()
    assert ts.color_to_go == 255


def test_update():
    ts = Tiles(4, 120)
    ts.update(0, 1)
    assert ts.tiles[0][1].color == 0
    assert ts.tiles[1][1].color == 0
    assert ts.black_num == 4
    assert ts.white_num == 1
    assert ts.color_to_go == 255
    assert ts.candidates == {(0, 2): [(1, 2)], (0, 0): [(1, 1)],
                             (2, 0): [(2, 1)]}


def test_black_tiles_num():
    ts = Tiles(4, 120)
    assert ts.black_tiles_num() == 2


def test_white_tiles_num():
    ts = Tiles(4, 120)
    assert ts.white_tiles_num() == 2


def test_total_tiles_num():
    ts = Tiles(4, 120)
    assert ts.total_tiles_num() == 4
