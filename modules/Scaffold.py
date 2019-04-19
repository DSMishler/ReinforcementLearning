# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:07:35 2019

@author: dsmis
"""
import Pacman
import Ghost
import Environment
import PacPlots

def startup():
    grid = Environment.Environment()
    grid.plot_me()
    print("starting grid above")
    pac = Pacman.Pacman(grid)
    ghost = Ghost.Ghost(grid)
    pac.eat(grid)
    PacPlots.plot_all(grid, ghost, pac, "firstplot")
    for i in range(20):
        pac.smartMove(grid)
        pac.eat(grid)
        if (int(i/2)*2==i/2 * 2):
            ghost.chase(grid)
        plotstr = "pacPlotv2" + str(i)
        PacPlots.plot_all(grid, ghost, pac, plotstr)
        
    '''
    ghost.move(5,5,grid)
    for i in range(33):    
        pac.decide(grid)
        pac.eat(grid)
    ghost.chase(grid)
    pac.punishment(grid)
    pac.reward(grid)
    pac.move(6,3,grid)
    pac.reward(grid)
    pac.smartMove(grid)
    '''
    
    
    PacPlots.plot_all(grid, ghost, pac, "endplot")
    

startup()