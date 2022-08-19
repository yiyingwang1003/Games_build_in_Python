DEFAULT_VAL = -1
ZERO = 0
ONE = 1


class AI:
    def __init__(self, SQUARE_NUM):
        self.SQUARE_NUM = SQUARE_NUM
        self.corner_set = {ZERO, SQUARE_NUM - ONE}
        self.x = DEFAULT_VAL
        self.y = DEFAULT_VAL

    def decide_best_move(self, candidates):
        """Uses two methods to find the best move for AI"""
        # method 1:
        # if there is a chance to place a tile in the corners,
        # do it.
        # (The most important tip to win Othello is trying to
        # put the tiles in the corners of the board, because
        # the tiles played in the corners can never be flipped,
        # and on the contrary, they can flip a great amount of
        # the tiles of the opponent.)
        for i in self.corner_set:
            for j in self.corner_set:
                if (i, j) in candidates:
                    self.x = i
                    self.y = j
                    return
        # method 2:
        # if there is no chance for applying method 1,
        # do the "greedy" move.
        # find the move that can flip the most tiles of the opponent.
        temp_num = ZERO
        for key in candidates.keys():
            if len(candidates[key]) > temp_num:
                temp_num = len(candidates[key])
                self.x = key[ZERO]
                self.y = key[ONE]

    def get_best_move(self):
        return self.x, self.y
