from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    g = GameController(600, 600)
    m = Maze(600, 600, 150, 450,
             150, 450, g)
    total_number_of_dots = ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                            (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)
    m.eat_dots(75, 450)
    assert m.dots.dots_left() == total_number_of_dots - 1
    # test for the dot located at the intersection
    m.eat_dots(150, 150)
    assert m.dots.dots_left() == total_number_of_dots - 3
    # test for the edge cases
    m.eat_dots(0, 450)
    assert m.dots.dots_left() == total_number_of_dots - 5
