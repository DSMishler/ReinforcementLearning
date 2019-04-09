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
    ghost.move(5,5,grid)
    for i in range(33):    
        pac.decide(grid)
        pac.eat(grid)
    ghost.chase(grid)
    PacPlots.plot_all(grid, ghost, pac, "endplot")
    

startup()