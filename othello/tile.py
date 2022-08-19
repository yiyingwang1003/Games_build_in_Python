COLOR_BLACK = 0
TILE_WIDTH = 100
TILE_HEIGHT = 100


class Tile:
    """A tile"""
    def __init__(self, color, x, y, SQUARE):
        self.color = color
        self.x = SQUARE * x + SQUARE / 2
        self.y = SQUARE * y + SQUARE / 2

    def display(self):
        """Draw the tile"""
        stroke(COLOR_BLACK)
        strokeWeight(2)
        fill(self.color)
        ellipse(self.x, self.y, TILE_WIDTH, TILE_HEIGHT)
