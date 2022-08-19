TILE_WIDTH = 100
TILE_HEIGHT = 100
COLOR_BLACK = 0
COLOR_WHITE = 255
DEFAULT_VAL = 0


class GameController:
    """Maintains the state of the game."""
    def __init__(self, BOARD_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.ABS_WIDTH = WINDOW_WIDTH - BOARD_WIDTH
        self.BOARD_WIDTH = BOARD_WIDTH
        self.HEIGHT = WINDOW_HEIGHT
        self.display_turn = True
        self.human_turn = True
        self.AI_turn = False
        self.game_over = False
        self.tie = False
        self.black_wins = False
        self.white_wins = False
        self.human_score = DEFAULT_VAL

    def update(self):
        """Carries out necessary actions"""
        fill(0)
        textSize(20)
        text("Welcome to Othello!", self.BOARD_WIDTH+40, 100)
        if self.display_turn and self.human_turn:
            fill(0)
            textSize(20)
            text("YOUR TURN", self.BOARD_WIDTH+100, self.HEIGHT/2)
            self.display_tile(COLOR_BLACK)
        if self.display_turn and self.AI_turn:
            fill(0)
            textSize(20)
            text("AI TURN", self.BOARD_WIDTH+100, self.HEIGHT/2)
            self.display_tile(COLOR_WHITE)
        if self.game_over and self.black_wins:
            fill(255, 0, 0)
            textSize(20)
            text("YOU WIN!", self.BOARD_WIDTH+50, self.HEIGHT/2)
            self.display_human_score()

        if self.game_over and self.white_wins:
            fill(255, 0, 0)
            textSize(20)
            text("AI WINS.", self.BOARD_WIDTH+50, self.HEIGHT/2)
            self.display_human_score()

        if self.game_over and self.tie:
            fill(255, 0, 0)
            textSize(30)
            text("TIE", self.BOARD_WIDTH+100, self.HEIGHT/2)
            self.display_human_score()

    def display_tile(self, color):
        stroke(0)
        strokeWeight(2)
        fill(color)
        ellipse(self.BOARD_WIDTH+self.ABS_WIDTH/2, self.HEIGHT/2+100,
                TILE_WIDTH, TILE_HEIGHT)

    def display_human_score(self):
        res_to_print = "YOUR SCORE:"+str(self.human_score)
        text(res_to_print, self.BOARD_WIDTH+50, self.HEIGHT/2+100)
