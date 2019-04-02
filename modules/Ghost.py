
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
        
        