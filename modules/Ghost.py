import numpy as np

class Ghost:
    def __init__(self, grid):
        self.pos_x = grid.ghost_ID.shape[0]-1
        self.pos_y = grid.ghost_ID.shape[1]-1
        self.hidden_variable = False
        self.neighbors = [] #to use later
        self.weights = [] # to use later
        self.ID = -1 # to change later
        grid.ghost_ID[self.pos_x, self.pos_y] = self.ID
        return
    
    def move(self, dest_x, dest_y, grid):
        grid.ghost_ID[self.pos_x, self.pos_y] = 0 # clean up where he was
        self.pos_x = dest_x
        self.pos_y = dest_y
        grid.ghost_ID[self.pos_x, self.pos_y] = self.ID # Note where he went
        return
    
    def findPac(self,grid):
        # find where Pacman is at on the grid
        for i in range(grid.ghost_ID.shape[0]):
            for j in range(grid.ghost_ID.shape[1]):
                if grid.agent_ID[i][j] == 1:
                    return(i,j)
    
    # this function assumes that the ghost is NOT on top of pacman already
    def chase(self, grid):
        (pac_pos_x, pac_pos_y) = self.findPac(grid)
        pac_diff_x = pac_pos_x-self.pos_x
        pac_diff_y = pac_pos_y-self.pos_y
        moveAngle = np.arctan(pac_diff_x / pac_diff_y)
        if(moveAngle <= -np.pi/4 or moveAngle >= np.pi/4):
            if(pac_diff_x > 0):
                self.move(self.pos_x+1, self.pos_y, grid)
            else:
                self.move(self.pos_x-1, self.pos_y, grid)
        else:
            if(pac_diff_y > 0):
                self.move(self.pos_x, self.pos_y+1, grid)
            else:
                self.move(self.pos_x, self.pos_y-1, grid)
        
        