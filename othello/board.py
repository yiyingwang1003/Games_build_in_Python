from tiles import Tiles
from ai_player import AI
from file_update import fileUpdate
DEFAULT_VAL = 0
ONE = 1
THRESHOLD_SWITCH = 2


class Board:
    """Draws the board and handles interactions between players and tiles"""
    def __init__(self, WIDTH, HEIGHT,
                 SQUARE_NUM_IN_ROW, SQUARE_SIDE, game_controller):

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TOTAL_SQUARE_NUM = SQUARE_NUM_IN_ROW * SQUARE_NUM_IN_ROW
        self.SQUARE_SIDE = SQUARE_SIDE
        self.gc = game_controller
        self.switch_turns = DEFAULT_VAL
        self.tiles = Tiles(SQUARE_NUM_IN_ROW, SQUARE_SIDE)
        self.AI = AI(SQUARE_NUM_IN_ROW)
        self.file = fileUpdate("scores.txt")
        self.file_updated = False

    def AI_move_update(self):
        """Updates the AI's move and the game status"""
        if self.tiles.remain_valid_candidate():
            # decides the AI's best move
            self.AI.decide_best_move(self.tiles.get_candidates())
            # gets the coordinates of the best move
            x, y = self.AI.get_best_move()
            # updates the tiles, resets the number of switching turn
            # and updates game status
            self.tiles.update(x, y)
            self.reset_switch_turns()
            self.game_status_update()

    def human_move_update(self, mouse_x, mouse_y):
        """Updates the human player's move and the game status"""
        if not self.gc.human_turn:
            return
        # Gets the coordinates of the mouse pressed on,
        # and converts them to the corresponding indexes of nested list
        x = mouse_x // self.SQUARE_SIDE
        y = mouse_y // self.SQUARE_SIDE
        # Checks if the coordinates of the mouse pressed on
        # is one of the candidates
        if self.tiles.is_valid_candidate(x, y):
            # if the place pressed on is a candidate,
            # updates the tiles, resets the number of switching turn
            # and updates game status
            self.tiles.update(x, y)
            self.reset_switch_turns()
            self.game_status_update()

    # defines a method to check if the game need to switch turns
    def need_switch_turns(self):
        if not self.tiles.remain_valid_candidate():
            return True
        return False

    # defines a method to update the players' turn and update game status
    def switch_turns_update(self):
        self.switch_turns += ONE
        self.tiles.switch_turns()
        self.game_status_update()

    # defines a method to reset the number of switching turn
    def reset_switch_turns(self):
        self.switch_turns = DEFAULT_VAL

    def game_status_update(self):
        """Updates the game status"""
        if self.gc.game_over:
            # When the game is over,
            # updates the player's name and score to the file
            if not self.file_updated:
                human_player_name = input('enter your name')
                self.file.update_file(human_player_name,
                                      self.tiles.black_tiles_num())
                self.file_updated = True
            return

        # switches the players' turn displayed on the screen
        if self.gc.human_turn:
            self.gc.human_turn = False
            self.gc.AI_turn = True
        else:
            self.gc.human_turn = True
            self.gc.AI_turn = False

        # If there is no more places on the board to put any tile,
        # or there is no legal move for both players
        # (the players' turn has already switched twice),
        # let the game over and decides the winner
        if ((self.tiles.total_tiles_num() == self.TOTAL_SQUARE_NUM) or
                (self.switch_turns >= THRESHOLD_SWITCH)):
            self.gc.game_over = True
            self.gc.display_turn = False
            self.gc.human_turn = False
            self.gc.AI_turn = False
            self.gc.human_score = self.tiles.black_tiles_num()

            if self.tiles.black_tiles_num() > self.tiles.white_tiles_num():
                self.gc.black_wins = True

            elif self.tiles.black_tiles_num() < self.tiles.white_tiles_num():
                self.gc.white_wins = True

            else:
                self.gc.tie = True

    def display(self):
        """ Draws the board and shows the tiles on the board"""
        self.tiles.display()

        stroke(0)
        strokeWeight(2)

        for i in range(self.WIDTH // self.SQUARE_SIDE):
            line(0, self.SQUARE_SIDE*(i+1), self.WIDTH, self.SQUARE_SIDE*(i+1))

        for i in range(self.HEIGHT // self.SQUARE_SIDE):
            line(self.SQUARE_SIDE*(i+1), 0,
                 self.SQUARE_SIDE*(i+1), self.HEIGHT)


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
