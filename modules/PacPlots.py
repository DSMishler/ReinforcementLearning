# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:19:13 2019

@author: dsmis
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_all(grid, ghost, pacman, filename):
    fig = plt.figure( figsize = (10,10))
    cs = plt.contourf(np.transpose(grid.agent_ID))
    plt.axis('image')
    plt.plot(ghost.pos_x, ghost.pos_y, 'ro')
    plt.plot(pacman.pos_x, pacman.pos_y, 'yo')
    plt.savefig(filename)
    plt.show()
