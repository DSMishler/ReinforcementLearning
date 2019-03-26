# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:19:13 2019

@author: dsmis
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_all(grid, ghost, pacman, filename):
    fig = plt.figure( figsize = (10,10))
    cs = plt.countourf(np.transpose(grid.Agent_ID))
    plt.axis('image')
    plt.plot(ghost.pos_x, ghost.pos_y, 'wo')
    plt.plot(pacman.pos_x, pacman.pos_y, 'ro')
    plt.savefig(filename)
    plt.show()
