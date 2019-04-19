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
    def decide(self, grid):
        final_x = self.pos_x
        final_y = self.pos_y
        #rand = np.random.randint(0, len(self.neighbors))
        #cnt = 0
        
        for sp in self.neighbors:
            pt_x = self.pos_x + sp[0]
            pt_y = self.pos_y + sp[1]
            if pt_x < 0 or pt_x > (grid.agent_ID.shape[0]-1) or pt_y < 0 or pt_y > (grid.agent_ID.shape[1]-1):
                continue
            if grid.pellet_ID[pt_x][pt_y] == 1:
                final_x = pt_x
                final_y = pt_y
        self.move(final_x, final_y, grid)
        return
    
    def smartMove(self,grid):
        weights = self.getRewards(grid, 1, 10)
        greatest_i = 0
        for i in range(len(weights)):
            if(weights[greatest_i]<weights[i]):
                greatest_i = i
        final_x = self.pos_x+self.neighbors[i][0]
        final_y = self.pos_y+self.neighbors[i][1]
        for i in range(len(weights)):
            print("my weight at " + str(i) + " is " + str(weights[i]) + "!")
        self.move(final_x,final_y,grid)
    
    def getRewards(self, grid, alpha, beta):
        weights = []
        for i in range(len(self.neighbors)):
            consider_x = self.pos_x+self.neighbors[i][0]
            consider_y = self.pos_y+self.neighbors[i][1]
            if(consider_x > grid.agent_ID.shape[0]-1) or (consider_x<0):
                weights.append(-1000)
                continue
            if(consider_y > grid.agent_ID.shape[1]-1) or (consider_y<0):
                weights.append(-1000)
                continue
            punishmentContrib = self.punishmentAt(grid,consider_x,consider_y)
            rewardContrib = self.rewardAt(grid,consider_x,consider_y)
            rewardsFinal = alpha*rewardContrib - beta*punishmentContrib
            if rewardsFinal < -1000:
                rewardsFinal = -999
            weights.append(rewardsFinal)
        return weights
    
    def eat(self, grid):
        if(grid.pellet_ID[self.pos_x][self.pos_y] == 1):
            grid.pellet_ID[self.pos_x][self.pos_y] = 0
            print("munch!")
        else:
            print("Nothing to eat here!")
        return

    def findGhost(self,grid):
        # find where Pacman is at on the grid
        for i in range(grid.ghost_ID.shape[0]):
            for j in range(grid.ghost_ID.shape[1]):
                if grid.ghost_ID[i][j] != 0:
                    return(i,j)
    
    def punishment(self,grid):
        (ghostI, ghostJ) = self.findGhost(grid)
        punishment = (((self.pos_x-ghostI)**2)+((self.pos_y-ghostJ)**2))**(1/2)
        #print(punishment) #for debugging
        return(punishment)

    def punishmentAt(self,grid,this_x,this_y):
        (ghostI, ghostJ) = self.findGhost(grid)
        punishment = (((this_x-ghostI)**2)+((this_y-ghostJ)**2))**(1/2)
        #print(punishment) #for debugging
        return(punishment)
    
    def reward(self, grid):
        reward = 0
        for i in range(grid.ghost_ID.shape[0]):
            for j in range(grid.ghost_ID.shape[1]):
                if (i == self.pos_x) and (j == self.pos_y):
                    continue
                if grid.pellet_ID[i][j] == 1:
                    reward += 1/((((self.pos_x-i)**2)+(self.pos_y-j)**2)**(1/2))
        #print(reward) #for debugging
        return(reward)
    
    def rewardAt(self, grid, this_x, this_y):
        reward = 0
        for i in range(grid.ghost_ID.shape[0]):
            for j in range(grid.ghost_ID.shape[1]):
                if (i == this_x) and (j == this_y):
                    continue
                if grid.pellet_ID[i][j] == 1:
                    reward += 1/((((this_x-i)**2)+(this_y-j)**2)**(1/2))
        #print(reward) #for debugging
        return(reward)