########################
# Where the cells exist
########################
import random


class Map():
    def __init__(self):
        self.grid = [[1, 0, 0, 0, 0, 0],
                     [2, 0, 0, 0, 0, 0],
                     [3, 0, 5, 0, 0, 0],
                     [4, 0, 0, 0, 0, 0],
                     [5, 0, 0, 0, 0, 0],
                     [6, 0, 0, 0, 0, 0]]
        self.grid_size = 6

    def create_life(self):
        for row_index, row in enumerate(self.grid):
            print("len of row = {}".format(len(row)))
            for col_index, col in enumerate(row):
                print("Col = {}".format(col))
                row[col_index] = random.randint(0, 1)
            print(row)

    """scans the grid and identifies
    who is near who"""

    def get_cell_position_data(self):
        pass


if __name__ == "__main__":
    f = Map()
    f.create_life()
