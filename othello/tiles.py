from tile import Tile
COLOR_BLACK = 0
COLOR_WHITE = 255
DEFAULT_VAL = 0
INIT_NUM = 2
DIVIDE_NUM = 2
ONE = 1
ZERO = 0


class Tiles:
    """ A collection of tiles"""
    def __init__(self, SQUARE_NUM, SQUARE):
        self.SQUARE_NUM = SQUARE_NUM
        self.SQUARE = SQUARE
        # Sets the first move for black color
        self.color_to_go = COLOR_BLACK
        # Initializes the nested list for all the tiles
        self.tiles = [[DEFAULT_VAL for _ in range(SQUARE_NUM)]
                      for _ in range(SQUARE_NUM)]
        mid_x1 = SQUARE_NUM // DIVIDE_NUM - ONE
        mid_x2 = mid_x1 + ONE
        mid_y1 = SQUARE_NUM // DIVIDE_NUM - ONE
        mid_y2 = mid_y1 + ONE
        # Draws the first 4 tiles in the middle
        self.tiles[mid_x1][mid_y1] = Tile(COLOR_WHITE, mid_x1, mid_y1, SQUARE)
        self.tiles[mid_x2][mid_y1] = Tile(COLOR_BLACK, mid_x2, mid_y1, SQUARE)
        self.tiles[mid_x1][mid_y2] = Tile(COLOR_BLACK, mid_x1, mid_y2, SQUARE)
        self.tiles[mid_x2][mid_y2] = Tile(COLOR_WHITE, mid_x2, mid_y2, SQUARE)
        self.black_num = INIT_NUM
        self.white_num = INIT_NUM
        self.candidates = {}
        # Calculates the candidates for the first move(the first human turn)
        self.calculate_candidates()

    def display(self):
        """Draws all the tiles"""
        for i in range(self.SQUARE_NUM):
            for j in range(self.SQUARE_NUM):
                if self.tiles[i][j]:
                    self.tiles[i][j].display()

    def calculate_candidates(self):
        """Gets all the candidates that can be placed
        the current player's tile on,
        and corresponding coordinates of the opponent's tiles
        which can be flipped"""
        # uses nested loop to go through all the squares on board,
        # to check if a square is a candidate for the next legal move
        for i in range(self.SQUARE_NUM):
            for j in range(self.SQUARE_NUM):
                # Initializes a temporary list for a square,
                # which stores its corresponding coordinates of
                # the opponent's tiles that can be flipped
                ij_opponents = []
                # checks 8 directions of this square to find any possible
                # coordinates of the opponent's tiles that can be flipped
                for direct_i in range(-1, 2):
                    for direct_j in range(-1, 2):
                        # it's more readable using -1, 0, 2 here
                        # to indicate the location and direction
                        if not (direct_i == 0 and direct_j == 0):
                            ij_opponents += \
                                self.check_around(i, j, direct_i, direct_j)
                # if a square is a candidate, stores its coordinates and all
                # the corresponding opponent's tiles that can be flipped
                if ij_opponents:
                    self.candidates[(i, j)] = ij_opponents

    def check_around(self, x, y, direct_x, direct_y):
        """Checks if a square could flip any opponent's tiles
        in a specific direction,
        returns all the opponents that can be flipped"""
        # Initializes a list to store the coordinates of the opponent's tiles
        # that can be flipped
        opponents = []
        # if the square does not have a tile on it,
        # and in the given direction, there are adjacent opponent's tiles
        # with a tile owned by current player,
        # stores and returns the list.
        if not self.tiles[x][y]:
            x += direct_x
            y += direct_y
            # it's more readable using 0 here
            # to indicate the boundary
            while ((0 <= x and x < self.SQUARE_NUM) and
                    (0 <= y and y < self.SQUARE_NUM)):
                if self.tiles[x][y]:
                    if self.tiles[x][y].color != self.color_to_go:
                        opponents.append((x, y))
                        x += direct_x
                        y += direct_y
                    else:
                        return opponents
                else:
                    break

        return []

    def is_valid_candidate(self, x, y):
        """Checks if the passed in coordinate is one of the candidates"""
        return (x, y) in self.candidates

    def get_candidates(self):
        return self.candidates

    def remain_valid_candidate(self):
        """Checks if there is any candidate for the next move"""
        return len(self.candidates) != DEFAULT_VAL

    def switch_turns(self):
        """Switches the color to go and updates the candidates"""
        if self.color_to_go == COLOR_BLACK:
            self.color_to_go = COLOR_WHITE
        else:
            self.color_to_go = COLOR_BLACK

        self.candidates.clear()
        self.calculate_candidates()

    def update(self, x, y):
        """Updates the tiles"""
        if self.color_to_go == COLOR_BLACK:
            self.tiles[x][y] = Tile(COLOR_BLACK, x, y, self.SQUARE)
            for coords in self.candidates[(x, y)]:
                self.tiles[coords[ZERO]][coords[ONE]].color = COLOR_BLACK
            self.color_to_go = COLOR_WHITE
            self.black_num += (ONE + len(self.candidates[(x, y)]))
            self.white_num -= len(self.candidates[(x, y)])

        else:
            self.tiles[x][y] = Tile(COLOR_WHITE, x, y, self.SQUARE)
            for coords in self.candidates[(x, y)]:
                self.tiles[coords[ZERO]][coords[ONE]].color = COLOR_WHITE
            self.color_to_go = COLOR_BLACK
            self.white_num += (ONE + len(self.candidates[(x, y)]))
            self.black_num -= len(self.candidates[(x, y)])

        self.candidates.clear()
        self.calculate_candidates()

    def black_tiles_num(self):
        return self.black_num

    def white_tiles_num(self):
        return self.white_num

    def total_tiles_num(self):
        return self.black_num + self.white_num
