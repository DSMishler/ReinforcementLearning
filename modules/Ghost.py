
class Ghost:
    def __init__(self, grid):
        self.pos_x = grid.agent_ID.shape[0]-1
        self.pos_y = grid.agent_ID.shape[1]-1
        self.hidden_variable = False
        self.neighbors = [] #to use later
        self.weights = [] # to use later
        self.ID = 9 # to change later
    def move(self, dest_x, dest_y):
        self.pos_x = dest_x
        self.pos_y = dest_y
        
        