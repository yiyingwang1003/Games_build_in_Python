from board import Board
from game_controller import GameController

SQUARE_NUM_IN_ROW = 8
SQUARE_SIDE = 120
BOARD_WIDTH = SQUARE_NUM_IN_ROW * SQUARE_SIDE
BOARD_HEIGHT = BOARD_WIDTH
WINDOW_WIDTH = BOARD_WIDTH + 300
WINDOW_HEIGHT = BOARD_HEIGHT
AI_DELAY = 180
SWITCH_DELAY = 120

game_controller = GameController(BOARD_WIDTH,
                                 WINDOW_WIDTH, WINDOW_HEIGHT)

bd = Board(BOARD_WIDTH, BOARD_HEIGHT, SQUARE_NUM_IN_ROW,
           SQUARE_SIDE, game_controller)

AI_delay_counter = AI_DELAY
switch_delay_counter = SWITCH_DELAY


def setup():
    size(WINDOW_WIDTH, WINDOW_HEIGHT)


def draw():
    global AI_delay_counter, switch_delay_counter
    background(255)
    rectMode(CORNER)
    fill(0, 128, 0)
    rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT)
    bd.display()
    game_controller.update()
    if bd.need_switch_turns():
        switch_delay_counter -= 1
    if (switch_delay_counter == 0):
        bd.switch_turns_update()
        switch_delay_counter = SWITCH_DELAY

    if game_controller.AI_turn:
        AI_delay_counter -= 1
    if (AI_delay_counter == 0):
        bd.AI_move_update()
        AI_delay_counter = AI_DELAY


def mousePressed():
    bd.human_move_update(mouseX, mouseY)
