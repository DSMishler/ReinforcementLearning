import numpy as np

class Pacman:
    def __init__(self, grid):
        self.pos_x = 0
        self.pos_y = 0
        self.neighbors = [[1,0],[0,1], [-1,0], [0,-1]] #Maybe useful later
        grid.agent_ID[self.pos_x,self.pos_y] = 1 #Initialize where he is
        return

    def move(self, dest_x, dest_y, grid):
        grid.agent_ID[self.pos_x,self.pos_y] = 0
        self.pos_x = dest_x
        self.pos_y = dest_y
        grid.agent_ID[self.pos_x,self.pos_y] = 1
        return