import numpy as np

class Pacman:
    def __init__(self, grid):
        self.pos_x = 0
        self.pos_y = 0
        self.neighbors = [[1,0],[0,1], [-1,0], [0,-1]]
        return

    def move_me(self, dest_x, dest_y):
        self.pos_x = dest_x
        self.pos_y = dest_y
        return

    def move(self, grid):
        return