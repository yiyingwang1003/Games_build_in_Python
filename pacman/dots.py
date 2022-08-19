from dot import Dot


class Dots:
    """A collection of dots."""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.top_row)):
            self.top_row[i].display()
        for i in range(0, len(self.bottom_row)):
            self.bottom_row[i].display()
        for i in range(0, len(self.left_col)):
            self.left_col[i].display()
        for i in range(0, len(self.right_col)):
            self.right_col[i].display()

    # TODO:
    # PROBLEM 3: implement dot eating
    # BEGIN CODE CHANGES
    def eat(self, x, y):  # Pass in the position of PacMan
        self.row_dot_remove(self.top_row, self.WIDTH, y, x)
        self.row_dot_remove(self.bottom_row, self.WIDTH, y, x)
        self.col_dot_remove(self.left_col, self.HEIGHT, x, y)
        self.col_dot_remove(self.right_col, self.HEIGHT, x, y)

    # defines the method to remove the dots on the rows
    def row_dot_remove(self, row, max_coord, fixed_coord, changing_coord):
        # Goes through all the dots on the row
        for dot in row:
            # If the PacMan is near the dot,
            # remove the dot from the row
            if abs(dot.y - fixed_coord) <= self.EAT_DIST:
                if abs(dot.x - changing_coord) <= self.EAT_DIST:
                    row.remove(dot)
                # Deal with the edge cases:
                # If PacMan goes near the left edge of the row,
                # and there exists a dot near the right edge of the row,
                # remove that dot from the row
                elif(abs(changing_coord - 0) <= self.EAT_DIST and
                        abs(max_coord - dot.x) <= self.EAT_DIST):
                    row.remove(dot)
                # If PacMan goes near the right edge of the row,
                # and there exists a dot near the left edge of the row,
                # remove that dot from the row
                elif (abs(changing_coord - max_coord) <= self.EAT_DIST and
                        abs(dot.x) <= self.EAT_DIST):
                    row.remove(dot)

    # defines the method to remove the dots on the columns
    def col_dot_remove(self, col, max_coord, fixed_coord, changing_coord):
        # Goes through all the dots on the column
        for dot in col:
            # If the PacMan is near the dot,
            # remove the dot from the column
            if abs(dot.x - fixed_coord) <= self.EAT_DIST:
                if abs(dot.y - changing_coord) <= self.EAT_DIST:
                    col.remove(dot)
                # Deal with the edge cases:
                # If PacMan goes near the top edge of the column,
                # and there exists a dot on the bottom edge of the column,
                # remove that dot from the column
                elif(abs(changing_coord - 0) <= self.EAT_DIST and
                        abs(max_coord - dot.y) <= self.EAT_DIST):
                    col.remove(dot)
                # If PacMan goes near the bottom edge of the column,
                # and there exists a dot on the top edge of the column,
                # remove that dot from the column
                elif (abs(changing_coord - max_coord) <= self.EAT_DIST and
                        abs(dot.y) <= self.EAT_DIST):
                    col.remove(dot)
    # END CODE CHANGES

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return (len(self.top_row) +
                len(self.bottom_row) +
                len(self.left_col) +
                len(self.right_col))
